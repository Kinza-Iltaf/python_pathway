class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class Toyota(Car):
    def __init__(self,color):
        self.color = color
        print("car color is:",self.color)


car = Toyota("Blue")
car.start()
car.stop()









  


            




        

