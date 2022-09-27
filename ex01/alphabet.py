import random
zen = 26
taisho = 10
kesson = 2
kaisu = 2

ze = list(range(65, 91))
zenal = [] #A~Z全てのリスト

while True:
    for i in ze:
        allist = chr(i)
        zenal.append(allist)

    taial = random.sample(zenal, 10) #対象アルファベットのリスト
    kessoal = random.sample(taial, 2)
    print("対象文字:")
    for j in taial:
        print(j, end=" ")
    print("\n" + "欠損文字:")
    for k in kessoal:
        print(k, end=" ")
    ketu1 = kessoal[0]
    ketu2 = kessoal[1]
    taial.remove(ketu1)
    taial.remove(ketu2)
    print("\n" + "表示文字:")
    for l in taial:
        print(l, end=" ")
    print()
    ketumon = int(input("欠損文字はいくつあるでしょうか？:"))
    if ketumon == len(kessoal):
        print("正解です。それでは具体的に欠損文字を1つずつ入力してください")
    else:
        print("不正解です。")

    dore = input("一つ目の文字を入力してください:")
    dore2 = input("二つ目の文字を入力してください:")
    if (dore == kessoal[1] or dore == kessoal[0]) and (dore2 == kessoal[1] or dore2 == kessoal[0]):
        print("正解です。")
    else:
        print("不正解です。また来てください。")
        break
    

