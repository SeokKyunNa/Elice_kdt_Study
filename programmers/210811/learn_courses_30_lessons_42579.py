'''
베스트 앨범
'''
'''
    장르별로 더해서 큰 것부터.
    장르 내에서 순위를 메기고 높은 순위부터.
    장르 장르 내에서 재생횟수가 같다면 고유 번호가 낮은 것부터.

    딕셔너리 안에 장르를 key로 갖고 딕셔너리를 value로 받음
    value dictionary는 점수가 key가 되고, index가 value가 됨
    장르 = { 클래식 : { 점수: 인덱스 }, 팝 : { 점수 : 인덱스 } }

    접근 방법을 다시 생각해야 할 듯.. 코드가 매우 지저분해졌다
'''
def solution(genres, plays):
    genres_set = set(genres)    # 중복없이 장르만 받음
    # 장르 = { 장르1 : { 점수: [인덱스] }, 장르2 : { 점수 : [인덱스] } }
    # 위 형태의 dictionary로 만듦
    genres_dict = {}
    for i in range(len(genres)):
        if genres[i] in genres_dict:
            if plays[i] in genres_dict[genres[i]]:
                genres_dict[genres[i]][plays[i]].append(i)
            else:
                genres_dict[genres[i]][plays[i]] = [i]
        else:
            genres_dict[genres[i]] = {plays[i]: [i]}

    # 총 재생횟수 순위를 위한 작업
    ranking = []
    for gen in genres_set:
        ranking.append([(sum(genres_dict[gen])), gen])
    
    ranking.sort(reverse=True)  # 재생횟수가 많은 순으로 정렬

    # 순위 리스트에서 점수(필요없음)와 장르를 꺼내고
    # 각 장르별로 가장 점수가 높으면서, 인덱스가 낮은 순으로 answer에 인덱스를 담아줌
    answer = []
    for total, gen in ranking:
        count = 0
        # 장르당 두 곡 씩만 넣어줌
        while count < 2:
            gen_max = max(genres_dict[gen]) # 해당 장르 안에서 가장 높은 재생 횟수
            answer.append( min(genres_dict[gen][gen_max]))  # 가장 낮은 인덱스를 넣음

            # 가장 높은 재생 횟수가 2개 이상인지(중복이 있는지) 확인
            if len(genres_dict[gen][gen_max]) > 1:  
                genres_dict[gen][gen_max].pop(0)    # 중복이 있다면 낮은 인덱스를 꺼냄(인덱스가 낮은 순으로 입력되었으므로 pop(0))
            else:  
                del genres_dict[gen][gen_max]   # 중복이 없다면 해당 재생횟수를 삭제
                # 삭제 후 해당 장르에 더이상 데이터가 없다면 멈춤(해당 장르의 재생 횟수가 1가지 뿐인 경우)
                if len(genres_dict[gen]) == 0:
                    break
            count += 1

    return answer


# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic", "kpop"], [600, 600, 800, 600, 2500]))




