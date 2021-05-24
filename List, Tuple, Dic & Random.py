#Q1
#-무작위 선택을 위해서 random 패키지를 사용
#-메뉴 화면은 튜플을 활용
#-이상형 목록은 리스트에 저장

import random
menu=("1.  이상형 추가","2.  결정하기","3.  이상형 명단보기","4.  새로 입력하기","5.  종료")
es=[]
i,j=0,0

print("===")
while True:
     for i in range(0,5):
          print("%s" %menu[i])
     an=int(input())
     
     if an==1:
          one=input("당신의 이상형은? ")
          es.append(one)
          
     elif an==2:
          if not es:
               print("값 없음")
               continue
          ran=random.randrange(len(es))
          print("당신의 이상형은 %s" %(es[ran]))
          
     elif an==3:
          print(es)
          
     elif an==4:
          es.clear()
          
     elif an==5:
          break





#Q2
#- 이름과 전화번호는 딕셔너리를 활용
#- Q를 입력하면 프로그램 종료

dic={}
i=0
while True:
     na=input("(입력모드) 이름을 입력하시오: ")
     
     if na=='Q':
          break
     
     if not na:
          a=0
          while a==0:
               sc=input("(검색모드) 이름을 입력하시오: ")
               if not sc:
                    a+=1
                    continue
               if dic.get(sc)==None:
                    print("%s 은 없습니다." %sc)
                    continue
               print("%s 의 전화번호는 %s 입니다." %(sc,dic.get(sc)))
          continue
     
     if na in dic.keys():
          up=input("(수정모드) 전화번호를 입력하시오: ")
          dic[na]=up
          continue
     
     ph=input("전화번호를 입력하시오: ")
     dic[na]=ph






#Q3
#-과목과 점수는 딕셔너리를 활용
#-입력을 받고 합계와 평균을 구하거나 입력 받는 과정에서 처리 가능
#-평균은 소수아래 한자리까지 반올림으로 출력

dic={}
summ,avg,i,ii=0,0,0,0
val,key=[],[]

while True:
     a=input("과목명: ")
     if not a:
          key=list(dic.keys())
          val=list(dic.values())
          for i in range(0,len(key)):
               print("%s %d" %(key[i],val[ii]))
               ii+=1
          print("합계는 %d점 입니다."%summ)
          print("평균은 %.1f점 입니다."%round(avg,1))
          break
     b=int(input("점수: "))
     summ+=b
     dic[a]=b
     avg=summ/len(dic)
