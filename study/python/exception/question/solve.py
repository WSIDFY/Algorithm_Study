# 문자를 입력받았을 때, 소수점을 입력받았을 때, 등의 예외처리 구문이 필요
class soldouterr(Exception):
    pass

chicken = 10  # 남은 치킨 수
waiting = 1  # 대기번호, 1부터 시작

while True:
    try:

        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
    
        if order > chicken:   # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")

        elif order == 0:
            print("주문 수량은 최소 1마리입니다!")

        else:
            print("[대기번호 {0}] {1}마리를 주문했습니다.\n".format(waiting, order))
            waiting += 1  # 대기번호 1 증가
            chicken -= order  # 주문 수만큼 남은 치킨 감소

        # 0마리 남았을 때 영업을 마감하는 if문 추가
        if chicken == 0:
            raise soldouterr

    except soldouterr:
        print("재고가 모두 소진되어 영업을 마감합니다. 감사합니다.")
        break

    except Exception as err:
        print("올바른 형식의 주문을 해주세요!\n")



# 아래는 답안입니다.
'''
class soldouterror(Exception): # 재고소진 에러 생성
    pass

chicken = 10
waiting = 1

while True:
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
        if order > chicken:   # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")

        # 주문량이 0이하라면 에러 발생 유도
        elif order <=0:
            raise ValueError

        else:
            print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
            waiting += 1  # 대기번호 1 증가
            chicken -= order  # 주문 수만큼 남은 치킨 감소

        if chicken == 0:
            raise soldouterror
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except soldouterror:
        print("재료가 소진되어 더 이상 주문을 받지 않습니다.")
        break
'''
