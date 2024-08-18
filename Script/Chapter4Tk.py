import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pydub import AudioSegment
from pydub.playback import play

root = tk.Tk()
root.title('Multimedia DP')


def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack()
        
        
def play_musik():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        threading.Thread(target=play, args=(audio,)).start()
        

load_image_button = tk.Button(root, text="Load Image", command=load_image)
load_image_button.pack()

play_button = tk.Button(root, text="Play", command=play_musik)
play_button.pack()

label = tk.Label(root)
label.pack()

root.mainloop()