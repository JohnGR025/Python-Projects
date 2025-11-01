#Import Section
import os
from tkinter import Tk, Text, Menu, Scrollbar, Radiobutton, Frame, Toplevel, Label, RIGHT, Y, BOTTOM, WORD, X, LEFT, BOTH, font, END
from tkinter import colorchooser, StringVar
from tkinter import filedialog

#Function Factory
def new_file():
    text_area.delete(1.0, END)

def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()

def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()

def popupmenu(event):
    edit_menu.post(event.x_root, event.y_root)

def open():
    cord = filedialog.askopenfilename(title="Open a File", filetypes=[("Κείμενο", ".txt")], initialdir="c:\\Users\\User\\Documents\\John's Workplace")
    print(cord)

def save():
    filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Κείμενο", ".txt")], initialdir="c:\\Users\\User\\Documents\\John's Workplace")

def coloring():
    global text_color
    global coverage
    text_color = colorchooser.askcolor()[1]
    if text_color:
        if coverage:
            text_area.config(fg=text_color)
        else:
            try:
                text_area.tag_add("colored", "sel.first", "sel.last")
                text_area.tag_configure("colored", foreground=text_color)
            except:
                pass    

def changingfont(font_name, size):
    global coverage
    if coverage:
        text_area.config(font=(font_name, size))
    else:
        try:
            text_area.tag_add("fonted", "sel.first", "sel.last")
            text_area.tag_configure("fonted", font=(font_name, size))
        except:
            pass

def changingsize():
    pass

def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    about_window = Toplevel()
    about_label = Label(about_window, font=("Aerial", 20, "italic"), text="This editor is the fucking best there is out there!!!", height="8", width="40")
    about_label.pack()

def stylingfont_bold():
    pass

def stylingfont_underline():
    pass

def stylingfont_italic():
    pass

def fullcoveraging():
    global coverage
    coverage = True

def partialcoveraging():
    global coverage
    coverage = False

#Creation of the widgets
window = Tk()
window.title("TextEditor")

#Variables
text_color = "black"
font_name = "Aerial"
size = 20
coverage = True

#Menu Items
mainmenu = Menu(window)

#File Options
file_menu = Menu(mainmenu, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open)
file_menu.add_command(label="Save", command=save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
mainmenu.add_cascade(label="File", menu=file_menu)

#Edit Options
edit_menu = Menu(mainmenu, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Size", command=changingsize)
edit_menu.add_command(label="Color", command=coloring)
mainmenu.add_cascade(label="Edit", menu=edit_menu)

#Submenu for the Font Options
font_options = Menu(edit_menu, tearoff=0)
available_fonts = list(font.families())#Get all the Fonts and store them as a list
for fontname in available_fonts:
    font_options.add_command(label=fontname, command=lambda name=fontname: changingfont(name, size))
edit_menu.add_cascade(label="Font", menu=font_options)

#Submenu for the Style Options (font style)
style_options = Menu(edit_menu, tearoff=0)
style_options.add_command(label="Bold", command=stylingfont_bold)
style_options.add_command(label="Underline", command=stylingfont_underline)
style_options.add_command(label="Italic", command=stylingfont_italic)
edit_menu.add_cascade(label="Style", menu=style_options)

#Info Options
info_menu = Menu(mainmenu, tearoff=0)
info_menu.add_command(label="About", command=about)
mainmenu.add_cascade(label="Info", menu=info_menu)

#Mode Options
mode_menu = Menu(mainmenu, tearoff=0)
mode_menu.add_command(label="Full", command=fullcoveraging)
mode_menu.add_command(label="Partial", command=partialcoveraging)
mainmenu.add_cascade(label="Mode", menu=mode_menu)

window.config(menu=mainmenu)

#ScrollBars (part 1)
vertical_scrollbar = Scrollbar(window, orient="vertical")
horizontal_scrollbar = Scrollbar(window, orient="horizontal")

#Text Widget
text_area = Text(window, wrap=WORD, width=50, height=10, fg=text_color, yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)
text_area.pack(side=LEFT, fill=BOTH, expand=True)
text_area.bind("<Button-3>", popupmenu)

#ScrollBars (part 2)
vertical_scrollbar.config(command=text_area.yview)
vertical_scrollbar.pack(side=RIGHT, fill=Y)
horizontal_scrollbar.config(command=text_area.xview)
horizontal_scrollbar.pack(side=BOTTOM, fill=X)

window.geometry("350x200+850+250")
window.mainloop()