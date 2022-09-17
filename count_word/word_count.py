import defnition as de

'テキストの読み取り'
f = open('turtle.txt', 'r')

'単語の数を調べやすいようにリストに変換する'
word_list = de.text_edit(f.read())

'単語の出現回数を出力'
print(de.word_count(word_list))
