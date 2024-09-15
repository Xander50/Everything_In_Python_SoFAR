# list1 = [10,20,72,86,90,99]
# pos2,pos4 = 2,4
# list1[pos2],list1[pos4]=list1[pos4],list1[pos2]
# pos2 = 2
# pos4 = 4
# list1[pos2] = list1[pos4]
# list1[pos4] = list1[pos2]
# print("list after swapping", list1)

# randList=["","","",""]
# numItems = len(randList)
# print("There are ",numItems, " items")

# randList=[[20,40],["Alexander","Jalil"],.3,[.9644664564,.545334]]
# numItems = len(randList[1])
# print("There are ",numItems, " items")

# numsList = [64,65,355,455,4]
# numsList[0] = numsList[4]
# numsList[4] = numsList[0]
# numsList[0],numsList[-1]=numsList[-1],numsList[0]
# print(numsList)

# numsList = [3,4,4,6,3,5,6,67,64,13]
# numInput = int(input("Enter the value for wether it exists in the list or not:"))
# if numInput in numsList:
#     print("This number exists in the list")
# else:
#     print("This number does not exist")
# for num in numsList:
#     if numInput == num:
#         print("This number exists in the list")
#     else:
#         print("This number does not exist in the list")

list1 = ["apple", "watermelon", "grape", "raisin","tomato"]
list2 = ["burger","Chick-fil-a-fries","Dr. Pepper","doritos","burrito"]
# list1.extend(list2)
# list1.append(list2)
combinedList=list1+list2
print(combinedList)
