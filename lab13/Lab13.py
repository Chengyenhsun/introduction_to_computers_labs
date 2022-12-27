import matplotlib.pyplot as plt  #匯入matplotlib.pyplot
from matplotlib.pyplot import MultipleLocator
import numpy as np
with open('Temperature.txt') as f:  #讀檔並建立各年月份溫度的list
    lines = f.read()
    T = lines.split('\n')
    list = []
    temp_list = []
    for i in range(1, len(T)):
        list.append([T[i]])
    for i in range(len(list)):
        a = [float(x) for x in list[i][0].split(',')]
        del a[0]
        temp_list.append(a)

years = np.array(range(2013, 2022))  #建立年份和月份
month = np.array(range(1, 13))    

fig = plt.figure(figsize=(15,6))  #建立1*2子圖
fig.subplots(1, 2)

plt.subplot(1, 2, 1)  #繪製第一個子圖
for i in range(len(temp_list)):
    t = temp_list[i]
    plt.plot(month, t, label=years[i])  #繪製歷年的台南氣溫資料折線圖
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Month')
x_major_locator = MultipleLocator(1)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.ylabel('Temperature in Degree C')
plt.legend(loc = 'lower center')


plt.subplot(1,2,2)  #繪製第二個子圖
monthly_mean = np.mean(temp_list, axis=0)  #計算平均溫度
mean = []
for i in range(len(monthly_mean)):
    a = round(monthly_mean[i], 2)
    mean.append(a)

plt.plot(month, mean, marker='o', mec='r',mfc='r')  #繪製歷年的每個月份每年的氣溫平均值
for a,b in zip(month, mean):
    plt.text(a, b, b, ha='center', va='bottom')
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
total_mean = round(np.mean(mean), 2)  #計算總平均值
plt.axhline(y=total_mean, ls='--', color="red", label='Mean of 9 Years') #繪製平均線
plt.legend(fontsize=8)
plt.xlabel('Month')
x_major_locator = MultipleLocator(1)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
plt.ylabel('Temperature in Degree C')

fig.savefig('lab13_03.png')   