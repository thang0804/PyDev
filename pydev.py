import tkinter.scrolledtext as ScrolledText
from tkinter import *
from tkinter.ttk import Style
from tkinter.ttk import Notebook
import threading

from lib import openpip
from lib import pyinsGUI
from lib import filemgr
from lib import codeF_mgr as codefmgr
from lib import threadmgr

print("[ ==== ] Starting PyDev++ ...")
print("[  OK  ] Started PyDev++")

filepath = ''
file = ''
cwd = ''

# Hàm tạo form
def createMain():
    gui = Tk()
    gui.title("Untitled - PyDev++")
    gui.geometry('1200x700')
    gui.minsize(720, 480)

    style = Style(gui)
    style.theme_use('winnative')

    thisStyle = Style()
    noteBook = Notebook(gui)
    thisStyle.configure('TNotebook.Tab', font=('Consolas', 10))


    frame = Frame(noteBook)
    noteBook.add(frame, text="Main area")
    noteBook.pack(fill=BOTH, padx=0, pady=0)

    menu = Menu(frame)
    gui.config(menu = menu)

    mainMenu = LabelFrame(frame, text='Untitled', width = 122, height = 60, bd = 1)
    mainMenu.pack(fill = BOTH, expand = 2, padx = 7, pady = 7)

    mainText = ScrolledText.ScrolledText(mainMenu, width = 120, height = 30)
    mainText.config(font = ('Consolas', '16'))
    mainText.pack(fill = BOTH, expand = 2)

    fileMenu = Menu(menu)
    menu.add_cascade(label = 'File', menu = fileMenu, underline = 0)
    fileMenu.add_command(label = 'New', accelerator = 'Ctrl+N', command=lambda: filemgr.newfile(gui, mainMenu, mainText))
    fileMenu.add_command(label = 'Open', accelerator = 'Ctrl+O', command=lambda: filemgr.openfile(gui, mainMenu, mainText))
    fileMenu.add_command(label = 'Save', accelerator = 'Ctrl+S', command=lambda: filemgr.savefile(gui, mainMenu, mainText))
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
    editMenu.add_command(label = 'Font...', command = lambda: codefmgr.selectFont(gui, mainText))

    toolMenu = Menu(menu)
    menu.add_cascade(label='Tools', menu=toolMenu)
    toolMenu.add_command(label="Run Script", accelerator='Ctrl+B', command=lambda: threadmgr.doRunScript(gui, mainMenu, mainText))
    toolMenu.add_command(label="Quick build Python to Exe", accelerator='Ctrl+Shift+B')
    toolMenu.add_separator()
    toolMenu.add_command(label='Pip Install Package', command=lambda: openpip.createPip(gui), accelerator = 'Ctrl+Shift+P')
    toolMenu.add_command(label='Open Terminal', command=threadmgr.openterm, accelerator = 'Ctrl+Alt+T')
    toolMenu.add_separator()
    toolMenu.add_command(label='PyInstaller GUI', accelerator='Ctrl+Alt+P', command=lambda: pyinsGUI.createGUI(gui))

    QuestionsMenu = Menu(menu)
    menu.add_cascade(label = 'Questions', menu = QuestionsMenu)
    QuestionsMenu.add_command(label = 'About')

    AnswerMenu = Menu(menu)
    menu.add_cascade(label = 'Answer', menu = AnswerMenu)
    AnswerMenu.add_command(label = 'About')

    helpMenu = Menu(menu)
    menu.add_cascade(label = 'Help', menu = helpMenu)
    helpMenu.add_command(label = 'About')

    gui.bind('<Control-b>', lambda master=None: threadmgr.doRunScript(gui, mainMenu, mainText))
    gui.bind('<Control-Shift-B>', lambda master=None, pathtofile=None: pyinsGUI.createThread(gui, mainMenu['text']))
    gui.bind('<Control-Shift-P>', lambda master=None: openpip.createPip(gui))
    gui.bind('<Control-Alt-t>', threadmgr.openterm)
    gui.bind('<Control-Alt-p>', lambda master=None: pyinsGUI.createGUI(gui))
    gui.bind('<Control-o>', lambda master=None: filemgr.openfile(gui, mainMenu, mainText))
    gui.bind('<Control-s>', lambda master=None: filemgr.savefile(gui, mainMenu, mainText))
    gui.bind('<Control-n>', lambda master=None: filemgr.newfile(gui, mainMenu, mainText))

    gui.mainloop()

luong1 = threading.Thread(target=createMain, args=())
luong1.start()
###