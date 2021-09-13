'''
범인 찾기
'''
def main():
    N, K = map(int, input().split())
    
    sector = [0 for n in range(100_001)]
    stack = [[N]]
    count = 0

    while sector[K]!=1:
        stack.append([])

        while stack[count]:
            current = stack[count].pop()
            sector[current] = 1

            if current*3==K or current+1==K or current-1==K:
                sector[K]=1
                break

            if current * 3 <= 100_000:
                if sector[current*3] == 0:
                    stack[count+1].append(current * 3)
            if current + 1 <= 100_000:
                if sector[current+1] == 0:
                    stack[count+1].append(current + 1)
            if current - 1 >= 0:
                if sector[current-1] == 0:
                    stack[count+1].append(current - 1)

        count += 1
        
    print(count)

        
if __name__=="__main__":
    main()