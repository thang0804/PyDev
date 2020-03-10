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

def browse(master, srcPathEntry):
    global file, filepath, cwd
    file = filedialog.askopenfilename(parent=master, title='Choose Script to Build Exe', filetypes={('Python Source Code', '*.py;*.pyw')}, defaultextension={('Python Source Code', '*.py;*.pyw')})
    filepath = file
    srcPathEntry.delete(0, END)
    srcPathEntry.insert(0, filepath)
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
def cmdprocess(master, srcPathEntry):
    global cwd, filepath
    if filepath == '':
        msgbox.showerror('Error !', 'Script path entry cannot be empty !')
        return None
    else:
        os.chdir(cwd)
        os.system('cls')
        start = timer()
        os.system("pyinstaller " + Path(filepath).name + " & pause")
        end = timer()
        print()
        print("[Build finished in " + str(end - start) + "]")
        os.system("pause")
        master.destroy()

def startProcess(master, filepath):
    try:
        luong3 = threading.Thread(target=cmdprocess, args=(master, filepath))
        luong3.start()
    except:
        return None

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
    btnCancel.place(x=610, y=65)
    btnOK = Button(exewin, text='OK', height=1, width=10, command=lambda : startProcess(master, filepath))
    btnOK.place(x=527, y=65)

def quickBuild(master, filepath):
    if filepath == '' or filepath == 'Untitled':
        file = filedialog.askopenfilename(parent=master, title='Choose Script to Build Exe',
                                          filetypes={('Python Source Code', '*.py;*.pyw')},
                                          defaultextension={('Python Source Code', '*.py;*.pyw')})
        cwd = file.replace(Path(file).name, '')
        os.chdir(cwd)
        os.system('cls')
        start = timer()
        os.system('pyinstaller {0}'.format(Path(file).name))
        end = timer()
        print()
        print("[Build finished in " + str(end - start) + "]")
        os.system('pause')
    else:
        cwd = filepath.replace(Path(filepath).name, '')
        os.chdir(cwd)
        os.system('cls')
        os.system('pyinstaller {0} & pause'.format(Path(filepath).name))

def createThread(master, filepath):
    try:
        luong3 = threading.Thread(target=quickBuild, args=(master, filepath))
        luong3.start()
    except:
        return None