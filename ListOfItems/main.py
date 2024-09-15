nums=[2,5,2,5,2,4,4565,56654,33,2304]
print(nums)
print(nums[8])
print(nums[2:8])
print(nums[:3])
print(nums[5:])
print(nums[-4])

names=["Alexandre","Jalil","Jose","Gabriel"]
print(names)
print(names[3])
print(names[:3])
print(names[-3])

tensNums=[10,20,30,40,50,60,70,80,90,100]
tensNums[1] = 3
print(tensNums)
tensNums[4:7]=[15,62,21]
print(tensNums)
tensNums[3:4]=[200,300]
print(tensNums)
tensNums[9:11] =[1000]
print(tensNums)

hundredNums = [100,200,300,400,500,600,700,800,900,1000]
hundredNums.insert(2,250)
print(hundredNums)

hundredNums.append(1100)
print(hundredNums)

fruits=["watermelon","apple","banana","strawberries","mango"]
vegetables=["green beans","carrots","broccoli","egg plant","cabbage"]
fruits.extend(vegetables)
print(fruits)

fruits.remove("apple")
fruits.remove(fruits[1])
fruits.pop(2)
print(fruits)