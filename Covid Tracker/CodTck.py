import tkinter as tk
import os
coro =tk.Tk()
coro.title("Corona Virus Information")
coro.geometry('800x500+200+100')
coro.configure(bg='#046173')
# coro.iconbitmap('corona.ico')     #download only ico files,
# coro.icon_path = 'corona.ico'



#labels

mainlabel = label(coro,text='Corona Virus Live Tracker ',font=('Times 20 bold',30,'bold'),bg = '#05897A',width=33,fg = 'black,bd=5')
mainlabel.place(x=0,y=0)

label1 = label(coro,text='Country Name',font=('Times 20 bold',30,'bold'),bg = '#046173')
label1.place(x=15,y=100)

label2 = label(coro,text='Download File in',font=('Times 20 bold',30,'bold'),bg = '#046173')
label2.place(x=15,y=200)
 
cntdata = StringVar()
entry1 =Entry(coro, textvariable    = cntdata ,font=('Times 20 bold',30,'italic bold'),relief=RIDGE, bd =2, width= 32) 
entry1.place(x=280,y=100)
 


coro.mainloop()
