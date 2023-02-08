import sys
input = sys.stdin.readline

N = int(input().rstrip())
people = []
for i in range(N):
    people.append(input().split())
    people[i][0] = int(people[i][0])

people.sort(key=lambda x : x[0])

for i in range(N) :
    print(f'{people[i][0]} {people[i][1]}')