def sorting():
    inputs = input("Enter words to sort: ")

    words = inputs.split()
    words.sort()

    print("Sorting Done...!!")
    for word in words:
        print(word)


if __name__ == "__main__":
    sorting()
