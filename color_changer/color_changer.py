import tkinter as tk

red = 'red'
blue = 'blue'
green = 'green'
root = tk.Tk()
root.geometry('550x500')
root.resizable(False,False)
root.title('Color changer')
root.config(bg='red')
var = tk.StringVar()
def changer():
    root.config(bg=var.get())

radio1 = tk.Radiobutton(root,text="Red",value=red,variable=var,command=changer)
radio1.grid(row=0,column=0,padx=10,pady=10)
radio1.select()
radio2 = tk.Radiobutton(root,text="Blue",value=blue,variable=var,command=changer)
radio2.grid(row=0,column=1,padx=10,pady=10)

radio3 = tk.Radiobutton(root,text="Green",value=green,variable=var,command=changer)
radio3.grid(row=0,column=2,padx=10,pady=10)

root.mainloop()
