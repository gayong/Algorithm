import sys
input = sys.stdin.readline

sentence = list(input().rstrip())
cnt = 0
for i in range(len(sentence)):
    if sentence[i].islower():
        continue
    else:
        match cnt:
            case 0:
                if 'U' == sentence[i]:
                    cnt += 1
            case 1:
                if 'C' == sentence[i]:
                    cnt += 1
            case 2:
                if 'P' == sentence[i]:
                    cnt += 1
            case 3:
                if 'C' == sentence[i]:
                    cnt += 1
if cnt == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
