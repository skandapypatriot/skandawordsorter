import random


def main():
    input_file_name = 'data/word_source.txt'
    refined_words = []
    f = open(input_file_name, "r")
    for lines in f.readlines():
        line = lines.strip().lower()
        refined_words.append(line)
    return refined_words


if __name__ == "__main__":
    print(main())
