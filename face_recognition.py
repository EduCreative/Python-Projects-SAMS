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
        title_lable.place(x=0, y=0, width=860,height=60)

        # Face Recognition Button
        imgbtn2 = Image.open(r"images\\faceRecognition.jpg")
        imgbtn2 = imgbtn2.resize((200, 160))
        self.btn2=ImageTk.PhotoImage(imgbtn2)

        b2=Button(self.root, image=self.btn2, command=self.face_recog, cursor="hand2", bg="purple")
        b2.place(x=320,y=200, width=200, height=160)

        b2_1=Button(self.root, text="FACE RECOGNITION", command=self.face_recog, cursor="hand2", bg="purple", fg="white")
        b2_1.place(x=320,y=360, width=200, height=40)
    
    #Attendance
    def mark_attendance(self, id, name, fname, dept):
        with open("attendance.csv", "r+", newline="\n") as myFile:
            myDataList = myFile.readlines()
            name_list = []
            print(myDataList)

            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
                #print(entry)                
            #print(name_list)
            #print(str(id))
            #print(str(id) not in name_list)

            if(str(id) not in name_list):
                print(name_list)
               #and (name not in name_list) and (fname not in name_list) and (dept not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                myFile.writelines(f"\n{id},{name},{fname},{dept},{dtString}, {d1}, Present")

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
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select father_name from student where std_id = "+ str(id))
                f = my_cursor.fetchone()
                f = "+".join(f)

                my_cursor.execute("select dept from student where std_id = "+ str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
              
                if confidence > 70:
                    cv2.putText(img, f"Student ID:{id}",(x,y-75), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Student Name:{n}",(x,y-55), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 3)
                    # cv2.putText(img, f"Father Name:{f}",(x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    # cv2.putText(img, f"Department:{d}",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Confidence:{confidence}%",(x,y-5), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 3)

                    self.mark_attendance(id, n, f, d)
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