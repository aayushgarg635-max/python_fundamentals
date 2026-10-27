from random import randint

class train:
    def __init__(self,trainno):
        self.trainno =trainno

    def book(self,fro,to):
        print(f" ticket is booked in train no :{self.trainno} from {fro} to {to}")

    def getstatus(self):
        print(f" The train no :{self.trainno} is tunning on time")

    def getfare(self,fro,to):
        print(f" the train fare for train no : {self.trainno} from {fro} to {to} is {randint(250,7500)}")

t = train(6500)
t.book("delhi","bombay")
t.getstatus()
t.getfare("delhi","bombay")


