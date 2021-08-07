'''
울타리
'''
def main():
    N, M, K = map(int, input().split())
    x_list = []
    y_list = []
    for _ in range(K):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)

    min_x = min(x_list)
    max_x = max(x_list)
    min_y = min(y_list)
    max_y = max(y_list)

    length_M = ((max_x+1) - (min_x-1)) * 2 
    length_N = ((max_y+1) - (min_y-1)) * 2 
    
    print(length_M + length_N)

if __name__=="__main__":
    main()