import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink= link.get()
        ytObj= YouTube(ytLink, on_progress_callback=on_progress)
        video=ytObj.streams.get_audio_only()

        title.configure(text=ytObj.title, text_color="blue")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Download Complete!")
    except:
        finishLabel.configure(text="Download Error!",text_color="red")
    
def on_progress(streams,chunk,bytes_remaining):
    total_size= streams.filesize
    bytes_downloaded=total_size - bytes_remaining
    percent_completed= bytes_downloaded / total_size *100
    per = str(int(percent_completed))
    pPercent.configure(text=per + '%')
    pPercent.update()

    progressbar.set(float(percent_completed)/100)


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(app, text= "Insert link")
title.pack(padx=10, pady=10)

urlVariable= tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=urlVariable)
link.pack()

finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack() 

pPercent = customtkinter.CTkLabel(app, text="0%")
pPercent.pack()

progressbar= customtkinter.CTkProgressBar(app , width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=20)

app.mainloop()