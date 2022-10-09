#建立字典dict0
dict0=dict(index=['國文', '英文', '數學', '自然', '社會'], StuA=[50, 60, 70, 80, 90], StuB=[57, 86, 73, 82, 43], StuC=[97, 96, 86, 97, 83])
print(dict0)

A=(dict0["StuA"])  #取出dict0字典中studentA的成績
sum = 0  #總合為0
for i in A:  #i在A list中
    sum += i  #成績加總
print()  
print("A學生平均成績 :", sum/len(A))  #顯示學生平均成績

B=(dict0["StuB"])
sum = 0
for i in B:
    sum += i  
print("B學生平均成績 :", sum/len(B))

C=(dict0["StuC"])
sum = 0
for i in C:
    sum += i
print("C學生平均成績 :", sum/len(C))

print()
avg=[]  #建立平均分數的list
subject=(dict0["index"])  #取出dict0字典中index的list
for i in range(len(A)):  #當i值為A序列長度
    temp=A[i]+B[i]+C[i]  #各科加總
    temp/=3  #計算平均
    avg.append(temp)  #將平均存入avg list

for i in range(len(A)):  #當i值為A序列長度
    print(subject[i]+"平均成績 : ",avg[i])  #顯示各科目平均分數
