def palindrome(nn):
    nn = nn.replace(" ", "")
    r = nn[:: -1]

    if nn.lower() == r.lower():
        print("It is Palindrome")
    else:
        print("Not a Palindrome")


n = input("Enter a word to check Palindrome")
palindrome(n)
