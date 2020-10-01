from tkinter import *
import tkinter.messagebox
import time
import pygame
import threading
import sys
from pygame.locals import *
import time
def love():
    master = Toplevel()

    master.title("I love U too")
    screenWidth = master.winfo_screenwidth()
    screenHeight = master.winfo_screenheight()
    width = 600
    height = 500
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2
    master.geometry("%dx%d+%d+%d" % (width, height, left, top))
    w = Label(master, image=lphoto)
    w.pack()
    Button(master,text='确定',command=master.quit).pack()

def dislove():
    master = Toplevel()

    master.title("想清楚了再说！！！")
    screenWidth = master.winfo_screenwidth()
    screenHeight = master.winfo_screenheight()
    width = 600
    height = 380
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2
    master.geometry("%dx%d+%d+%d" % (width, height, left, top))
    w = Label(master, image=disphoto)
    w.pack()
    Button(master,text='确定',command=master.destroy).pack()

def callbackClose():
    tkinter.messagebox.showwarning(title='警告', message='不许关闭，好好回答！！！')

def biaobai():
    pygame.mixer.init()
    pygame.mixer.music.load(".\image\贝应铭 - 慢慢喜欢你 (Cover：莫文蔚).mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    bg_size = width,height = 200,190
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption('Music')
    clock = pygame.time.Clock()
    root = Tk()

    root.title("这个方式不太土")
    screenWidth = root.winfo_screenwidth()  # 获取显示区域的宽度
    screenHeight = root.winfo_screenheight()  # 获取显示区域的高度
    width = 600  # 设定窗口宽度
    height = 400  # 设定窗口高度
    left = (screenWidth - width) / 2
    top = (screenHeight - height) / 2

    # 宽度x高度+x偏移+y偏移
    # 在设定宽度和高度的基础上指定窗口相对于屏幕左上角的偏移位置
    root.geometry("%dx%d+%d+%d" % (width, height, left, top))

    frame1 = Frame(root)
    frame2 = Frame(root)

    textlable = Label(frame1,text='Hi，小姐姐 Do you love me?')
    textlable.pack()

    global lphoto
    global disphoto
    lphoto = PhotoImage(file=r"./image/07_400_300.jpg")
    disphoto = PhotoImage(file=r"./image/08_400_300.jpg")
    photo = PhotoImage(file=r"./image/09_400_300.jpg")
    w = Label(frame1, image=photo)
    w.pack()

    Button(frame2,text='喜欢',command=love,width=15)\
        .grid(row=0,column=0,sticky=W,padx=50,pady=5)

    Button(frame2,text='不喜欢',command=dislove,width=15)\
        .grid(row=0,column=1,sticky=E,padx=50,pady=5)

    frame1.pack()
    frame2.pack()


    root.protocol("WM_DELETE_WINDOW", callbackClose)

    mainloop()

if __name__ == '__main__':
    biaobai()
    time.sleep(60)
