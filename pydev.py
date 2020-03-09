import tkinter.scrolledtext as ScrolledText
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Style
from threaded import *

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
    gui.minsize(720, 480)

    style = Style(gui)
    style.theme_use('winnative')

    frame = Frame(gui)
    frame.pack(fill = BOTH, expand = 1)

    menu = Menu(frame)
    gui.config(menu = menu)

    frameMenu = LabelFrame(frame, text = "[ Quick Menu ]", width = 120, height = 60)
    frameMenu.pack(fill = BOTH, expand = 2, padx = 7, pady = 7)

    mainMenu = LabelFrame(frame, text = "Untitled", width = 122, height = 60, bd = 1)
    mainMenu.pack(fill = BOTH, expand = 2, padx = 7, pady = 7)

    buttonRunScript = Button(frameMenu, text = "Run Script", command=lambda: threadmgr.doRunScript(gui, mainMenu, mainText))
    buttonRunScript.config(width=8, height=1)
    buttonRunScript.pack(side=LEFT, padx = 7, pady = 7)

    buttonOpenTerm = Button(frameMenu, text='Open Terminal', command=threadmgr.openterm)
    buttonOpenTerm.config(width=13, height=1)
    buttonOpenTerm.pack(side=LEFT, padx=7, pady=7)

    buttonPyToExe = Button(frameMenu, text='Build Python to Exe', command=lambda: pyinsGUI.quickBuild(gui, file))
    buttonPyToExe.config(width=15, height=1)
    buttonPyToExe.pack(side=LEFT, padx=7, pady=7)

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

    gui.bind('<F5>', lambda master=None: threadmgr.doRunScript(gui, mainMenu, mainText))
    gui.bind('<F6>', lambda master=None, pathtofile=None: pyinsGUI.quickBuild(gui, file))
    gui.bind('<Control-Shift-P>', lambda master=None: openpip.createPip(gui))
    gui.bind('<Control-Alt-t>', threadmgr.openterm)
    gui.bind('<Control-Alt-p>', lambda master=None: pyinsGUI.createGUI(gui))
    gui.bind('<Control-o>', lambda master=None: filemgr.openfile(gui, mainMenu, mainText))
    gui.bind('<Control-s>', lambda master=None: filemgr.savefile(gui, mainMenu, mainText))
    gui.bind('<Control-n>', lambda master=None: filemgr.newfile(gui, mainMenu, mainText))

    gui.mainloop()

createMain().start()
createMain().join()
###