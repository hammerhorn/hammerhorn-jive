#!/usr/bin/env python
"""
Generates dummy output chatter is words, sentences, or chunks.
Set some maximum lengths and zero out sentence_count
"""
from random import randint

__author__ = 'Chris Horn <hammerhorn@gmail.com>'
__license__ = 'GPL'

class TextGen(object):
    WORD_MAXLENGTH = 10
    SENTENCE_LENGTH = 20
    sentence_count = 0 #Number of sentences within the last chunk() written
    sentence_total = 0 #Total number of sentences written

    @classmethod
    def word(cls):
        """
        Words will be between 1 and WORD_MAXLENGTH letters long.
        """
        word = ''
        for _ in range(randint(1, cls.WORD_MAXLENGTH)):
            word += chr(randint(97, 122))
        return word

    @classmethod
    def sentence(cls):
        """
        Sentences will have exactly SENTENCE_LENGTH words.
        """
        sentence = cls.word().capitalize()
        for _ in range(1, cls.SENTENCE_LENGTH):
            sentence += ' ' + cls.word()
        sentence += '.'
        return sentence

    @classmethod
    def chunk(cls):
        """
        a paragraph
        """
        chunk = cls.sentence()
        sentence_count = 1

        #An interesting type of probability curve
        while True:
            if sentence_count == 2 and randint(1, 100) > 98.75:
                break
            elif sentence_count == 3 and  randint(1, 12) == 1:
                break
            elif sentence_count == 4 and randint(1, 1000) > 750:
                break
            elif sentence_count == 5 and randint(0, 1) == 1:
                break
            elif sentence_count == 6 and randint(1, 1000) > 375:
                break
            elif sentence_count == 7 and randint(1, 4) != 1:
                break
            elif sentence_count == 8 and randint(1, 8) != 1:
                break
            elif sentence_count == 9:
                break
            chunk += '  ' + cls.sentence()
            sentence_count += 1

        cls.sentence_count = sentence_count
        cls.sentence_total += sentence_count
        return chunk
