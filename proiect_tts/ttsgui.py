from tkinter import *
import pyttsx3


class tts_gui:
    def __init__(self, master):
        self.master = master
        master.title("Sound with Interface")
        master.geometry("300x150")
        self.label = Label(master, text="Enter text to be read")
        self.label.pack()
        self.text = Entry(master)
        self.text.pack()
        self.button = Button(master, text="Play", command=self.play)
        self.button.pack()

    def play(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(self.text.get())
        engine.runAndWait()


root = Tk()
my_gui = tts_gui(root)
root.mainloop()