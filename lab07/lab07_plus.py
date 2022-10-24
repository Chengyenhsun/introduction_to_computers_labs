class Animal():  #定義父類別Animal
    def __init__(self, weight, mood):  #建構式
        self.weight = weight  #定義共用屬性
        self.mood = mood

    def feed(self):  #定義共用method
        pass

    def walk(self):
        pass

    def bath(self):
        pass

class Dogs(Animal):  #定義子類別
    def __init__(self, weight, mood):  #建構式
        super().__init__(weight, mood)  #執行父類別的方法 

    def feed(self, n_feed):  #定義子類別的共用方法
        self.weight = self.weight + n_feed*0.2
        self.mood = self.mood + n_feed*1

    def walk(self, n_walk):
        self.weight = self.weight - n_walk*0.2
        self.mood = self.mood + n_walk*2

    def bath(self, n_bath):
        self.weight = self.weight
        self.mood = self.mood - n_bath*2

    def printf(self, n_feed, n_walk, n_bath):  #定義輸出次數方法
        Dogs.feed(self, n_feed)  #呼叫子類別方法
        Dogs.walk(self, n_walk)
        Dogs.bath(self, n_bath)
        print("狗狗現在的體重=", self.weight ,"kg,", "心情", self.mood)  #輸出

class Shiba(Dogs):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)
    
    def feed(self, n_feed):
        self.weight = self.weight + n_feed*0.3
        self.mood = self.mood + n_feed*5
    
    def printf(self, n_feed, n_walk, n_bath):
        Shiba.feed(self, n_feed)
        Shiba.walk(self, n_walk)
        Shiba.bath(self, n_bath)
        print("柴犬現在的體重=", self.weight ,"kg,", "心情", self.mood)  #輸出

    def mood_constraint(self, constraint):
        self.constr = constraint
        if(90<=constraint<300):
                self.mood = self.constr
                print("所以，柴犬現在的心情", self.mood)
        print("mood 最高只能為=", self.constr)
    

shiba = Shiba(5, 70) 
shiba.printf(20, 10, 3) 
shiba.mood_constraint(90)







    

    
