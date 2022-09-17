import re


def is_anagram(word1, word2):
    """
    This function determines anagrams.
    :param word1: Alphabetical words
    :param word2: Alphabetical words
    :return: True or False
    """
    if re.search(r"\d", word1) or re.search(r"\d", word2):
        print("入力できるのはアルファベットのみです！")
        exit()

    # 大文字小文字の分別をなくすために全て小文字にしました。
    word1_unit = sorted(word1.lower())
    word2_unit = sorted(word2.lower())
    print(word2_unit)
    return word1_unit == word2_unit


if __name__ == "__main__":
    print(is_anagram("Listen", "Silent"))