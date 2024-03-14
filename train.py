from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        #Make a Window
        self.root=root
        self.root.geometry("830x640+20+20")
        self.root.title("Train Dataset")

        #add background images
        img = Image.open("images\\9117392.jpg")
        img = img.resize((1000,800))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1000, height=800)

        
        #add background images
        img = Image.open("images\\9117392.jpg")
        img = img.resize((1000,800))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1000, height=800)

        # Title Label
        title_lable = Label(bg_img, text="TRAIN DATA SET", font=("Arial",20, "bold"),bg="white", fg="darkgreen")
        title_lable.place(x=0, y=0, width=860,height=60)

        # Training Button
        imgbtn2 = Image.open(r"images\\trainData.jpg")
        imgbtn2 = imgbtn2.resize((200, 160))
        self.btn2=ImageTk.PhotoImage(imgbtn2)

        b2=Button(self.root, image=self.btn2, command=self.train_classifier, cursor="hand2", bg="purple")
        b2.place(x=320,y=200, width=200, height=160)

        b2_1=Button(self.root, text="TRAIN DATA SET", command=self.train_classifier, cursor="hand2", bg="purple", fg="white")
        b2_1.place(x=320,y=360, width=200, height=40)


    def train_classifier(self):
        #messagebox.showinfo("Start", "Training datasets Started!")
        data_dir = ("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces=[] 
        ids=[]

        for image in path:
            img=Image.open(image).convert("L") #Gray Scale Image conversion
            imageNp = np.array(img, 'uint8')
            id= int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
            
        ids = np.array(ids)

        #Train the Classifier and save
        #clf = cv2.face.LBPHFaceRecognizer
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()

        messagebox.showinfo("Result", "Training datasets completed!")

if __name__== "__main__":
    root = Tk()
    obj=Train(root)
    root.mainloop()