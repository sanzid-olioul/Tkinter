import tkinter
'''
Defining a Window.
'''
window = tkinter.Tk()
window.geometry("680x550")
window.resizable(False,False)
window.title("My First")
image = tkinter.PhotoImage(file='marker.png')
window.config(bg='indigo')
window.iconphoto(False,image)
'''
Designing the body
'''
txt = tkinter.StringVar(window,"")
def call_me():
    txt.set('Hii , '+entry.get())
label1 = tkinter.Label(window,text = "Enter Your name",bg='indigo',fg='white',font=('arial',22,'bold'),pady=10)
label1.pack()
entry = tkinter.Entry(window,width=25,font=('arial',22,'bold'))
entry.pack(pady=10)
button = tkinter.Button(window,text='Say Hii',bg='green',fg='white',padx=5,pady=5,font=('arial',18),command=call_me,border=5)
button.pack(padx=10,pady=10)


label2 = tkinter.Label(window,textvariable = txt,bg='indigo',fg='white',font=('arial',18,'bold'),pady=10)
label2.pack()
window.mainloop()