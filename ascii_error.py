# Amodule to make your error messages less scary

import sys

err_message = "You certainly messed something up."
if len(sys.argv) > 1:
    err_message = ' '.join(sys.argv[1:])

one_line = False
err_line_1 = err_message.split('--')[0]
try:
    err_line_2 = err_message.split('--')[1]
except:
    one_line = True
    err_line_2 = err_line_1
    
if len(err_line_1) >= len(err_line_2):
    max_length = len(err_line_1)
    long_line_label = 1
else:
    max_length = len(err_line_2)
    long_line_label = 2
    
#Ascii Art from https://www.asciiart.eu/animals/cats
#Anonymous artist
ascii_cat = """
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

s1 = " " * 16 + "_" * (max_length + 6) 
s2 = " " * 15 + "/" + " " * (max_length + 6) + "\\"

if not one_line:
    if long_line_label == 1:
        length_diff = len(err_line_1) - len(err_line_2)
        s3 = " " * 15 + "|" + " " * 3 + err_line_1 + " " * 3 + "|"
        s4 = " " * 15 + "|" + " " * 3 + err_line_2 + " " * length_diff + " " * 3 + "|"
    elif long_line_label == 2:
        length_diff = len(err_line_2) - len(err_line_1)
        s3 = " " * 15 + "|" + " " * 3 + err_line_1 + " " * length_diff + " " * 3 + "|"
        s4 = " " * 15 + "|" + " " * 3 + err_line_2 + " " * 3 + "|"
else:
    s34 = " " * 15 + "|" + " " * 3 + err_message + " " * 3 + "|"
    
s5 = " " * 15 + "\\" + " " * 2 + "_" * (max_length + 4) + "/"
s6 = " " * 14 + "/  /"

if not one_line:
    speech_bubble = s1 + "\n" + s2 + "\n" + s3 + "\n" + s4 + "\n" + s5 + '\n' + s6
else:
    speech_bubble = s1 + "\n" + s2 + "\n" + s34 + "\n" + s5 + '\n' + s6
    
print("\n\n\n" + speech_bubble + ascii_cat + "\n\n\n")


