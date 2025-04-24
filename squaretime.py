def square(n):
    iter=0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            iter+=1
    print("when n is ",n,"iteration",iter)

square(13)
square(12)
square(7)
square(4)
