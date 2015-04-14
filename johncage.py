# johncage.py
# creates a John Cage simulation to play a random-length piece of music using I-Ching cards and excerpts of John Cage's music
#
# Judy Jackson
# 12/19/14

import random
from multiprocessing import *
import music
from tkinter import *

################## random number generations/infrastructure ###################

#### initial variables #####
time = random.randint(1, 8)
print("The piece will be", time, "minutes long.")
number = time * 2
raw_list = []
iching_list = []
card_list = []

#### raw random number generation ####
for i in range(number):
    x = random.randint(1, 8)
    y = random.randint(1, 8)
    z = (x, y)
    raw_list.append(z)
    
rl_length = len(raw_list)


#### turns numbers into lists for creating data for files ####
ichingfile = open("ichingtable.txt", "r")

for line in ichingfile:
    l = line
    ll = l.split(" ")
    iching_list.append(ll)

for i in range (8):
    for j in range(8):
        x = iching_list[i][j]
        y = x.strip("\n")
        iching_list[i][j] = y

for i in range(rl_length):
    x = raw_list[i][0] - 1
    y = raw_list[i][1] - 1
    card = iching_list[y][x]
    card_list.append(card)

################# music making ########################
def music_function(L): 
    piece = music.Music()
    for i in range(rl_length):
        soundfile = "/Users/jcj1108/Desktop/csci/cage_clips/" + L[i] + ".wav"
        excerpt = music.Music(soundfile)
        piece.concat(excerpt)
        
    piece.play()
    
    
################# picture making #######################
def picture_function(L):
    window = Tk()
    for i in range(len(L)):
        filename = "/Users/jcj1108/Desktop/csci/iching_cards/" + L[i] + ".gif"
        photo = PhotoImage(file=filename)
        x = Label(window, image=photo)
        x.image = photo 
        x.pack(side=LEFT)
    window.mainloop()


################## launches functions ######################
p1 = Process(target=music_function, args=(card_list, ))
p1.start()

x = picture_function(card_list)

