#!/usr/bin/python/
# coding=UTF-8

import os, pprint, sys, textwrap, time

from cjh.cli import Cli, ListPrompt
from cjh.geometry import Graph, Point
from cjh.lists import Enumeration, ItemList
from cjh.things import Thing

class Goban(Graph):
    """
    a crude graphing calculator in the shape of a go board
    """
    def __init__(
        self, size=19, skinfile='unicode1.json', sh_obj=Cli(), adjust_ssize=0):
        """
        Call parent constructor; declare empty list, 'self.groups'.
        """
        super(Goban, self).__init__(size, skinfile, sh_obj, adjust_ssize)
        self.groups = []

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['sh_obj']
        return state

    ###########
    #  BOARD  #
    ###########
    def is_hoshi(self, x, y):
        """
        Return True if the point is a starpoint; should take A1 type args.
        """
        # Convert ordered pair to array indices
        x += self.max_domain
        y = self.max_domain - y

        # Determine starpoint
        if self.size >= 12:
            starpoint = 4
        elif self.size >= 9:
            starpoint = 3
        else: starpoint = 2

        side_point = False
        if self.size % 2 == 1 and self.size >= 13:
            side_point = True

        if x == starpoint - 1 and y == starpoint - 1:
            return True

        if side_point:
            if (x == self.max_domain and y == starpoint - 1) or \
               (x == starpoint - 1 and y == self.max_domain) or \
               (x == starpoint - 1 and y == self.max_domain) or \
               (x == self.size - starpoint and y == self.max_domain) or \
               (x == self.max_domain and y == self.size - starpoint):
                return True

        if (x == self.size - starpoint and y == starpoint - 1) or \
           (x == starpoint - 1 and y == self.size - starpoint) or \
           (x == self.size - starpoint and y == self.size - starpoint):
            return True
        return False

    def access_gnugo_functs(self, basename):
        """
        Scoring/estimating tools from gnugo; this should take filename instead.
        """
        Cli.make_page(
            'WRITE FILE: {}.sgf'.format(basename), self, lambda: self.write_sgf(
            basename))

        menu1 = ListPrompt(['..', 'fast', 'medium', 'slow'])
        sel1 = Cli.make_page('MENU: GNUGO Scoring Tools', self, menu1.input)
        gnugo_dict = {'fast':'estimate', 'medium':'finish', 'slow':'aftermath'}
        print('') #pylint: disable=C0325
        if sel1 != 1:
            os.system('gnugo --score ' + gnugo_dict[menu1.items[sel1 - 1]] +\
                      ' --quiet -l {}.sgf'.format(basename))
            Cli.wait()

    ############
    #  POINTS  #
    ############
    def place_stone(self, letter, number, color):
        """
        Add a stone to the board.  letter, number are the coordinates, color is
        color.
        """
        letter = letter.upper()

        # 'I' is skipped in th enumeration
        if letter >= 'I':
            ordinal = ord(letter) - 66
        else: ordinal = ord(letter) - 65
        tmp_pt = self.indices_to_point(ordinal, self.size - number)

        x_val, y_val = tmp_pt.x_mag, tmp_pt.y_mag

        #If it is a legal move
        #????????????????

        self.plot_point(x_val, y_val, color)
        self.cursor = x_val, y_val        
        

class GoStone(Point):
    def __init__(self, color, pt_tuple):
        super(GoStone, self).__init__()
        #self.alive = True
        self.color = color
        self.pt_tuple = pt_tuple


class Turn(Thing):
    def __init__(self, color, pt_tuple, comments):
        super(Turn, self).__init__()
        self.address = pt_tuple
        self.color = color
        self.comments = comments

    def __remove_captured_stones():
        pass

    def __repr__(self):
        commentsf = textwrap.fill(self.comments, replace_whitespace=False, width=45)
        #return self.address + '\n' + self.color + '\n\n' + commentsf + '\n'
        if len(commentsf) > 0: string = '{}{} ({})'.format(self.address[0], self.address[1], commentsf)
        else: string = '{}{}'.format(self.address[0], self.address[1])
        return string

    def __getitem__(self, index):
        return self.address[index]

#    def __str__(self):
#        return "{}{}".format(self.address[0], self.address[1])

class Group(Thing):
    def __init__(self, seed_stone):
        self.liberties = 4
        pass        

class GoGame(Thing):
    header = {}
    moves = []

    def __init__(self, sgf_str='', skin='unicode1.json'):

        # Parent constructor
        super(GoGame, self).__init__()

        # Declare a new dictionary
        self.header_dict = {}

        # If an sgf string is given...
        if len(sgf_str) > 0:

            # Split it up into units
            self.units = sgf_str.split(';')

            # Get the header string
            self.units = self.units[1:]
            self.header_str = self.units[0]

            # Get the list of moves and 
            self.moves = self.units[1:]

            # Strip off any whitespace
            self.moves = [move.strip() for move in self.moves]

            # Convert the header information to a dictionary
            self.head_list = self.header_str.split(']')[:-1]
            for unit in self.head_list:
                l = unit.split('[')
                l = [i.strip() for i in l]
                self.header_dict.update({l[0]:l[1]})

            self.size = eval(self.header_dict['SZ']) #there is a better way i think

            # Convert the sgf representations to Turn objects
            for i, v in enumerate(self.moves):
                if self.moves[i][0] == 'B': colour = 'black'
                elif self.moves[i][0] == 'W': colour = 'white'
                address = (self.moves[i][2].upper(), self.size - (ord(self.moves[i][3]) - 97))
                self.moves[i] = Turn(colour, address, self.moves[i][5:])



        else:

            # If this is a new game, there will be no header.  So let's make one.
            black_player = Cli.input("Black player's name: ")
            white_player = Cli.input("White player's name: ")
            self.header_dict.update({'SZ': 19, 'PW': white_player, 'PB': black_player, 'KM': 6.5, 'GM':1})

        # If this is a new games, there will be no moves....
                    
    def __str__(self):
        s = '\n' + Cli.term_fx('b', self.label)
        s += Cli.term_fx('nu', 'header') + ": {}".format(pprint.pformat(self.header_dict))
        s += "\n\n"
        s += Cli.term_fx('nu', 'moves') + ": {}".format(self.moves)
        return s

    def __getitem__(self, index):
        return self.moves[index]

    def __len__(self):
        return len(self.moves)

    def __iter__(self):
        return

    def __repr__(self):
        string = ''
        try:
            if self.header_dict['GM'] == '1': 
                string += 'Game: Go\n'
            elif self.header_dict['GM'] == '2':
                string += 'Game: Reversi\n'
        except:pass

        try:
            string += "Size: {} x {}\n".format(self.header_dict['SZ'])
        except:pass

        try:
            string += "{} vs. {}\n".format(self.header_dict['PW'], self.header_dict['PB'])
        except:pass

        try:
            string += "Komi: {}\n".format(self.header_dict['KM'])
        except: pass

        try:
            for game, index in enumerate(self.game_list):
                self.game_list[index].header = str(game[1]) + "\n"
        except: # type?
            pass



        ### This block doesn't work ###
        bullet_items = []
        try:
            bullet_items.append("SGF generated by {}.".format(self.header['AP']))
        except:pass
        if 'DT' in self.header:
            bullet_items.append(self.header['DT'])
        #if "GM" in self.header:
        #    game = ''
        #    if self.header['GM'] == '1':
        #        game = 'go'
        #    else: game = 'unknown'
        #    s += ["The game is {}.".format(game)]
        if 'RU' in self.header:
            bullet_items += ["{} rules.".format(self.header['RU'])]
        if 'SZ' in self.header:
            bullet_items += ["The board size is {0} × {0}.".format(self.header['SZ'])]
        if 'KM' in self.header:
            bullet_items += ["Komi is {}.".format(self.header['KM'])]
        if 'PB' in self.header:
            bullet_items += ["Black Player: {}".format(self.header['PB'])]
        if 'PW' in self.header:
            bullet_items += ["White Player: {}".format(self.header['PW'])]
        self.bullets = ItemList(bullet_items)
        ###############################


        moves_enum = Enumeration(self.moves)
        return ('\n' + Cli.term_fx('u', self.label.title()) + #self.ul_label() + 
                string + #'\n\nself.bullets: ' + str(self.bullets) + 
                '\nmoves_enum: ' + str(moves_enum) +
                '\n' + Cli.hrule(string=True, width=40))

    def less(self):
        Cli.less(str(self))

    def play_thru(self, autoplay=False):
        goban = Goban(int(self.header_dict['SZ'])) #, skinfile=self.skin)
        color = 'black'
        for _, turn in enumerate(self.moves):
            goban.place_stone(turn[0], int(turn[1:]), color)
            if autoplay:
                func = lambda: time.sleep(.25)
            else: func = Cli.wait
            Cli.make_page(self.label, str(goban), func)
            if color == 'white':
                color = 'black'
            elif color == 'black':
                color = 'white'

class GameRecord(Thing):
    """
    First, I will try to make it work with single-game files.
    """
    def __init__(self, filename, skin="unicode1.json"):
        super(GameRecord, self).__init__()
        GoGame.count = 0
        self.headers = []
        self.games = []

        # Read file into buffer
        self.buffer_ = Cli.cat(files=[filename], quiet=True, return_str=True)

        self.chunks = self.buffer_.split('(')[1:]
        
        for chunk in self.chunks:
            self.games.append(GoGame(chunk))

#        # Break the buffer up into units, with ';' as the delimiter
#        self.unit_list = self.buffer_.split(';')

        # Strip newlines off of units in unit_list
#        for index, unit in enumerate(self.unit_list):
#            self.unit_list[index] = unit.strip()

        # Get headers
#        for index, unit in enumerate(self.unit_list):
#            if unit.startswith('('):
#                self.headers.append(self.unit_list[index + 1])
        #if len(this_game) > 0:
#                self.games.append(GoGame(self.headers[0]))
#                this_game.append(unit)
#                print "game = " + str(this_game)
#            print('[+] unit_list[{}]: {}'.format(index, self.unit_list[index]))
#        self.headers.append(self.unit_list[1])
        #self.games.append(GoGame(self.headers[0]))
#        moves = []
#        Cli.wait()
#        count = 2
#        board = Goban()

#        while True:
#            address = unit_list[count].split('[')[1][0:2]
#            if unit_list[count][0] == 'B': color = 'black'
#            elif unit_list[count][0] == 'W': color = 'white'
#            if len(unit_list[count]) > 5: comments = unit_list[count][7:-2]
#            else: comments = ''
#            turn = Turn(color, address, comments)
#            board.place_stone(address[0].upper(), ord(address[1]) - 96, color)
#            Cli.clear()
#            print board
#            print '\n' + Cli.term_fx('u', "Turn:") + str(turn)
#            count += 1
#            Cli.wait()

    def __str__(self):
        #s = ''
        #for game in self.game_list:
        #    s += ("\n" + str(game))
        #return s
        return self.buffer_

    def __getitem__(self, index):
        return self.games[index]

    def __len__(self):
        return len(self.games)

    def __iter__(): pass
