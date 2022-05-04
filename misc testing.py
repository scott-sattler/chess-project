

c_1 = not False
if c_1:
    print "X"



'''
white_first_move = None
print bool(white_first_move)


valid_move_list = []
if bool(valid_move_list):  # a list can function as a bool. empty=false
    print "True"
'''

'''
import Tkinter as tki # Tkinter -> tkinter in Python 3

class GUI(tki.Tk):
    def __init__(self):
        tki.Tk.__init__(self)

        # create a popup menu
        self.aMenu = tki.Menu(self, tearoff=0)
        self.aMenu.add_command(label="Undo", command=self.hello)
        self.aMenu.add_command(label="Redo", command=self.hello)

        # create a frame
        self.aFrame = tki.Frame(self, width=512, height=512)
        self.aFrame.pack()

        # attach popup to frame
        self.aFrame.bind("<Button-3>", self.popup)

    def hello(self):
        print "hello!"

    def popup(self, event):
        self.aMenu.post(event.x_root, event.y_root)

gui = GUI()
gui.mainloop()
'''

'''
some_list = [1,1,1,1,1,
             1,1,1,2,2,
             2,2,2,1,1,
             1,1,1,1,1,
             1,1,1,1,1]

for i in range(15):
    print some_list[-15 + i],
    if some_list[-15 + i] == 2:
        pass
        #print "foo"

'''


'''
i = -1
#c_1 = 7 < i
#c_2 = i < 0
#if c_1 or c_2:
if -1 < i < 8:
    print "True"
else:
    print "False"
'''


'''
import datetime
from time import sleep

d1 = datetime.datetime.utcnow()
sleep(1)
d2 = datetime.datetime.utcnow() # after a 5-second or so pause
d2 - d1

#datetime.timedelta(0, 5, 203000)

print d2 - d1
'''
'''




#!usr/bin/env python
#coding=utf-8

import pyaudio
import wave

#define stream chunk
chunk = 1024

#open a wav format music
f = wave.open(r"C:/users/admin/dropbox/chess/sounds/castle_while_checked.wav","rb")
#instantiate PyAudio
p = pyaudio.PyAudio()
#open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data
data = f.readframes(chunk)

#paly stream
while data != '':
    stream.write(data)
    data = f.readframes(chunk)

#stop stream
stream.stop_stream()
stream.close()

#close PyAudio
p.terminate()

'''







import pygame as pg
import time


'''
pg.mixer.init()
pg.init()

a1Note = pg.mixer.Sound("sounds/castle_while_checked.wav")
a2Note = pg.mixer.Sound("sounds/piece_capture.wav")
a3Note = pg.mixer.Sound("sounds/digi_plink.wav")

pg.mixer.set_num_channels(50)

for i in range(25):
    a3Note.play()
    a1Note.play()
    time.sleep(0.3)
    #a2Note.play()
    #time.sleep(0.3)

'''


#promotion_object_lookup_names = ['white_queen', 'something']



#print promotion_object_lookup_names[0][6:]

'''
import itertools

promotion_object_lookup_names = ['white_queen', 'white_knight', 'white_rook', 'white_bishop', 'black_queen', 'black_knight', 'black_rook', 'black_bishop']

for entry in promotion_object_lookup_names:
    print promotion_object_lookup_names.index(entry)
    if entry.index == 3:
        print promotion_object_lookup_names[entry.index]
'''


"""
if 2 == (2 and 3):
    print "foo"

for x in range(0, -2):
    print x
"""

'''
if True:
    if True:
        if True:
            if False:
                print "impossible"
else:
    print "one"
'''



'''
white_castle_flags = {'king': False, 'rook': False}  # () vs [] vs {}
print white_castle_flags
white_castle_flags['king'] = True
print white_castle_flags
'''


'''
from Tkinter import *
import Tkinter

top = Tkinter.Tk()

B1 = Tkinter.Button(top, text ="circle", relief=RAISED,\
                         cursor="circle")
B2 = Tkinter.Button(top, text ="plus", relief=RAISED,\
                         cursor="plus")
B1.pack()
B2.pack()
top.mainloop()
'''

'''# Use Tkinter for python 2, tkinter for python 3
import Tkinter as tk
from Tkinter import *

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # <create the rest of your GUI here>

        self.container = Canvas(parent, width=600, height=600)
        self.container.pack()
        self.container.bind('<Button-1>', self.move_piece)

        canvas1 = Canvas(self.container, width=200, height=200)
        canvas1.pack()
        canvas1.bind('<ButtonPress-1>', self.some_fun)
        canvas1.bind('<B1-Motion>', self.move_piece)

        canvas2 = Canvas(self.container, width=200, height=200)
        canvas2.config(bg='green')
        canvas2.pack()
        canvas2.bind('<Button-1>', self.some_fun)

        canvas3 = Canvas(self.container, width=200, height=200)
        canvas3.config(bg='blue')
        canvas3.pack()
        #canvas3.bind('<ButtonRelease-1>', self.second_fun)
        canvas3.bind('<ButtonRelease-1>', self.move_piece)
        #canvas3.bind('<Enter>', self.c_u)

        # find_closest(x, y, halo=None, start=None)


    def some_fun(self, event):
        print event.x, event.y
        return

    def second_fun(self, event):
        print "second fun"
        return

    def c_u(self, event):
        print "i c u"
        return

    def motion(self, event):
        print "motion:", event.x, event.y
        return

    def move_piece(self, event):
        #find_closest(x, y, halo=None, start=None)
        print root.winfo_containing(event.x_root, event.y_root)
        print event.x, event.y
        #print self.container.find_closest(event.x, event.y)


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.focus_force()
    root.mainloop()
'''