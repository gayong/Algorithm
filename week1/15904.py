#UCPC 약자
import sys
input = sys.stdin.readline
words = input()

target = ['U', 'C', 'P', 'C']

# upper = ''
# for char in words:
#     if char.isupper() == True:
#         upper += char

idx = 0
result = ''
#어차피 대문자랑 일치하는지 보는거면 upper 필요없음
for A in words:
  if result == 'UCPC':
    break
  elif A == target[idx]:
    result += A
    idx += 1

if result == 'UCPC':
    print('I love UCPC')
else:
    print('I hate UCPC')
