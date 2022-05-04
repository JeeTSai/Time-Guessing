def prime_factors(nn):
    i = 2
    factors = list()

    while nn != 0:
        if (nn % i) == 0:
            factors.append(i)
            nn = nn / i
        else:
            i = i + 1

    for f in factors:
        print(f)


if __name__ == "__main__":
    n = int(input("Enter the number to find prime factors"))
    prime_factors(n)
