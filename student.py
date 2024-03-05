from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("830x640+20+20")
        self.root.title("Face Recognition System")

        #add background images
        img = Image.open("H:\\My Drive\\Python-Projects-SAMS\\images\\9117392.jpg")
        img = img.resize((1000,800))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1000, height=800)

        # Title Label
        title_lable = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("Arial",20, "bold"),bg="white", fg="darkgreen")
        title_lable.place(x=0, y=0, width=1000,height=60)

        #main frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20,y=60,width=780, height=720)

        #left label frame
        left_frame = LabelFrame(main_frame, bd=2,bg="gray", relief=RIDGE, text="Student Details", font=("Arial", 10, "bold" ))
        left_frame.place(x=10,y=10, width=360, height=500)

        #Current Course
        current_course_frame = LabelFrame(left_frame, bd=2,bg="gray", relief=RIDGE, text="Current Course", font=("Arial", 10, "bold" ))
        current_course_frame.place(x=10,y=10, width=340, height=160)

        #department Lable
        dep_label = Label(current_course_frame, text="Department", bg="white", font=("Arial", 10, "bold" ), width=10 )
        dep_label.grid(row=0, column=0, padx=10)

        #department ComboBox
        dep_combo = ttk.Combobox(current_course_frame, font=("Arial", 10, "bold" ), state="readonly",width=17)
        dep_combo["values"]=("Select Department", "Computer", "IT", "Business")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=2)

        #Course Lable
        course_label = Label(current_course_frame, text="Course", bg="white", font=("Arial", 10, "bold" ), width=10 )
        course_label.grid(row=1, column=0, padx=10)

        #Course ComboBox
        course_combo = ttk.Combobox(current_course_frame, font=("Arial", 10, "bold" ), state="readonly",width=17)
        course_combo["values"]=("Select Course", "Computer", "IT", "Business")
        course_combo.current(0)
        course_combo.grid(row=1, column=1, padx=2, pady=2)

        #Year Lable
        year_label = Label(current_course_frame, text="Year", bg="white", font=("Arial", 10, "bold" ), width=10 )
        year_label.grid(row=2, column=0, padx=10)

        #Year ComboBox
        year_combo = ttk.Combobox(current_course_frame, font=("Arial", 10, "bold" ), state="readonly",width=17)
        year_combo["values"]=("Select year", "Computer", "IT", "Business")
        year_combo.current(0)
        year_combo.grid(row=2, column=1, padx=2, pady=2)

        #Semester Lable
        year_label = Label(current_course_frame, text="Semester", bg="white", font=("Arial", 10, "bold" ), width=10 )
        year_label.grid(row=3, column=0, padx=10)

        #Semester ComboBox
        semester_combo = ttk.Combobox(current_course_frame, font=("Arial", 10, "bold" ), state="readonly",width=17)
        semester_combo["values"]=("Select year", "Computer", "IT", "Business")
        semester_combo.current(0)
        semester_combo.grid(row=3, column=1, padx=2, pady=2)

        #Class Student Information frame
        class_student_frame = LabelFrame(left_frame, bd=2,bg="gray", relief=RIDGE, text="Class Student Information", font=("Arial", 10, "bold" ))
        class_student_frame.place(x=10,y=200, width=340, height=260)

        #Student ID Lable
        studentid_label = Label(class_student_frame, text="Student ID", bg="white", font=("Arial", 10, "bold" ), width=10 )
        studentid_label.grid(row=0, column=0, padx=10)

        #Student ID Entry
        studentid_entry = Entry(class_student_frame, width=20, font=("Arial", 10, "bold" ))
        studentid_entry.grid(row=0, column=1, padx=2, pady=2)

        #Student Name Lable
        studentname_label = Label(class_student_frame, text="Student Name", bg="white", font=("Arial", 10, "bold" ), width=10 )
        studentname_label.grid(row=1, column=0, padx=10)

        #Student Name Entry
        studentname_entry = Entry(class_student_frame, width=20, font=("Arial", 10, "bold" ))
        studentname_entry.grid(row=1, column=1)

        #Student Roll No. Lable
        studentrollno_label = Label(class_student_frame, text="Student Roll No", bg="white", font=("Arial", 10, "bold" ), width=10 )
        studentrollno_label.grid(row=2, column=0, padx=10)

        #Student Roll No. Entry
        studentrollno_entry = Entry(class_student_frame, width=20, font=("Arial", 10, "bold" ))
        studentrollno_entry.grid(row=2, column=1)

        #Radio Buttons
        radiobtn1=ttk.Radiobutton(class_student_frame, text="Take Photo Sample", value="yes")
        radiobtn1.grid(row=5, column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame, text="No Take Photo Sample", value="yes")
        radiobtn2.grid(row=5, column=1)

        #bbuttons frame
        btn_frame = Frame(class_student_frame, bd=2,bg="blue", relief=RIDGE)
        btn_frame.place(x=0,y=150, width=340, height=200)

        #Save button
        save_btn=Button(btn_frame, text="Save", width=8, font=("Arial", 10, "bold"))
        save_btn.grid(row=0, column=0)

        #Update button
        update_btn=Button(btn_frame, text="Update", width=8, font=("Arial", 10, "bold"))
        update_btn.grid(row=0, column=1)

        #Delete button
        delete_btn=Button(btn_frame, text="Delete", width=8, font=("Arial", 10, "bold"))
        delete_btn.grid(row=0, column=2)

        #Reset button
        reset_btn=Button(btn_frame, text="Reset", width=8, font=("Arial", 10, "bold"))
        reset_btn.grid(row=0, column=3)

        #Take a Photo button
        take_photo_btn=Button(btn_frame, text="Take Photo", width=8, font=("Arial", 10, "bold"))
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

        self.student_table=ttk.Treeview(table_frame,columns=("dept","course", "year", "semester", "rollno", "student_name", "father_name"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("rollno", text="Roll No")
        self.student_table.heading("student_name", text="Student Name")
        self.student_table.heading("father_name", text="Father Name")

        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("rollno", width=100)
        self.student_table.column("student_name", width=100)
        self.student_table.column("father_name", width=100)
         
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH, expand=1)
        
      
if __name__== "__main__":
    root = Tk()
    obj=Student(root)
    root.mainloop()
