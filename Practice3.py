            # STRINGS #


# #STRING INDICES
# str = 'Hello World'
# print(str[1])
# print(str[2+4])
# print(str[-1])



# # STRING OPERATIONS
# str1 = 'Hello'
# str2 = 'World'
# str3 = str1 + str2
# print(str3)
# print(str1 * 2)
# print('Wo' in str2)
# print('lo' not in str1)
# print(str3[0:5])
# print(str3[0:11:2])
# print(str1[-6:-1])



# #BUILT IN FUNCTIONS
# str1 = 'hello'
# str2 = 'WORLD'
# str3 = '     Hello'
# str4 = 'World     '
# str5 = '   Hello   '
# str6 = 'India is a great Country'
# print(len(str1))
# print(str1.title())
# print(str2.lower())
# print(str1.upper())
# print(str1.count('l'))
# print(str2.find('D'))
# print(str1.index('l'))
# print(str2.endswith('W'))
# print(str1.startswith('h'))
# print(str2.isalnum())
# print(str1.islower())
# print(str2.isupper())
# print(str1.isspace())
# print(str2.istitle())
# print(str3.lstrip())
# print(str4.rstrip())
# print(str5.strip())
# print(str1.replace('l','*'))
# print(str6.partition('is'))
# print(str6.split())



# #CHAR COUNT IN STRING
# def charcount(ch,st):
#     count = 0
#     for character in st:
#         if character == ch:
#             count += 1
#     return count
# st = input("Enter a string: ")
# ch = input("Enter the character to be searched: ")
# count = charcount(ch,st)
# print("The number of times the character ",ch," has occured is: ",count)



# #REPLACE VOWELS
# def replacevowel(st):
#     newstr = ''
#     for character in st:
#         if character in 'aeiouAEIOU':
#             newstr += '*'
#         else:
#             newstr += character
#     return newstr
# st = input("Enter a string: ")
# str1 = replacevowel(st)
# print("the original string: ",st)
# print("The modified string: ",str1)



# #REVERSE A STRING
# def reversestring(st):
#     newstr = ''
#     for i in range(-1,-len(st)-1,-1):
#         newstr += st[i]
#     return newstr

# st = input("Enter a string: ")
# str = reversestring(st)
# print("The reversed string is: ",str)



# #PALINDROME OF STRING
# def checkPalin(st):
#     i = 0
#     j = len(st) - 1
#     while i <= j:
#         if(st[i] != st[j]):
#             return False
#         i += 1
#         j -= 1
#     return True

# st = input("Enter a string: ")
# result = checkPalin(st)
# if result == True:
#     print("The given string ",st," is Palindrome")
# else:
#     print("The given string ",st," is not Palindrome")





           # LISTS #

# #LIST INDICES
# list = [4,12,'D','R',24,9]
# print(list)
# print(list[3])
# print(list[1+4])
# print(list[-6])



# #LIST OPERATIONS
# list1 = [2,4,6]
# list2 = [8,10,12]
# print(list1 + list2)
# print(list1 * 2)
# print(10 in list2)
# print(list1[0:2])
# print(list2[0:3:2])
# print(list1[::-1])



# #BUILT IN FUNCTIONS
# list1 = [10,20,30,40,50]
# print(len(list1))
# list1.append(60)
# print(list1)
# list2 = [70,80]
# list1.extend(list2)
# print(list1)
# list1.insert(8,90)
# print(list1)
# print(list1.count(20))
# print(list1.index(50))
# list1.remove(90)
# print(list1)
# print(list1.pop(4))
# list1.reverse()
# print(list1)
# list1.sort(reverse = True)
# print(list1)
# print(min(list1),max(list1),sum(list1))



# #MENU DRIVEN OPERATIONS ON LIST
# list = [22,4,16,38,13]
# choice = 0
# while True:
#     print("\nLIST OPERATIONS")
#     print("1. Append an element")
#     print("2. Insert an element at desired position")
#     print("3. Append a lst to given list")
#     print("4. Modify an existing element")
#     print("5. Delete an existing element by its position")
#     print("6. Delete an existing element by its value")
#     print("7. Sort the list in ascending order")
#     print("8. Sort the list in descending order=")
#     print("9. Display the list")
#     print("10. EXIT")

#     choice = int(input("Enter your choice (1-10): "))

#     if choice == 1:
#         element = int(input("Enter the element to be appended: "))
#         list.append(element)
#         print("The element has been appended\n")

#     elif choice == 2:
#         element = int(input("Enter the element to be appended: "))
#         pos = int(input("Enter the position: "))
#         list.insert(pos,element)

#     elif choice == 3:
#         list2 = eval(input("Enter the elements seperated by commas"))
#         list.extend(list2)
#         print("The list has been appended\n")

#     elif choice == 4:
#         i = int(input("Enter the position of element to be modified: "))
#         if i < len(list):
#             newelement = int(input("Enter the new element: "))
#             oldelement = list[i]
#             list[i] = newelement
#             print("The element ",oldelement," has ben modified\n")
#         else:
#             print("Position of element is more than the lenght of string")

#     elif choice == 5:
#         i = int(input("Enter the position of element to be deleted: "))
#         if i < len(list):
#             element = list.pop(i)
#             print("The element  has been deleted\n")
#         else:
#             print("Position is more than length of string")
    
#     elif choice == 6:
#         element = int(input("Enter the element to be deleted: "))
#         if element in list:
#             list.remove(element)
#             print("The element has been deleted\n")
#         else:
#             print("Element ",element," is not present in the list")
    
#     elif choice == 7:
#         list.sort()
#         print("The list has been sorted\n")

#     elif choice == 8:
#         list.sort(reverse = True)
#         print("The list has been sorted in reverse order\n")

#     elif choice == 9:
#         print("The list is: ",list)

#     elif choice == 10:
#         break

#     else:
#         print("Choice is not valid..!!")



# #AVERAGE MARKS OF N STUDENTS
# def average(list,n):
#     total = 0
#     for marks in list:
#         total += marks
#     average = total/n
#     return average
# list = []
# print("How many students marks you want to enter: ")
# n = int(input())
# for i in range(0,n):
#     print("Enter marks of student: ")
#     marks = int(input())
#     list.append(marks)
# average = average(list,n)
# print("Average marks of ",n," students is: ",average)



# #SEARCHING A NUMBER IN LIST
# def search(num,list):
#     for i in range (0,len(list)):
#         if list[i] == num:
#             return i
#     return None
# list = []
# n = int(input("Enter the number of elements: "))
# for i in range (0,n):
#     m = int(input("Enter the elements: "))
#     list.append(m)
# num = int(input("Enter the number to be searched: "))
# result = search(num,list)
# if result is None:
#     print("Number",num," is not present in list")
# else:
#     print("Number ",num," is present at ",result," index")




            # TUPLES #

# # TUPLE INDICES
# tuple1 = (10,20,'Python','CSE')
# print(tuple1)
# print(tuple1[2])
# print(tuple1[1+2])
# print(tuple1[-1])
# tuple2 = (1,2,3,[8,9])
# tuple2 [3][1] = 10
# print(tuple2)



# # TUPLE OPERATIONS
# tuple1 = (1,3,5,7,9)
# tuple2 = (2,4,6,8,10)
# print(tuple1 + tuple2 )
# print(tuple1 + (11,13))
# print(tuple2 * 2)
# print(2 in tuple2)
# print(tuple1[0:5])
# print(tuple2[0:5:2])
# print(tuple1[::-1])



# #BUILT IN FUNCTIONS
# tuple1 = (2,4,6,8,10)
# print(len(tuple1))
# tuple2 = tuple()
# print(tuple1.count(4))
# print(tuple1.index(8))
# print(max(tuple1),min(tuple1),sum(tuple1))



# #ASSIGNMENT OF TUPLES
# record = ('Python','101','CS')
# (Subject,Code,Branch) = record
# print(Subject)
# print(Code)
# (num1,num2) = (10+5,20-8)
# print(num1,num2)



# #NESTED TUPLES
# st = ((101,'Aman',98),(102,'Geet',95),(103,'Sahil',87),(104,'Pawan',79))
# print('SNo','   RollNo','     Name','  Marks')
# for i in range(0,len(st)):
#     print((i+1),'\t',st[i][0],'\t',st[i][1],'\t',st[i][2])



# #SWAP NUMBERS
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter a second number: "))
# print("\nNumbers before swapping:")
# print("First Number: ",num1)
# print("Second Number: ",num2)
# (num2,num1) = (num1,num2)
# print("\nNumbers after swapping: ")
# print("First Number: ",num1)
# print("Second Number: ",num2)



# #AREA CIRCUMFERENCE OF CIRCLE
# def circle(r):
#     area = 3.14 * r * r
#     circumference = 2 * 3.14 * r
#     return (area,circumference)
# r = float(input("Enter the radius: "))
# area,circumference = circle(r)
# print("Area is ",area)
# print("Circumference is: ",circumference)



# #N NUMBERS IN TUPLE MAXMIN
# numbers = tuple()
# n = int(input("Enter the number of elements: "))
# for i in range (0,n):
#     num = int(input())
#     numbers = numbers +(num,)
# print("\nThe numbers in tuple are: ")
# print(numbers)
# print("\nThe maximum number is: ",max(numbers))
# print("\nThe minimum number is: ",min(numbers))








                 # DICTIONARIES #

# #DICTIONARY INDICES
# dict1 = {'Mohan':95,'Ram':89,'Suhel':92,'Sangeeta':85}
# print(dict1['Ram'])
# # print(dict1['Shyam'])
# dict1['Meena'] = 78
# print(dict1)
# dict1['Suhel'] = 93.5
# print(dict1)



# # BUILT IN FUNCTIONS
# dict1 = {'Mohan':95,'Ram':89,'Suhel':92, 'Sangeeta':85}
# dict2 = {'Sohan':79,'Geeta':89}
# print(len(dict1))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# print(dict1.get('Sangeeta'))
# dict1.update(dict2)
# print(dict1)
# del dict1 ['Ram']
# print(dict1)
# del dict2
# # print(dict2)
# dict1.clear()
# print(dict1)



# #MANIPULATION OF DICTIONARIES
# ODD = {1:'One',3:'Three',5:'Five',7:'Seven',9:'Nine'}
# print(ODD)
# print(ODD.keys())
# print(ODD.values())
# print(ODD.items())
# print(len(ODD))
# print(7 in ODD)
# print(2 in ODD)
# print(ODD.get(9))
# del ODD[9]
# print(ODD)



# #EMPLOYEE SALARY DICTIONARY
# n = int(input("Enter the number of employees: "))
# count = 1
# employee = dict()
# while count <= n:
#     name = input("Enter the name of the employee: ")
#     salary = int(input("Enter the salary of the employee: "))
#     employee[name] = salary
#     count += 1
# print("\nEmployee Name  \t Salary")
# for k in employee:
#     print(k,'\t\t',employee[k])



# #CHARACTER COUNT 
# st = input("Enter a string: ")
# dic = {}
# for ch in st:
#     if ch in dic:
#         dic[ch] += 1
#     else:
#         dic[ch] = 1
# for key in dic:
#     print(key,':',dic[key])



# #NUM TO NUMNAME
# def convert(num):
#     numberNames = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',\
#  5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
#     result = ''
#     for ch in num:
#         key = int(ch)
#         value = numberNames[key]
#         result = result + ' ' + value
#     return result
# num = input("Enter any number: ")
# result = convert(num)
# print("The number is : ",num)
# print("The numberName is: ",result)