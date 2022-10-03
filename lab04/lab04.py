A = []  #建立A學生成績list
B = []  #建立B學生成績list
C = []  #建立C學生成績list
avg=[]  #建立平均分數的list

print("開始輸入A學生的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:") 
count = 0  #迴圈起始值為0
while(count < 5):  #當圈數<5時
    scoreA = int(input())  #輸入A學生成績
    A.append(scoreA)  #將成績存入A list
    count += 1  #計數+1

print("A學生成績:")  #顯示"A學生成績:"
print("國文:", A[0], "、英文:", A[1], "、數學:", A[2], "、自然:", A[3], "、社會:", A[4])  #分別抓出list中的值顯示成績

print()       
print("開始輸入B學生的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:")
count = 0
while(count < 5):
    scoreB = int(input())
    B.append(scoreB)
    count += 1

print("B學生成績:")
print("國文:", B[0], "、英文:", B[1], "、數學:", B[2], "、自然:", B[3], "、社會:", B[4])

print()      
print("開始輸入C學生的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:")
count = 0
while(count < 5):
    scoreC = int(input())
    C.append(scoreC)
    count += 1

print("C學生成績:")
print("國文:", C[0], "、英文:", C[1], "、數學:", C[2], "、自然:", C[3], "、社會:", C[4])

intA = [int(i) for i in A]  #將學生各科成積存為數值的list
sum = 0  #總合為0
for i in intA:  #i在intA list中
    sum += i  #成績加總
print()  
print("A學生平均成績 :", sum/len(A))  #顯示學生平均成績

intB = [int(i) for i in B]
sum = 0
for i in intB:
    sum += i
print("B學生平均成績 :", sum/len(B))

intC = [int(i) for i in C]
sum = 0
for i in intC:
    sum += i
print("C學生平均成績 :", sum/len(C))

print() 
for i in range(len(A)):  #當i值為A序列長度
    temp=intA[i]+intB[i]+intC[i]  #各科加總
    temp/=3  #計算平均
    avg.append(temp)  #將平均存入avg list

x=["國文平均 :", "英文平均 :", "數學平均 :", "自然平均 :", "社會平均 :"]  
for i in range(len(A)):  #當i值為A序列長度
    print(x[i],avg[i])  #顯示各科目平均分數
