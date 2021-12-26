# def decorator_function(func):
#     def wrapper():
#         print('Функция обертка!')
#         print('Обарачиваемая функция: {}'.format(func))
#         print("Выполняем обёрнутую функцию...")
#         func()
#         print("Выходим из обертки")
#
#     return wrapper
#
#
# @decorator_function
# def hello_world():
#     print('Hello world!')


# hello_world()

# def benchmark(func):
#     import time
#
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#         return return_value
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage(url):
#     import requests
#     webpage = requests.get(url)
#     return webpage.text
#
#
# webpage = fetch_webpage('https://www.google.com.')
# print(webpage)
#
# def benchmark(func):
#
#     import time
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print('[*] Время выполнения: {} секунд.'.format(end - start))
#
#     return wrapper
#
#
# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://www.google.com.')
#
#
# fetch_webpage()
import random


def benchmark(func):
    import time
    def wrapper(sequence, look_for):
        start = time.time()
        print(func(sequence, look_for))
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
    return wrapper


@benchmark
def fetch_webpage(sequence, look_for):
    i = 0
    lengths = len(sequence)

    while i < lengths and look_for != sequence[i]:
        i += 1
    return i if i < lengths else None


random_list = [random.randint(1, 10000) for x in range(10000)]
random_integer = 10
fetch_webpage(random_list, random_integer)
