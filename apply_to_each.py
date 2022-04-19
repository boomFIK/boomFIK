def aplly_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# numbers = [1, 0, 3.14, -2]

# aplly_to_each(numbers, abs)
# print(numbers)
# aplly_to_each(numbers, int)
# print(numbers)
# aplly_to_each(numbers, float)
# print(numbers)
# aplly_to_each(numbers, str)
# print(numbers)
numbers = [2, -2, 14, 0, 9.14, -1.25]

def change_direction(x):
    return x * -1

aplly_to_each(numbers, change_direction)
print(numbers)




