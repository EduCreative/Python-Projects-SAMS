from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

Window_Geometry = "830x640+20+20"
sizeX = 830
sizeY = 640
mydata=[]

class Attendance:
    def __init__(self, root):
        #Make a Window
        self.root=root
        self.root.geometry(Window_Geometry)
        self.root.title("ATTENDANCE")

        #variables
        self.var_dept = StringVar()
        self.var_std_id = StringVar()
        self.var_student_name = StringVar()
        self.var_father_name = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()
        global mydata

        #add background images
        img = Image.open("images\\9117392.jpg")
        img = img.resize((830,640))
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=830, height=640)

        # Title Label
        title_lable = Label(bg_img, text="ATTENDANCE MANAGEMENT", font=("Arial",20, "bold"),bg="blue", fg="yellow")
        title_lable.place(x=0, y=0, width=840,height=60)

        #main frame
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=20,y=60,width=780, height=720)

        #left label frame
        left_frame = LabelFrame(main_frame, bd=2,bg="darkgray", relief=RIDGE, text="Student Attendance Details", font=("Arial", 10, "bold" ))
        left_frame.place(x=10,y=10, width=360, height=500)

        #Left inside frame
        left_inside_frame = Frame(left_frame, bd=2,bg="gray", relief=RIDGE)
        left_inside_frame.place(x=10,y=30, width=340, height=160)

        #Label and Entry
        
        #Attendance ID Lable
        attendanceid_label = Label(left_inside_frame, text="Student ID", bg="white", font=("Arial", 10, "bold" ), width=10 )
        attendanceid_label.grid(row=0, column=0, padx=10)

        #Attendance ID Entry
        attendanceid_entry = Entry(left_inside_frame, textvariable=self.var_std_id, width=20, font=("Arial", 10, "bold" ))
        attendanceid_entry.grid(row=0, column=1, padx=2, pady=2)


        #Name ID Lable
        student_name_label = Label(left_inside_frame, text="Student Name", bg="white", font=("Arial", 10, "bold" ), width=10 )
        student_name_label.grid(row=1, column=0, padx=10)

        #Name ID Entry
        student_name_entry = Entry(left_inside_frame, textvariable=self.var_student_name, width=20, font=("Arial", 10, "bold" ))
        student_name_entry.grid(row=1, column=1, padx=2, pady=2)

        #Department Lable
        dept_label = Label(left_inside_frame, text="Department", bg="white", font=("Arial", 10, "bold" ), width=10 )
        dept_label.grid(row=2, column=0, padx=10)

        #Department Entry
        dept_entry = Entry(left_inside_frame, textvariable=self.var_dept, width=20, font=("Arial", 10, "bold" ))
        dept_entry.grid(row=2, column=1, padx=2, pady=2)

        #Date Lable
        date_label = Label(left_inside_frame, text="Date", bg="white", font=("Arial", 10, "bold" ), width=10 )
        date_label.grid(row=3, column=0, padx=10)

        #Date Entry
        date_entry = Entry(left_inside_frame, textvariable=self.var_date, width=20, font=("Arial", 10, "bold" ))
        date_entry.grid(row=3, column=1, padx=2, pady=2)

        #Time Lable
        time_label = Label(left_inside_frame, text="Time", bg="white", font=("Arial", 10, "bold" ), width=10 )
        time_label.grid(row=4, column=0, padx=10)

        #Time Entry
        time_entry = Entry(left_inside_frame, textvariable=self.var_time, width=20, font=("Arial", 10, "bold" ))
        time_entry.grid(row=4, column=1, padx=2, pady=2)

        #Attendance Lable
        attendance_label = Label(left_inside_frame, text="Attendance", bg="white", font=("Arial", 10, "bold" ), width=10 )
        attendance_label.grid(row=5, column=0, padx=10)

        #Attendance ComboBox
        attendance_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_attendance, font=("Arial", 10, "bold" ), state="readonly",width=17)
        attendance_combo["values"]=("Select Attendance", "Present", "Absent")
        # attendance_combo.current(0)
        attendance_combo.grid(row=5, column=1, padx=2, pady=2)

        #buttons frame
        btn_frame = Frame(left_frame, bd=2,bg="green", relief=RIDGE)
        btn_frame.place(x=0,y=180, width=340, height=200)

        #Save button
        save_btn=Button(btn_frame, text="Import CSV", command=self.importCSV, width=8, font=("Arial", 10, "bold"))
        save_btn.grid(row=0, column=0, padx=5)

        #Update button
        update_btn=Button(btn_frame, text="Export CSV", command=self.exportCSV, width=8, font=("Arial", 10, "bold"))
        update_btn.grid(row=0, column=1, padx=5)

        #Delete button
        delete_btn=Button(btn_frame, text="Update",  width=8, font=("Arial", 10, "bold"))
        delete_btn.grid(row=0, column=2,padx=5)

        #Reset button
        reset_btn=Button(btn_frame, text="Reset", command=self.reset_data, width=8, font=("Arial", 10, "bold"))
        reset_btn.grid(row=0, column=3, padx=5)


        #Right label frame
        right_frame = LabelFrame(main_frame, bd=2,bg="lightgray", relief=RIDGE, text="Student Details", font=("Arial", 10, "bold" ))
        right_frame.place(x=370,y=10, width=400, height=500)

        
        #Table frame
        table_frame = Frame(right_frame, bd=2, bg="lightgray", relief=RIDGE)
        table_frame.place(x=10,y=120, width=380, height=360)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("std_id", "student_name", "father_name", "dept", "date", "time", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("std_id", text="Student ID")
        self.student_table.heading("student_name", text="Student Name")
        self.student_table.heading("father_name", text="Father Name")
        self.student_table.heading("dept", text="Department")
        self.student_table.heading("date", text="Date")
        self.student_table.heading("time", text="Time")
        self.student_table.heading("attendance", text="Attendance")
        

        self.student_table.column("std_id", width=100)
        self.student_table.column("student_name", width=100)
        self.student_table.column("father_name", width=100)
        self.student_table.column("dept", width=100)
        self.student_table.column("date", width=100)
        self.student_table.column("time", width=100)
        self.student_table.column("attendance", width=100)
         
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetchData(mydata)


    #To get table data into form after click on record
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_student_name.set(data[1]),
        self.var_father_name.set(data[2]),
        self.var_dept.set(data[3]),
        self.var_date.set(data[5]),
        self.var_time.set(data[4]),
        self.var_attendance.set(data[6])

    def fetchData(self, rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert("", END, values=i)
    

    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #Export CSV
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No Data Found", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="\n") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your Data has been Exported to "+os.path.basename(fln)+ "Successfully", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #To Reset data
    def reset_data(self):
        self.var_attendance.set("Select Attendance")

        self.var_std_id.set("")
        self.var_student_name.set("")
        self.var_father_name.set("")
        self.var_dept.set("")
        self.var_date.set("")
        self.var_time.set("")

            



if __name__== "__main__":
    root = Tk()
    obj=Attendance(root)
    root.mainloop()
