import pygame # type: ignore
import PIL
import cv2
import moviepy.editor as mp # type: ignore
import pydub
import tkinter as tk

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:")
    print("✅ Pydub version:")
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()