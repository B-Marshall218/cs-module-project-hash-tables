def word_count(s):
    # Your code here
    # Conver string into lowercase
    s = s.lower()
    # Break string when see space
    s = s.split(" ")
    # initialize dict to store frequency of words
    word_frequency = {}
    for i in s:
        # If word is already in the keys, increment frequency
        if i in word_frequency:
            word_frequency[i] += 1
        # If the word doesnt yet exist
        else:
            word_frequency[i] = 1
    return(word_frequency)


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
