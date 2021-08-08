'''
사무실 짓기
'''
def main():
    N = int(input())
    home = list(map(int, input().split()))

    rjfl = 0
    _list = []
    for office in range(1_000_000):
        rjfl = 0
        for h in home:
            rjfl += abs(h-office)
        _list.append(rjfl)
    print(_list[:20])

    min_d = min(_list)
    
    print(_list.count(min_d))

if __name__=="__main__":
    main()