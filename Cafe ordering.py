#카페 주문 프로그램

ame, caf, ma, cont=0,0,0,0
c_ame, c_caf, c_ma=0,0,0

while True:
     print("""\n===== 슈먼 카페 =====
1.  아메리카노 : 2000원
2.  카페라떼 : 2500원
3.  마끼아또 : 3000원
4.  주문종료\n""")

     
     me = int(input("메뉴를 입력해주세요 => "))
     if me==4:
          print("주문을 종료합니다.")
          print("""\n**** 총 주문내역 ****
1.  아메리카노 : %d잔
2.  카페라떼 : %d잔
3.  마끼아또 : %d잔
총금액 : %d원""" %(ame,caf,ma,cont))
          break
     
     if me<=0 or me>4:
          print("잘못 입력되었습니다. 다시 입력해주세요.")
          print("""\n**** 총 주문내역 ****
1.  아메리카노 : %d잔
2.  카페라떼 : %d잔
3.  마끼아또 : %d잔
총금액 : %d원""" %(ame,caf,ma,cont))
          continue

     
     su = int(input("수량을 입력해주세요 => "))
     if me==1:
          ame+=su
          c_ame += 2000*su
     elif me==2:
          caf+=su
          c_caf += 2500*su
     elif me==3:
          ma+=su
          c_ma += 3000*su

     cont=c_ame+c_caf+c_ma
     
     print("""\n**** 총 주문내역 ****
1.  아메리카노 : %d잔
2.  카페라떼 : %d잔
3.  마끼아또 : %d잔
총금액 : %d원""" %(ame,caf,ma,cont))
