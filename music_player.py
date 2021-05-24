from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
from tkinter import filedialog 
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
import random
from mutagen.mp3 import MP3
from os.path import normpath, basename

my_dir = Path(__file__).parent

#==========================================================Gui

root =Tk()
root.geometry('1100x550+200+50')
root.title('SOHAM MUSIC PLAYER')
print(__file__)
root.iconbitmap(__file__+"/../images/ICO FILES/MUSIC_PLAYER.ico")
root.resizable(False,False)
root.configure(background="purple")

#==========================================================global variable

audiotrack = StringVar()
currentvol = 0
total_song_Length = 0
count = 0
text =''
AudioStatusLabel=''
font=('verdana', 20, 'italic bold')
font1=('verdana', 10)

#===========================================================background image

# music_image = PhotoImage(file= __file__+"/../images/JPEG, PNG/music_image_3.jpg")
music_image = Image.open(__file__+"/../images/JPEG, PNG/music_image_3.jpg")
photo = ImageTk.PhotoImage(music_image)

label = Label(root, image = photo, background="white")
# label.place(x=0, y=0, relwidth=5, relheight=6)
# label.pack(side=TOP)
label.place(x=0,y=0)



MUSIC_FILE=""
MUSIC_NAME = ''
MUSIC_FILE_LEN =0
select_label=''
filefolder=[]
path_of_folder=''
PathOfMusic=''

def search_btnClicked(event=None):
    global MUSIC_FILE, MUSIC_FILE_LEN, mfile, MUSIC_NAME
    PathOfMusic = askopenfile(defaultextension='.Mp3', filetypes=(('Audio File','*.Mp3'),('All files', '*.*')))
    MUSIC_FILE = PathOfMusic.name
    MUSIC_FILE_LEN =len(MUSIC_FILE)
    MUSIC_NAME= str(basename(normpath(MUSIC_FILE)))

    print(PathOfMusic)
    print(MUSIC_FILE)
    print(MUSIC_NAME)
    print(MUSIC_FILE_LEN)
    # print(MUSIC_NAME_len)
    if MUSIC_FILE == "":
            return
    else:
            
            MUSIC_LOCATION["text"] = ''
            Music_name_label['text']= MUSIC_NAME
            MUSIC_LOCATION["text"] = MUSIC_FILE
            Music_name_label.place(x=550, y=400, relwidth=length, relheight=.08, anchor="center")
            slider_Label.grid_remove()
            slider_Label.grid(row=5, column=0, padx=260,pady=300,columnspan=3)
            # repeatUnrepeatBtn.place(x=75, y=500, relwidth=.04, relheight=.08)
            # shuffleUnshuffleBtn.place(x=990, y=500, relwidth=.04, relheight=.08)
            # nextBtn.place(x=650, y=500, relwidth=.04, relheight=.08)
            # previousBtn.place(x=450, y=500, relwidth=.04, relheight=.08)
            # rewinedBtn.place(x=500, y=500, relwidth=.04, relheight=.08)
            # fastForwardBtn.place(x=600, y=500, relwidth=.04, relheight=.08)

#     global MUSIC_FILE, select_label, filefolder, path_of_folder, PathOfMusic
#     search_dialogue = tk.Toplevel()
#     search_dialogue.geometry('450x250+500+200')
#     search_dialogue.title('Search')
#     search_dialogue.resizable(0, 0)

#     # frame
#     search_frame = ttk.LabelFrame(search_dialogue, text = 'Select')
#     search_frame.pack(pady=20)
#     # search_frame.place(search_dialogue, x=20, y=20, relwidth=.02, relheight=.2)

#     filefolder=[
#         "FILE",
#         "FOLDER"
#     ]

#     # labels
#     style = ttk.Style()
#     style.theme_use("default")
#     style.map('TCombobox', fieldbackground=[('readonly','#310A3D')])
#     style.map('TCombobox', selectbackground=[('readonly', '#310A3D')])
#     style.map('TCombobox', selectforeground=[('readonly', 'white')])
#     n= tk.StringVar(value="---SELECT FILE/FOLDER---")
#     n.set(value="---SELECT FILE/FOLDER---")
#     select_label = ttk.Combobox(search_frame, font=font, justify='center', textvariable=n)
#     select_label['values']= filefolder
#     select_label["state"] = "readonly"
#     select_label.bind('<<ComboboxSelected>>')
#     select_label.current()
#     select_label.pack(side=TOP, pady=25)
#     Search2Btn = Button(search_frame, image=search_icon, compound=tk.RIGHT, font=font, relief='ridge', command=Search2, bg= "#310A3D")
#     # Search2Btn.place(x=850, y=80, relwidth=.2, relheight=.08)
#     Search2Btn.pack(side=TOP, pady=40)

    # def Search2(event=None):
    # global MUSIC_FILE, select_label, filefolder, PathOfMusic,path_of_folder
    # choice=select_label.get()
    # if (choice==filefolder[0]):
    # PathOfMusic = askopenfile(defaultextension='.Mp3', filetypes=(('Audio File','*.Mp3'),('All files', '*.*')))
    # MUSIC_FILE = PathOfMusic.name
    # MUSIC_NAME= str(basename(normpath(MUSIC_FILE)))
    # MUSIC_NAME_len = len(MUSIC_NAME)
    # print(PathOfMusic)
    # print(MUSIC_FILE)
    # print(MUSIC_NAME)
    # print(MUSIC_NAME_len)
    

    #     if MUSIC_FILE == "":
    #         return
    #     else:
    #         length=(int(MUSIC_NAME_len)/100)+.1
    #         MUSIC_LOCATION["text"] = MUSIC_FILE
    #         Music_name_label= Label(root, text= MUSIC_NAME, font=('algerian', 15), state="disabled", compound=tk.LEFT, background= "black", foreground= "white")
    #         Music_name_label.place(x=550, y=400, relwidth=length, relheight=.08, anchor="center")

    # elif(choice==filefolder[1]):
    #     path_of_folder = askdirectory()
    #     if filename.endwith('.mp3'):
    #         MUSIC_FILE= filename

    # MUSIC_NAME= str(basename(normpath(MUSIC_FILE)))
    # MUSIC_NAME_len = len(MUSIC_NAME)
    # # print(PathOfMusic)
    # print(MUSIC_FILE)
    # print(MUSIC_NAME)
    # print(MUSIC_NAME_len)


def musicurl():
    global MUSIC_FILE
    # try:
    dd=MUSIC_FILE
    audiotrack.set(dd)

#============================================================slider

ss = 'DEVOLOPED BY SOHAM DAS BISWAS.'
slider_Label = Label(root, text=ss, font=('algerian', 25), bg='#842DCE', fg='black')
# slider_Label.pack(side=TOP, padx=20, pady=250)#, columnspan = 3)
slider_Label.grid(row=5, column=0, padx=260,pady=380,columnspan=3)

def IntroLabelTrick():
    global count, text
    if (count>=len(ss)):
        count = -1
        text = ''
        slider_Label.configure(text=text)

    else:
        text = text+ss[count]
        slider_Label.configure(text=text)
    count +=1
    slider_Label.after(200, IntroLabelTrick)

IntroLabelTrick()
mixer.init()

Mlen = (MUSIC_FILE_LEN)-18

title = Label(root, text= 'SOHAM MUSIC PLAYER.', font=('algerian', 30), state="disabled", background= "black", foreground= "white")
title.place(x=550, y=30, relwidth=.4, relheight=.08, anchor="center")

music_label= Label(root, text= 'Select Your Song : ', font=('algerian', 20), state="disabled", background= "black", foreground= "white")
music_label.place(x=200, y=100, relwidth=.3, relheight=.08, anchor="center")

MUSIC_LOCATION = Label(root, text= '', font=('verdana', 10), state="disabled", background= "#310A3D", foreground= "black")
MUSIC_LOCATION.place(x=600, y=100, relwidth=.4, relheight=.08, anchor="center")

Music_name_label= Label(root, text='', font=('algerian', 15), state="disabled", compound=tk.LEFT, background= "black", foreground= "white")

#====================================================================================================================Play/pause

pause_icon = tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/pause.png')
play_icon = tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/play.png')
resume_icon = tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/resume.png')
stop_icon = tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/stop.png')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
length = ''
random_music = ''
mfile=''
ListOfSongsInDir = []
def Play(event=None):
    global random_music, mfile, length, ListOfSongsInDir, MUSIC_NAME
    # if (shuffleUnshuffleBtn['text'] == ''): 
    #     mfile= MUSIC_FILE+'/../'
    #     print("Shuffle")
    #     print(mfile)
    #     songs =os.listdir(mfile)
    #     noOfSongs=len(songs)
    #     ListOfSongsInDir = [i for i in range(1, noOfSongs+1)]
    #     print(songs)
    #     print(len(songs))
    #     print(ListOfSongsInDir)
    #     random_music = random.choice(songs)
    #     while (progressbar_music_starttime==progressbar_music_startend):
    #         print(random.choice(songs))
    #         random_music = random.choice(songs)
    #         # sleep()
    #     print(random_music)
    #     c=(os.path.join(mfile, random_music))
    #         # i+=1
            
    #     mixer.init()
    #     # ad=audiotrack.get()
        
    #     mixer.music.load(c)
    #     print(c)
    #     # print("abcd")
    #     progressbar_Ibl.place()
    #     mixer.music.play()
    #     mixer.music.get_busy()
    #     progressbar_music_label.place()
    #     mixer.music.set_volume(0.4)
    #     progressbar_volume['value']=40
    #     progressbar_volume_label['text']='40%'
    #     song=MP3(mfile+random_music)
    #     print(mfile)
    #     # m_file =str(basename(normpath(mfile)))
    #     Music_name_label['text']= random_music
    #     # print(type(mfile))
    #     MUSIC_LOCATION["text"] = mfile + random_music

    #     MUSIC_NAME_len1 = ''
    #     MUSIC_NAME_len1 = len(random_music)
    #     length1 = 0
    #     length1=(int(MUSIC_NAME_len1)/100)+.1
    #     Music_name_label.place_forget()
    #     Music_name_label.place(x=550, y=400, relwidth=length1, relheight=.08, anchor="center")
    #     print(length1)
    #     print('shuffle length')
                
        

    # elif repeatUnrepeatBtn['text'] == '':
    #     print('a')
        

    # else:
    mixer.init()
    print('NOrmal')
    # ad=audiotrack.get()
    mixer.music.load(MUSIC_FILE)
    progressbar_Ibl.place()
    mixer.music.play()
    progressbar_music_label.place()
    mixer.music.set_volume(0.4)
    progressbar_volume['value']=40
    progressbar_volume_label['text']='40%'
    song=MP3(MUSIC_FILE)
    # AudioStatusLabel['text']="Playing...."
    Music_name_label['text']= MUSIC_FILE
    MUSIC_LOCATION["text"] = MUSIC_FILE
    MUSIC_NAME_len= str(basename(normpath(MUSIC_FILE)))
    MUSIC_NAME_len =''
    MUSIC_NAME_len = len(MUSIC_NAME)
    length=0
    length=(int(MUSIC_NAME_len)/100)+.1
    print(length)
    print('normal length')
    Music_name_label.place_forget()
    Music_name_label.place(x=550, y=400, relwidth=length, relheight=.08, anchor="center")

    
    total_song_Length = int(song.info.length)
    progressbar_music['maximum'] = total_song_Length
    progressbar_music_startend.configure(text='{}'.format(str(datetime.timedelta(seconds=total_song_Length))))

    def func():
        global progressbar_music
        current_song_Length = mixer.music.get_pos()//1000
        progressbar_music['value']=current_song_Length
        progressbar_music_starttime.configure(text='{}'.format(str(datetime.timedelta(seconds=current_song_Length))))
        progressbar_music.after(2,func)
    func()


def createwidthes():
    global search_icon, play_icon, imvolumeup, imvolumedown, imvolumeup, resume_icon
    global progressbar_music_startend, progressbar_music_starttime, progressbar_music
    global AudioStatusLabel, progressbar_Ibl, progressbar_volume, progressbar_volume_label, progressbar_music_label

#-----------------------------------------------------------------------------------------------------------------------------------------------------------

playBtn = Button(root, text="PLAY     ", image=play_icon, compound=tk.RIGHT, command=Play, font=font, fg='white', bg='#310A3D')
playBtn.place(x=50, y=150, relwidth=.15, relheight=.08)

#====================================================================================================================Pause/resume

def pause_resume(event=None):
    global AudioStatusLabel
    if pause_resumeBtn['text']=='RESUME ':
        pause_resumeBtn['text']='PAUSE   '
        pause_resumeBtn['image']=pause_icon
        mixer.music.unpause()
        # AudioStatusLabel['text']='Paused'

    elif pause_resumeBtn['text']=='PAUSE   ':
        pause_resumeBtn['text']='RESUME '
        pause_resumeBtn['image']=resume_icon
        mixer.music.pause()
        # AudioStatusLabel['text']='Playing....'

#---------------------------------------------------------------------------------------------------------------------------------------------

pause_resumeBtn = Button(root, text="PAUSE   ", image=pause_icon, compound=tk.RIGHT, command=pause_resume, font=font, fg='white', bg='#310A3D')
pause_resumeBtn.place(x=50, y=225, relwidth=.15, relheight=.08)

#===================================================================================================================stop

def stop(event=None):
    global AudioStatusLabel
    mixer.music.stop()
    # AudioStatusLabel['text']='Stop'

#----------------------------------------------------------------------------------------------------------------------------------------------

stopBtn = Button(root, text="STOP     ", image=stop_icon, compound=tk.RIGHT, command=stop, font=font, fg='white', bg='#310A3D')
stopBtn.place(x=50, y=300, relwidth=.15, relheight=.08)

#====================================================================================================================search

search_icon = tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/search.png')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

SearchBtn = Button(root, text="Search   ", image=search_icon, compound=tk.RIGHT, font=font, relief='ridge', command=search_btnClicked, fg= "white", bg= "black")
SearchBtn.place(x=850, y=80, relwidth=.2, relheight=.08)

#======================================================================================================================fast forward/rewined/shutdown

# fast_forward_icon= tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/fast_forward.png')
# def fast_forward(event=None):
#     def func():
#         global progressbar_music
#         current_song_Length = mixer.music.get_pos()//1000
#         print(current_song_Length)
#         # mixer.music.pause()
#         f= current_song_Length+10
#         mixer.music.set_pos(f)
#         progressbar_music['value']=f
#         # mixer.music.progressbar_music(seconds=current_song_Length+10)
#         progressbar_music_starttime.configure(text='{}'.format(str(datetime.timedelta(seconds=f))))
#         progressbar_music.after(2,func)
#     func()

# fastForwardBtn = Button(root, bg='#310A3D', image=fast_forward_icon, command=fast_forward)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------

shutdownicon= tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/shutdown.png')
def shutdown(event=None):
    exit()

shutdownBtn = Button(root, bg='#310A3D', image=shutdownicon, command=shutdown)
shutdownBtn.place(x=550, y=500, relwidth=.04, relheight=.08)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

# rewinedicon= tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/rewined.png')
# def rewined(event=None):
#     pass

# rewinedBtn = Button(root, bg='#310A3D', image=rewinedicon, command=rewined)


#====================================================================================================================previous/ next

# previousicon= tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/previous.png')
# def previous(event=None):
#     pass

# previousBtn = Button(root, bg='#310A3D', image=previousicon, command=previous)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# nexticon= tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/next.png')


# def next(event=None):
#     current_index=ListOfSongsInDir.get_index()
#     mixer.music.stop()
#     mixer.music.play(current_index+1)

# nextBtn = Button(root, bg='#310A3D', image=nexticon, command=next)


#====================================================================================================================Repeat/unrepeat

# repeaticon= tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/repeat.png')
# unrepeaticon= tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/repeat_cross.png')
# def repeat_unrepeat(event=None):
#     if (repeatUnrepeatBtn['text'] == ''):
#         repeatUnrepeatBtn['image'] = unrepeaticon
#         repeatUnrepeatBtn['text'] = ' '

#         # print(1234)

#     elif (repeatUnrepeatBtn['text'] == ' '):
#         repeatUnrepeatBtn['image'] = repeaticon
#         repeatUnrepeatBtn['text'] = ''
#         # print(4567)

# repeatUnrepeatBtn = Button(root, text=' ', bg='#310A3D', image=unrepeaticon, command=repeat_unrepeat)


#====================================================================================================================shuffle/unshuffle

# shuffleicon= tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/shuffle.png')
# unshuffleicon= tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/shuffle_cross.png')
# def shuffle_unshuffle(event=None):
    
#     if (shuffleUnshuffleBtn['text'] == ''):
#         shuffleUnshuffleBtn['image'] = unshuffleicon
#         shuffleUnshuffleBtn['text'] = ' '
        
#         # print(1234)

#     elif (shuffleUnshuffleBtn['text'] == ' '):
#         shuffleUnshuffleBtn['image'] = shuffleicon
#         shuffleUnshuffleBtn['text'] = ''
#         print('mixer.music.stop(random_music)')
#         # print(4567)

# shuffleUnshuffleBtn = Button(root, text=' ', bg='#310A3D', image=unshuffleicon, command=shuffle_unshuffle)


#====================================================================================================================VOLUME UP/DOWN/mute

def volumeup(event=None):
    vol=mixer.music.get_volume()
    if (vol<=vol*100):
        mixer.music.set_volume(vol+0.01)
    else:
        mixer.music.set_volume(vol+0.01)
    progressbar_volume_label.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressbar_volume['value'] =mixer.music.get_volume()*100

imvolumeup = tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/volume_up.png')
Volume_up_Btn = Button(root, text='Volume UP       ', bg='#310A3D', fg='white', font=("arial",13,'bold'), image=imvolumeup, compound=RIGHT, command=volumeup)
Volume_up_Btn.place(x=850, y=150, relwidth=.15, relheight=.08)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

def volumedown(event=None):
    vol=mixer.music.get_volume()
    if (vol<=vol*100):
        mixer.music.set_volume(vol-0.01)
    else:
        mixer.music.set_volume(vol-0.01)
    progressbar_volume_label.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressbar_volume['value'] =mixer.music.get_volume()*100

imvolumedown = tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/volume_down.png')
Volume_down_Btn = Button(root,text='Volume Down   ', bg='#310A3D', fg='white', font=("arial",13,'bold'), image=imvolumedown, compound=RIGHT, command=volumedown)
Volume_down_Btn.place(x=850, y=225, relwidth=.15, relheight=.08)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------


def volumemute(event=None):
    global currentvol
    if Volume_mute_unmute_Btn['text']=='Volume Mute   ':
        Volume_mute_unmute_Btn['text']='Volume Unmute '
        Volume_mute_unmute_Btn['image']= imvolumeup
        currentvol =mixer.music.get_volume()
        mixer.music.set_volume(0)


    elif Volume_mute_unmute_Btn['text']=='Volume Unmute ':
        Volume_mute_unmute_Btn['text']='Volume Mute   '
        Volume_mute_unmute_Btn['image']= imvolumemute
        # currentvol=mixer.music.set_volume(40.0)
        print("currentvol "+ str(currentvol))
        mixer.music.set_volume(currentvol)
        

imvolumemute = tk.PhotoImage(file=__file__+ '/../images/JPEG, PNG/icons/volume_mute.png')
Volume_mute_unmute_Btn = Button(root,text='Volume Mute   ', bg='#310A3D', fg='white', font=("arial",13,'bold'), image=imvolumemute, compound=RIGHT, command=volumemute)
Volume_mute_unmute_Btn.place(x=850, y=300, relwidth=.15, relheight=.08)

#=====================================================================================================================progressbar volume up down

a = ttk.Style()
a.theme_use('clam')
a.configure("#310A3D.Vertical.TProgressbar", foreground='#310A3D', troughcolor ='lightgrey', background='#310A3D')


progressbar_Ibl = Label(root, text="",bg="#310A3D")
# progressbar_Ibl.grid(row=3,column=7, rowspan=3)
progressbar_Ibl.place(x=1050, y=150,  relwidth=.031, relheight=.354)

progressbar_volume = Progressbar(progressbar_Ibl, style="#310A3D.Vertical.TProgressbar", orient=VERTICAL, mode='determinate', value=40,length=190)
progressbar_volume.grid(row=0, column=0,ipadx=5)

progressbar_volume_label=Label(progressbar_Ibl, text='40%', font=('algerian',9), width=3)
progressbar_volume_label.grid(row=0, column=0)



# #====================================================================================================================progressbar runing time

b = ttk.Style()
b.theme_use('clam')
b.configure("#310A3D.Horizontal.TProgressbar", foreground='#310A3D', troughcolor ='lightgrey', background='#310A3D')

progressbar_music_label = Label(root,text='',bg="#310A3D")
# progressbar_music_label.grid(row=5,column=0,columnspan=3,padx=20,pady=20)
progressbar_music_label.place(x=70, y=450, relwidth=.875, relheight=.08)
# progressbar_music_label.grid_remove()
# progressbar_music_label.place_forget()

progressbar_music_starttime=Label(progressbar_music_label, font=('algerian',9), text="0:00:0", bg='#9999ff', width=7)
progressbar_music_starttime.grid(row=0, column=0)

progressbar_music = Progressbar(progressbar_music_label, style="#310A3D.Horizontal.TProgressbar", orient=HORIZONTAL,mode='determinate', value=0)
progressbar_music.grid(row=0, column=1, ipadx=380,ipady=0)

progressbar_music_startend =Label(progressbar_music_label, font=('algerian',9),text="0:00:0 ", bg='#9999ff')
progressbar_music_startend.grid(row=0,column=2)
#====================================================
# unmute_vol=progressbar_Ibl.selection_get()

createwidthes()
root.mainloop()