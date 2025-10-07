'''
입력받는 수에 따라 정렬될 공간을 조절해줘야 하기 때문에
정렬될 공간을 N으로 설정 > 사용자의 입력에 따라 공간 할당
'''
N = int(input())

for i in range(1, N+1):
    print(str('*'*i).rjust(N))

# ex) 5칸 자리수 & 우측 정렬 -> .rjust(5)
# ex) 8칸 자리수 & 좌측 정렬 -> .ljust(8)
