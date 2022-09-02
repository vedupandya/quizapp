import tkinter
from PIL import Image, ImageTk, ImageSequence

filepath = 'right.gif'


class App:
    def __init__(self, parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(
            parent,
            height=200, width=200,
            bg="#ffffff",
            bd=0,
            )
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                         for img in ImageSequence.Iterator(
                                    Image.open(filepath))]
        self.image = self.canvas.create_image(100, 100, image=self.sequence[0])
        self.animate(1)

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(70, lambda: self.animate((counter+1)
                                                   % len(self.sequence)))
