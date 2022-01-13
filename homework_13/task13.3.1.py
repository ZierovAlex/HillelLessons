from task13_2 import list_2d_operations as matrix
from task13_2 import input_check as check


print(matrix.matrix_generation_with_summs(), "\n")
a = matrix.matrix_2d_generator()
print(a, "\n")

print(matrix.wired_matrix(), "\n")

my_integer = check.integer_from_input()
print(my_integer, "\n")

my_string = check.string_from_input()
print(my_string, "\n")

my_2_words = check.two_words_sep_space()
print(my_2_words)

