list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3=[1,2,3]
sum_list = []
for (item1, item2,k) in zip(list1, list2,list3):
    sum_list.append(item1+item2+k)

print(sum_list)
