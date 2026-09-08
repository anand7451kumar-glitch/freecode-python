smallest_so_far = 100
print('Before', smallest_so_far)
for the_num in [9, 54, 56, 78] :
    if the_num < smallest_so_far :
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print('After', smallest_so_far)