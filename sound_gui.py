from tkinter import ttk
from email import message
from fileinput import filename
from tkinter import *
from tkinter import filedialog
from email.mime import audio
import moviepy
import moviepy.editor as edit 
import os

app = Tk()
mp3ext = IntVar()
#CLICK EVENTS
def openfile():
    global files
    files= filedialog.askopenfilenames(title="Open file", initialdir="/")
    for i in range(len(files)):
        display = os.path.basename(files[i])
        allFiles.insert(i,display)
def update_progress(value):
    progress["value"]=value
    app.update()
def extract():
    
    directory = "extracted songs"
    parent_dir  = os.getcwd()
    path = os.path.join(parent_dir,directory)
    if os.path.exists(directory):
        os.chdir(path)
    else:
        os.mkdir(directory)
        os.chdir(path)
    for i in range(len(files)):
        value_factor = int(100/len(files))
        Message.config(text="Extracting....")
        output = os.path.basename(files[i])
        video = edit.VideoFileClip(files[i])
        audio = video.audio
        if x.get()==0:
            audio.write_audiofile(output.replace(output[-4:],'.mp3'))
        elif x.get()==1:
            audio.write_audiofile(output.replace(output[-4:],'.aac'))
        else:
            audio.write_audiofile(output.replace(output[-4:],'.wav'))
        audiofile = output.replace(output[-4:],'.mp3')
        allExtractedfiles.insert(i,audiofile)
        value_factor+=value_factor
        update_progress(value_factor)
    if len(files)==1:
            Message.config(text="Your audio is here:👇")
    else:
            Message.config(text="Your audio files are here:👇")
#APP ITSELF
app.title("Audio extractor")
# app.resizable(False,False)
app.geometry("400x600")
icon = PhotoImage(file="soundtrack.png")
app.iconphoto(True,icon)

Title = Label(app, text="Audio extractor", font=("Algerian", 15),fg='blue')
Title.grid(row=0,column=1,ipadx=5)


openFile = Button(
    app,
    text="Open File",
    command=openfile,
    width=10,
    height=3,
    bg="#4284ff",
    fg="white",
    activebackground="#4284ff",
    activeforeground="white",
    border=0
)
openFile.grid(row=1,column=0, pady=5)
selectedFiles = Label(app,text="Your video file shows up here👇")
selectedFiles.grid(row=1,column=1)
allFiles = Listbox(
    app,
    width=50
)
allFiles.config(height=10)
allFiles.grid(row=2,column=1)



Extract = Button(
    app,
    text="Extract Audio",
    command=extract,
    width=10,
    height=3,
    bg="#4284ff",
    fg="white",
    activebackground="#4284ff",
    activeforeground="white",
    border=0
)
Extract.grid(row=3,column=0, pady=5)
Message = Label(app,text="Your audio file shows up here👇")
Message.grid(row=3,column=1)
allExtractedfiles = Listbox(
    app,
    width=50
)
allExtractedfiles.config(height=10)
allExtractedfiles.grid(row=4,column=1)
progress = ttk.Progressbar(
    app,
    length="300",
    mode="determinate"
)
progress.grid(row=5,column=1,sticky=W)
exts = ("MP3","WAV")
x=IntVar()
for i in range(len(exts)):
    extButton = Radiobutton(app,text=exts[i],variable=x,value=i)
    extButton.grid(column=1,sticky=W)

app.mainloop()

#😊THANKYOU🙏FOR VISITING😉AND I`D LOVE YOUR LIKE ON THE PROJECT😘