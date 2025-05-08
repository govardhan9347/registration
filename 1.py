from tkinter import *
root=Tk()
def getvals():
    print("Accepted")
root.geometry("500x300")


Label(root ,text="Python Registraction Form" , font="arial 15 bold" ).grid(row=0,column=3)
name=Label(root,text="name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
mail=Label(root,text="mail")
Emergency=Label(root,text="Emergency")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
mail.grid(row=4,column=2)
Emergency.grid(row=5,column=2)

# variables strong the data
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
mailvalue=StringVar
Emergencyvalue=StringVar
Checkvalue=IntVar

# creating entry field
nameentry=Entry(root,textvariable="namevalue")
phoneentry=Entry(root,textvariable="phonevalue")
genderentry=Entry(root,textvariable="gendervalue")
mailentry=Entry(root,textvariable="mailvalue")
Emergencyentry=Entry(root,textvariable="Emergencyvalue")

#packing entry fiekds  

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
mailentry.grid(row=4,column=3)
Emergencyentry.grid(row=5,column=3)

# creating check box

Checkbtn=Checkbutton(text="remember me ?",variable=Checkvalue)
Checkbtn.grid(row=6,column=3)

# submit button

Button(text="Submit",command=getvals).grid(row=7,column=3)
root.mainloop()