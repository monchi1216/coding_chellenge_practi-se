import itertools
import re


def gakkou(word, order):
    """
    The target uppercase alphabetic word and the final output number are given as arguments, and the word corresponding
     to the input output number is output in dictionary form from among the words sorted by that word.
    :param word: Characters to be converted
    :param order: What is the number of the combination
    :return: Characters of the specified number
    """

    if re.search(r'\d', word) or word.islower():
        print("数字、記号を含まない大文字の文字を入力してください。")
        exit()
    elif 1 > order or order > 10**2:
        print("出力番号は 1 <= 単語文字数 <= 10**2 の範囲でお願いします。")
        exit()

    # orderが文字列の組み合わせ数を超えてしまうとエラーになるためこの処理を書きました。
    try:
        word_unit = sorted(set([i for i in itertools.permutations(word)]))
        print(word_unit)
        return "".join(word_unit[order - 1])
    except IndexError:
        print(f"指定した数値({order})は文字列の組み合わせ数({len(word_unit)})より多いです。")
        exit()


if __name__ == "__main__":
    print(gakkou("GAKKOU", 100))