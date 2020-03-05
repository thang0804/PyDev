from tkinter import *
from tkinter.ttk import Style
import tkinter.scrolledtext as ScrolledText
from tkinter import filedialog
import tkfontchooser as fontdialog
import codecs, os

print("Team PyDEV Never DIE !!!")

filepath = ''
file = ''

# Hàm Hệ Thống
def newFile():
    global file
    mainText.delete()
    mainMenu['text'] = "Untitled"

def openFile():
    global filepath
    file = filedialog.askopenfilename(parent = gui, title = 'Select File To Open',
                                      filetypes = [('Python Files', '*.py;*pyw')],
                                      defaultextension = [('Python Files', '*.py;*pyw')])
    filepath = file
    if file is not None:
        fopen = codecs.open(file, 'r', encoding = 'UTF-8')
        content = fopen.read()
        mainText.insert('1.0', content)
        fopen.close()
        gui.title(str(filepath) + ' - PyDev++')
        mainMenu['text'] = file


def saveFile():
    global filepath, file
    if filepath == '':
        file = filedialog.asksaveasfilename(parent = gui, title = 'Save', filetypes = [('Python Files', '*.py;*pyw')],
                                            defaultextension = [('Python Files', '*.py;*pyw')])
        fopen = codecs.open(file, 'w', encoding = 'UTF-8')
        saveText = str(mainText.get(1.0, END))
        fopen.write(saveText)
        fopen.close()
        return file

    elif filepath != '':
        fopen = codecs.open(filepath, 'w', encoding = 'UTF-8')
        saveText = str(mainText.get(1.0, END))
        fopen.write(saveText)
        fopen.close()

def selectFont():
    font = fontdialog.askfont(master = gui, text = 'ABCD', title = 'Select Font')
    font['family'] = font['family'].replace(' ', '\ ')
    font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
    mainText.config(font = font_str)

def copy():
    mainText.clipboard_clear()
    copytext = mainText.get("sel.first", "sel.last")
    mainText.clipboard_append(copytext)


def paste():
    pastetext = mainText.selection_get(selection = 'CLIPBOARD')
    mainText.insert("insert", pastetext)


def cut():
    mainText.clipboard_clear()
    copytext = mainText.get("sel.first", "sel.last")
    mainText.clipboard_append(copytext)
    mainText.delete("sel.first", "sel.last")


def selall():
    mainText.tag_add('sel', '1.0', 'end')

def RunScript():
    global file, filepath
    if file != '':
        os.system("cls")
        os.system(file)
    else:
        file = saveFile()
        os.system("cls")
        os.system("python -u " + filepath)

# Hàm tạo form
gui = Tk()
gui.title("PyDev++")
style = Style(gui)
style.theme_use('winnative')

frame = Frame(gui)
frame.pack(fill = BOTH, expand = 1)

frameMenu = LabelFrame(frame, text = "Quick Menu", width = 120, height = 60)
frameMenu.pack(fill = BOTH, expand = 2, padx = 7, pady = 7)

mainMenu = LabelFrame(frame, text = file, width = 122, height = 60, bd = 1)
mainMenu.pack(fill = BOTH, expand = 2, padx = 7, pady = 7)

buttonRunScript = Button(frameMenu, text = "Run Script", command = RunScript)
buttonRunScript.config(width=8, height=1)
buttonRunScript.pack(side=LEFT, padx = 7, pady = 7)

mainText = ScrolledText.ScrolledText(mainMenu, width = 120, height = 30)
mainText.config(font = ('Consolas', '16'))
mainText.config()
mainText.pack(fill = BOTH, expand = 2)

menu = Menu(frame)
gui.config(menu = menu)

fileMenu = Menu(menu)
menu.add_cascade(label = 'File', menu = fileMenu, underline = 0)
fileMenu.add_command(label = 'New', command=lambda: newFile(), accelerator = 'Ctrl+N')
fileMenu.add_command(label = 'Open', command = lambda: openFile(), accelerator = 'Ctrl+O')
fileMenu.add_command(label = 'Save', command = lambda: saveFile(), accelerator = 'Ctrl+S')
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = gui.destroy, accelerator = 'Ctrl+Q')

editMenu = Menu(frame)
menu.add_cascade(label = 'Edit', menu = editMenu, underline = 0)
editMenu.add_command(label = 'Undo', accelerator = 'Ctrl+Z')
editMenu.add_command(label = 'Redo', accelerator = 'Ctrl+Y')
editMenu.add_separator()
editMenu.add_command(label = 'Cut', accelerator = 'Ctrl+X')
editMenu.add_command(label = 'Copy', accelerator = 'Ctrl+C')
editMenu.add_command(label = 'Paste', accelerator = 'Ctrl+V')
editMenu.add_command(label = 'Select All', accelerator = 'Ctrl+A')
editMenu.add_separator()
editMenu.add_command(label = 'Word Wrap')
editMenu.add_command(label = 'Font...', command = lambda: selectFont())

QuestionsMenu = Menu(menu)
menu.add_cascade(label = 'Questions', menu = QuestionsMenu)
QuestionsMenu.add_command(label = 'About')

AnswerMenu = Menu(menu)
menu.add_cascade(label = 'Answer', menu = AnswerMenu)
AnswerMenu.add_command(label = 'About')

helpMenu = Menu(menu)
menu.add_cascade(label = 'Help', menu = helpMenu)
helpMenu.add_command(label = 'About')

gui.bind("<Control-n>", newFile)
gui.bind("<Control-o>", openFile)
gui.bind("<Control-s>", saveFile)
gui.bind("<Alt-c>", copy)
gui.bind("<Alt-v>", paste)
gui.bind("<Control-x>", cut)
gui.bind("<Control-a>", selall)

gui.mainloop()