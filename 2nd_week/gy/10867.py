#중복빼고 N개의 정수 오름차순 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
num = set(map(int, input().split()))
num_sorted = sorted(num)

sys.stdout.write(' '.join(map(str, num_sorted)))
