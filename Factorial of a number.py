def factorial_number():
    n = int(input("enter a number: "))
    f = 1
    if n>=1:
        for i in range(1,n+1):
            f = f * i
        print("Maths raada neeku? ingo factorial:", f)
    else:
        print("ah number ki nuvve chesko factorial")

factorial_number()