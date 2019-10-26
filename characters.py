# A class of all available ascii characters

import random

class AsciiCharacter():

    def __init__(self):
        self._characters = [x for x in dir(self) if x.find('__') == -1]

        self._choice = random.choice(self._characters)

        self.character = eval('self.%s()' %self._choice)
        
    #define new characters as functions below

    def ascii_cat(self):
        #Ascii Art from https://www.asciiart.eu/animals/cats
        #Anonymous artist
        ascii_cat_character = """
 ,_     _    / /
 |\\\_,-~/   /'
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \\  _T_/-._( (
 /         `. \\
|         _  \\ |
 \\ \\ ,  /      |
  || |-_\\__   /
 ((_/`(____,-'
"""
        return ascii_cat_character



