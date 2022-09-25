from tkinter import *


class qr_generator:
    def __init__(self,root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("900x500+200+50")
        self.root.resizable(False,False)

        title = Label(self.root,text="QR Code Generator",font=('times new roman',30,'bold'),bg='green',fg='white')
        title.place(x=0,y=0,relwidth=1)

        #Person Detail
        per_details=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        per_details.place(x=50,y=85,width=500,height=380)

        per_title=Label(per_details,text="Person Details",font=('goudy old style',25,'bold'),bg='#698B69',fg='white')
        per_title.place(x=0,y=0,relwidth=1)

        #Person ID
        per_id=Label(per_details,text='Person ID',font=('times new roman',15,'bold'),bg='white')
        per_id.place(x=20,y=60)

        txt_id=Entry(per_details,font=('times new roman',15,'bold'),bg='#F0FFFF')
        txt_id.place(x=200,y=60)

        #Person Name
        per_name=Label(per_details,text='Person Name',font=('times new roman',15,'bold'),bg='white')
        per_name.place(x=20,y=100)

        txt_name=Entry(per_details,font=('times new roman',15,'bold'),bg='#F0FFFF')
        txt_name.place(x=200,y=100)

        #Person Study
        per_study=Label(per_details,text='Person Study',font=('times new roman',15,'bold'),bg='white')
        per_study.place(x=20,y=140)

        txt_study=Entry(per_details,font=('times new roman',15,'bold'),bg='#F0FFFF')
        txt_study.place(x=200,y=140)

        #Department
        dep=Label(per_details,text='Person ID',font=('times new roman',15,'bold'),bg='white')
        dep.place(x=20,y=180)

        txt_dep=Entry(per_details,font=('times new roman',15,'bold'),bg='#F0FFFF')
        txt_dep.place(x=200,y=180)

        #Generate button
        gen_btn=Button(per_details,text='Generate QR Code',font=('times new roman',15,'bold'),bg='#458B00',fg='white')
        gen_btn.place(x=40,y=250,width=200,height=30)

        #Clear button
        clear_btn=Button(per_details,text='Clear',font=('times new roman',15,'bold'),bg='#3D9140',fg='white')
        clear_btn.place(x=250,y=250,width=150,height=30)


root = Tk()
obj = qr_generator(root)
root.mainloop()