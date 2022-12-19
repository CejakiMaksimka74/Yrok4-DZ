# 17
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# n=int(input("Введите длину списка "))
# b=[1,1,2,0,-1,3,4,4]
# a=set(b)
# print(a)
# print(len(a))

# 19
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 2
# Output:  [4, 5, 1, 2, 3]
# num=[1,2,3,4,5]
# result=[]
# for i in range(0,len(num)):
# pop-вытолкнуть элемент
# n = 2
# array = [1, 2, 3, 4, 5]

# for i in range(0,n):
#     tmp = array[-1]
#     array.pop(-1)
#     array.insert(0,tmp)

# print(array)


# k=2
# n=[1,2,3,4,5]
# result=[]
# for i in range(0,k):
#     n.insert(0,n[-1])
#     print(n)
#     n.pop(-1)
# print(n)


# 19
# import random

# n = int(input('Введите длину списка >>> '))
# l = []
# for num in range(0,n):
    
#     random_number = round(random.randint(-10,10))
#     l.append(random_number)
# print(l)

# k = int(input('Введите на сколько индексов сдвигать >>> '))
# for i in range(k):
#     p = l.pop(-1)
#     l.insert(0, p)

# print(l)


# Напишите программу для печати всех уникальных значений в словаре. СЛОВАРЬ

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# slovar = {
#     "I": "S001",
#     "II": "S002",
#     "III": "S001",
#     "IV": "S005",
#     "V": " S005 ",
#     "VI": " S009 ",
#     "VII": " S007 ",
# }
# slovarB = slovar.values()
# print(set(slovarB))
# inpDict={
#     "I": "S001",
#     "II": "S002",
#     "III": "S001",
#     "IV": "S005",
#     "V": " S005 ",
#     "VI": " S009 ",
#     "VII": " S007 ",
# }
# res=set(inpDict.values())
# print(sorted(res))





# 23
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером) 


# Input: [0, -1, 5, 2, 3]
# Output: 2 

# пояснение
# (-1 < 5, 2 < 3

# array=[0, -1, 5, 2, 3]
# count=0
# for i in range(1,len(array)):
#     if array[i-1]<array[i]:
#         count +=1
# print(array)
# print(count)
