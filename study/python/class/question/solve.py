class House:

    def __init__(self, location, house_type, deal_type, price, completion_year):
        # 정보를 객체 내부에 저장
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 해당 메서드는 '객체 자신이 이미 가지고 있는 정보를 보여주는 것'
    def show_detail(self):

        # self를 활용하여 객체가 가지고 있는 변수에 접근
        print("{0} {1} {2} {3} 원 {4}년".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
        

houses = []     # 생성된 건물의 수를 저장하는 리스트

# House 클래스를 활용하여 서로 다른 정보를 가진 3가지의 독릭접인 '객체 생성'
gangnam = House('강남', '아파트', '매매', '10억', '2010')
mapo = House('마포', '오피스텔', '전세', '5억', '2007')
songpa = House('송파', '빌라', '월세', '500/50만', '2000')

# Houses 리스트에 차례대로 객체 추가
houses.append(gangnam)
houses.append(mapo)
houses.append(songpa)

# 출력문
print("총 {}가지 매물이 있습니다.".format(len(houses)))
gangnam.show_detail()
mapo.show_detail()
songpa.show_detail()

# 반복문으로도 출력 가능
# for house in houses:
#    house.show_detail()
