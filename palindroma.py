def palindroma_e(s):
    s2 = s[::-1]
    if s == s2:
        return True
    else:
        return False


s = input("Adjon meg egy szot: ")
if palindroma_e(s):
    print("Palindroma")
else:
    print("Nem palindroma")
