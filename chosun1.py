# Q. 서기 연도가 인수로 주어졌을 때, 조선왕조의 계보로 변환하여 출력하는 함수를 작성하세요.
# 주어진 서기연도는 1392년 이상 1450년 이하
# 태조 원년 : 1392
# 정종 원년 : 1398
# 태종 원년 : 1400
# 세종 원년 : 1418
# 문종 원년 : 1450
# 예를 들어 1400년이 인수로 주어지면 '태종 1년'을 출력합니다.

import sys

def chosun(year):
    if year < 1392:
        print('조선시대 이전입니다.')
    elif year < 1398:
        print('태조' + str(year - 1391) + "년")
    elif year < 1400:
        print('정종' + str(year - 1397) + "년")
    elif year < 1418:
        print('태종' + str(year - 1399) + "년")
    elif year < 1450:
        print('세종' + str(year - 1417) + "년")
    elif year < 1452:
        print('문종' + str(year - 1449) + "년")
    else:
        print("범위를 벗어났습니다.")

input_year = input('연도 입력 : ')

if not input_year.isdecimal:
    print('정수를 입력해주세요')
    sys.exit()

change_year = int(input_year)

chosun(change_year)
