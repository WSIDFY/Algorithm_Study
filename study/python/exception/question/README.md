# 실습 문제 : 치킨 주문하기

#### 문제
- 항상 대기 손님이 많은 맛있는 치킨 가게가 있습니다. 손님들의 대기 시간을 줄이고자 자동 주문 프로그램을 만들었습니다.<br>
다음 코드를 확인하고 적절한 예외 처리 구문을 추가하세요.

#### 코드
```python
chicken = 10  # 남은 치킨 수
waiting = 1  # 대기번호, 1부터 시작

while True:
    print("[남은 치킨 : {0}]".format(chicken))
    order = int(input("치킨을 몇 마리 주뭄ㄴ하시겠습니까? "))
    if order > chicken:   # 남은 치킨보다 주문량이 많을 때
        print("재료가 부족합니다.")
    else:
        print("[대기번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
        waiting += 1  # 대기번호 1 증가
        chicken -= order  # 주문 수만큼 남은 치킨 감소
```
