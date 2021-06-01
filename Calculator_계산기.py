from tkinter import *

def click(key):
     if key=='=':
          result=eval(display.get())
          s=str(result)
          display.delete(0,END)
          display.insert(END,s)
     elif key=='C':
          display.delete(0,END)

     else:
          display.insert(END,key)

buttonText=[
     '7','8','9','/','C',
     '4','5','6','*','',
     '1','2','3','-','',
     '0','.','=','+','']

rowIndex=1
colIndex=0

window=Tk()
window.title("Calculator")
display=Entry(window,width=33)
display.grid(row=0,column=0,columnspan=5)

for button_Text in buttonText:
     def process(t=button_Text):
          click(t)
     Button(window,text=button_Text,width=5,
   command=process).grid(row=rowIndex,column=colIndex)
     colIndex+=1
     if colIndex>4:
          rowIndex+=1
          colIndex=0

window.mainloop()
