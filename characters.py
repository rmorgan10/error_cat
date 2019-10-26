# A class of all available ascii characters

import random

class AsciiCharacter():

    def __init__(self):
        self._characters = [x for x in dir(self) if x.find('__') == -1]

        #make ascii_cat the most probable
        self._characters += ['ascii_cat'] * (2 * len(self._characters))

        #choose random character
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


    def ascii_seahorse(self):
        #Ascii Art from https://www.asciiart.eu/animals/
        #Artist: Morfina
        ascii_seahorse_character = """
             / /
      \\/)/)  /'
    _'  oo(_.-. 
  /'.     .---'
/'-./    (
)     ; __\\
\\_.'\ : __|
     )  _/
    (  (,.
     '-.-'
"""
        return ascii_seahorse_character


    def ascii_bat(self):
        #https://www.asciiart.eu/animals/bats
        #Artist: Joan Stark
        ascii_bat_character = """
             / / 
   /\\        /'       /\\
  / \\'._   (\\_/)   _.'/ \\
 /_.''._'--('.')--'_.''._\\
 | \\_ / `;=/ " \\=;` \\ _/ |
  \\/ `\\__|`\\___/`|__/`  \\/
   `      \\(/|\\)/       `
           " ` "
"""
        return ascii_bat_character

    def ascii_dog(self):
        #https://www.asciiart.eu/animals/dogs
        #Anonymous artist 
        ascii_dog_character = """
     |\\_/|   / /               
     | @ @   /' 
     |   <>              _  
     |  _/\\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|
"""
        return ascii_dog_character

    
