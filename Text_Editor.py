#NA BALO,UNDO

from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window=Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
dm = IntVar()
win = IntVar()

def open_file():
    """Open a file for editing"""
    filepath = askopenfilename(

            filetypes=[("Text files", "*txt"), ("All FilesL", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as imput_file:
        txt = imput_file.read()
        txt_edit.insert(END, txt)
    window.title(f"Simple Text Editor = {filepath}")

def save_file():
    """Save the current file as a new file"""
    filepath = asksaveasfilename(

        defaultextension="txt",
        filetypes=[("Text files", "*txt"), ("All FilesL", "*.*")]
    )

    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")

def new():
    txt_edit.delte(0,END)

def exit():
    window.destroy()

def view():
    if dm.get() == 1:
        txt_edit.config(background="black", foreground="white")
    else:
        txt_edit.config(background="white", foreground="black")


menu = Menu(window)

new_item = Menu(menu, tearoff=0)

new_item.add_command(label="Open",command=open_file)

new_item.add_command(label="New",command=new)

new_item.add_command(label="Save As",command=save_file)

new_item.add_command(label="Exit",command=exit)

menu.add_command(label="Copy", command=lambda: win.event_generate('<Control-c>'))
menu.add_command(label="Cut", command=lambda: win.event_generate('<Control-x>'))
menu.add_command(label="Paste", command=lambda: win.event_generate('<Control-v>'))

menu.add_cascade(label="File", menu=new_item)

window.config(menu=menu)


view = Menu(window)

new_item = Menu(menu, tearoff=5)

new_item.add_checkbutton(label="Darkmode", variable=dm, command=view)

menu.add_cascade(label="darkmode", menu=view)

window.config(menu=view)





txt_edit =Text(window)
txt_edit.grid(row=0, column=1, sticky="nsew")




window.mainloop()



