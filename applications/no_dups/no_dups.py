from collections import Counter


def no_dups(s):
    # Your code here
    s = s.split(" ")
    # joins elements to iterate over
    for i in range(0, len(s)):
        s[i] = "".join(s[i])

    unique = Counter(s)
    s = " ".join(unique.keys())
    return s

    # How do I get rid of returning None?
    # Is that just an effect of Counter?


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
