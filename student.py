from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

Window_Geometry = "830x640+20+20"
sizeX = 830
sizeY = 640

class Student:
    def __init__(self, root):
        #Make a Window
        self.root=root
        self.root.geometry(Window_Geometry)
        self.root.title("Face Recognition System")

        #variables
        self.var_dept = StringVar()
        self.var_course  = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_student_name = StringVar()
        self.var_father_name = StringVar()
        self.var_address = StringVar()
        self.var_phone = StringVar()


        #add background images
        img = Image.open("H:\\My Drive\\Python-Projects-SAMS\\images\\9117392.jpg")
        img = img.resize((1000,800))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1000, height=800)

        # Title Label
        title_lable = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Arial",20, "bold"),bg="blue", fg="yellow")
        title_lable.place(x=0, y=0, width=1000,height=60)

        #main frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20,y=60,width=780, height=720)

        #left label frame
        left_frame = LabelFrame(main_frame, bd=2,bg="darkgray", relief=RIDGE, text="Student Details", font=("Arial", 10, "bold" ))
        left_frame.place(x=10,y=10, width=360, height=500)

        #Current Course
        current_course_frame = LabelFrame(left_frame, bd=2,bg="gray", relief=RIDGE, text="Current Course", font=("Arial", 10, "bold" ))
        current_course_frame.place(x=10,y=10, width=340, height=160)

        #department Lable
        dep_label = Label(current_course_frame, text="Department", bg="white", font=("Arial", 10, "bold" ), width=10 )
        dep_label.grid(row=0, column=0, padx=20)

        #department ComboBox
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dept, font=("Arial", 10, "bold" ), state="readonly",width=17)
        dep_combo["values"]=("Select Department", "Computer", "Business")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=2)

        #Course Lable
        course_label = Label(current_course_frame, text="Course", bg="white", font=("Arial", 10, "bold" ), width=10 )
        course_label.grid(row=1, column=0, padx=20)

        #Course ComboBox
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("Arial", 10, "bold" ), state="readonly",width=17)
        course_combo["values"]=("Select Course", "Software Engineering", "IT", "Business Administration")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=2, pady=2)

        #Year Lable
        year_label = Label(current_course_frame, text="Year", bg="white", font=("Arial", 10, "bold" ), width=10 )
        year_label.grid(row=2, column=0, padx=10)

        #Year ComboBox
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("Arial", 10, "bold" ), state="readonly",width=17)
        year_combo["values"]=("Select year", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025")
        year_combo.current(0)
        year_combo.grid(row=2, column=1, padx=2, pady=2)

        #Semester Lable
        year_label = Label(current_course_frame, text="Semester", bg="white", font=("Arial", 10, "bold" ), width=10 )
        year_label.grid(row=3, column=0, padx=10)

        #Semester ComboBox
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("Arial", 10, "bold" ), state="readonly",width=17)
        semester_combo["values"]=("Select Semester", "1st", "2nd", "3rd", "4th")
        semester_combo.current(0)
        semester_combo.grid(row=3, column=1, padx=2, pady=2)

        #======Class Student Information frame======
        class_student_frame = LabelFrame(left_frame, bd=2,bg="gray", relief=RIDGE, text="Class Student Information", font=("Arial", 10, "bold" ))
        class_student_frame.place(x=10, y=200, width=340, height=300)

        #Student ID Lable
        studentid_label = Label(class_student_frame, text="Student ID", bg="white", font=("Arial", 10, "bold" ), width=10 )
        studentid_label.grid(row=0, column=0, padx=10)

        #Student ID Entry
        studentid_entry = Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=("Arial", 10, "bold" ))
        studentid_entry.grid(row=0, column=1, padx=2, pady=2)

        #Student Name Lable
        student_name_label = Label(class_student_frame, text="Student Name", bg="white", font=("Arial", 10, "bold" ), width=10 )
        student_name_label.grid(row=1, column=0, padx=10)

        #Student Name Entry
        student_name_entry = Entry(class_student_frame, textvariable=self.var_student_name, width=20, font=("Arial", 10, "bold" ))
        student_name_entry.grid(row=1, column=1)

        # Father Name Lable
        father_name_label = Label(class_student_frame, text="Father Name", bg="white", font=("Arial", 10, "bold" ), width=10 )
        father_name_label.grid(row=2, column=0, padx=10)

        # Father Name Entry
        father_name_entry = Entry(class_student_frame, textvariable=self.var_father_name, width=20, font=("Arial", 10, "bold" ))
        father_name_entry.grid(row=2, column=1)

        #Address Lable
        address_label = Label(class_student_frame, text="Address ", bg="white", font=("Arial", 10, "bold" ), width=10 )
        address_label.grid(row=3, column=0, padx=10)

        #Address Entry
        address_name_entry = Entry(class_student_frame, textvariable=self.var_address, width=20, font=("Arial", 10, "bold" ))
        address_name_entry.grid(row=3, column=1)

        #Phone Lable
        phone_label = Label(class_student_frame, text="Phone ", bg="white", font=("Arial", 10, "bold" ), width=10 )
        phone_label.grid(row=4, column=0, padx=10)

        #Phone Entry
        phone_entry = Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("Arial", 10, "bold" ))
        phone_entry.grid(row=4, column=1)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes") 
        radiobtn1.grid(row=6, column=0)

        #self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Take Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        #bbuttons frame
        btn_frame = Frame(class_student_frame, bd=2,bg="green", relief=RIDGE)
        btn_frame.place(x=0,y=180, width=340, height=200)

        #Save button
        save_btn=Button(btn_frame, text="Save", command=self.add_data, width=8, font=("Arial", 10, "bold"))
        save_btn.grid(row=0, column=0)

        #Update button
        update_btn=Button(btn_frame, text="Update", command=self.update_data, width=8, font=("Arial", 10, "bold"))
        update_btn.grid(row=0, column=1)

        #Delete button
        delete_btn=Button(btn_frame, text="Delete", command=self.delete_data, width=8, font=("Arial", 10, "bold"))
        delete_btn.grid(row=0, column=2)

        #Reset button
        reset_btn=Button(btn_frame, text="Reset", command=self.reset_data, width=8, font=("Arial", 10, "bold"))
        reset_btn.grid(row=0, column=3)

        #Take a Photo button
        take_photo_btn=Button(btn_frame, command=self.generate_dataset, text="Take Photo", width=8, font=("Arial", 10, "bold"))
        take_photo_btn.grid(row=2, column=0)

        #Update a Photo button
        update_photo_btn=Button(btn_frame, text="Update Photo", width=8, font=("Arial", 10, "bold"))
        update_photo_btn.grid(row=2, column=2)


        #Right label frame
        right_frame = LabelFrame(main_frame, bd=2,bg="lightgray", relief=RIDGE, text="Student Details", font=("Arial", 10, "bold" ))
        right_frame.place(x=370,y=10, width=400, height=500)

        # Search System

        #Search Student frame
        search_frame = LabelFrame(right_frame, bd=2,bg="gray", relief=RIDGE, text="Search System", font=("Arial", 10, "bold" ))
        search_frame.place(x=10,y=10, width=400, height=500)

        #Search Label
        search_label = Label(search_frame, text="Search By:")
        search_label.grid(row=0,column=0, padx=2, pady=2, sticky=W)

        #Search ComboBox
        search_combo = ttk.Combobox(search_frame, font=("Arial", 10, "bold" ), state="readonly",width=17)
        search_combo["values"]=("Select", "Roll No", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=2, sticky=W)

        #Search Entry
        search_entry = Entry(search_frame, width=20, font=("Arial", 10, "bold" ))
        search_entry.grid(row=0, column=2)

        #Search button
        search_btn=Button(search_frame, text="Search", width=8, font=("Arial", 10, "bold"))
        search_btn.grid(row=1, column=0)

        #Show All button
        showAll_btn=Button(search_frame, text="Show All", width=8, font=("Arial", 10, "bold"))
        showAll_btn.grid(row=1, column=1)

        #Table frame
        table_frame = Frame(right_frame, bd=2, bg="lightgray", relief=RIDGE)
        table_frame.place(x=10,y=120, width=380, height=360)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dept","course", "year", "semester", "std_id", "student_name", "father_name", "address", "phone", "sample_photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("std_id", text="Student ID")
        self.student_table.heading("student_name", text="Student Name")
        self.student_table.heading("father_name", text="Father Name")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("sample_photo", text="Sample Photo")
        

        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("std_id", width=100)
        self.student_table.column("student_name", width=100)
        self.student_table.column("father_name", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("sample_photo", width=100)
         
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # funciton declaration
    def add_data(self):
        if self.var_dept.get()=="Select Deparment" or self.var_student_name.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", user="root", password="password@123", database="sams")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.var_dept.get(), self.var_course.get(), self.var_semester.get(), self.var_year.get(), self.var_std_id.get(), self.var_student_name.get(), self.var_father_name.get(), self.var_address.get(), self.var_phone.get(), self.var_radio1.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Detailed has been added succesfully!", parent=self.root)        
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    

    #To Fetch Data from table and display in form
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", user="root", password="password@123", database="sams")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if (len(data) != 0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()



    #To get table data into form after click on record
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_year.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_student_name.set(data[5]),
        self.var_father_name.set(data[6]),
        self.var_address.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_radio1.set(data[9]),
      
    #To update table data into form after click on record
    def update_data(self):
        if self.var_dept.get()=="Select Deparment" or self.var_student_name.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update", "Do you want to Update Student Details?", parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost", user="root", password="password@123", database="sams")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student SET dept=%s, course=%s, semester=%s, year=%s, student_name=%s, father_name=%s, address=%s, phone=%s, sample_photo=%s where std_id=%s", (self.var_dept.get(), self.var_course.get(), self.var_semester.get(), self.var_year.get(), self.var_student_name.get(), self.var_father_name.get(), self.var_address.get(), self.var_phone.get(), self.var_radio1.get(), self.var_std_id.get()) )
                    #UPDATE `sams`.`student` SET `dept` = 'Computer', `semester` = '1st', `year` = '2024' WHERE (`std_id` = '2');

                else:
                    if not update:
                        return
        
                messagebox.showinfo("Success", "Student Details successfully updated!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #To Delete data
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student ID is required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete", "Do you want to Delete Student Details?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", user="root", password="password@123", database="sams")
                    my_cursor=conn.cursor()
                    sql="delete from student where std_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Record Deleted Successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    
    #To Reset data
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_semester.set("Select Semester")
        self.var_year.set("Select Year")

        self.var_std_id.set("")
        self.var_student_name.set("")
        self.var_father_name.set("")
        self.var_address.set("")
        self.var_phone.set("")
        self.var_radio1.set("")
        
    #SQL Query to insert record
    #INSERT INTO `sams`.`student` (`std_id`, `student_name`, `father_name`, `Address`, `phone`, `dept`, `course`, `semester`, `year`) VALUES ('1', 'Ali', 'Ahhmed', 'House NO. 123, Latifabad', '0333-1306603', 'Computer', 'BSWE', '2nd', '2024');
    
    
    # Generate data set or Take photo samples
    def generate_dataset(self):
        if self.var_dept.get()=="Select Deparment" or self.var_student_name.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", user="root", password="password@123", database="sams")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student SET dept=%s, course=%s, semester=%s, year=%s, student_name=%s, father_name=%s, address=%s, phone=%s, sample_photo=%s where std_id=%s", (self.var_dept.get(), self.var_course.get(), self.var_semester.get(), self.var_year.get(), self.var_student_name.get(), self.var_father_name.get(), self.var_address.get(), self.var_phone.get(), self.var_radio1.get(), self.var_std_id.get() == id+1 ) )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #Load predefined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling factor = 1.3
                    #Minimum Neighor = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                #open camera
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    
                        #cropped image/face
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        #Make file names
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Data Sets Completed Successfully!")
                

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


        
                

if __name__== "__main__":
    root = Tk()
    obj=Student(root)
    root.mainloop()
