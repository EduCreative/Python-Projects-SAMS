from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os

from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendace import Attendance

Window_Geometry = "830x640+20+20"
sizeX = 830
sizeY = 640
class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry(Window_Geometry)
        self.root.title("Face Recognition Attendance System")

        #add background images
        img = Image.open("images\\9117392.jpg")
        img = img.resize((sizeX, sizeY))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=sizeX, height=sizeY)

        # Title Label
        title_lable = Label(bg_img, text="FACE RECOGNTION ATTENDANCE SYSTEM", font=("Arial",20, "bold"),bg="yellow", fg="blue")
        title_lable.place(x=0, y=0, width=sizeX, height=60)

        #add button image
        imgbtn1 = Image.open(r"images\\add.jpg")
        imgbtn1 = imgbtn1.resize((200, 160))
        self.btn1=ImageTk.PhotoImage(imgbtn1)

        b1=Button(bg_img, image = self.btn1, command = self.student_details, cursor="hand2", bg="purple")
        b1.place(x=20,y=100, width=200, height=160)

        b1_1=Button(bg_img, text="Add Student Detail", command = self.student_details, cursor="hand2", bg="purple", fg="white", font=("Arial",10, "bold"))
        b1_1.place(x=20,y=260, width=200, height=40)

        #button
        imgbtn2 = Image.open(r"images\\faceRecognition.jpg")
        imgbtn2 = imgbtn2.resize((200, 160))
        self.btn2=ImageTk.PhotoImage(imgbtn2)

        b2=Button(bg_img, image=self.btn2, command=self.face_data, cursor="hand2", bg="purple")
        b2.place(x=20,y=400, width=200, height=160)

        b2_2=Button(bg_img, text="Face Recognition", command=self.face_data, cursor="hand2", bg="purple", fg="white", font=("Arial",10, "bold"))
        b2_2.place(x=20,y=560, width=200, height=40)

        #button
        imgbtn3 = Image.open(r"images\\attendance.jpg")
        imgbtn3 = imgbtn3.resize((200, 160))
        self.btn3=ImageTk.PhotoImage(imgbtn3)

        b3=Button(bg_img, image=self.btn3, command=self.add_attendance, cursor="hand2", bg="purple")
        b3.place(x=320,y=100, width=200, height=160)

        b3_3=Button(bg_img, text="Attendance Record", command=self.add_attendance, cursor="hand2", bg="purple", fg="white", font=("Arial",10, "bold"))
        b3_3.place(x=320,y=260, width=200, height=40)


        #next row of buttons

        #add button image
        imgbtn5 = Image.open(r"images\\trainData.jpg")
        imgbtn5 = imgbtn5.resize((200, 160))
        self.btn5=ImageTk.PhotoImage(imgbtn5)

        b5=Button(bg_img, image=self.btn5, command=self.train_data, cursor="hand2", bg="purple")
        b5.place(x=320,y=400, width=200, height=160)

        b5_5=Button(bg_img, text="Train Data", command=self.train_data, cursor="hand2", bg="purple", fg="white", font=("Arial",10, "bold"))
        b5_5.place(x=320,y=560, width=200, height=40)

        #button
        imgbtn6 = Image.open(r"images\\photos.jpg")
        imgbtn6 = imgbtn6.resize((200, 160))
        self.btn6=ImageTk.PhotoImage(imgbtn6)

        b6=Button(bg_img, image=self.btn6, cursor="hand2", bg="blue", command=self.open_img,)
        b6.place(x=620,y=100, width=200, height=160)

        b6_6=Button(bg_img, command=self.open_img, text="Photos", cursor="hand2", bg="purple", fg="white", font=("Arial",10, "bold"))
        b6_6.place(x=620,y=260, width=200, height=40)

        #button
        imgbtn8 = Image.open(r"images\\exit.jpg")
        imgbtn8 = imgbtn8.resize((200, 160))
        self.btn8=ImageTk.PhotoImage(imgbtn8)

        b8=Button(bg_img, image=self.btn8, cursor="hand2", bg="red")
        b8.place(x=620,y=400, width=200, height=160)

        b8_8=Button(bg_img, text=" Exit ", cursor="hand2", font=("Arial",10, "bold"), bg="pink")
        b8_8.place(x=620,y=560, width=200, height=40)


    def open_img(self):
        os.startfile("data")

    #function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    #function buttons
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    #function buttons
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    #Add Attendance function button
    def add_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app = Attendance(self.new_window)



if __name__== "__main__":
    root = Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
