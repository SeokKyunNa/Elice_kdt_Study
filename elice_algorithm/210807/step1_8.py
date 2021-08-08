'''
무어의 법칙[Moore's Law]
'''
N = int(input())

performance = str(2**N)
result = 0

for c in performance:
    result += int(c)

print(result)