
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import font, simpledialog

import os

font_size = 12
font_family = 'lucida'

# File Menu Functions Ends

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

# File Menu Functions Ends

# Edit Menu Functions Starts

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad v1.01")

# Edit Menu Functions Starts



# Font Menu Functions Starts

def change_font():
    # get available font families
    available_fonts = font.families()
    FontDialog(root)

class FontDialog:
    def __init__(self, root):
        self.top = Toplevel(root)
        Label(self.top, text="Select a font").pack()
        self.fontlist = Listbox(self.top)
        self.fontlist.pack()
        
        # List of popular fonts to include
        popular_fonts = ["Arial", "Courier", "Helvetica", "Times", "Verdana", "Calibri", "Cambria", "Georgia", "Tahoma", "Garamond", "Comic Sans MS"]
        for item in popular_fonts:
            self.fontlist.insert(END, item)
        self.fontlist.bind('<<ListboxSelect>>', self.on_select)
        self.value = None
        Button(self.top, text="OK", command=self.ok).pack()


    def on_select(self, evt):
        index = self.fontlist.curselection()[0]
        self.value = self.fontlist.get(index)
        

    def ok(self):
        if self.value:
            TextArea.configure(font=(self.value, TextArea.cget('font').split()[1]))
        self.top.destroy()



def change_font_size():
    font_size = simpledialog.askinteger("Font size", "Enter font size:", initialvalue=10)
    TextArea['font'] = (TextArea['font'][0], font_size)

# Font Menu Functions Ends


# Style Menu Functions Start

def toggle_bold():
    # get current font attributes
    current_font = font.Font(font=TextArea.cget('font'))
    if current_font.actual()['weight'] == 'normal':
        # if the font weight is normal, change it to bold
        TextArea.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'bold'))
    else:
        # if the font weight is bold, change it to normal
        TextArea.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'normal'))

def toggle_italic():
    # get current font attributes
    current_font = font.Font(font=TextArea.cget('font'))
    if current_font.actual()['slant'] == 'roman':
        # if the font slant is roman, change it to italic
        TextArea.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'italic'))
    else:
        # if the font slant is italic, change it to roman
        TextArea.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'roman'))

def toggle_underline():
    # get current font attributes
    current_font = font.Font(font=TextArea.cget('font'))
    if current_font.actual()['underline'] == 0:
        # if the font is not underlined, underline it
        TextArea.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'underline'))
    else:
        # if the font is underlined, remove underline
        TextArea.configure(font=(current_font.actual()['family'], current_font.actual()['size'], 'normal'))

# Style Menu Functions Ends



if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("924x568")
    root.minsize(420,240)
    #Add TextArea
    TextArea = Text(root, font="TimesNewRoman 12")
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command = openFile)
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu = EditMenu)
    # Edit Menu Ends

    # Font Menu Satrts
    FontMenu = Menu(MenuBar, tearoff=0)
    FontMenu.add_command(label="Change Font", command=change_font)
    FontMenu.add_command(label="Change Size", command=change_font_size)
    MenuBar.add_cascade(label="Font", menu=FontMenu)
    # Font Menu Ends

    # Style Menu Starts
    style_menu = Menu(MenuBar, tearoff=0)
    style_menu.add_command(label="Bold", command=toggle_bold)
    style_menu.add_command(label="Italic", command=toggle_italic)
    style_menu.add_command(label="Underline", command=toggle_underline)
    MenuBar.add_cascade(label="Style", menu=style_menu)
    # Style Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # Help Menu Ends


    root.config(menu=MenuBar)

    #Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
