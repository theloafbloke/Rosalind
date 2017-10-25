n,m = raw_input("n: "), raw_input("m: ")
n,m = int(n),int(m)
generations = [1,1]

def fib(i,j):
    count = 2
    while (count < i):
        if (count < j):
            generations.append(generations[-2] + generations[-1])
        elif (count == j or count == j+1):
            print("in base cases for newborns (1st gen + 2nd gen deaths)")
            generations.append((generations[-2] + generations[-1] -1))
        else:
            generations.append(generations[-2] + generations[-1] - generations[-(j+1)])
        count += 1
    return generations[-1]
print fib(n,m)
