#left numeric triangle

# num = 1
# for i in range(1,5):
#     for _ in range(i):
#         print(num,end = " ")
#         num += 1
#     print()

#==================================
    
# #Floyd's pyramid

for i in range(6):
    for _ in range(5-i):
        print(" ",end="")
        
    
    for j in range(i):
        print(j+1,end=" ")
        
    print()

#==================================

# # left star triangle
# for i in range(5):
#     for _ in range(i):
#         print("*", end = " ")
#     print()
    
#==================================

# # right star triangle 


#==================================

# star pyramid
for i in range(5):
    for _ in range(4-i):
        print(" ",end = "")
    
    for _ in range(i):
        print("*", end =" ")
        
    print()

#==================================

#inverted centered star pyramid

# for i in range(5):
#     for _ in range(4, i):
#         print(" ",end = "")
    
#     for _ in range(i):
#         print("*", end =" ")
        
#     print()