# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i} * {j} = {i * j}")
#     print()
for i in range(2,9,2):
    if i == 2 or i == 4 or i == 8:
        for j in range(2,9,2):
            if i == 2 or i == 4 or i == 8:
                print(f"{i } * {j} = {i * j}")
