#윈도우 창-지정된 위젯을 클릭했을 때 다른 함수 호출
from tkinter import *
from tkinter import messagebox

   #함수 선언 부분#
def clickImage(event):
     messagebox.showinfo("마우스","토끼에서 마우스가 클릭됨")

   #메인 코드 부분#
window=Tk()
window.geometry("400x400")

photo=PhotoImage(file="rabbit.gif")
label1=Label(window,image=photo)

label1.bind("<Button>",clickImage)

label1.pack(expand=1,anchor=CENTER)
window.mainloop()
