key =input("Enter keys : ")

value =str(input("Enter values : "))
val =value.replace(" ", "")
v =val.split(',')


A =input("Enter keys : ")

scoreA =str(input("Enter values : "))
scoA =scoreA.replace(" ", "")
AA =scoA.split(',')


B =input("Enter keys : ")

scoreB =str(input("Enter values : "))
scoB =scoreB.replace(" ", "")
BB =scoB.split(',')

C =input("Enter keys : ")

scoreC =str(input("Enter values : "))
scoC =scoreC.replace(" ", "")
CC =scoC.split(',')

dict0 ={key:v, A:AA, B:BB, C:CC}
print("dict0 =",dict0)