import tkinter as tk
from tkinter import ttk
'''
Creating Window
'''
background_color = '#D6DBDF'
text_color = '#2C3E50'
button_color = '#95A5A6'
root = tk.Tk()
root.title("BMI Calculator")
img = tk.PhotoImage(file='bmi.png')
root.iconphoto(None,img)
root.config(bg=background_color)
root.geometry('680x540')
root.resizable(False,False)
'''
Creating Body
'''

scale_type = tk.StringVar()
label1 = tk.Label(root,text='Enter the height : ',bg=background_color,fg=text_color,font=('Helvetica',18,'bold'),padx=10,pady=10)
label1.grid(row=0,column=0,padx=10,pady=10)
height = tk.Entry(root,width=10,bg=background_color,fg=text_color,font=('Helvetica',18,'bold'))
height.grid(row=0,column=1,padx=10,pady=10)
style = ttk.Style(root)
style.configure('.',bg=background_color)
scale = ttk.Combobox(root,textvariable=scale_type,state='readonly',font=('Helvetica',18,'bold'),values=['Feet','CM','M'],width=7)
scale.grid(row=0,column=2)
scale.current(0)


label2 = tk.Label(root,text='Enter the weight : ',bg=background_color,fg=text_color,font=('Helvetica',18,'bold'),padx=10,pady=10)
label2.grid(row=1,column=0,padx=10,pady=10)
weight = tk.Entry(root,width=10,bg=background_color,fg=text_color,font=('Helvetica',18,'bold'))
weight.grid(row=1,column=1,padx=10,pady=10)
label2 = tk.Label(root,text=' Kg ',bg=background_color,fg=text_color,font=('Helvetica',18,'bold'),padx=10,pady=10)
label2.grid(row=1,column=2,padx=10,pady=10)

result = tk.StringVar()
comment = tk.StringVar()
def calculate():
    meeter : float
    try:
        match scale.get():
            case 'Feet':
                meeter = 0.3048 * float(height.get())
            case 'CM':
                meeter = float(height.get())/100
            case other:
                meeter = float(height.get())
        result.set("BMI : "+format(float(weight.get())/(meeter**2),'.2f'))
    except Exception as e:
        result.set(e)
    if meeter:
        if meeter < 18.5:
            comment.set('Comment : You are under weight')
        elif meeter < 24.9:
            comment.set('Comment : You are in perfect weight')
        else:
            comment.set('Comment : You are over weight')


button = tk.Button(root,text='Calculate',command=calculate,bg=button_color,fg=text_color,font=('Helvetica',18,'bold'),padx=10,pady=10)
button.grid(row=2,column=1,padx=10,pady=10)

label3 = tk.Label(root,textvariable= result ,bg=background_color,fg=text_color,font=('Helvetica',18,'bold'),padx=10,pady=10)
label3.grid(row=3,column=0,columnspan=1,padx=10,pady=10)
label4 = tk.Label(root,textvariable= comment ,bg=background_color,fg=text_color,font=('Helvetica',18,'bold'),padx=10,pady=10)
label4.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky='WE')
root.mainloop()







