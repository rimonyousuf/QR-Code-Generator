from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage


class qr_generator:
    def __init__(self,root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("900x500+200+50")
        self.root.resizable(False,False)

        title = Label(self.root,text="QR Code Generator",font=('times new roman',30,'bold'),bg='green',fg='white')
        title.place(x=0,y=0,relwidth=1)


        #Variables
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_session=StringVar()

        #Person Detail
        per_details=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        per_details.place(x=50,y=85,width=500,height=380)

        per_title=Label(per_details,text="Person Details",font=('goudy old style',25,'bold'),bg='#698B69',fg='white')
        per_title.place(x=0,y=0,relwidth=1)

        #Person ID
        per_id=Label(per_details,text='Student ID',font=('times new roman',15,'bold'),bg='white')
        per_id.place(x=20,y=60)

        txt_id=Entry(per_details,textvariable=self.var_id,font=('times new roman',15,'bold'),bg='#F0FFFF')
        txt_id.place(x=200,y=60)

        #Person Name
        per_name=Label(per_details,text='Student Name',font=('times new roman',15,'bold'),bg='white')
        per_name.place(x=20,y=100)

        txt_name=Entry(per_details,textvariable=self.var_name,font=('times new roman',15,'bold'),bg='#F0FFFF')
        txt_name.place(x=200,y=100)

        #Person Study
        per_study=Label(per_details,text='Course Name',font=('times new roman',15,'bold'),bg='white')
        per_study.place(x=20,y=140)

        txt_study=Entry(per_details,textvariable=self.var_course,font=('times new roman',15,'bold'),bg='#F0FFFF')
        txt_study.place(x=200,y=140)

        #Department
        dep=Label(per_details,text='Session',font=('times new roman',15,'bold'),bg='white')
        dep.place(x=20,y=180)

        txt_dep=Entry(per_details,textvariable=self.var_session,font=('times new roman',15,'bold'),bg='#F0FFFF')
        txt_dep.place(x=200,y=180)

        #Generate button
        gen_btn=Button(per_details,command=self.generate,text='Generate QR Code',font=('times new roman',15,'bold'),bg='#458B00',fg='white')
        gen_btn.place(x=40,y=250,width=200,height=30)

        #Clear button
        clear_btn=Button(per_details,command=self.clear_func,text='Clear',font=('times new roman',15,'bold'),bg='#3D9140',fg='white')
        clear_btn.place(x=250,y=250,width=150,height=30)

        self.lbl_msg=Label(per_details,text='',font=('times new roman',15),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)

        #QR Code Window
        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_frame.place(x=600,y=85,width=270,height=380)

        qr_title=Label(qr_frame,text="QR Code",font=('goudy old style',25,'bold'),bg='#698B69',fg='white')
        qr_title.place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_frame,text='QR Code not available',font=('times new roman',15),bg="#66CDAA",fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)


    def clear_func(self):
        self.var_id.set('')
        self.var_name.set('')
        self.var_course.set('')
        self.var_session.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')


    def generate(self):
        if self.var_id.get()=='' or self.var_name.get()=='' or self.var_course.get()=='' or self.var_session.get()=='':
            self.msg='All fields are required!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Student ID: {self.var_id.get()}\nStudent Name: {self.var_name.get()}\nCourse  Name: {self.var_course.get()}\nSession Name: {self.var_session.get()}")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            #print(qr_code)
            qr_code.save("G:/Rimon Study/QR Code Generator/QR Code Image"+str(self.var_id.get())+'.png')

            #QR Code Image
            self.im=ImageTk.PhotoImage(file="G:/Rimon Study/QR Code Generator/QR Code Image"+str(self.var_id.get())+'.png')
            self.qr_code.config(image=self.im)

            self.msg='QR Code Generate Successfully!'
            self.lbl_msg.config(text=self.msg,fg='green')


root = Tk()
obj = qr_generator(root)
root.mainloop()