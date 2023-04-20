import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox as msg
background_color = '#D6DBDF'
text_color = '#2C3E50'
button_color = '#95A5A6'

root = tk.Tk()
root.title('Text Editor')
image = tk.PhotoImage(file='notepad.png')
root.iconphoto(None,image)
root.geometry('680x540')
root.resizable(False,False)

var = tk.StringVar()
def save_me():
    f_name = label.get()
    text = text_area.get("1.0", tk.END)
    if f_name:
        with open(f_name,'w+') as f:
            f.write(text)
        msg.showinfo(message =str(f_name+' Added Successfully'),title='Success')
        label.delete("0",tk.END)
        text_area.delete("1.0", tk.END)
        

text_area = scrolledtext.ScrolledText(root,font=('Halvatika',16),height=20,width=54,wrap = tk.WORD,bg=background_color,fg=text_color)
text_area.grid(column=0,row=0,columnspan=3,padx=5,pady=5)

text_label = tk.Label(text="Enter File Name: ",font=('Halvatika',14))
text_label.grid(row=1,column=0,sticky='W',padx=5,pady=5)
label = tk.Entry(root,font=('Halvatika',14),bg=background_color,fg=text_color)
label.grid(row=1,column=1,padx=5,pady=5,sticky='W')
button = tk.Button(text='Save',padx=5,command=save_me,bg=button_color,fg=text_color,font=('Halvatika',14))
button.grid(row=1,column=2,padx=5,pady=5,sticky='E')


root.mainloop()