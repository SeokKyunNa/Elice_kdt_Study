import sys
import heapq
sys.setrecursionlimit(100000)

def getMST(graph) :
    V = len(graph)
    visited = [False] * V
    mst = []
    heap = [(0, 1)]
    total_weight = 0

    while heap:
        s, weight = heapq.heappop(heap) # 가중치가 가장 적은 간선 추출
        if not visited[s]:
            visited[s] = True
            mst.append((s))
            total_weight += weight
            
            for edge in graph[s]:
                heapq.heappush(heap, edge)

    return total_weight
    
    # [
    #     0 [(1, 3), (5, 1)], 
    #     1 [(0, 3), (2, 4), (3, 1), (5, 1)], 
    #     2 [(1, 4), (4, 6), (6, 9), (7, 4)], 
    #     3 [(1, 1), (4, 2)], 
    #     4 [(2, 6), (3, 2), (6, 9)], 
    #     5 [(0, 1), (1, 1)], 
    #     6 [(2, 9), (4, 9), (7, 3)], 
    #     7 [(2, 4), (6, 3)]
    # ]

def main():
    '''
    Do not change this code
    '''

    line = [int(x) for x in input().split()]

    n = line[0]
    m = line[1]

    graph = [ [] for i in range(n) ]

    for i in range(m) :
        line = [int(x) for x in input().split()]

        graph[line[0]].append((line[1], line[2]))
        graph[line[1]].append((line[0], line[2]))

    print(getMST(graph))

if __name__ == "__main__":
    main()