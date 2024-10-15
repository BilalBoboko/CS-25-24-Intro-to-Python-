# numbers = [1, 2, 3, 4, 5]
# number_1 = numbers[:]
# numbers[0] = 100
# number_1[1]= 200
# print("numbers:", numbers)
# print("number_1:", number_1)

# numbers= [1,2,3,4,5,6,7]
# slice_numbers = numbers[-3:]
# print(slice_numbers)
# a =[1,2,3]
# a =[1,2,3]
# b = [1,2,3,4]
# a.extend([10])
# print(a)

# b = []
# for i in a:
#     if i > 0:
#         b.append(i)
# print(b)

#
# a = [-3, -2, -1, 0, 1, 2]
# print( [int (item / 2)for item in a if item > 0 ])
# #
                                                                                                                                                           
# numbers = [-3, -2, -1, 0, 1, 2, 3]
# new_numbers = [n * 2 if n > 0 else n for n in numbers]
# print(new_numbers)

numbers = [-3, -2, -1, 0, 1, 2, 3]
new_numbers = [n ** 2 if  n < 0 else n ** 3 for n in numbers]
print(new_numbers)


a = 'Hello'
for c in a:
    print(a)
    