# Q.no. 1(a) function to find sum of first n odd terms
num = int(input("Print sum of odd numbers till : "))
sum = 0;

for i in range(1, num + 1):

    if(i % 2 != 0):
        sum += i;

print("\nSum of odd numbers from 1 to", num, "is :", sum)

# (b) function to sum of first n even terms
num = int(input("Print sum of odd numbers till : "))
sum = 0;

for i in range(1, num + 1):

    if(i % 2 == 0):
        sum += i;

print("\nSum of odd numbers from 1 to", num, "is :", sum)

#Q.no. 2

t1 = (1,2,5,7,9,2,4,6,8,10)

#(a) Print half the values of tuple in one line and other half in the next line.
a = t1[:5]
b = t1[5:]
print(a)
print(b)

#(b) Print another tuple whose values are even numbers in the given tuple.
n = list(t1)
m = list()

for x in n :
    if x in n:
        if (x%2 == 0) :
            m.append(x)
    s = tuple(m)
print("Tuple =",s) 

#(c) Concatenate a tuple t2 (11,13,15) with t1
t2 = (11,13,15)
a = list(t1)
b = list(t2)
c = a+b
print(c)

#(d) Return  maximun and minimum value from this tuple
print("Max number = ",max(t1) )
print("Min number = ",min(t1))

# Q.no. 3. a menu driven program to perform to perform some functions on strings.
def string():
    choice =int(input('''Enter your choice 
1 = length of the string
2 = maximum of three strrings
3 = Replace every successive character with #
4 = number of words in the string
'''))

    if choice == 1:
        n = input("Enter a string : ")
        l=len(n)
        print("The length of the string is =",l)      
    elif choice == 2:
        n1 = input("Enter 1st string : ")
        n2 = input("Enter 2nd string : ")
        n3 = input("Enter 3rd string : ")
        print("The maximum of the three strings is =",max(n1,n2,n3))    
    elif choice == 3:
        n = input("Enter a string : ")
        s = ""
        m = list(n)
        for i in range(len(n)):
            if (i%2 != 0):
                if m[i] == " ":
                    m[i] = " "
                else:
                    m[i] = "#"
        for x in m:
            s=s+x
        print("The sucessive character in the string is replaced with # :",s) 
    elif choice == 4:
            n = input("Enter a string : ")
            c = 0
            for y in n :
                if y == " " :
                    c += 1
            w = c+1
            print("The number of words = ",w) 
    else :
        print("Please Choose from the given option only")

string()
