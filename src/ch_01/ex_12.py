# determining the most frequently occurring items in a sequence
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)

more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes', 'the']
# for word in more_words:
    # word_counts[word] += 1

word_counts.update(more_words)

a = Counter(words)
b = Counter(more_words)
c = a + b
d = a - b

if __name__ == '__main__':
    print(top_three)
    print(word_counts['eyes'])
    print(word_counts['the'])
    print(word_counts['look'])
    print(a)
    print(b)
    print(c)
    print(d)
