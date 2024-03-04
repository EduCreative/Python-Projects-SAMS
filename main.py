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

        #add button image
        imgbtn1 = Image.open(r"H:\\My Drive\\Python-Projects-SAMS\\images\\add.png")
        imgbtn1 = imgbtn1.resize((50,60))
        self.btn1=ImageTk.PhotoImage(imgbtn1)

        b1=Button(bg_img, image=self.btn1, cursor="hand2")
        b1.place(x=200,y=100, width=130, height=100)

        b1_1=Button(bg_img, text="Add Student Detail", cursor="hand2")
        b1_1.place(x=200,y=200, width=130, height=40)

        #button
        imgbtn2 = Image.open(r"H:\\My Drive\\Python-Projects-SAMS\\images\\add.png")
        imgbtn2 = imgbtn2.resize((50,60))
        self.btn2=ImageTk.PhotoImage(imgbtn2)

        b2=Button(bg_img, image=self.btn2, cursor="hand2")
        b2.place(x=400,y=100, width=130, height=100)

        b2_2=Button(bg_img, text="Add Student Attendance", cursor="hand2")
        b2_2.place(x=400,y=200, width=130, height=40)

        #button
        imgbtn3 = Image.open(r"H:\\My Drive\\Python-Projects-SAMS\\images\\add.png")
        imgbtn3 = imgbtn3.resize((80,80))
        self.btn3=ImageTk.PhotoImage(imgbtn3)

        b3=Button(bg_img, image=self.btn3, cursor="hand2")
        b3.place(x=600,y=100, width=130, height=100)

        b3_3=Button(bg_img, text="Student Attendance", cursor="hand2")
        b3_3.place(x=600,y=200, width=130, height=40)

if __name__== "__main__":
    root = Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

