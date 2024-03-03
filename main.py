from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("830x640+20+20")
        self.root.title("Face Recognition System")

        #add background images
        img = Image.open("H:\\My Drive\\Python-Projects-SAMS\\images\\9117392.jpg")
        img = img.resize((830,640))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=830, height=640)

        # Title Label
        title_lable = Label(bg_img, text="FACE RECOGNTION ATTENDANCE SYSTEM", font=("Arial",20, "bold"),bg="white", fg="red")
        title_lable.place(x=0, y=0, width=840,height=60)

if __name__== "__main__":
    root = Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

