'''
금 줍기
Case 2. 오답, 95점
'''
def main():
    N = int(input())
    gold = list(map(int, input().split()))
    gold_weight = []
    for i in range(N-2):
        gold_weight.append(gold[i] + gold[i+1] + gold[i+2])

    first = max(gold_weight)
    first_index = gold_weight.index(first)

    if first_index <= 2:
        del gold_weight[:first_index+3]
    elif first_index >= len(gold_weight)-2:
        del gold_weight[first_index-2:]
    else:
        del gold_weight[first_index-2:first_index+3]

    second = max(gold_weight)
    
    print(first + second)

if __name__=="__main__":
    main()

