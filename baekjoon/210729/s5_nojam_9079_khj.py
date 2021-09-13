def reverseCoin(_list, rc, loc):
    if rc == 1: #row
        for i in range(3):
            if _list[loc][i] == "H":
                _list[loc][i] = "T"
            else:
                _list[loc][i] = "H"
    else: #col
        for i in range(3):
            if _list[i][loc] == "H":
                _list[i][loc] = "T"
            else:
                _list[i][loc] = "H"

def allOfCase():
    #모든 경우의 수를 알아 보는 함수
    return
#arr = [[['','',''], ['','',''], ['','','']], 
#      [['','',''], ['','',''], ['','','']],
#      ...]
arr = []
T = int(input())
for i in range(T):
    arr_tmp = [list(map(str, input().split())) for _ in range(3)]
    arr.append(arr_tmp)

for i in range(T):
    _list = arr[i] #첫번째 테스트 케이스