my_list = [1, 2, 3, 4, 5]

a, b, c, d, e = my_list
print(f"Unpacked values: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")

a, _, c, _, e = my_list
print(f"Skipping some values: a = {a}, c = {c}, e = {e}")

x, *rest = my_list
print(f"First element: x = {x}, Remaining: rest = {rest}")

*start, z = my_list
print(f"Last element: z = {z}, Starting elements: start = {start}")

first, *middle, last = my_list
print(f"First: first = {first}, Middle: middle = {middle}, Last: last = {last}")

try:
    a, b, c, d, e, f = my_list
except ValueError as ve:
    print("Error:", ve)

a, b, *rest = my_list
print(f"First two: a = {a}, b = {b}, Rest: rest = {rest}")