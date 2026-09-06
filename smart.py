
print("====welcome to smartcalc====")

while True:#while loop

    print("/n.add/subtract/multiply/division")

    print ("compare a and b")

    print("count from 1 to n")

    print("exit")

choice=input("enter your choice:") # input

#type conversion
if choice in['1','2']:
    a=int(input("enter first numberA"))
    b=int(input("enter second numberB"))

#if else

if choice =='1':

    print("addition:",a+b)

    print("subtraction:",a-b)

    print("multiplication:",a*b)

    print("division:",a/b)

elif choice=='2':

    if a>b:

        print("True")

    elif a< b:

        print("False")

    else:

        print("both equal")

elif choice=='3':

    n=int(input("count till:"))

    for i in range(i,n+i):

        print(i,end=" ")

elif choice=='4':

    print("Good bye")

else:

    print("invalid choice")





       

 



















