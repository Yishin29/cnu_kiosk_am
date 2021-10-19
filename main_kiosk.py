####################################
## 키오스크 프로그램 메인 조작부
## 개발자: 조의신
## 일자: 2021. 10.12
#################################
## vIEW - console
## CONTROLLER - python
## MODEL(DB) - list, dict



## 조건
## 버거 1개, 사이드 1개, 음료 1개 주문 가능

# 메뉴와 가격표
set_name = {1: '모짜버거세트', 2: '베이컨버거세트', 3: '치즈치킨버거세트'}
burger_name = {1: '모짜버거', 2: '베이컨버거', 3: '치즈치킨버거'}
side_name = {1: '감자', 2: '치즈감자', 3: '치킨너겟'}
drink_name = {1: '콜라', 2: '펩시', 3: '닥터페퍼'}

set_price = {1: 8000, 2: 7000, 3: 8500}
burger_price = {1: 5000, 2: 4000, 3: 6000}
side_price = {1: 2000, 2: 3000, 3: 2500}
drink_price = {1: 1000, 2: 1000, 3: 1500}

#고객 주문 기록 저장
menu_save = {} #고객 주문 메뉴 기록
price_save = {} #고객 주문 금액 기록

#함수

########################
## 1. 메인메뉴 선택
########################

print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ == CNU 버거(ver.01) ==')
print('■■ CNU 버거에 방문해주셔서 감사합니다.')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('□■ 메뉴')
print('□■ 1.햄버거 세트') #버거, 사이드, 음료
print('□■ 2.햄버거 단품')
print('□■ 3.사이드 메뉴')
print('□■ 4.음료')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')

while True:
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    menu_num = int(input('>> 번호:'))  # 사용자부터 주문 MENU 입력

    if menu_num >= 1 and menu_num <= 4: #사용자가 정상적인 값 입력
        break
    else:
        print('1-4의 번호만 입력해주세요 :)') #MSG

#####################
## 2. 세부메뉴 선택
#####################
if menu_num == 1: # 버거 세트
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 버거 메뉴')
    print('□■ 1.모짜버거 5000원')
    print('□■ 2.베이컨버거 4000원')
    print('□■ 3.치즈치킨버거 6000원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num = int(input('>> 번호:'))
        if choice_num >= 1 and choice_num <= 3:
            menu_save['burger'] = burger_name[choice_num]  # 사용자가 선택한 버거메뉴 기록
            price_save['burger'] = burger_price[choice_num]  # 사용자가 선택한 버거메뉴의 가격 기록
            break
        else:
            print('1-3의 번호만 입력해주세요 :)')

    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 사이드 메뉴')
    print('□■ 1.감자 2000원')
    print('□■ 2.치즈감자 3000원')
    print('□■ 3.치킨너겟 2500원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    while True:
        choice_num = int(input('>> 번호:'))
        if choice_num >= 1 and choice_num <= 3:
            menu_save['side'] = side_name[choice_num]
            price_save['side'] = side_price[choice_num]
            break
        else:
            print('1-3의 번호만 입력해주세요 :)')

    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 음료 메뉴')
    print('□■ 1.콜라 1000원')
    print('□■ 2.펩시 1000원')
    print('□■ 3.닥터페퍼 1500원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    while True:
        choice_num = int(input('>> 번호:'))

        if choice_num >= 1 and choice_num <= 3:
            menu_save['drink'] = drink_name[choice_num]
            price_save['drink'] = drink_price[choice_num]
            break
        else:
            print('1-3의 번호만 입력해주세요 :)')

elif menu_num == 2: # 버거 단품
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 버거 메뉴')
    print('□■ 1.모짜버거 5000원')
    print('□■ 2.베이컨버거 4000원')
    print('□■ 3.치즈치킨버거 6000원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')

    while True:
        choice_num = int(input('>> 번호:'))
        if choice_num >= 1 and choice_num <= 3:
            menu_save['burger'] = burger_name[choice_num] # 사용자가 선택한 버거메뉴 기록
            price_save['burger'] = burger_price[choice_num] # 사용자가 선택한 버거메뉴의 가격 기록
            break
        else:
            print('1-3의 번호만 입력해주세요 :)')  # MSG

elif menu_num == 3: # 사이드
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 사이드 메뉴')
    print('□■ 1.감자 2000원')
    print('□■ 2.치즈감자 3000원')
    print('□■ 3.치킨너겟 2500원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    while True:
        choice_num = int(input('>> 번호:'))
        if choice_num >= 1 and choice_num <= 3:
            menu_save['side'] = side_name[choice_num]
            price_save['side'] = side_price[choice_num]
            break
        else:
            print('1-3의 번호만 입력해주세요 :)')

elif menu_num == 4: #음료
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('□■ 음료 메뉴')
    print('□■ 1.콜라 1000원')
    print('□■ 2.펩시 1000원')
    print('□■ 3.닥터페퍼 1500원')
    print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    print('■■ 원하시는 메뉴의 번호를 입력해주세요.')
    while True:
        choice_num = int(input('>> 번호:'))

        if choice_num >= 1 and choice_num <= 3:
            menu_save['drink'] = drink_name[choice_num]
            price_save['drink'] = drink_price[choice_num]
            break
        else:
            print('1-3의 번호만 입력해주세요 :)')

print(menu_save)
print(price_save)

###########################
## 3. 주문 메뉴와 금액 정산 및 출력
###########################

#Total 주문 금액 계산

total_price = 0 # Total 주문금액

# price_save ==> {'burger': 3000}
for price in price_save.values():
    total_price += price

print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ 고객님이 주문하신 메뉴는')
for i, menu in enumerate(menu_save.values()):
    print('□■ {}. {}'.format(i+1, menu))
print('■■ (으)로 총 주문금액은 {}원 입니다.'.format(total_price))
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
print('■■ 이용해주셔서 감사합니다. 또 오세요 ;)')
print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
