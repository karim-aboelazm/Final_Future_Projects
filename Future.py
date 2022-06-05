# pip install tk
from tkinter import *
# pip install pillow
from PIL import Image, ImageTk

from assistant import Listen_name

class AnimateGifLabel(Label):
    def __init__(self, *argv, image = None,  **kwargs):
        self.master = 0
        self.filename = image
        self.check_cadrs()
        self.i = 0
        self.img = Image.open(image)
        self.img.seek(0)
        self.image = ImageTk.PhotoImage(self.img)
        super().__init__(*argv, image = self.image, **kwargs)
        if 'delay' in kwargs:
            self.delay = kwargs['delay']
        else:
            try:
                self.delay = self.img.info['duration']
            except:
                self.delay = 100
        self.after(self.delay, self.show_new_cadr)


    def check_cadrs(self):
        self.cadrs = Image.open(self.filename).n_frames
        
    def show_new_cadr(self):
        if self.i == self.cadrs:
            self.i=0
        self.img.seek(self.i)
        self.image = ImageTk.PhotoImage(self.img)
        self.config(image = self.image)
        self.i+=1
        self.master.after(self.delay, self.show_new_cadr)


root=Tk()
p1 = PhotoImage(file = 'voice-message.png')
  
# Setting icon of master window
root.iconphoto(False, p1)

root.title("FUTURE VOICE ASSISTANT")
canvas=Canvas(root,width=800,height=600)
root.resizable(False, False)

image=AnimateGifLabel(image = 'wel.gif') 

canvas.create_window(0,0,anchor=NW,window=image)
canvas.pack()


dwnd = PhotoImage(file='btn2.png')
button = Button(root, 
                text="",
                command=Listen_name,
                bg="#2962ff",
                bd=0,
                image=dwnd,
                highlightthickness=0,
                borderwidth=0,
                relief='ridge',
                fg="#2962ff",
                activebackground="#2962ff",
                activeforeground="#2962ff",
                cursor="hand2")

button.place(x=350,y=230)

root.mainloop()
