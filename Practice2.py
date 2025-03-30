         # FLOW OF CONTROL #

# #POSITIVE DIFF B/W NUMBERS
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))

# if num1 > num2:
#    diff = num1 - num2
# else:
#    diff = num2 - num1

# print("The difference is ",diff)


# #SIGNAL AT ROAD CROSSING
# signal = input("Enter the color: ")

# if signal == 'red' or signal == 'RED':
#    print("STOP")
# elif signal == 'orange' or signal == 'ORANGE':
#    print("GET READY")
# elif signal == 'green' or signal == 'GREEN':
#    print("GO..!!")    



#  #FOUR FUNCTION CALCULATOR
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# op = input("Enter any one of the operator (+,-,*,/): ")

# if op == '+':
#    print(num1 + num2)
# elif op == '-':
#    if num1 > num2:
#       print (num1 - num2)
#    else:
#       print(num2 - num1)
# elif op == '*':
#    print(num1 * num2)
# elif op == '/':
#    if num2 == 0:
#       print("Error..Division by Zero is not allowed")
#    else:
#       print(num1 / num2)
# else: 
#    print("Wrong input...")



# #FACTORS OF A NUMBER
# num = int(input("Enter a number: "))
# print(1)
# factor = 2
# while factor <= num//2:
#     if num % factor == 0:
#        print(factor)
#     factor += 1
# print(num)



# #BREAK
# num = 0
# for num in range(10):
#     num += 1
#     if num == 7:
#         break
#     print(num)



# #ADDITION TILL NEGATIVE NUMBER
# entry = 0
# sum1 = 0
# print("Enter numbers to find sum...Negative number ends the loop")
# while True:
#   entry = int(input())
#   if (entry < 0):
#       break
#   sum1 += entry

# print(sum1)



# #PRIME NUMBER
# num = int(input("Enter a number: "))
# flag = 0
# if num > 1:
#     for i in range (2,int(num/2)):
#         if (num % i == 0):
#             flag = 1
#             break
#     if flag == 1:
#         print(num,"is not a prime number")
#     else:
#         print(num,"is a prime number")
# else:
#     print("Entered number is <= 1")



# #CONTINUE
# num = 0
# for num in range (5):
#     num += 1
#     if num == 3:
#         continue
#     print(num)




# #NESTED FOR LOOPS
# for var1 in range(3):
#     print('Iterartion ' + str(var1 + 1) + ' of outer loop')
#     for var2 in range(2):
#         print(var2 + 1)
#     print("Out of inner loop")
# print("Out of outer loop")



# #PATTERN PRINTING
# num = int(input("Enter a number to generate its pattern: "))
# for i in range (1,num +1):
#     for j in range (1,i + 1):
#         print(j,end = " ")
#     print()



# #PRIME NUMBERS USING NESTED LOOPS
# for i in range (2,50):
#     j = 2
#     while ( j <= (i/2)):
#         if i % j == 0:
#             break
#         j += 1
#     if (j > i/j):
#         print(i,"is a prime number")



# #FACTORIAL OF A NUMBER
# num = int(input("Enter a number: "))
# fact = 1

# if num == 0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range (1, num + 1):
#         fact *= i
#     print("Factorial of ",num," is ",fact)





          # FUNCTIONS #

# #COST OF TENT
# def cyl(h,r):
#     areaofcyl = 2*3.14*r*h
#     return(areaofcyl)

# def con(l,r):
#     areaofcon = 3.14*r*l
#     return(areaofcon)

# def tax(cost):
#     tax = 0.18 * cost;
#     net_price = cost + tax
#     return(net_price)

# print("Enter values of cylindrical part of tent in meters: ")
# h = float(input("Enter the height: "))
# r = float(input("Enter the radius: "))
# csa_cyl = cyl(h,r)

# l = float(input("Enter slant height of conical area in meters: "))
# csa_con = con(l,r)

# canvas_area = csa_cyl + csa_con
# print("Area of canvas = ",canvas_area,"m^2")

# unit_price = float(input("Enter the cost of 1 m^2 canvas in rupees: "))
# total = unit_price * canvas_area

# print("Total cost of canvas = ",total)



# #ADD TWO NUMBERS
# def addnum():
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     sum = num1 + num2
#     print("Ths sum is ",sum)

# addnum()



# #SUM OF N NUMBERS
# def sumofn(n):
#     sum = 0
#     for i in range(1,n + 1):
#         sum += i
#     print("The sum is : ",sum)
# num = int(input("Enter the number: "))
# sumofn(num)



# #ID OF ARGUMENTS AND PARAMETERS
# def incr(num):
#     print("The ID of ",num," is ",id(num))
#     num = num + 5
#     print("Th ID of ",num," is ",id(num))
# number = int(input("Enter a number: "))
# print("ID of argument is: ",id(number))
# incr(number)



# #MEAN OF VALUES
# def mymean(list1):
#     total = 0
#     count = 0
#     for i in list1:
#         total = total + i
#         count = count + 1
#     mean = total/count
#     print("The mean is: ",mean)
# list1 = [1,3.2,4.5,6.3,5]
# mymean(list1)



# #FACTORIAL OF A NUMBER
# def fact(num):
#     fact = 1
#     for i in range (num,0,-1):
#         fact *= i
#     print("The factorial is: ",fact)
# num = int(input("Enter a number: "))
# fact(num)



# #STRING AS PARAMETERS
# def fullname(first,last):
#     fullname = first + " " + last
#     print(fullname)
# first = input("Enter first name: ")
# last = input("Enter last name: ")
# fullname(first,last)




# #MIXED FRACTIONS
# def mixed(num,deno = 1):
#     remainder = num % deno
#     if remainder != 0:
#         quotient = int(num/deno)
#         print("The mixed fraction: ",quotient,"(",remainder,"/",deno,")")
#     else: 
#         print("The given fraction evaluates to whole number")

# num = int(input("Enter the numerator: "))
# deno = int(input("Enter the denominator: "))
# print("You entered: ",num,"/",deno)
# if num > deno:
#     mixed(num,deno)
# else: 
#     print("It is a proper fraction")



# #AREA PERI OF RECTANGLE
# def calcAreaPeri(length,breadth):
#     area = length* breadth
#     peri = 2 * (length + breadth)
#     return (area,peri)
# l = float(input("Enter the length: "))
# b = float(input("Enter the breadth: "))
# area,peri = calcAreaPeri(l,b)
# print("Area is: ",area,"\nPerimeter is: ",peri)



# #TRAFFIC LIGHT
# def trafficlight():
#     signal = input("Enter the color of traffc light: ")
#     if (signal not in ("RED","ORANGE","GREEN")):
#         print("Please a valid traffic light color in CAPITALS")
#     else:
#         value = light(signal)
#         if (value == 0):
#            print("STOP,Your Life is Precious")
#         elif (value == 1):
#            print("Please Go Slow")
#         else:
#            print("GO! Thank YOu for being patient")

# def light(color):
#     if (color == "RED"):
#        return (0);
#     elif (color == "ORANGE"):
#        return (1);
#     else:
#        return (2);

# trafficlight()
# print("SPEED THRILLS BUT KILLS") 



# #PALINDROME OF A STRING
# s = input("Enter a string: ")

# i,j = 0, len(s) - 1

# isPalindrome = True
# while i < j:
#     if s[i] != s[j]:
#         isPalindrome = False
#         break
#     i += 1
#     j -= 1

# if isPalindrome:
#     print("YES")
# else:
#     print("NO")
        
         
   
# #PALINDROME OF A NUMBER
# def check_palindrome(n):
#     temp = n
#     rev = 0
#     while n > 0:
#         dig = n % 10
#         rev = rev * 10 + dig
#         n = n // 10
#     return temp == rev

# num = int(input("Enter a number: "))
# print("YES" if check_palindrome(num) else "NO")



# #ARMSTRONG NUMBERS
# def is_armstrong(num):
#     order = len(str(num))
#     total = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         total += digit ** order
#         temp //= 10
#     return num == total

# def main():
#     num = int(input("Enter a number: "))
#     if is_armstrong(num):
#         print(f"{num} is an Armstrong number")
#     else:
#         print(f"{num} is not an Armstrong number")

# main()



#FIBONACCI SERIES
# def fibonacci(n):
#     fib_series = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_series.append(a)
#         a, b = b, a + b
#     return fib_series

# def main():
#     n = int(input("Enter a number: "))
#     series = fibonacci(n)
#     print(f"Fibonacci series for {n} numbers: {series}")

# main()