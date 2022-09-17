import random
from termcolor import colored

print("ジャンケンスタート！！\n")

# 初期化
hand_type = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}
options = tuple(hand_type.keys())
decision_to_win = False         # 勝敗を結果を保持する
if_draw = True                  # 引き分け時に繰り返すかのBool値ほ保持する

while if_draw:
    # CPUとユーザーの手を決める
    cpu_hand = random.choice(options)
    user_hand = input("自分の手を選んでください"
                      "（R:Rock, P:Paper, S:Scissors）> ").upper()

    # ジャンケンの手以外のキーが入力された場合の処理
    while  user_hand not in options:
        user_hand = input("(R, P, S)の中から選んでください！"
                          "（R:Rock, P:Paper, S:Scissors）> ").upper()

    print(f'あなたの手：{user_hand} ({hand_type[user_hand]})')
    print(f'CPUの手  ：{cpu_hand} ({hand_type[cpu_hand]})')

    # 勝敗の判定
    if user_hand == cpu_hand:
       decision_to_win = 'あいこです！'
       if_draw = True
    else:
        if user_hand == 'R' and cpu_hand == 'S':
            decision_to_win = True
            if_draw = False
        elif user_hand == 'P' and cpu_hand == 'R':
            decision_to_win = True
            if_draw = False
        elif user_hand == 'S' and cpu_hand == 'P':
            decision_to_win = True
            if_draw = False
        else:
            decision_to_win = False
            if_draw = False

    if isinstance(decision_to_win, bool):
        decision_to_win = 'あなたの勝ち！' if decision_to_win else 'CPUの勝ち！'

    # 結果発表
    print(f'結果は{colored(decision_to_win,"green")}')

    # 勝負が着くまで繰り返し
    if if_draw:
        print('もう1戦！\n')
        decision_to_win = False
