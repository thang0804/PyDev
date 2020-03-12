from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.filedialog as filedialog
from pathlib import Path
import os
from timeit import default_timer as timer
from . import threadmgr
import threading

file = ''
filepath = ''
cwd = ''

def browse(master, srcPathEntry, fileField):
    global file, filepath, cwd
    file = filedialog.askopenfilename(parent=master, title='Choose Script to Build Exe', filetypes={('Python Source Code', '*.py;*.pyw')}, defaultextension={('Python Source Code', '*.py;*.pyw')})
    filepath = file
    srcPathEntry.delete(0, END)
    srcPathEntry.insert(0, filepath)
    fileField.config(state=NORMAL)
    fileField.delete(0, END)
    fileField.insert(0, Path(filepath).name)
    fileField.config(state='readonly')
    cwd = filepath.replace(Path(filepath).name, '')
'''
def process(master, srcPathEntry, outputText):
    global cwd, filepath
    os.chdir(cwd)
    proc = sub.Popen(['pyinstaller', Path(filepath).name], stdout=sub.PIPE)
    output = proc.communicate()
    outputText.delete(0, END)
    outputText.insert(0, str(output))
'''
def cmdprocess(master, args):
    global cwd, filepath
    if args.get() == '':
        if filepath == '':
            msgbox.showerror('Error !', 'Script path entry cannot be empty !')
            return None
        else:
            os.chdir(cwd)
            os.system('cls')
            os.system("pyinstaller " + Path(filepath).name)
    elif args.get() != '':
        if filepath == '':
            msgbox.showerror('Error !', 'Script path entry cannot be empty !')
            return None
        else:
            os.chdir(cwd)
            os.system('cls')
            os.system('pyinstaller {0} '.format(args.get()) + Path(filepath).name + ' & pause')

def startProcess(master, args):
    try:
        luong3 = threading.Thread(target=cmdprocess, args=(master, args))
        luong3.start()
    except:
        return None

def createGUI(master=None):
    exewin = Toplevel(master)
    exewin.title('PyInstaller GUI Tools')
    exewin.geometry('700x300')
    exewin.maxsize(width=700, height=300)
    exewin.resizable(0,0)

    menuButton = Menubutton(exewin, text='Choose Mode')
    menuButton.place()
    menuButton.menu = Menu(menuButton)
    menuButton["menu"] = menuButton.menu

    lb0 = Label(exewin, text='Choose script to build Exe:')
    lb0.config(font=('Segoe UI', '11'))
    lb0.place(x=2, y=1)

    scriptEntry = Entry(exewin, width=85)
    scriptEntry.config(font=('Consolas', '10'))
    scriptEntry.place(x=5, y=30)

    lb1 = Label(exewin, text='Command:')
    lb1.config(font=('Segoe UI', '11'))
    lb1.place(x=2, y=50)

    pyinstallerEntry = Entry(exewin, width=12)
    pyinstallerEntry.config(font=('Consolas', '10'))
    pyinstallerEntry.place(x=5, y=79)
    pyinstallerEntry.insert(0, 'pyinstaller')
    pyinstallerEntry.config(state='readonly')

    argField = Entry(exewin, width=50)
    argField.config(font=('Consolas', '10'))
    argField.place(x=95, y=79)

    filenameEntry = Entry(exewin, width=33, state='readonly')
    filenameEntry.config(font=('Consolas', '10'))
    filenameEntry.place(x=452, y=79)

    btnBrowse = Button(exewin, text='Browse..', height=1, width=10, command=lambda: browse(exewin, scriptEntry, filenameEntry))
    btnBrowse.place(x=610, y=27)
    '''
    lb1 = Label(exewin, text='Output:')
    lb1.config(font=('Segoe UI', '11'))
    lb1.place(x=2, y=50)
    processText = ScrolledText.ScrolledText(exewin, width=84, height=23, state=DISABLED)
    processText.place(x=5, y=80)
    '''
    '''
    btnCancel = Button(exewin, text='Cancel', height=1, width=10, command=exewin.destroy)
    btnCancel.place(x=610, y=460)
    btnOK = Button(exewin, text='OK', height=1, width=10, command=lambda: process(master, scriptEntry, processText))
    btnOK.place(x=527, y=460)
    '''
    btnCancel = Button(exewin, text='Cancel', height=1, width=10, command=exewin.destroy)
    btnCancel.place(x=610, y=150)
    btnOK = Button(exewin, text='OK', height=1, width=10, command=lambda : startProcess(exewin, argField))
    btnOK.place(x=527, y=150)

def quickBuild(master, filepath, args):
    if filepath == '' or filepath == 'Untitled':
        file = filedialog.askopenfilename(parent=master, title='Choose Script to Build Exe',
                                          filetypes={('Python Source Code', '*.py;*.pyw')},
                                          defaultextension={('Python Source Code', '*.py;*.pyw')})
        cwd = file.replace(Path(file).name, '')
        os.chdir(cwd)
        os.system('cls')
        os.system('pyinstaller -F {0}'.format(Path(file).name) + ' & pause')
    else:
        cwd = filepath.replace(Path(filepath).name, '')
        os.chdir(cwd)
        os.system('cls')
        os.system('pyinstaller -F {0}'.format(Path(filepath).name) + ' & pause')

def createThread(master, filepath):
    try:
        luong3 = threading.Thread(target=quickBuild, args=(master, filepath))
        luong3.start()
    except:
        return None
