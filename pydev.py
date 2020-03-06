from tkinter import *
from tkinter.ttk import Style
import tkinter.scrolledtext as ScrolledText
from tkinter import filedialog
import tkfontchooser as fontdialog
from lib import openpip
import codecs, os
from timeit import default_timer as timer
from pathlib import Path

print("[ ==== ] Starting PyDev++ ...")
print("[  OK  ] Started PyDev++")

filepath = ''
file = ''

# Hàm Hệ Thống
def newfile(args=None):
    mainMenu['text'] = 'Untitled'
    mainText.delete("1.0", END)
    gui.title("Untitled - PyDev++")

def openfile(args=None):
    global filepath, file
    try:
        file = filedialog.askopenfilename(parent=gui, title='Select File to Open', filetypes={('Python Source Code', '*.py;*.pyw')}, defaultextension={('Python Source Code', '*.py;*.pyw')})
        if file == filepath:
            return None
        else:
            filepath = file
            mainMenu['text'] = filepath
            content = codecs.open(file, 'r', encoding='UTF-8')
            mainText.insert("1.0", content.read())
            content.close()
            gui.title(filepath + " - PyDev++")
    except FileNotFoundError:
        mainMenu['text'] = 'Untitled'

def savefile(args=None):
    global filepath, file
    if file != '' and filepath != '':
        content = codecs.open(file, 'w', encoding='UTF-8')
        saveText = mainText.get("1.0", END)
        content.write(saveText)
        content.close()
    else:
        try:
            file = filedialog.asksaveasfilename(parent=gui, title='Save As', filetypes={('Python Source Code', '*.py;*.pyw')}, defaultextension={('Python Source Code', '*.py;*.pyw')})
            filepath = file
            content = codecs.open(file, 'w', encoding='UTF-8')
            saveText = mainText.get("1.0", END)
            content.write(saveText)
            content.close()
            gui.title(filepath + " - PyDev++")
            mainMenu['text'] = filepath
        except FileNotFoundError:
            mainMenu['text'] = "Untitled"

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

def runscript(args=None):
    global file, filepath, mainMenu
    if mainMenu['text'] != 'Untitled':
        os.system("cls")
        start = timer()
        os.system("python " + filepath)
        end = timer()
        print()
        print("[Run finished in " + str(end - start) + "]")
        os.system("pause")
    elif mainMenu['text'] == 'Untitled':
        try:
            savefile()
            if filepath == '' or filepath == None:
                return None
            elif filepath != '' or filepath != None:
                os.system("cls")
                start = timer()
                os.system("python " + filepath)
                end = timer()
                print()
                print("[Run finished in " + str(end - start) + "]")
                os.system("pause")
        except FileNotFoundError:
            return None

def openterm(args=None):
    global file, filepath
    if file != '' and filepath != '':
        cwd = filepath.replace(Path(filepath).name, '')
        os.chdir(cwd)
        os.system('start')
    else:
        os.chdir('C:\\')
        os.system('start')
# Hàm tạo form
gui = Tk()
gui.title("Untitled - PyDev++")
style = Style(gui)
style.theme_use('winnative')

frame = Frame(gui)
frame.pack(fill = BOTH, expand = 1)

frameMenu = LabelFrame(frame, text = "Quick Menu", width = 120, height = 60)
frameMenu.pack(fill = BOTH, expand = 2, padx = 7, pady = 7)

mainMenu = LabelFrame(frame, text = "Untitled", width = 122, height = 60, bd = 1)
mainMenu.pack(fill = BOTH, expand = 2, padx = 7, pady = 7)

buttonRunScript = Button(frameMenu, text = "Run Script", command=runscript)
buttonRunScript.config(width=8, height=1)
buttonRunScript.pack(side=LEFT, padx = 7, pady = 7)

buttonOpenTerm = Button(frameMenu, text='Terminal', command=openterm)
buttonOpenTerm.config(width=8, height=1)
buttonOpenTerm.pack(side=LEFT, padx=7, pady=7)

mainText = ScrolledText.ScrolledText(mainMenu, width = 120, height = 30)
mainText.config(font = ('Consolas', '16'))
mainText.config()
mainText.pack(fill = BOTH, expand = 2)

menu = Menu(frame)
gui.config(menu = menu)

fileMenu = Menu(menu)
menu.add_cascade(label = 'File', menu = fileMenu, underline = 0)
fileMenu.add_command(label = 'New', accelerator = 'Ctrl+N', command=newfile)
fileMenu.add_command(label = 'Open', accelerator = 'Ctrl+O', command=openfile)
fileMenu.add_command(label = 'Save', accelerator = 'Ctrl+S', command=savefile)
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = gui.destroy, accelerator = 'Ctrl+Q')

editMenu = Menu(menu)
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

toolMenu = Menu(menu)
menu.add_cascade(label='Tools', menu=toolMenu)
toolMenu.add_command(label='Pip Install Package', command=lambda: openpip.createPip(gui), accelerator = 'Ctrl+Shift+P')
toolMenu.add_command(label='Open Terminal', command=openterm, accelerator = 'Ctrl+Alt+T')

QuestionsMenu = Menu(menu)
menu.add_cascade(label = 'Questions', menu = QuestionsMenu)
QuestionsMenu.add_command(label = 'About')

AnswerMenu = Menu(menu)
menu.add_cascade(label = 'Answer', menu = AnswerMenu)
AnswerMenu.add_command(label = 'About')

helpMenu = Menu(menu)
menu.add_cascade(label = 'Help', menu = helpMenu)
helpMenu.add_command(label = 'About')

gui.bind('<F5>', runscript)
gui.bind('<Control-Shift-P>', lambda master=None: openpip.createPip(gui))
gui.bind('<Control-Alt-t>', openterm)
gui.bind('<Control-o>', openfile)
gui.bind('<Control-s>', savefile)
gui.bind('<Control-n>', newfile)

gui.mainloop()