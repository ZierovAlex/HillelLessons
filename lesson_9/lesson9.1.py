def decorator_function(func):
    def wrapper():
        print('Функция обертка!')
        print('Обарачиваемая функция: {}'.format(func))
        print("Выполняем обёрнутую функцию...")
        func()
        print("Выходим из обертки")

    return wrapper


@decorator_function
def hello_world():
    print('Hello world!')


hello_world()

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
