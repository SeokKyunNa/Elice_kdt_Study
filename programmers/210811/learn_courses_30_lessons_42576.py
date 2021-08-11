'''
완주하지 못한 선수
'''
def solution(participant, completion):
    # participant = participant.rstrip().strip('[]').replace('"','').replace(' ','').split(',')
    _dict = {}
    for member in participant:
        if member in _dict:
            _dict[member] += 1
        else:
            _dict[member] = 1
    # print(participant)

    # completion = completion.rstrip().strip('[]').replace('"','').replace(' ','').split(',')
    # print(completion)

    result = ''
    for member in completion:
        if _dict[member] > 0:
            _dict[member] -= 1
        else:
            result = member

    if result == '':
        for member, count in _dict.items():
            if count == 1:
                result = member

    return result

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))