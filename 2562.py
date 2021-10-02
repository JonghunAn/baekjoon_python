num_list = list(input() for i in range(9))
num_list = list(map(int,num_list))
print(max(num_list))
print(num_list.index(max(num_list))+1)