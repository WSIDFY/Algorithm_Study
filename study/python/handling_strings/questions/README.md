# 실습문제: 비밀번호 만들기

#### 문제
- 사이트별로 비밀번호를 생성하는 프로그램을 작성하세요.<br>
`http://naver.com`<br>
`http://daum.net`<br>
`http://google.com`<br>
`http://youtube.com`<br>

#### 조건
1. http:// 부분은 제외한다.(ex. naver.com)
2. 처음 만나는 점(.)이후 부분도 제외한다.(ex. naver)
3. 남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e'의 개수 + '!'로 구성한다.(ex. nav + 5 + 1 + ! = nav51!)

#### 실행 결과
```python
http://naver.com의 비밀번호는 nav51!입니다.
```
답안은 'solve_1'파일에서 확인하실 수 있습니다.

---
# 셀프체크

#### 문제
- 영어 문장이 주어졌을 때 첫 번째 글자는 대문자로, 나머지 글자는 모두 소문자로 변환하는 프로그램을 작성하세요.

#### 실행결과
```python
# 주어진 문장 : the early bird catches the worm.
The early bird catches the worm.
```
답안은 'solve_2'파일에서 확인하실 수 있습니다.
