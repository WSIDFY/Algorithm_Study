# 풀이 진행 중
keyword_list = []

for i in range(0,100):
    keyword = input()

    if (keyword[0] or keyword[-1]) == ' ':
        break
    else:
        keyword_list.append(keyword)
        continue

for j in range(len(keyword_list)):
    print(keyword_list[j],end='\n')
