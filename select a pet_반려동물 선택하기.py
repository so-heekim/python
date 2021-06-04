from tkinter import *

def button_click():
     
     if animal.get()==1:
          label2.pack_forget()
          photo=PhotoImage(file="dog3.jpg");
          pLabel.configure(image=photo)
          pLabel.image=photo
          
     if animal.get()==2:
          label2.pack_forget()
          photo=PhotoImage(file="cat2.jpg");
          pLabel.configure(image=photo)
          pLabel.image=photo
          
     if animal.get()==3:
          label2.pack_forget()
          photo=PhotoImage(file="rabbit.jpg");
          pLabel.configure(image=photo)
          pLabel.image=photo

          
window=Tk()

window.title("반려동물 선택하기")
window.geometry("400x410")
window.resizable(False, False)

label=Label(window,text="좋아하는 동물 투표",font=("궁서체",20),fg="blue",width=250)

animal=IntVar()
rb1=Radiobutton(window,text="강아지",variable=animal,value=1)
rb2=Radiobutton(window,text="고양이",variable=animal,value=2)
rb3=Radiobutton(window,text="토끼",variable=animal,value=3)

action=Button(window,text="사진 보기",command=button_click)
label2=Label(window,bg="yellow",width=100,height=100)

photo=PhotoImage()
pLabel=Label(window,image=photo,bg="yellow",width=200,height=200)

label.pack(pady=8,padx=8)

rb1.pack(pady=6,padx=6)
rb2.pack(pady=6,padx=6)
rb3.pack(pady=6,padx=6)

action.pack(pady=6,padx=6)
label2.pack(side="bottom",pady=6,padx=6)

pLabel.pack(side="bottom",pady=4,padx=4)

window.mainloop()
