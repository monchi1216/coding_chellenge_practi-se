import string

def word_count(word_list):
    """
        文章内の単語を調べ辞書に単語と回数を代入していく
    :param word_list:
        句読点、改行のない単語のリスト
    :return:
        単語と数の書かれた辞書
    """
    word_dict = {}
    for i in word_list:
        if i in word_dict.keys():
             word_dict[i] += 1
        else:
             word_dict[i] = 1
    # print(word_dict)
    return dict_count(word_dict)


def dict_count(word_dict):
    """
        出現回数の辞書を展開する
    :param word_dict:
        単語と出現回数の記載された辞書を渡す
    """
    for key, value in word_dict.items():
        print(f'{key} {value}')


def text_edit(text):
    """
        単語の出現回数を調べやすいように句読点、スペースのないリストに変換する
    :param text:
        オリジナルのテキスト
    :return:
        単語だけのリスト
    """
    edited_text = ''.join([i.lower() for i in text if i not in
                    string.punctuation])

    return (' '.join(edited_text.split('\n'))).split(' ')
