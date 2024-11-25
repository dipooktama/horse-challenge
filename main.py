import random

# tes = random.randrange(1,99)
# print(tes)

# first make an array contains 5 arrays of 5 horses
big_array = []

for i in range(0,6):
    small_array = []
    for j in range(0,6):
        small_array.append(random.randrange(1,99))
    big_array.append(small_array)

print("initial horses")
print(big_array)
# eg [[46, 10, 85, 66, 27, 32], [70, 1, 50, 92, 67, 25], [25, 8, 26, 93, 86, 98], [20, 27, 68, 67, 11, 6], [96, 53, 20, 72, 42, 15], [64, 78, 76, 26, 67, 45]]

# now sort each array, and sort the big array by their first element
for smol_array in big_array:
    smol_array.sort(reverse=True)

print("first round")
print(big_array)

first_index_array = []
for content in big_array:
    first_index_array.append(content[0])

first_index_array.sort(reverse=True)
print("fastest in each batch on first round")
print(first_index_array)

new_big_array = []
for element in first_index_array:
    for content in big_array:
        if element == content[0]:
            new_big_array.append(content)

# starting second round
# fetch the peakest horse on first round
# then, compare the 2nd peakest horse against the first's batch
# if it wins, then it deserve its position, if not then it will be the third

the_peakest_horses = []
the_peakest_horses.append(new_big_array[0][0])

first_peakest_array = new_big_array[0]
first_peakest_array.pop(0)

temp_horse = new_big_array[1][0]
first_peakest_array.append(temp_horse)
print("second round batch")
print(first_peakest_array)

first_peakest_array.sort(reverse=True)
print("second round result")
print(first_peakest_array)
if first_peakest_array[0] == temp_horse:
    the_peakest_horses.append(temp_horse)
    first_peakest_array.remove(temp_horse)
    temp_horse = new_big_array[2][0]
    first_peakest_array.append(temp_horse)
    print("third round batch")
    print(first_peakest_array)
    first_peakest_array.sort(reverse=True)
    the_peakest_horses.append(temp_horse)
else:
    the_peakest_horses.append(first_peakest_array[0])
    if(first_peakest_array[1] == temp_horse):
        the_peakest_horses.append(temp_horse)
    else:
        the_peakest_horses.append(first_peakest_array[1])

print("final result")
print(the_peakest_horses)
