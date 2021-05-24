#이름과 전화번호는 딕셔너리를 활용
#Q를 입력하면 프로그램 종료

#다음 기능을 추가해서 최종버전
#검색모드에서 “경영학과”, “소프트웨어학과“, “컴퓨터학과＂중 하나가 입력되면 해당학과 학생수와 이름 목록 출력

list2={}     #이름,학과 저장할 딕셔너리
b=[]         #추가-이름목록 담아둘 리스트
su=0        #추가-학생수 세기

while True:
     name=input("(입력모드) 이름을 입력하시오:")     #입력모드
     
     if name=='Q':     #입력모드에서 Q입력시 종료
          break
      
     if name in list2:         #입력받은 이름이 이미 입력받은 이름일때
          up=input("(수정모드) 학과를 입력하시오:")        #수정모드
          list2[name]=up       #수정결과 반영
          continue        #입력모드 변환
     
     if not name:             #입력모드에서 엔터입력시
          co=0                 #검색모드에서 엔터입력시 입력모드로 빠져나가기 위한 변수
          while co==0:       #엔터입력 전까지만 반복
               name_2=input("(검색모드) 이름을 입력하시오:")       #검색모드
          
               if name_2=="경영학과":             #추가-검색모드에서 경영학과 입력시
                    for key,value in list2.items():       #딕셔너리안의 이름과 전공 전체 반복
                         if value == '경영학과':      #그중 전공이 경영학과이면
                              b.append(key)        #이름목록 리스트에 이름 추가
                              su+=1                 #경영학과 학생 수 세기
                    print("경영학과 학생수:",su,"   이름목록:",b)     #경영학과 학생 수 , 이름목록 출력
                    su=0                          #학생수 초기화
                    b.clear()                      #이름목록 초기화

               if name_2=="컴퓨터학과":          #추가-검색모드에서 컴퓨터학과 입력시 (if문 안은 경영학과와 원리 같음)
                    for key,value in list2.items(): 
                         if value == '컴퓨터학과':
                              b.append(key)
                              su+=1
                    print("컴퓨터학과 학생수:",su,"   이름목록:",b)
                    su=0
                    b.clear()

               if name_2=="소프트웨어학과":       #추가-검색모드에서 소프트웨어학과 입력시 (if문 안은 경영학과와 원리 같음)
                    for key,value in list2.items(): 
                         if value == '소프트웨어학과':
                              b.append(key)
                              su+=1
                    print("소프트웨어학과 학생수:",su,"   이름목록:",b)
                    su=0
                    b.clear()
          
               if name_2 in list2:        #검색모드에서 입력한 이름이 딕셔너리에 있으면
                    print(name_2,"학생의 학과는",list2.get(name_2),"입니다.")         #입력한 이름 학생의 학과 출력
                    
               if not name_2:       #검색모드에서 엔터 입력시
                    co+=1           #while문 빠져나가기
                    continue        
               
               if list2.get(name_2)==None and name_2!="경영학과" and name_2!="컴퓨터학과" and name_2!="소프트웨어학과":        #검색모드 입력한 이름이 없을경우, 추가한 부분입력시 문구 출력 안되게 막기
                    print(name_2,"학생은 없습니다.")         #검색모드 입력한 이름의 학생은 없다고 출력
                    continue   
          continue       

     clas=input("학과를 입력하시오:")       #입력모드에서 학과 입력받기
     list2[name]=clas          #딕셔너리에 이름, 학과 저장
