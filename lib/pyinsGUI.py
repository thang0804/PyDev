from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.filedialog as filedialog
from pathlib import Path
import os

file = ''
filepath = ''
cwd = ''

def browse(master, srcPathEntry):
    global file, filepath, cwd
    file = filedialog.askopenfilename(parent=master, title='Choose Script to Build Exe', filetypes={('Python Source Code', '*.py;*.pyw')}, defaultextension={('Python Source Code', '*.py;*.pyw')})
    filepath = file
    srcPathEntry.delete(0, END)
    srcPathEntry.insert(0, filepath)
    cwd = filepath.replace(Path(filepath).name, '')

def cmdprocess(master, srcPathEntry):
    global cwd, filepath
    if filepath == '':
        msgbox.showerror('Error !', 'Script path entry cannot be empty !')
        return None
    else:
        os.chdir(cwd)
        os.system('cls')
        os.system("pyinstaller " + Path(filepath).name + " & pause")
        master.destroy()

def createGUI(master=None):
    exewin = Toplevel(master)
    exewin.title('PyInstaller GUI Tools')
    exewin.geometry('700x100')
    exewin.maxsize(width=700, height=100)
    exewin.resizable(0,0)
    lb0 = Label(exewin, text='Choose script to build Exe:')
    lb0.config(font=('Segoe UI', '11'))
    lb0.place(x=2, y=1)
    scriptEntry = Entry(exewin, width=85, text='Src code')
    scriptEntry.config(font=('Consolas', '10'))
    scriptEntry.place(x=5, y=30)
    btnBrowse = Button(exewin, text='Browse..', height=1, width=10, command=lambda: browse(exewin, scriptEntry))
    btnBrowse.place(x=610, y=27)
    btnCancel = Button(exewin, text='Cancel', height=1, width=10, command=exewin.destroy)
    btnCancel.place(x=610, y=65)
    btnOK = Button(exewin, text='OK', height=1, width=10, command=lambda : cmdprocess(master, scriptEntry))
    btnOK.place(x=527, y=65)

def quickBuild(master, filepath):
    if filepath == '':
        file = filedialog.askopenfilename(parent=master, title='Choose Script to Build Exe',
                                          filetypes={('Python Source Code', '*.py;*.pyw')},
                                          defaultextension={('Python Source Code', '*.py;*.pyw')})
        cwd = file.replace(Path(file).name, '')
        os.chdir(cwd)
        os.system('cls')
        os.system('pyinstaller {0} & pause'.format(Path(file).name))
    else:
        cwd = filepath.replace(Path(filepath).name, '')
        os.chdir(cwd)
        os.system('cls')
        os.system('pyinstaller {0} & pause'.format(Path(filepath).name))
