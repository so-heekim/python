#지우개 / 여러 도형 / 이미지 넣기 / 선 종류 / 도장

from tkinter import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *
from tkinter.filedialog import *

def mouseClick(event):
     global x1, y1, x2, y2   
     x1=event.x               
     y1=event.y
     
def mouseDrop(event):
     global x1, y1, x2, y2, penWidth, penColor
     x2=event.x
     y2=event.y
     canvas.create_line(x1, y1, x2, y2, width=penWidth, fill=penColor)

def getColor():
     global penColor
     color=askcolor()
     penColor=color[1]
     
def getWidth():
     global penWidth
     penWidth=askinteger("선 두께", "선 두께(1~10)를 입력하세요",minvalue=1,maxvalue=10)

def clear():
     global penColor,penWidth,dColor,dWidth
     penColor="#f1f1f1"
     dColor="#f1f1f1"

def clearCanvas():
     canvas.delete("all")

def f_open():
    global im,x2,y2
    photo = askopenfilename(parent=window ,title="Select file",
                                    filetypes=(("GIF 파일","*.gif"),("모든 파일","*.*")))
    im=PhotoImage(file=photo)
    canvas.create_image(x2,y2,image=im)
     
def f_exit():
     window.destroy()

def p1(event):
    global x1,y1
    x1=event.x
    y1=event.y
    canvas.create_oval(x1-50,y1-50,x1+50,y1+50,fill=color[1])
    
def p2(event):
    global x1,y1
    x1=event.x
    y1=event.y
    canvas.create_rectangle(x1-50,y1-50,x1+50,y1+50,fill=color[1])

def p3(event):
    global x1,y1
    x1=event.x
    y1=event.y
    canvas.create_polygon(x1, y1-70, x1-60, y1+40, x1+60, y1+40, fill=color[1])      #(x1,y1),(x2,y2),(x3,y3)을 꼭짓점으로 하는 삼각형 그리기
    
def ce():
    global color
    color=askcolor()
    canvas.bind("<Double-Button-1>",p1)

def rec():
    global color
    color=askcolor()
    canvas.bind("<Double-Button-1>",p2)

def tri():
    global color
    color=askcolor()
    canvas.bind("<Double-Button-1>",p3)

def sun(event):
     if t=='b':
          global x1, y1, penWidth, penColor
          canvas.create_line(x1,y1,event.x,event.y, width=penWidth, fill=penColor)
          x1=event.x
          y1=event.y

def sun2(event):
      if t=='b':
          global x1, y1, penWidth, penColor
          canvas.create_text(x1,y1,text = "⁕", font=("나눔고딕코딩", penWidth+7), fill=penColor)
          x1=event.x
          y1=event.y

def sun3(event):
      if t=='b':
          global x1, y1, penWidth, penColor
          canvas.create_text(x1,y1,text = "♡", font = ("나눔고딕코딩", penWidth+7), fill=penColor)
          x1=event.x
          y1=event.y
     
def a():
     global t
     t='a'
     canvas.bind("<ButtonRelease-1>",mouseDrop)
     
def b():
     global t
     t='b'
     canvas.bind("<B1-Motion>", sun)

def c():
     global t
     t='b'
     canvas.bind("<B1-Motion>", sun2) 

def d():
     global t
     t='b'
     canvas.bind("<B1-Motion>", sun3) 

def Color():
     global dColor
     color=askcolor()
     dColor=color[1]
     
def Width():
     global dWidth
     dWidth=askinteger("도장 크기", "도장 크기(1~50)를 입력하세요",minvalue=1,maxvalue=50)

def ha(event):
     global x1, y1, dWidth, dColor
     x1=event.x               
     y1=event.y
     canvas.create_text(x1,y1,text ="♡", font =("나눔고딕코딩", dWidth), fill=dColor)

def bha(event):
     global x1, y1, dWidth, dColor
     x1=event.x               
     y1=event.y
     canvas.create_text(x1,y1,text = "♥", font = ("나눔고딕코딩", dWidth), fill=dColor)
     
def st(event):
     global x1, y1, dWidth, dColor
     x1=event.x               
     y1=event.y
     canvas.create_text(x1,y1,text = "☆", font = ("나눔고딕코딩", dWidth), fill=dColor)
     
def bst(event):
     global x1, y1, dWidth, dColor
     x1=event.x               
     y1=event.y
     canvas.create_text(x1,y1,text = "★", font = ("나눔고딕코딩", dWidth), fill=dColor)
     
def le(event):
     global x1, y1, dWidth, dColor
     x1=event.x               
     y1=event.y
     canvas.create_text(x1,y1,text = "←", font = ("나눔고딕코딩", dWidth), fill=dColor)
     
def ri(event):
     global x1, y1, dWidth, dColor
     x1=event.x               
     y1=event.y
     canvas.create_text(x1,y1,text = "→", font = ("나눔고딕코딩", dWidth), fill=dColor)
     
def che(event):
     global x1, y1, dWidth, dColor
     x1=event.x               
     y1=event.y
     canvas.create_text(x1,y1,text = "√", font = ("나눔고딕코딩", dWidth), fill=dColor)
     
def h():
     canvas.bind("<ButtonRelease-3>", ha)

def bh():
     canvas.bind("<ButtonRelease-3>", bha)

def s():
     canvas.bind("<ButtonRelease-3>", st)

def bs():
     canvas.bind("<ButtonRelease-3>", bst)

def l():
     canvas.bind("<ButtonRelease-3>", le)

def r():
     canvas.bind("<ButtonRelease-3>", ri)

def ch():
     canvas.bind("<ButtonRelease-3>", che)
             

    
window=None
canvas=None
x1, y1, x2, y2=None, None, None, None
penColor="black"
penWidth=5
dColor="black"
dWidth=20

if __name__=="__main__":
     window=Tk()
     window.resizable(False, False)
     window.title("PyQt5 그림판")
     
     canvas=Canvas(window,height=500, width=500)
     canvas.bind("<Button-1>",mouseClick)
     canvas.bind("<ButtonRelease-1>", mouseDrop)
     canvas.pack()
     
     mainMenu=Menu(window)
     window.config(menu=mainMenu)

     m_1=Menu(mainMenu,tearoff=0)
     mainMenu.add_cascade(label="파일",menu=m_1)
     m_1.add_command(label="그림 불러오기(위치먼저선택)",command=f_open)
     m_1.add_separator()
     m_1.add_command(label="끝내기",command=f_exit)

     m_2=Menu(mainMenu,tearoff=0)
     mainMenu.add_cascade(label="선 설정",menu=m_2)
     m_2.add_command(label="직선(기본)",command=a)
     m_2.add_separator()
     m_2.add_command(label="곡선",command=b)
     m_2.add_separator()
     m_2.add_command(label="⁕선",command=c)
     m_2.add_separator()
     m_2.add_command(label="♡선",command=d)

     m_3=Menu(mainMenu,tearoff=0)
     mainMenu.add_cascade(label="펜 설정",menu=m_3)
     m_3.add_command(label="색상 선택",command=getColor)
     m_3.add_separator()
     m_3.add_command(label="두께 결정",command=getWidth)

     m_4=Menu(mainMenu,tearoff=0)
     mainMenu.add_cascade(label="도형(더블클릭)",menu=m_4)
     m_4.add_command(label="원",command=ce)
     m_4.add_separator()
     m_4.add_command(label="네모",command=rec)
     m_4.add_separator()
     m_4.add_command(label="세모",command=tri)

     m_5=Menu(mainMenu,tearoff=0)
     mainMenu.add_cascade(label="도장(오른쪽 클릭)",menu=m_5)
     m_5.add_command(label="♡",command=h)
     m_5.add_separator()
     m_5.add_command(label="♥",command=bh)
     m_5.add_separator()
     m_5.add_command(label="☆",command=s)
     m_5.add_separator()
     m_5.add_command(label="★",command=bs)
     m_5.add_separator()
     m_5.add_command(label="←",command=l)
     m_5.add_separator()
     m_5.add_command(label="→",command=r)
     m_5.add_separator()
     m_5.add_command(label="√",command=ch)

     m_6=Menu(mainMenu,tearoff=0)
     mainMenu.add_cascade(label="도장 설정",menu=m_6)
     m_6.add_command(label="도장 색",command=Color)
     m_6.add_separator()
     m_6.add_command(label="도장 크기",command=Width)

     m_7=Menu(mainMenu,tearoff=0)
     mainMenu.add_cascade(label="지우개",menu=m_7)
     m_7.add_command(label="부분 지우기",command=clear)
     m_7.add_separator()
     m_7.add_command(label="모두 지우기",command=clearCanvas)

window.mainloop()
