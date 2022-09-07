try:
    num = int(input("정수 입력."))
    print("입력된 값은 {}입니다.".format(num))
except:
    print("예외 발생")
finally:
    print("반드시 실행하십시오.")


def f():
    print("test()함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        asfl.asohf()
        print("try구문의 return 뒤입니다.")
    except:
        print("except구문이 실행되었습니다.")
        return
    finally:
        print("finally 구문이 실행되었습니다.")
        print("test()함수의 마지막 줄입니다.")


f()

while True:
    print("반복문의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try구문의 break 뒤입니다.")
    except:
        print("except구문이 실행되었습니다.")
        break
    finally:
        print("finally 구문이 실행되었습니다.")
        print("반복문의 마지막 줄입니다.")
