numbers = [1, 2, 3, 4, 5]

new_numbers = []
for i in numbers:
    new_numbers.append(i*i)



result =[i*i for i in numbers if i%2!=0]

test = (i*i for i in numbers)

while True:
    try:
        print(next(test))
    except StopIteration:
        print("End of iteration")
        break

str1="hello"
str_itr = iter(str1)
#print(next(str_itr))
#print(next(str_itr))


def test_gen(limit):
    count = 0
    while count < limit:
        yield count
        count += 1

res = test_gen(3)
print(next(res))



def fibonacci(n):
    if n ==0 or n ==1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(7))

def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibo()
for i in range(57):
    print(next(fib))