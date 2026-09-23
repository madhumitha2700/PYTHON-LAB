def check(x):
    if (x % 2 == 0 or x % 4 == 0):
        return 1
#call check() for every value between 2 to 21
evens = list(filter(check, range(2, 22)))
print(evens)