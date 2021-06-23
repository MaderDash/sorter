#data = [ 1, 2, 3, 4, 5, 6]

def sorter(first_count):
    for count in range (first_count):
        if data[count+1] > data[count]:
            x = data[count]
            data[count] = data[count+1]
            data[count+1] = x
            print(data)
            


for first_count in range (len(data)-1,0,-1):
    print(first_count)
    sorter(first_count)
    print(data)
