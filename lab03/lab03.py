number =int(input("1. please input a number : ")) #將"輸入一個數"轉換型別為整數number
if (number%2)==0: #若number被2整除
    print("This is even") #寫出"這是偶數"
else: #否則
    print("This is odd") #寫出"這是奇數"
char=str(input("2.please input your student ID first character : ")) #將"輸入學號第一個英文字"轉換型別為字串char
idnumber=int(input("3.please input your student ID last 8 number : " )) #將"輸入學號後8碼"轉換型別為整數idnumber
if (idnumber%2)==0: #若idnumber被2整除
    print("your student ID number is even") #寫出"你的學號是偶數"
else: #否則
    print("your student ID number is odd") #寫出"你的學號是奇數"
ID=str(idnumber) #將idnumber轉換型別為字串
stuid=char+ID #學號stuid為字串char加上字串ID
print("your student ID is: "+stuid) #寫出"你的學號為:stuid"




