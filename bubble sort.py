data_list = [3, 2, 1, 5, 4]
for i in range(len(data_list)-1):
    flag = False
    for x in range(len(data_list)-1-i):
        if data_list[x] > data_list[x+1]:
            data_list[x], data_list[x+1] = data_list[x+1], data_list[x]
            flag = True
    if not flag:
        break
print(data_list)