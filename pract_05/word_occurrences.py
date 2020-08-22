def main():
    word_count = {}
    text = input("Enter text: ")
    words = text.split()
    for word in words:
        count = word_count.get(word, 0)
        word_count[word] = count + 1

    words = list(word_count.keys())
    words.sort()

    max_length = max((len(word) for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, word_count[word]))


if __name__ == '__main__':
    main()