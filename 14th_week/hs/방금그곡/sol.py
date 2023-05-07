def solution(m, musicinfos):
    m = m.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')
    answer = (0, '')
    for musicinfo in musicinfos:
        start, end, title, sheet = musicinfo.split(',')
        times = int(end[-2:]) - int(start[-2:])
        if start[:2] != end[:2]:
            times += 60*(int(end[:2])-int(start[:2]))
        sheet = sheet.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')

        sheet = (sheet * (times // len(sheet) + 1))[:times]

        if m in sheet and answer[0] < times:
            answer = (times, title)

    if answer[0] == 0:
        return '(None)'
    else:
        return answer[1]



print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))