import random  #匯入隨機模組
list1 = ["One", "Two", "Three", "Four", "Five", "Six"]  #建立骰子1~6點的list
result_list=[0,0,0,0,0,0]  #建立1~6點出現次數的list
for i in range(1000000):  #當i在1000000次內
    roll = random.randint(1,6)  #擲骰子點數為1~6中隨機一個整數
    result_list[roll-1] += 1  #則result_list中點數出現的次數+1，list從0開始 因此把骰出值-1為點數的值

for i in range(len(result_list)):  
    print("The probability of", list1[i], "is", 'percent:{:.2%}'.format(result_list[i]/1000000)) #輸出結果，取百分比小數點後2位

