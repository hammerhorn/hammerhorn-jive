#!/bin/bash

function replace-and-play()
{
   mv -f tmp1 tmp
   write-and-play
}

function write-and-play()
{
   echo "Data written to 'tmp'"
   #./listfreqs.jar < tmp 2> ./choose_player.py 
   ./listfreqs.jar < tmp > /dev/null 2>&1 | ./choose_player.py 
}

function print-title()
{
   str=""
   for ((count=0;count<=(( $(tput cols)/2-10 ));count++))
   do
      str=" $str"
   done
   tput bold
   echo -e "$str CHRIS'S TONE ROW EDITOR\n"
   tput sgr0
}

## Start program ##
#cd ~/bin
clear
print-title
while [[ "$command" != [qQxX] ]]; do
   echo -e "\nCommands: _\bnew, _\bplay, re_\bverse, _\binvert, _\brotate, (_\b+/_\b-)pitch, _\bsave, _\bload, e_\bxit" |ul
   echo -n "twelvetone>"
   read -n 1 command
   case "$command" in 
      n|N)
#         clear
#         print-title
         echo -e -n "\b"
         echo -e "_\bN_\bE_\bW\n" |ul
         ./play-new-row.sh
         ./draw_row.py < tmp
      ;;

      v|V)
         echo -e -n "\b"
         echo -e "_\bR_\bE_\bV_\bE_\bR_\bS_\bE\n" |ul
         ./mirror.pl < tmp > tmp1
         replace-and-play
      ;;

      r|R)
         echo -e -n "\b"
         echo -e "_\bR_\bO_\bT_\bA_\bT_\bE\n" |ul
         ./rotate.pl < tmp > tmp1 
         replace-and-play
      ;;

      p|P|'')
         [[ "$command" = "" ]] && echo -e -n "\033[1Atwelvetone>"  || echo -e -n "\b"; 
         echo -e "_\bP_\bL_\bA_\bY\n"|ul 
         write-and-play
      ;;

      -)
         read amount
         ./up.pl $(( -1 * amount )) < tmp > tmp1
         replace-and-play        
      ;;

      +)
         read amount
         ./up.pl "$amount" < tmp > tmp1
         replace-and-play
      ;;

      l|L)
         echo -e -n "\bload from file: "
         read file
         cp "$file" tmp
         write-and-play
      ;;

      i|I)
         echo -e -n "\b"
         echo -e "_\bI_\bN_\bV_\bE_\bR_\bT\n"|ul
         #cat tmp|./flip.pl > tmp1
         ./flip.pl < tmp > tmp1
         replace-and-play
      ;;

      s|S)
         echo -e -n "\bsave to file: "
         read file
         cp out.ogg "$file.ogg"
         cp tmp "$file"
         echo -e "\nData written to $file."
         echo -e "Audio written to $file.ogg\n"
      ;;

      x|X|q|Q)
         echo -en "\b"
         echo -e "_\bE_\bX_\bI_\bT\n"|ul
      ;;

      )clear;;

      *)
          echo
          ;;
   esac
done
#cd -
