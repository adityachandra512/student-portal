from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        #first image
        img=Image.open(r"C:\Users\adity\Downloads\face_recognitation_tkinter\college_images\face-recognition.png")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #Second image
        img1=Image.open(r"C:\Users\adity\Downloads\face_recognitation_tkinter\college_images\smart-attendance.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\adity\Downloads\face_recognitation_tkinter\college_images\iStock-182059956_18390_t12.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=1000,y=0,width=500,height=130)


        #background image
        img3=Image.open(r"C:\Users\adity\Downloads\face_recognitation_tkinter\college_images\R.jpeg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3) 
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new Roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"C:\Users\adity\Downloads\face_recognitation_tkinter\college_images\AdobeStock_303989091.jpeg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl2=Label(Left_frame,image=self.photoimg_left)
        f_lbl2.place(x=5,y=0,width=720,height=130)


        #current course informatation
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course Informatation",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=120)

        #Department
        dep_label=Label(current_course_frame,text='Department',font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17)
        dep_combo["value"]=("Select Department","Computer","IT","Civil","mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        course_combo["value"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        year_combo["value"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semerter
        Semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        Semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        Semester_combo["value"]=("Select Semester","Semester-1","Semester-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student informatation
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="class student Informatation",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=260,width=720,height=290)
        
        # Student ID
        studentId_label = Label(
            class_student_frame, text="Student ID:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(
            class_student_frame, text="Student Name:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(
            class_student_frame, text="Class Division:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(
            class_student_frame, text="Roll No:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(
            class_student_frame, text="Gender:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date of Birth
        dob_label = Label(
            class_student_frame, text="DOB:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(
            class_student_frame, text="Email:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_label = Label(
            class_student_frame, text="Phone No:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(
            class_student_frame, text="Address:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(
            class_student_frame, text="Teacher Name:", font=("Times New Roman", 12, "bold"), bg="white"
        )
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, width=20, font=("Times New Roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        #radio button
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo sample",value="YES")
        radiobtn1.grid(row=6,column=0)

        #no radio button
        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo sample",value="YES")
        radiobtn2.grid(row=6,column=1)

        #button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        #save button
        save_btn=Button(btn_frame,text="Save",font=("Times New Roman", 12, "bold"), bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0)

        #update button
        update_btn=Button(btn_frame,text="Update",font=("Times New Roman", 12, "bold"), bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1)

        #delete button
        delete_btn=Button(btn_frame,text="Delete",font=("Times New Roman", 12, "bold"), bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",font=("Times New Roman", 12, "bold"), bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
        #take photo button
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",font=("Times New Roman", 12, "bold"), bg="blue",fg="white",width=15)
        take_photo_btn.grid(row=0,column=0)

        #update photo button
        #reset button
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",font=("Times New Roman", 12, "bold"), bg="blue",fg="white",width=15)
        update_photo_btn.grid(row=0,column=1)

        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=660,height=580)


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()