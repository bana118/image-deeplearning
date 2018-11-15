#-*- coding: utf-8 -*-
import os, sys
import re
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog


def pushed():
    global img
    fileType = [("png", "*.png"), ("tiff", "*.tif")] #画像の種類を選択
    iDir = "/Users/Desktop/"
    f = filedialog.askopenfilename(filetypes = fileType, initialdir = iDir)
    if re.match(r"(.*)\.png", f) :
        print("pngです")
        img = tk.PhotoImage(file=str(f))
        canvas = tk.Canvas(bg="white", width=500, height=500)
        canvas.place(x=400, y=400)
        canvas.create_image(0,0,image=img, anchor=tk.NW)
    elif re.match(r"(.*)\.jpg", f) :
        print("jpgです")
        #img = Image.open(f)
        #tkpi = ImageTk.PhotoImage(img)
        #label_image = tk.Label(root, image=tkpi)
        #label_image.pack()
    else :
        print("それ以外です")


def run ():
    global root
    root = tk.Tk()
    root.title("オーキド博士")
    root.geometry("1200x900+1000+10")
    root.protocol("WM_DELETE_WINDOW", root.quit)
    button = tk.Button(root,text="ファイル送信",command=pushed)
    button.pack()
    root.mainloop()

if __name__ == "__main__":
    run()