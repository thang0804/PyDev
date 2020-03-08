from tkinter import *
import tkinter.messagebox as msgbox
import os

def doInstall(entry, master, packageCall=None):
    if packageCall == None:
        os.system("cls")
        package = entry.get()
        if package == '':
            msgbox.showerror('Error !', 'Package to install entry cannot be empty !')
            return None
        else:
            os.system("pip install " + package + " & pause")
            master.destroy()
    elif packageCall != None:
        os.system("cls")
        os.system("pip install " + packageCall + " & pause")

def createPip(master):
    pwin = Toplevel(master)
    pwin.title('Install Package with Pip')
    pwin.geometry('550x100')
    pwin.maxsize(width=550, height=100)
    pwin.resizable(0,0)
    lb0 = Label(pwin, text='Package to install:')
    lb0.config(font=('Segoe UI','12'))
    lb0.place(x=1, y=1)
    pkgEntry = Entry(pwin, width=60)
    pkgEntry.config(font=('Consolas', '12'))
    pkgEntry.place(x=3, y=30)
    buttonOK = Button(pwin, text='OK', command=lambda: doInstall(pkgEntry, pwin))
    buttonCancel = Button(pwin, text='Cancel', command=pwin.destroy)
    buttonCancel.config(width=10, height = 1)
    buttonCancel.place(x = 465, y = 60)
    buttonOK.config(width=10, height=1)
    buttonOK.place(x=383, y = 60)