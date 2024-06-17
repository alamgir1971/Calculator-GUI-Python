
import tkinter as tk
root= tk.Tk()
root.title("Calculator by Md. Alamgir")
canvas1 = tk.Canvas(root, width = 320, height = 300, bg="salmon")
canvas1.pack()
entry1 = tk.Entry (root) 
canvas1.create_window(210, 100, window=entry1)
entry2 = tk.Entry (root) 
canvas1.create_window(210, 140, window=entry2)
entry3 = tk.Entry (root) 
canvas1.create_window(210, 240, window=entry3)

label1 = tk.Label(root, text='First number ')
label1.config(font=('helvetica', 10))
canvas1.create_window(100, 100, window=label1)
label2 = tk.Label(root, text='Second number')
label2.config(font=('helvetica', 10))
canvas1.create_window(85, 140, window=label2)

label3 = tk.Label(root, text='Result', bg= "yellow")
label3.config(font=('helvetica', 10, 'bold'))
canvas1.create_window(120, 240, window=label3)

def add():  
    v1 = entry1.get()
    v2 = entry2.get()
    label4 = tk.Label(root, text= float(v1)+float(v2),font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(210, 240, window=label4)
      
buttonAdd = tk.Button(text='Add', command=add, bg='blue', fg='white', font=('helvetica', 9, 'bold'), width = 5)
canvas1.create_window(90, 190, window=buttonAdd)

def sub():  
    v1 = entry1.get()
    v2 = entry2.get()
    label5 = tk.Label(root, text= float(v1)-float(v2),font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(210, 240, window=label5)
buttonSub = tk.Button(text='Sub', command=sub, bg='green', fg='white', font=('helvetica', 9, 'bold'), width = 5)
canvas1.create_window(140, 190, window=buttonSub)

def mul():  
    v1 = entry1.get()
    v2 = entry2.get()
    label6 = tk.Label(root, text= float(v1)*float(v2),font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(210, 240, window=label6)
      
buttonMul = tk.Button(text='Multi', command=mul, bg='red', fg='white', font=('helvetica', 9, 'bold'), width = 5)
canvas1.create_window(190, 190, window=buttonMul)

def div():  
    v1 = entry1.get()
    v2 = entry2.get()
    label7 = tk.Label(root, text= float(v1)/float(v2),font=('helvetica', 10, 'bold'),bg='white')
    canvas1.create_window(210, 240, window=label7)
      
buttonDiv = tk.Button(text='Div', command=div, bg='gray', fg='white', font=('helvetica', 9, 'bold'), width = 5)
canvas1.create_window(240, 190, window=buttonDiv)

root.mainloop()
