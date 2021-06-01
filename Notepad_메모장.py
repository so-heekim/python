from tkinter import *
from tkinter.filedialog import *
import os

def saveFile():
     f=asksaveasfile(mode="w",defaultextension=".txt")
     if f is None:
          return
     ts=str(ta.get(1.0,END))
     f.write(ts)
     f.close()

top=Tk()
top.title("메모장")
top.geometry("400x400")

ta=Text(top)

#텍스트 입력부분 크기에 맞게 전체 윈도우 사이즈 조절
top.grid_rowconfigure(0,weight=1)
top.grid_columnconfigure(0,weight=1)

#텍스트가 4면을 모두 다 채우도록 고정
ta.grid(sticky=N+E+S+W)

file=None
mb=Menu(top)
fi=Menu(mb)
mb.add_cascade(label="파일",menu=fi)
fi.add_command(label="저장",command=saveFile)

top.config(menu=mb)

top.mainloop()
