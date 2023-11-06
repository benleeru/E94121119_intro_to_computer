class Animal():
    def __init__(self, weight, mood):
        self.weight=weight
        self.mood=mood
    def feed(self):
        pass
    def walk(self):
        pass
    def bath(self, n_bath):
        self.mood = self.mood -2*n_bath #參考寫法，也可以寫pass 狗貓洗澡心情都-2
    
class Dogs(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight , mood)  #繼承Animal的attributes
        #繼承 self.weight=weight 
        #繼承 self.mood=mood

    def feed(self, n_feed):
        self.n_feed=n_feed
        self.weight = self.weight - n_feed*0.2
        self.mood = self.mood + n_feed*2

    def walk(self, n_walk):
        self.n_walk=n_walk
        self.weight = self.weight - n_walk*0.2
        self.mood = self.mood + n_walk*2

    def bath(self, n_bath):
        super().bath(n_bath) # 參考寫法
    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed) #這裡需要呼叫前面的方法，不然前面打得程式碼不會被跑到
        self.walk(n_walk)
        self.bath(n_bath)
        print("狗狗現在的體重=" , self.weight, "狗狗現在的mood=", self.mood )
        # print(f"狗狗現在的體重= {self.weight}kg 狗狗現在的mood={self.mood}")
              
class Shiba(Dogs):
    def __init__(self, weight, mood):
        super().__init__(weight , mood) #繼承屬性

    def feed(self, n_feed):
        self.n_feed=n_feed
        self.weight = self.weight + n_feed*0.3
        self.mood = self.mood + n_feed*5

    def walk(self, n_walk):
        super().walk(n_walk)

    def bath(self,n_bath ):
        super().bath(n_bath)

    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed)
        self.walk(n_walk)
        self.bath(n_bath)
        print("柴犬現在的體重=" , self.weight, "柴犬現在的mood=", self.mood )
              
    def mood_constraint(self, constraint):
        self.constr = constraint
        print("mood最高只能為=" ,self.constr )
        if ( self.constr < self.mood ):
            self.mood = self.constr
            print("所以，柴犬現在的心情", self.mood)

shiba = Shiba(5, 70) 
shiba.printf(20, 10, 3) 
shiba.mood_constraint(300) #請在這邊改變你的mood_constraint