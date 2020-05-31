# pythonで簡単な数字当てゲームを作りました！

import random
# ランダムを導入
answer = random.randint(1,20)
# ランダム範囲を指定
count = 0
# カウントを定義
while True:
# ループを定義
    print("予想は何番？", end="")
    # 改行させないようにする
    guess = int(input())
    # intで入力値を整数値に変換する（計算で使える）
    count += 1
    # カウント方法を定義
    if answer == guess:
    # 条件定義
        print("ファイナルアンサー？。。。。。。正解！")
        break
        # ループ終わらす
    elif answer > guess:
    # 答えが予想より大きい場合
        print("もっとでかいぜ")
    else:
        print("もっと小さいぜ")

    



