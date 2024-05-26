from tkinter import*
import tkSnack

root = Tk()
tkSnack.initializeSnack(root)

snd = tkSnack.Sound()
snd.read('sound.mp3')
snd.play(blocking=1)