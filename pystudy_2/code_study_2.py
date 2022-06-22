score = float(input("당신의 점수를 입력해주세요."))

if 9 < score and score <= 10:
    print("S+ Rank")
elif 8 < score:
    print("S Rank")
elif 7 < score:
    print("A Rank")
elif 6 < score:
    print("B Rank")
elif 5 < score:
    print("C Rank")
elif 4 < score:
    print("D Rank")
elif 3 < score:
    print("E Rank")
else:
    print("F Rank")

