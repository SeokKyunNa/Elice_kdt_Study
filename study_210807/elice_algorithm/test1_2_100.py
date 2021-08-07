'''
금 줍기
'''
def main():
    N = int(input())
    gold = list(map(int, input().split()))
    gold_weight = []
    for i in range(N-2):
        gold_weight.append(gold[i] + gold[i+1] + gold[i+2])

    get_gold = []
    for i in range(len(gold_weight)):
        if i > len(gold_weight)-3: break
        for j in range(i+3, len(gold_weight)):
            get_gold.append(gold_weight[i] + gold_weight[j])
    print(max(get_gold))

if __name__=="__main__":
    main()

