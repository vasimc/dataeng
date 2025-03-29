"""
1. Given a sentence, count occurrence of each word. 
Sample - 
Input : Try new coding on new coding platform 
Expected output : { Try : 1, new: 2, coding : 2, on : 1, platform : 1 }
"""
# Using Counter from collections

from collections import Counter

def word_count(sentence):
    words = sentence.split() 
    return dict(Counter(words))

sentence = "Try new coding on new coding platform"
result = word_count(sentence)
print(result) # {'Try': 1, 'new': 2, 'coding': 2, 'on': 1, 'platform': 1}