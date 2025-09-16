from tkinter import *
from tkinter import messagebox

from ReportPage1 import Report1Class
from ReportPage2 import Report2Class
from ReportPage3 import Report3Class
from avail import Avail
from changepasswordpage import ChangePasswordClass
from coursepage import CourseClass
from departmentpage1 import DepartmentClass
from studentpage import StudentClass

from PIL import Image, ImageTk

from userpage import UserClass


class HomepageClass:
    def __init__(self,un,ut):
        self.un=un
        self.ut=ut
        self.window = Tk()
        self.window.title("library_management")

        # ------------- settings ------------------
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()

        w1 = int(w/2)
        h1 = int(h/2)
        x1 = int(w/4)
        y1 = int(h/4)
        self.window.minsize(w1,h1)
        self.window.geometry("%dx%d+%d+%d"%(w1,h1,x1,y1))#wxh+x+y
        self.window.state('zoomed')

        #--------------- Frames -----------------
        f1_width=200
        f2_width=w-f1_width
        self.f1 = Frame(self.window,background='#982B1C')  #'#AB9F92' '#2a3d45'
        self.f2 = Frame(self.window,background='#AB9F92')
        self.f1.place(x=0,y=0,width=f1_width,height=h)
        self.f2.place(x=f1_width,y=0,width=f2_width,height=h)

        #---------------- Menu in frame 1 --------------------------
        x1=5
        y1=5
        b1_width=f1_width-10
        b1_height=50
        y_diff = b1_height+5
        if self.ut=='Admin':
            mycolor1='#2a3d45'
        else:
            mycolor1='#2a3d45'
        mycolor2='#AB9F92'
        myfont1 = ('Cambria',13,'bold')


        self.btnpimg1 = ImageTk.PhotoImage(Image.open("app_images//st.png").resize((30,20)))
        self.btnpimg2 = ImageTk.PhotoImage(Image.open("app_images//ab.png").resize((30,20)))
        self.btnpimg3 = ImageTk.PhotoImage(Image.open("app_images//user.png").resize((30,20)))
        self.btnpimg4 = ImageTk.PhotoImage(Image.open("app_images//r1.png").resize((30,20)))
        self.btnpimg5 = ImageTk.PhotoImage(Image.open("app_images//r2.png").resize((30,20)))
        self.btnpimg6 = ImageTk.PhotoImage(Image.open("app_images//r3.png").resize((30,20)))
        self.btnpimg7 = ImageTk.PhotoImage(Image.open("app_images//cp.png").resize((30,20)))
        self.btnpimg8 = ImageTk.PhotoImage(Image.open("app_images//lg.png").resize((30,20)))



        # self.b1 = Button(self.window,text='Student',command=lambda : StudentClass()) # to open independent window
        self.b1 = Button(self.window,foreground=mycolor2,text='Student',image=self.btnpimg1,compound=LEFT, background=mycolor1,font=myfont1,command=lambda : StudentClass(self.window)) # to open dependent window
        self.b2 = Button(self.window,foreground=mycolor2,text='Available Books',image=self.btnpimg2,compound=LEFT, background=mycolor1,font=myfont1,command=lambda : Avail(self.window)) # to open dependent window
        self.b3 = Button(self.window,foreground=mycolor2,text='Course',background=mycolor1,image=self.btnpimg1,font=myfont1,command=lambda : CourseClass(self.window)) # to open dependent window
        self.b4 = Button(self.window,foreground=mycolor2,text='User',image=self.btnpimg3,compound=LEFT, background=mycolor1,font=myfont1,command=lambda : UserClass(self.window)) # to open dependent window
        self.b5 = Button(self.window,foreground=mycolor2,text='Report',image=self.btnpimg4,compound=LEFT, background=mycolor1,font=myfont1,command=lambda : Report1Class(self.window)) # to open dependent window
        self.b6 = Button(self.window,foreground=mycolor2,text='Books Report',image=self.btnpimg5,compound=LEFT, background=mycolor1,font=myfont1,command=lambda : Report2Class(self.window)) # to open dependent window
        self.b7 = Button(self.window,foreground=mycolor2,text='Report By Date',image=self.btnpimg6,compound=LEFT, background=mycolor1,font=myfont1,command=lambda : Report3Class(self.window)) # to open dependent window
        self.b8 = Button(self.window,foreground=mycolor2,text='Change Password',image=self.btnpimg7,compound=LEFT, background=mycolor1,font=myfont1,command=lambda : ChangePasswordClass(self.window,self.un)) # to open dependent window
        self.b9 = Button(self.window,foreground=mycolor2,text='Logout',image=self.btnpimg8,compound=LEFT, background=mycolor1,font=myfont1,command=self.quitter ) # to open dependent window


        if self.ut=="Employee":
            self.b6['state']='disable'

        #------------- placement -------------------
        self.b1.place(x=x1,y=y1,width=b1_width,height=b1_height)
        y1+=y_diff
        self.b2.place(x=x1,y=y1,width=b1_width,height=b1_height)
        # y1+=y_diff
        # self.b3.place(x=x1,y=y1,width=b1_width,height=b1_height)
        y1+=y_diff
        if self.ut=='Admin':
            self.b4.place(x=x1,y=y1,width=b1_width,height=b1_height)
            y1+=y_diff
        self.b5.place(x=x1,y=y1,width=b1_width,height=b1_height)
        y1+=y_diff
        self.b6.place(x=x1,y=y1,width=b1_width,height=b1_height)
        y1+=y_diff
        # if self.ut=='Admin':
        #     self.b7.place(x=x1,y=y1,width=b1_width,height=b1_height)
        #     y1+=y_diff
        self.b8.place(x=x1,y=y1+400,width=b1_width,height=b1_height)
        y1+=y_diff
        self.b9.place(x=x1,y=y1+400,width=b1_width,height=b1_height)
        y1+=y_diff


        #------------------ Background in Frame 2 ----------------------
        # show image
        self.bkimg1 = Image.open("app_images//opp.jpg").resize((f2_width,h))
        self.bkpimg1 = ImageTk.PhotoImage(self.bkimg1)
        self.bklbl = Label(self.f2,image=self.bkpimg1)
        self.bklbl.place(x=0,y=0)

        #--------------------------------------------------------------------


        self.window.mainloop()

    def quitter(self):
        ans = messagebox.askquestion("Confirmation","Are you sure to Logout??",parent=self.window)
        if ans=='yes':
            self.window.destroy()
            from Loginpage import LoginClass
            LoginClass()

