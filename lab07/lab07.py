#super()，讓子類別具有父類別的方法。super().bath(....)
#沒有用到的def method()，可以直接pass。

class Animal():
    def __init__(self, weight, mood):
        self.weight=weight
        self.mood=mood
    def feed(self):
        pass
    def walk(self):
        pass
    def bath(self, n_bath):
        self.n_bath=n_bath
        self.mood = self.mood - n_bath*2 #super()，讓子類別具有父類別的方法。
    
class Dogs(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight , mood)  #繼承Animal的attributes
        #繼承 self.weight=weight 
        #繼承 self.mood=mood
    def feed(self, n_feed):
        self.n_feed=n_feed
        self.weight = self.weight + n_feed*0.2
        self.mood = self.mood + n_feed*1

    def walk(self, n_walk):
        self.n_walk = n_walk
        self.weight=self.weight - n_walk*0.2
        self.mood = self.mood + n_walk*2

    def bath(self, n_bath):
        #super()，讓子類別具有父類別的方法。super().bath(....)
        super().bath(n_bath)
        #super().bath(self, n_bath) TypeError: bath() takes 2 positional arguments but 3 were  given on line 33

    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed) #這裡需要呼叫前面的方法，不然前面打得程式碼不會被跑到
        self.walk(n_walk)
        self.bath(n_bath)
        print("狗狗現在的體重=" , self.weight, "狗狗現在的mood=", self.mood )

class Cats(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight , mood)  #繼承Animal的attributes

    def feed(self, n_feed):
        self.n_feed=n_feed
        self.weight = self.weight + n_feed*0.1
        self.mood = self.mood + n_feed*1

    def walk(self, n_walk):
        self.n_walk = n_walk
        self.weight=self.weight - n_walk*0.1
        self.mood = self.mood - n_walk*1

    def bath(self, n_bath):
        #super()，讓子類別具有父類別的方法。super().bath(....)
        super().bath(n_bath)
        #super().bath(self, n_bath) TypeError: bath() takes 2 positional arguments but 3 were  given on line 33

    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed) #同上，這裡需要呼叫前面的方法，不然前面打得程式碼不會被跑到
        self.walk(n_walk)
        self.bath(n_bath)
        print("貓貓現在的體重=" , self.weight, "貓貓現在的mood=", self.mood )

dog = Dogs(4.8, 65) 
dog.printf(18, 10, 4) 

cat = Cats(8.2, 60) 
cat.printf(40, 7, 1) 

#狗狗現在的體重= 6.4 kg, 心情 95
#貓貓現在的體重= 11.5 kg, 心情 91