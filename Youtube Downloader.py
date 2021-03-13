from tkinter import *
from pytube import YouTube

root = Tk()
root.title("YouTube Video Downloader")
 
#Creating Function for Button Click

def button_Click():
    
    link = e.get()
    path = e_Path.get()

    #Handling Exceptions For Network Connection Problem
    
    try:
        
        yt = YouTube(str(link))
    
    except:

        label_Connerror = Label(root, text="Connection Error!")
        label_Connerror.pack()

    #Getting the Higher Resolution 
    
    out_Video = yt.streams.get_highest_resolution()

    #Downloading the Video

    out_Video.download(str(path))

    #Displaying Downloaded Path and Finish
    
    label_Showpath = Label(root, text="File Downloaded to " + path + yt.title)
    label_Finish = Label(root, text="Task Completed!")
    label_Showpath.pack()
    label_Finish.pack()
    
#Displaying Title

label_Title = Label(root, text="YouTube Video Downloader", fg="red", font=("Arial",18,"bold"))
label_Title.pack()

#Creating Entry Widget

e = Entry(root, width=50)
e_Path = Entry(root, width=50)
e.pack()
e.insert(0,"Paste Your Link")
e_Path.pack()
e_Path.insert(0,"Enter Your Path")

#Creating Download Button

button_Download = Button(root, text="DOWNLOAD", command=button_Click, fg="orange", font=("Arial",18,"bold"))
button_Download.pack()


root.geometry('500x250')
root.mainloop()