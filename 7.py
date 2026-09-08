smallest = None
print('Before')
for value in [9, 45, 45, 45, 35] :
    if smallest is None :
        smallest = value

    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)