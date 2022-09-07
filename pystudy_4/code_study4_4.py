try:
   a = [273, 103, 52, 57, 100]
   number = int(input("정수를 입력해주세요(0~4 사이의 값을 입력해주세요.)"))
   print(a[number])
except ValueError as exception:
    print("값에 문제가 있습니다.")
except IndexError as exception:
    print("0~4까지 입력해주세요.")
except Exception as exception: # !!
    print("Bug found. Please send this message to us.")


raise Exception("니 코드 틀림ㅋㅋ")