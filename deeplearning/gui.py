#-*- coding: utf-8 -*-
import os, sys
import re
import tkinter as tk
import PIL
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog


def pushed():
    global img
    fileType = [("png", "*.png"), ("jpg", "*jpg")] #画像の種類を選択
    iDir = "/Users/Desktop/"
    f = filedialog.askopenfilename(filetypes = fileType, initialdir = iDir)
    if re.match(r"(.*)\.png", f) :
        print("pngです")
        img = Image.open(open(str(f),"rb"))
        img.thumbnail((200,200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        canvas = tk.Canvas(bg="white", width=200, height=200)
        canvas.place(x=100, y=100)
        canvas.create_image(0,0,image=img, anchor=tk.NW)
    elif re.match(r"(.*)\.jpg", f) :
        print("jpgです")
        img = Image.open(open(str(f),"rb"))
        img.thumbnail((200,200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        canvas = tk.Canvas(bg="white", width=200, height=200)
        canvas.place(x=100, y=100)
        canvas.create_image(0,0,image=img, anchor=tk.NW)
    else :
        print("それ以外です")


def run ():
    global root
    root = tk.Tk()
    root.title("オーキド博士")
    root.geometry("800x600+1000+10")
    root.protocol("WM_DELETE_WINDOW", root.quit)
    button = tk.Button(root,text="ファイル送信",command=pushed)
    button.pack()
    root.mainloop()

if __name__ == "__main__":
    run()