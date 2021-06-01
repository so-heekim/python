from tkinter import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *

   ## 함수 선언 부분 ##

#마우스 클릭 시 실행되는 함수
def mouseClick(event):
     global x1, y1, x2, y2   #전역 변수로 쓰인 변수를 이 함수 내부에서 사용
     x1=event.x               #x1, y1를 이벤트가 발생한 좌표값으로 설정
     y1=event.y

#마우스 클릭 해제(드롭)시 실행되는 함수
def mouseDrop(event):
     global x1, y1, x2, y2, penWidth, penColor
     x2=event.x             #x2, y2를 이벤트가 발생한 좌표값으로 설정
     y2=event.y
     #지정된 좌표 및 선 두께, 색상을 이용하여 선 만들기
     canvas.create_line(x1, y1, x2, y2, width=penWidth, fill=penColor)

#선 색상 선택 버튼 클릭 시 실행되는 함수
def getColor():
     global penColor
     color=askcolor()
     penColor=color[1]

#선 두께 결정 버튼 클릭 시 실행되는 함수
def getWidth():
     global penWidth
     penWidth=askinteger("선 두께", "선 두께(1~10)를 입력하세요",minvalue=1,maxvalue=10)


    ## 전역 변수 선언 부분 ##
window=None
canvas=None
x1, y1, x2, y2,=None, None, None, None     #선의 시작점과 끝점
penColor="black"
penWidth=5

    ## 메인 코드 부분 ##
if __name__=="__main__":
     window=Tk()
     window.title("그림판 비슷한 프로그램")
     canvas=Canvas(window,height=300, width=300)

     canvas.bind("<Button-1>",mouseClick)
     canvas.bind("<ButtonRelease-1>",mouseDrop)
     canvas.pack()

     mainMenu=Menu(window)
     window.config(menu=mainMenu)

     fileMenu=Menu(mainMenu)
     mainMenu.add_cascade(label="설정",menu=fileMenu)
     fileMenu.add_command(label="선 색상 선택",command=getColor)
     fileMenu.add_separator()
     fileMenu.add_command(label="선 두께 결정",command=getWidth)

     window.mainloop()
       
