# 3. Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
#
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа.
#
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
#
# – Ура, можно построить треугольник!;
#
# – С отрицательными числами ничего не выйдет!;
#
# – Нужно вводить только числа!;
#
# – Жаль, но из этого треугольник не сделать.
#
#
#
# Нужно вспомнить правило для треугольника и длин его сторон

class TriangleChecker:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    # Метод is_triangle принимает 3 значения соответствующие размерам сторон
    # треугольника, опираясь на введенные данные определяет можно ли
    # построить треугольник, либо подходят ли данные которые ввел пользователь!

    def is_triangle(self, a, b, c):
        a = str(a)
        b = str(b)
        c = str(c)
        if (a.isdigit() or (a[0] == '-' and a[1:].isdigit())) and b.isdigit() or \
                (b[0] == '-' and b[1:].isdigit()) \
                and \
                c.isdigit() or (c[0] == '-' and c[1:].isdigit()):
            a = int(a)
            b = int(b)
            c = int(c)
            if a < 0 or b < 0 or c < 0:
                print('С отрицательными числами ничего не выйдет!')
            else:
                if a + b > c and a + c > b and b + c > a:
                    print('Ура, можно построить треугольник!')
                else:
                    print('Жаль, но из этого треугольник не сделать')

        else:
            print('Нужно вводить только числа!')


triangle1 = TriangleChecker()
triangle2 = TriangleChecker()
triangle3 = TriangleChecker()
triangle4 = TriangleChecker()
triangle1.is_triangle(20, 20, -20)
triangle2.is_triangle('cacda', 323, 343)
triangle3.is_triangle(300, 100, 50)
triangle4.is_triangle(5, 7, 10)

