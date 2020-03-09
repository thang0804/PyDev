from tkinter import *
import tkinter.filedialog as filedialog
import tkfontchooser as fontdialog

def selectFont(master, codeF):
    font = fontdialog.askfont(master = master, text = 'ABCD', title = 'Select Font')
    font['family'] = font['family'].replace(' ', '\ ')
    font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
    codeF.config(font = font_str)

def copy(master, codeF):
    codeF.clipboard_clear()
    copytext = codeF.get("sel.first", "sel.last")
    codeF.clipboard_append(copytext)

def paste(master, codeF):
    pastetext = codeF.selection_get(selection = 'CLIPBOARD')
    codeF.insert("insert", pastetext)

def cut(master, codeF):
    codeF.clipboard_clear()
    copytext = codeF.get("sel.first", "sel.last")
    codeF.clipboard_append(copytext)
    codeF.delete("sel.first", "sel.last")

def selall(master, codeF):
    codeF.tag_add('sel', '1.0', 'end')
