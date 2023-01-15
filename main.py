import tkinter
import customtkinter as c
from pytube import YouTube


def download():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=onProgress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title)
        finishedlabel.configure(text="")
        video.download()
        finishedlabel.configure(
            text="Download successful! : )", text_color="green")
    except:
        finishedlabel.configure(
            text="Invalid YouTube link! : (", text_color="red")


def onProgress(streams, chunk, bytes_remaining):
    totalSize = streams.filesize
    bytesDownloaded = totalSize - bytes_remaining
    percentageCompletion = bytesDownloaded / totalSize * 100
    perCompletion = str(int(percentageCompletion))
    progPercentage.configure(text=perCompletion + " %")
    progPercentage.update()

    # Update progress bar
    progBar.set(float(percentageCompletion) / 100)


# System Settings
c.set_appearance_mode("System")
c.set_default_color_theme("blue")

# App Frame
app = c.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI Elements

# Header text
title = c.CTkLabel(
    app,
    text="Insert a youtube video link"
)
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = c.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished download label
finishedlabel = c.CTkLabel(app, text="")
finishedlabel.pack()

# Progress percentage
progPercentage = c.CTkLabel(app, text="0 %")
progPercentage.pack()

progBar = c.CTkProgressBar(app, width=400)
progBar.set(0)
progBar.pack()

# Dowwnload button
dwld_btn = c.CTkButton(
    app, text="Download", command=download)
dwld_btn.pack(padx=10, pady=20)


# Render Loop
app.mainloop()
