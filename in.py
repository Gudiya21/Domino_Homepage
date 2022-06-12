# i=0
# while i<=10:
#     i+=1
#     if i==6:
#         continue 
#     print(i)
    

a=[1,3,3,2,4,4]
list=[]
for i in a:
    if i not in list:
        list.append(i)
print(list)


#     if b not in a:
#         print(a)
# #         list.append(a)
# # print(list)

# def rec(x):
#     if x==1:
#         return 1
#     else:
#         return(x*rec(x-1))
# num=3
# print(rec(num))
