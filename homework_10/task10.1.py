import random


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return_value = end - start
        print(return_value)
        return return_value

    return wrapper


@benchmark
def linear_search(sequence, look_for):
    i = 0
    length = len(sequence)

    while i < length and look_for != sequence[i]:
        i += 1
    return i if i < length else None


random_list = [random.randint(6, 10000) for x in range(2000000)] + [5]
random_integer = 5
a = linear_search(random_list, random_integer)


@benchmark
def linear_search_virt(sequence1, look_for1):
    j = 0
    sequence1.append(look_for1)
    length1 = len(sequence1) - 1

    while look_for1 != sequence1[j]:
        j += 1
    return j if j < length1 else None


b = linear_search_virt(random_list, random_integer)

print(f"Обычный линейный поиск занимает {a} секунд и улучшенный Витром {b} "
      f"секунд что на "
      f" {a - b} секунд меньше")
