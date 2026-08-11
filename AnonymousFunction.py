#map() function
num_list = [2,5, 3, 7, 4, 8, 9, 1]

cube = list(map(lambda x: x**3, num_list))
print(cube)

#filter() function
num_list = [2,5, 3, 7, 4, 8, 9, 1]

even = list(filter(lambda x: x%2==0, num_list))
print(even)