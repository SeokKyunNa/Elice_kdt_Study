'''
베스트 앨범
'''
def solution(genres, plays):
    # 장르별로 더해서 큰 것부터.
    # 장르 내에서 순위를 메기고 높은 순위부터.
    # 장르 장르 내에서 재생횟수가 같다면 고유 번호가 낮은 것부터.

    # 딕셔너리 안에 장르를 key로 갖고 딕셔너리를 value로 받음
    # value dictionary는 점수가 key가 되고, index가 value가 됨
    # 장르 = { 클래식 : { 점수: 인덱스 }, 팝 : { 점수 : 인덱스 } }
    genres_dict = {}
    genres_set = set(genres)
    for i in range(len(genres)):
        if genres[i] in genres_dict:
            if plays[i] in genres_dict[genres[i]]:
                genres_dict[genres[i]][plays[i]].append(i)
            else:
                genres_dict[genres[i]][plays[i]] = [i]
        else:
            genres_dict[genres[i]] = {plays[i]: [i]}

    ranking = []
    for gen in genres_set:
        ranking.append([(sum(genres_dict[gen])), gen])
        
    ranking.sort(reverse=True)

    # 장르 = { 클래식 : { 점수: 인덱스 }, 팝 : { 점수 : 인덱스 } }
    answer = []
    for total, gen in ranking:
        count = 0
        while count < 2:
            answer.append(genres_dict[gen][max(genres_dict[gen])])
            if len(genres_dict[gen][max(genres_dict[gen])]) > 1:
                genres_dict[gen][max(genres_dict[gen])].pop(0)
            else:
                del genres_dict[gen][max(genres_dict[gen])]
            count += 1
    answer = sum(answer, [])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))