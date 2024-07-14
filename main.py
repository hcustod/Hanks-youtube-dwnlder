import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import PytubeError, RegexMatchError, VideoUnavailable


def startDownload():
    try:
        ytLink = link.get()
        print(f"Attempting to download: {ytLink}")
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        statusLabel.configure(text="")
        video.download()
        statusLabel.configure(text="Downloaded!", text_color="green")
    except RegexMatchError:
        print("Invalid YouTube URL")
        statusLabel.configure(text="Invalid YouTube URL", text_color="red")
    except VideoUnavailable:
        print("Video is unavailable")
        statusLabel.configure(text="Video is unavailable", text_color="red")
    except PytubeError as e:
        print(f"Pytube error: {e}")
        statusLabel.configure(text=f"Download Error: Pytube issue - {e}", text_color="red")
    except Exception as e:
        print(f"General error: {e}")
        statusLabel.configure(text="Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completeion = bytes_downloaded / total_size * 100
    strPer = str(int(percentage_of_completeion))
    pPercentage.configure(text=strPer + '%')
    pPercentage.update()

    # Update progress bar
    progressBar.set(float(percentage_of_completeion) / 100)


#tkinter settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app settings
app = customtkinter.CTk()
app.geometry("720x720")
app.title("Hanks Youtube Downloader")

# UI title
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Inputing Link
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Status label
statusLabel = customtkinter.CTkLabel(app, text="")
statusLabel.pack()

# Progress bar percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()  

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download buttom
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=20)


app.mainloop()


