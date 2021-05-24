#덧셈, 뺄셈, 곱셈, 나눗셈, 제곱을 하는 계산기 함수를 작성
def add(a,b):
     re=0
     re=a+b
     return re

def sub(a,b):
     re=0
     re=a-b
     return re

def mul(a,b):
     re=0
     re=a*b
     return re

def div(a,b):
     re=0
     re=a/b
     return re

def squ(a,b):
     re=0
     re=pow(a,b)
     return re

re=0

inp1=int(input("첫 번째 수를 입력하세요 : "))
inp=input("계산을 입력하세요(+, -, *, /, **) : ")
inp2=int(input("두 번째 수를 입력하세요 : "))

if inp1==0 or inp2==0:
     print("0으로는 나누면 안 됩니다.ㅠㅠ")
else:
     if inp=="+":
          re=add(inp1,inp2)
     if inp=="-":
          re=sub(inp1,inp2)
     if inp=="*":
          re=mul(inp1,inp2)
     if inp=="/":
          re=div(inp1,inp2)
     if inp=="**":
          re=squ(inp1,inp2)

     print("## 계산기 : %d %s %d = %d" %(inp1,inp,inp2,re))
