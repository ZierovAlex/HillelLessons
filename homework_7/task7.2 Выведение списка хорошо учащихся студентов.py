# Создайте кортеж из 7-ми именованных кортежей учащихся ВУЗов. В именованном
# кортеже будут присутствовать следующие поля: имя студента, возраст, оценка
# за семестр, город проживания.#
# Написать код который готов обработать такой кортеж.
# Необходимо посчитать среднюю оценку по всем учащимся и выводить на печать
# следующее сообщение:
# “Ученики {имена студентов через запятую} в этом семестре хорошо учатся!”.
# В список студентов, которые выводятся по результатам работы программы, попадут
# лишь те, у которых оценка за семестр равна или выше средней по всем учащимся.

import random
good_students = []
students_tuple = (

  ("Иван", 18, 7.1, "Киев"),

  ("Светлана", 20, 8.2, "Киев"),

  ("Дмитрий", 19, 5.1, "Фастов"),

  ("Николай", 18, 7.0, "Одесса"),

  ("Стас", 18, 6.7, "Киев"),

  ("Илона", 20, 9.9, "Жмерынка"),

  ("Надя", 21, 8.6, "Маякы")

)
counter = 0
average_grade = 0
while True:
    average_grade += students_tuple[counter][2]
    counter += 1
    if counter == len(students_tuple):
        break
average_grade = round(average_grade / len(students_tuple), 1)
print(f"Средняя оценка по всем учащимся: {average_grade}")

for i in students_tuple:
    if i[2] >= average_grade:
        good_students.append(i[0])
if len(good_students) > 0:
    print(f"Ученики: {', '.join(good_students)} в этом семестре хорошо учатся!")
else:
    print('Ученики в этом семестре учатся плохо')

print('*'*100)
print("Реализовано со случайно генерирующимися оценками в диапазоне от 1 до "
      "10:")
print('*'*100)

good_students1 = []
students_tuple1 = (

  ("Иван", 18, round(random.uniform(1, 10), 1), "Киев"),

  ("Светлана", 20, round(random.uniform(1, 10), 1), "Киев"),

  ("Дмитрий", 19, round(random.uniform(1, 10), 1), "Фастов"),

  ("Николай", 18, round(random.uniform(1, 10), 1), "Одесса"),

  ("Стас", 18, round(random.uniform(1, 10), 1), "Киев"),

  ("Илона", 20, round(random.uniform(1, 10), 1), "Жмерынка"),

  ("Надя", 21, round(random.uniform(1, 10), 1), "Маякы")

)
print(students_tuple1)
counter1 = 0
average_grade1 = 0

while True:
    average_grade1 += students_tuple1[counter1][2]
    counter1 += 1
    if counter1 == len(students_tuple1):
        break
average_grade1 = round(average_grade1 / len(students_tuple1), 1)
print(f"Средняя оценка по всем учащимся: {average_grade1}")

for j in students_tuple1:
    if j[2] >= average_grade1:
        good_students1.append(j[0])
if len(good_students1) > 0:
    print(f"Ученики: {', '.join(good_students1)} в этом семестре хорошо "
          f"учатся!")
else:
    print('Ученики в этом семестре учатся плохо')