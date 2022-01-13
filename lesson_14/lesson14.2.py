# class MyFirstClass:
#     pass
#
# print(type(MyFirstClass))
#
# first_object = MyFirstClass()
#
# print(type(first_object))

class NewCar():
    model = "BMW"
    maxspeed = "300 hm/h"
    def start_engine(self):
        print("wroooom!!!")
    def turn(self):
        pass
    def stop(self):
        print(f"'{self.model}' stopped")

car_of_future = NewCar()
car_of_future.start_engine()
car_of_future.stop()
