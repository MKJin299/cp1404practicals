"""
Word Occurrences
Estimate: 25 minutes
Actual: 20 minutes
"""

def main():
    print("Word Occurrences")
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    print_word_occurrences(word_counts)

def count_word_occurrences(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def print_word_occurrences(word_counts):
    max_word_length = max(len(word) for word in word_counts)
    sorted_words = sorted(word_counts.keys())
    for word in sorted_words:
        print(f"{word:{max_word_length}} : {word_counts[word]}")

if __name__ == "__main__":
    main()