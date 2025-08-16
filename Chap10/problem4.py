from random import randint
class train:
    def __init__(self, trainno):
        self.trainno = trainno
    def book(self,trainno,fro,to):
        print(f"Ticket booked in train no:{trainno} from {fro} to {to}")
    def getStatus(self,trainno):
        print(f"Train no:{trainno} is running on time")
    def getfare(self,trainno,fro,to):
        print(f"Ticket fare in train no:{trainno} from {fro} to {to} is {randint(222,888)}")

t= train(12345)
t.book(12345, "Delhi", "Mumbai")  # This will book a ticket
t.getStatus(12345)  # This will book a ticket
t.book(12346, "Kolkata", "Mumbai")  # This will book a ticket