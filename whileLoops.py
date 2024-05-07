# nested for loops 
# nums = range(1,10000)
# # for num in nums:
# #     if num == 3:
# #         print('Found!')
# #         continue
# #     print(num)

# for num in nums:
#     for letter in 'abc':
#         for letter2 in 'abc':
#              for letter3 in 'abc':
#                  for letter4 in 'abc':
#                      print(num, letter, letter2, letter3) 

# #while loop
# #when you do not know the number of interactions 
# for i in range(1, 10):
#     print(i)

# x=0
# while True:
#     if x == 5:
#         break
#     print(x)
#     x += 1

while True:
    print("Enter your name:")
    name = input()
    if name == 'your name':
        print("your name is" + name)
        break
    else:
        print("Thank you!")