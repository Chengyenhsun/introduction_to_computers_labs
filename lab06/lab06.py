def gcd(a,b):  #定義計算最大公因數的函數
    if (a==0) or (b==0) :  #若其中一數為0
        print("0沒有gcd")  #輸出"0沒有最大公因數"
    else:  #否則取a,b中最大值、最小值
        m = max(a, b)  
        n = min(a, b)  
        r = m % n  #r為m/n之餘數
        while r != 0:  #當r不等於0
            m = n  
            n = r
            r = m % n  #r為m/n之餘數
        if n==1:  #若最大公因數為1
            print(a, "和", b, "互質")  #則輸出a和b互質
        else:
            print(a, "和", b, "的最大公因數為", n)  #否則輸出a和b最大公因數為n


ans1 = gcd(80, 20)  #計算80,20之最大公因數
ans2 = gcd(10, 0)   #計算10,0之最大公因數
ans3 = gcd(19, 20)  #計算19,20之最大公因數


