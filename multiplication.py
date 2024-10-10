from tkinter import *
from tkinter.ttk import *
#combobox is defined inside ttk

window = Tk()
window.geometry("450x700")
window.title("Times Tables")
Labelmaths = Label(window, text = "Mathematical Table")
Labelnum = Label(window, text = "Number and Range")

num = IntVar()
combo = Combobox(window,textvariable = num, width = 5)
combo["values"] = tuple(range(101))
sequence = IntVar()


def generation():
    print(sequence.get())
    print(num.get())
    tables = ""
    for i in range(sequence.get()):
        tables +=(f'{num.get()} x {i} = {num.get()* i}\n')
    tabl.config(text = tables)
    
    
tabl = Label(window)
    
r10 = Radiobutton(window,text = "10",variable = sequence,value = 11 )
r20 = Radiobutton(window,text = "20",variable = sequence,value = 21 )
r30 = Radiobutton(window,text = "30",variable = sequence,value = 31 )

generate = Button(window,text = "Generate",command = generation)

Labelmaths.place(x = 150, y = 30)
Labelnum.place(x = 20, y = 70)
combo.place(x = 160, y = 70)
r10.place(x = 330, y = 70)
r20.place(x = 330, y = 110)
r30.place(x = 330, y = 150)
generate.place(x = 160, y = 180)
tabl.place(x = 140, y = 220)

window.mainloop()