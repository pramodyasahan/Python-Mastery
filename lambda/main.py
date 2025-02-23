add = lambda a, b: a + b

print(add(3, 7))

points_2D = [(1, 2), (4, -3), (10, 7), (-2, 8)]
sorted_list_first = sorted(points_2D, key=lambda point: point[0])
sorted_list_second = sorted(points_2D, key=lambda point: point[1])
print(f"sorted_list_first: {sorted_list_first}")
print(f"sorted_list_second: {sorted_list_second}")

num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mult_list = map(lambda x: x * 2, num_lst)
print(list(mult_list))

num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = filter(lambda x: x % 2 == 0, num_lst)
print(list(even_list))
