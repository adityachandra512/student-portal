from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Attandance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

         # First image
        img = Image.open(r"college_images\smart-attendance.jpg")
        img = img.resize((800, 200), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second image
        img1 = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=800, y=0, width=800, height=200)

        # Background image
        img3 = Image.open(r"college_images\R.jpeg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("Times New Roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("Times New Roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"college_images\AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl2 = Label(Left_frame, image=self.photoimg_left)
        f_lbl2.place(x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=10, y=135, width=720, height=370)

        #=====label and entry==================
        #attendance id
        AttandanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("Times New Roman", 12, "bold"), bg="white")
        AttandanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        AttandanceID_entry = ttk.Entry(left_inside_frame, width=20, font=("Times New Roman", 12, "bold"))
        AttandanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # roll
        roll_label = Label(left_inside_frame, text="Roll:", font=("Times New Roman", 12, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=4, pady=8)
        atten_entry = ttk.Entry(left_inside_frame, width=20, font=("Times New Roman", 12, "bold"))
        atten_entry.grid(row=0, column=3, pady=8)

        #Name
        NameLabel = Label(left_inside_frame, text="Name:", font=("Times New Roman", 12, "bold"), bg="white")
        NameLabel.grid(row=1, column=0)
        atten_name = ttk.Entry(left_inside_frame, width=20, font=("Times New Roman", 12, "bold"))
        atten_name.grid(row=1, column=1)

        #department
        dep_label = Label(left_inside_frame, text='Department', font=("Times New Roman", 12, "bold"), bg="white")
        dep_label.grid(row=1, column=2)
        
        atten_dep=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)


        #time
        timeLable=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLable.grid(row=2,column=0)
        
        atten_time=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        #date
        dateLable=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        dateLable.grid(row=2,column=2)
        
        atten_date=ttk.Entry(left_inside_frame,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        #attendance
        attandanceLable=Label(left_inside_frame,text="Attendance Status:",bg="white",font="comicsansns 11 bold")
        attandanceLable.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
        self.atten_status["value"]=("status","present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        save_btn = Button(btn_frame, text="Import csv",  width=17, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv", width=17, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Updated", width=17, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",  width=17, font=("Times New Roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("Times New Roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=730, height=580)


if __name__ == "__main__":
    root = Tk()
    obj = Attandance(root)
    root.mainloop()
