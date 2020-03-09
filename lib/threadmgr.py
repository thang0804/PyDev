from tkinter import *
import tkinter.filedialog as filedialog
from pathlib import Path
import os, codecs
from timeit import default_timer as timer
import threading


def openterm(args=None):
    global file, filepath, cwd
    if file != '' and filepath != '':
        cwd = filepath.replace(Path(filepath).name, '')
        os.chdir(cwd)
        os.system('start')
    else:
        os.chdir('C:\\')
        os.system('start')

def runscript(master, mainMenu, codeF):
    global filepath, file
    if mainMenu['text'] != 'Untitled':
        filepath = mainMenu['text']
        content = codecs.open(filepath, 'w', encoding='UTF-8')
        saveText = codeF.get("1.0", END)
        content.write(saveText)
        content.close()
        os.system("cls")
        start = timer()
        os.system("python " + filepath)
        end = timer()
        print()
        print("[Run finished in " + str(end - start) + "]")
        os.system("pause")
    elif mainMenu['text'] == 'Untitled':
        try:
            file = filedialog.askopenfilename(parent=master, title='Select script to Run',
                                              filetypes={('Python Source Code', '*.py;*.pyw')},
                                              defaultextension={('Python Source Code', '*.py;*.pyw')})
            filepath = file
            if filepath == '' or filepath == None:
                return None
            elif filepath != '' or filepath != None:
                content = codecs.open(file, 'w', encoding='UTF-8')
                saveText = codeF.get("1.0", END)
                content.write(saveText)
                content.close()
                os.system("cls")
                start = timer()
                os.system("python " + filepath)
                end = timer()
                os.system("pause")
                print()
                print("[Run finished in " + str(end - start) + "]")
        except FileNotFoundError:
            return None


def doRunScript(master, mainMenu, codeF):
    try:
        luong2 = threading.Thread(target=runscript, args=(master, mainMenu, codeF))
        luong2.start()
    except:
        return None
