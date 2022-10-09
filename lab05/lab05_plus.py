key =input("Enter keys : ")  #將輸入的"Enter keys :"存為key

value =str(input("Enter values : "))  #將輸入的values存為字串
val =value.replace(" ", "")  #去除字串中的所有空格
v =val.split(',')  #用","作為字串的分隔


A =input("Enter keys : ")  

scoreA =str(input("Enter values : "))  #將輸入的分數存為字串
scoA =scoreA.replace(" ", "")  #去除字串中的所有空格
AA =scoA.split(',')  #用","作為字串的分隔


B =input("Enter keys : ")

scoreB =str(input("Enter values : "))
scoB =scoreB.replace(" ", "")
BB =scoB.split(',')

C =input("Enter keys : ")

scoreC =str(input("Enter values : "))
scoC =scoreC.replace(" ", "")
CC =scoC.split(',')

dict0 ={key:v, A:AA, B:BB, C:CC}  #建立字典
print("dict0 =",dict0)  #輸出字典