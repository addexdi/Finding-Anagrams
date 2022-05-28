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
    word = "Adam"
    anagram = "Maddam"
    str1_anagram = sorted(word)
    str2_anagram = sorted(anagram)
    if str1_anagram == str2_anagram:
        return True
    else:
            return False
print(find_anagram("Adam", "Maddam"))

