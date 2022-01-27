n1,n2=3,7
big=n1 if n1>n2 else n2
while True:
    if big%n1==0 and big%n2==0:
        print("LCM=",big)
        break
    big+=1