"""
1. Given a sentence, count occurrence of each word. 
Sample - 
Input : Try new coding on new coding platform 
Expected output : { Try : 1, new: 2, coding : 2, on : 1, platform : 1 }
"""

class WordCounter:
    """
    Class for counting word occurrences in a sentence.
    """

    def __init__(self,sentence):
        self.sentence = sentence
        self.words =  sentence.split()

    def count_with_loop(self):
        """
        Counts word occurrences using a for loop and dictionary.
        """
        word_freq = {}
        for word in self.words:
            word_freq[word] = word_freq.get(word, 0) + 1
        return word_freq
    
# Example usage
sentence = "Try new coding on new coding platform coding project with new project"
counter = WordCounter(sentence)
result = counter.count_with_loop()

# Print the result
print(result)