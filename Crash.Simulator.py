import random, time
reco=""
times = int(input("How many times you want to play? "))
for i in range(times):
    x = random.uniform(0.01, 0.01)
    y = 1;
    z = random.uniform(0, 100000) / random.uniform(10, 10100)
    print('{0:.2f}'.format(z))
    user = float(input("Enter your value: "))
    while y < z:
        y += x
        p = lambda: float(y);
        [print('{0:.2f}'.format(p(), t=time.sleep(.1)), end='\r')]
    if user <= z:
        print("You win!")
        reco=reco+str(user)+" WIN "
    elif user > z:
        print("You lost!")
        reco=reco+str(user)+" LOSE "
        if y < 2:
            x = random.uniform(0.01, 0.01)
        elif 2 >= y < 3:
            x = random.uniform(0.07, 0.10)
        elif 3 >= y < 6:
            x = random.uniform(0.10, 0.16)
        elif 6 >= y < 10:
            x = random.uniform(0.20, 0.35)
        elif 10 >= y < 50:
            x = random.uniform(0.40, 0.70)
        elif 50 >= y < 200:
            x = random.uniform(0.75, 6)
        else:
            x = random.uniform(8, 18)
    if (y >= z) and (y <= 1):
        p = lambda: float(z);
        [print('{0:.0f}'.format(p(), t=time.sleep(.1)), end='\n')]
        print("Crash!")
    elif y > z:
        p = lambda: float(z);
        [print('{0:.2f}'.format(p(), t=time.sleep(.1)), end='\n')]
        print("Crash!")
print("Your plays of today are: "+reco)