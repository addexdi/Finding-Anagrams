# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

# True anagram
def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = "hello"
    anagram = "olleh"
    str1_anagram = sorted(word)
    str2_anagram = sorted(anagram)
    if str1_anagram == str2_anagram:
        return True
    else:
            return False
print(find_anagram("hello", "olleh"))

    
# False anagram
def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = "adam"
    anagram = "maddam"
    str1_anagram = sorted(word)
    str2_anagram = sorted(anagram)
    if str1_anagram == str2_anagram:
        return True
    else:
            return False
print(find_anagram("Adam", "Maddam"))

# User input
def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input("Enter word: ")
    anagram = input("Enter anagram: ")
    str1_anagram = sorted(word)
    str2_anagram = sorted(anagram)
    if str1_anagram == str2_anagram:
        print("This is an anagram")
    else:
        print("This in not an anagram")
print(find_anagram("", ""))
