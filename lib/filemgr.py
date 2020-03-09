from tkinter import *
import tkinter.filedialog as filedialog
import codecs, os
from pathlib import Path

file, filepath = '', ''

def newfile(master, mainMenu, codeF):
    global file, filepath
    mainMenu['text'] = 'Untitled'
    codeF.delete("1.0", END)
    master.title("Untitled - PyDev++")
    file = ''
    filepath = ''

def openfile(master, mainMenu, codeF):
    global filepath, file
    try:
        file = filedialog.askopenfilename(parent=master, title='Select File to Open', filetypes={('Python Source Code', '*.py;*.pyw')}, defaultextension={('Python Source Code', '*.py;*.pyw')})
        if file == filepath:
            return None
        else:
            filepath = file
            mainMenu['text'] = filepath
            content = codecs.open(file, 'r', encoding='UTF-8')
            codeF.insert("1.0", content.read())
            content.close()
            master.title(filepath + " - PyDev++")
            cwd = filepath.replace(Path(filepath).name, '')
            os.chdir(cwd)
    except FileNotFoundError:
        mainMenu['text'] = 'Untitled'

def savefile(master, mainMenu, codeF):
    global filepath, file
    if file != '' and filepath != '':
        content = codecs.open(file, 'w', encoding='UTF-8')
        saveText = codeF.get("1.0", END)
        content.write(saveText)
        content.close()
    else:
        try:
            file = filedialog.asksaveasfilename(parent=master, title='Save As', filetypes={('Python Source Code', '*.py;*.pyw')}, defaultextension={('Python Source Code', '*.py;*.pyw')})
            filepath = file
            content = codecs.open(file, 'w', encoding='UTF-8')
            saveText = codeF.get("1.0", END)
            content.write(saveText)
            content.close()
            master.title(filepath + " - PyDev++")
            mainMenu['text'] = filepath
            cwd = filepath.replace(Path(filepath).name, '')
            os.chdir(cwd)
        except FileNotFoundError:
            mainMenu['text'] = "Untitled"