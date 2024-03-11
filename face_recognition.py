from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        #Make a Window
        self.root=root
        self.root.geometry("830x640+20+20")
        self.root.title("FACE RECOGNITION")

        #add background images
        img = Image.open("images\\9117392.jpg")
        img = img.resize((1000,800))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1000, height=800)

        # Title Label
        title_lable = Label(bg_img, text="FACE RECOGNITION", font=("Arial",20, "bold"),bg="white", fg="yellow")
        title_lable.place(x=0, y=0, width=1000,height=60)        #add background images
        img = Image.open("images\\9117392.jpg")
        img = img.resize((1000,800))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1000, height=800)

        # Title Label
        title_lable = Label(bg_img, text="FACE RECOGNITION", font=("Arial",20, "bold"),bg="lightgray", fg="yellow")
        title_lable.place(x=0, y=0, width=1000,height=60)

        # Training Button
        b1_1=Button(self.root, text="FACE RECOGNITION", command=self.face_recog, cursor="hand2", bg="purple", fg="white")
        b1_1.place(x=200,y=200, width=540, height=40)
    
    #Attendance
    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList =f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString}, {d1}, Present")


    #Face Recognition
    def face_recog(self):
        def draw_boundry(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x,y),(x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost", user="root", password="password@123", database="sams")
                my_cursor=conn.cursor()

                my_cursor.execute("select student_name from student where std_id = "+ str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select father_name from student where std_id = "+ str(id))
                f = my_cursor.fetchone()
                f = "+".join(f)

              
                if confidence > 77:
                    cv2.putText(img, f"Student ID:{id}",(x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Student Name:{i}",(x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Father Name:{f}",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img,(x,y),(x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face",(x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x,y,w,h]

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundry(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition: ", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__== "__main__":
    root = Tk()
    obj=Face_Recognition(root)
    root.mainloop()