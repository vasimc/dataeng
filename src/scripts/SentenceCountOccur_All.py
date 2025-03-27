class WordCounter:
    """
    A class to count word occurrences in a sentence using different approaches.
    """

    def __init__(self, sentence):
        self.sentence = sentence
        self.words = sentence.split()

    def count_with_loop(self):
        """
        Counts word occurrences using a for loop and dictionary.
        """
        word_freq = {}
        for word in self.words:
            word_freq[word] = word_freq.get(word, 0) + 1
        return word_freq

    def count_with_set(self):
        """
        Counts word occurrences using a set for unique words and list.count().
        """
        unique_words = set(self.words)
        word_freq = {word: self.words.count(word) for word in unique_words}
        return word_freq

    def count_with_defaultdict(self):
        """
        Counts word occurrences using defaultdict from collections.
        """
        from collections import defaultdict
        word_freq = defaultdict(int)
        for word in self.words:
            word_freq[word] += 1
        return dict(word_freq)

    def count_with_reduce(self):
        """
        Counts word occurrences using reduce from functools.
        """
        from functools import reduce
        word_freq = reduce(lambda acc, word: {**acc, word: acc.get(word, 0) + 1}, self.words, {})
        return word_freq

    def count_with_map_filter(self):
        """
        Counts word occurrences using map and filter.
        """
        word_freq = {word: len(list(filter(lambda x: x == word, self.words))) for word in set(self.words)}
        return word_freq


# Example usage
sentence = "Try new coding on new coding platform"
counter = WordCounter(sentence)

# Uncomment one of the following lines to test a specific approach:
# result = counter.count_with_loop()
# result = counter.count_with_set()
# result = counter.count_with_defaultdict()
result = counter.count_with_reduce()
# result = counter.count_with_map_filter()

# Print the result
print(result)  # Uncomment to see the output