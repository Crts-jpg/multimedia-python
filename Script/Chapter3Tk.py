import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pydub import AudioSegment
from pydub.playback import play

root = tk.Tk()
root.title('Multimedia DP')

def display_image(image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()
def play_musik():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)

display_image('../Gambar/IamMarvelJesus.jpg')

play_button = tk.Button(root, text="Play", command=play_musik)
play_button.pack()

root.mainloop()
