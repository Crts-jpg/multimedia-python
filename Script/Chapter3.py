from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

video = VideoFileClip('/workspaces/multimedia-python/Video/Deadpool_Intro.mp4')

video.write_videofile('.././Video/Deadpool_joget.mp4')

short_video = video.subclip(0, 10)
short_video.write_videofile('.././Video/Short_DP.mp4')

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('.././Video/gabunganShort_dan_aslinya.mp4')

reversed_video = short_video.fx(vfx.time_mirror)
reversed_video.write_videofile('.././Video/MJ_tapi_reverse.mp4')

speed_up_video = short_video.fx(vfx.speedx, 2)
speed_up_video.write_videofile('.././Video/DP_buutFastt.mp4')

# ? hasilnya ada di folder script


# ! GUI Tkinter

import tkinter as tk

root = tk.Tk()
root.title('Multimedia DP')

root.mainloop()

# ! Buat Gambar
from PIL import Image, ImageTk

image = Image.open('/workspaces/multimedia-python/Gambar/IamMarvelJesus.jpg')
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack()

# ! klo ini audio

from tkinter import filedialog
from pydub import AudioSegment
from pydub.playback import play

def play_musik():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

play_button = tk.Button(root, text="play", command=play_musik)
play_button.pack()