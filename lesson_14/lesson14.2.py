# class MyFirstClass:
#     pass
#
# print(type(MyFirstClass))
#
# first_object = MyFirstClass()
#
# print(type(first_object))
#
# class NewCar():  # Название класса
#     model = "BMW"  # атрибут класса
#     maxspeed = "300 hm/h"
#     def start_engine(self):
#         print("wroooom!!!")
#     def turn(self):
#         pass
#     def stop(self):
#         print(f"'{self.model}' stopped")
#
# car_of_future = NewCar()
# car_of_future.start_engine()
# car_of_future.stop()

class Cat:
    name = "Myrka"
    color = "Black"

    def say(self):
        print(f"{self.name} - said Meow")
        self. name = "Yellow"

    def play(self):
        print(f"{self.name} - is playing...")
        self.say()

cat1 = Cat()
print(cat1.name)

cat2 = Cat()
print(cat2.name)

cat1.name = "Vasyka"

print(cat1.name, cat2.name)

cat1.play()
cat2.play()