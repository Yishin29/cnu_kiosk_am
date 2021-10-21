#1. 햄버거 세부메뉴 선택하는 함수
def choice_burger():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 버거 메뉴')
    print('□■ 1.모짜버거 5000원')
    print('□■ 2.베이컨버거 4000원')
    print('□■ 3.치즈치킨버거 6000원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num1 = int(input('>> 번호: '))
        if choice_num1 >= 1 and choice_num1 <= 3:
            break
        else:
            print('1-3의 번호만 입력해주세요 :)')
    return choice_num1

#2. 사이드 세부메뉴 선택하는 함수
def choice_side():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 사이드 메뉴')
    print('□■ 1.감자 2000원')
    print('□■ 2.치즈감자 3000원')
    print('□■ 3.치킨너겟 2500원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    while True:
        choice_num2 = int(input('>> 번호: '))
        if choice_num2 >= 1 and choice_num2 <= 3:
            break
        else:
            print('1-3의 번호만 입력해주세요 :)')
    return choice_num2

#3. 음료 세부메뉴 선택하는 함수
def choice_drink():
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 음료 메뉴')
    print('□■ 1.콜라 1000원')
    print('□■ 2.펩시 1000원')
    print('□■ 3.닥터페퍼 1500원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    while True:
        choice_num3 = int(input('>> 번호: '))

        if choice_num3 >= 1 and choice_num3 <= 3:
            break
        else:
            print('1-3의 번호만 입력해주세요 :)')
    return choice_num3