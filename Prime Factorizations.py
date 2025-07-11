# Prime Factorization in Python

n = int(input("Enter a number: "))
print("Prime factors of", n, "are:", end=" ")

i = 2
while i <= n:
    while n % i == 0:
        print(i, end=" ")
        n = n // i
    i += 1
