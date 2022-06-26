from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Text Editor") 
root.geometry("1200x660") 

global open_status_name
open_status_name = False

global selected
selected = False

def new_file():
    while True:
        my_text.delete("1.0", END)
        root.title("New File - Text Editor")
        status_bar.config(text="New File        ")

        global open_status_name
        open_status_name = False

        break

def open_file():
    my_text.delete("1.0", END)

    text_file = filedialog.askopenfilename(initialdir="C:/", title="Open FIle", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    
    if text_file:
        global open_status_name
        open_status_name = text_file
    
    name = text_file
    status_bar.config(text=f"{name}        ")
    name = name.replace("C:/", "")
    root.title(f"{name} - Text Editor")
    try:
        text_file = open(text_file, "r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()
    except IOError:
        status_bar.config(text=f"Cant open file        ")
    
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files" "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f"Saved: {name}        ")
        name = name.replace("C:/", "")
        root.title(f"{name} - Text Editor")

        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.config(text=f"Saved: {open_status_name}        ")
        name = open_status_name
        name = name.replace("C:/", "")
        root.title(f"{name} - Text Editor")
    else:
        save_as_file()

def copy_text(e):
    while True:
        global selected
        if my_text.selection_get():
            selected = my_text.selection_get()
        break

def paste_text(e):
    while True:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)
        break

my_frame = Frame(root)
my_frame.pack(pady=5)


text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)


my_text = Text(my_frame, width=97, height=25, font=("Helvectica", 16), selectbackground="#dcdcdc", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)

my_menu = Menu(root)
root.config(menu=my_menu)


file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste", command=lambda: paste_text(False))


status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)


root.mainloop()