#importing libraries 
from pygame import mixer
from tkinter import *
from tkinter import filedialog

#add many songs to the playlist
def addsongs():
    #a tupple of songs is returned 
    temp_song=filedialog.askopenfilenames(initialdir="music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    #loop through every item in the tupple
    for s in temp_song:
        songs_list.insert(END,s)
        print(temp_song)
        print(s)    
            
def deletesong():
    pass
    
    
def Play():
    song=songs_list.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

#to pause the song 
def Pause():
    mixer.music.pause()

#to stop the  song 
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song

def Resume():
    mixer.music.unpause()

#Function to navigate from the current song
def Previous():
    pass

def Next():
    pass

#creating the root window 
root=Tk()
root.title('DataFlair Music player App ')
#initialize mixer 
mixer.init()

#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)

#font is defined which is to be used for the button font 
#defined_font = font.Font(family='Helvetica')

#play button
play_button=Button(root,text="Play",width =7,font="Helvetica",command=Play)
#play_button['font']=defined_font
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",width =7,font="Helvetica",command=Pause)
#pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#stop button
stop_button=Button(root,text="Stop",width =7,font="Helvetica",command=Stop)
#stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

#resume button
Resume_button=Button(root,text="Resume",width =7,font="Helvetica",command=Resume)
#Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

#previous button
previous_button=Button(root,text="Prev",width =7,font="Helvetica",command=Previous)
#previous_button['font']=defined_font
previous_button.grid(row=1,column=4)

#nextbutton
next_button=Button(root,text="Next",width =7,font="Helvetica",command=Next)
#next_button['font']=defined_font
next_button.grid(row=1,column=5)

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)


mainloop()
