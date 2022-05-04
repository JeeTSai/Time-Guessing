def searching():
    v = input("Enter the list of values: ")
    values = v.split()

    for v in values:
        print(v, end=" ")

    num = input("\n\nSelect the number for which you want to know index: ")
    print(values.index(num))


if __name__ == "__main__":
    searching()
