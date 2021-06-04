#1
n1 = int(input("첫번째 수를 입력해 주세요 : "))
n2 = int(input("두번째 수를 입력해 주세요 : "))

print(n1+n2)





#2
def len_long(wordList):
    for word in wordList:
        if len(word)>len(word1):
            a= word
        else:
            a=word1
    print (a)

word1=input("\n첫번째 문자열을 입력하시오 : ")
word=input("두번째 문자열을 입력하시오 : ")

wordList = word1.split()
wordList = word.split()

len_long(wordList)





#3
n= int(input("\n수를 입력해주세요 : "))

for i in range(0, n+1):
    print("*"*(n-i))





#4.
world=input("문자열을 입력해주세요 : ")
print('\"%s\"' %world)





#5.
number=int(input("\n숫자를 입력하세요 : "))
print(abs(number))





#6.
num1=int(input("\n첫번째 수를 입력하세요 : "))
num2=int(input("두번째 수를 입력하세요 : "))

if num1==num2:
    result=num1+num2
    print(result)
else:
    result_2=num2-num1
    print(result_2)





#7  - 1부터 n까지의 수 출력
i=0
nlist=[]
inp=int(input("\n숫자를 입력하시오 : "))

for i in range(0,inp):
     nlist.append(inp)
     inp=inp-1

pri=sorted(nlist,reverse=False)

i=0
for i in pri:
     print(i)





#8  - 배열 arr에서 인접하는 두 숫자 중 첫 번째 숫자에서 두 번째 숫자를 뺀 값을 차례대로 출력 
i=0
a=[]

inp1=int(input("\n배열 크기 입력 : "))        #4
inp2=input("숫자 입력 : ")             #"1 3 6 2"

a=inp2.split(" ")           #a=["1","3","6","2"]

for i in range(1, inp1):   #1,2,3
     print(int(a[i-1])-int(a[i]))





#9   
number=int(input("\n자연수를 입력하세요 : "))
print(int(str(number)[::-1]))





#10
s=input("\n문자열을 입력해주세요 : ")

if '1' in s:
    print(s.count('1'))
else:
    print(0)
