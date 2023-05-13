def solution(m, musicinfos):
    ans = []
    for info in musicinfos:
        music = info.split(',')
        start = music[0].split(':')
        end = music[1].split(':')

        playtime = (int(end[0]) * 60 + int(end[1])) - (int(start[0]) * 60 + int(start[1]))  # 재생시간 계산

        # 소문자로 바꿔주기
        if 'A#' in music[3] or m:
            music[3] = music[3].replace('A#', 'a')
            m = m.replace('A#', 'a')
        if 'F#' in music[3] or m:
            music[3] = music[3].replace('F#', 'f')
            m = m.replace('F#', 'f')
        if 'C#' in music[3] or m:
            music[3] = music[3].replace('C#', 'c')
            m = m.replace('C#', 'c')
        if 'G#' in music[3] or m:
            music[3] = music[3].replace('G#', 'g')
            m = m.replace('G#', 'g')
        if 'D#' in music[3] or m:
            music[3] = music[3].replace('D#', 'd')
            m = m.replace('D#', 'd')

        len_music = len(music[3])  # 음악의 길이
        # 재생시간동안 재생된 음 (ㅎㅏ...)
        played = music[3] * (playtime // len_music) + music[3][:playtime % len_music]

        if m in played:
            ans.append([playtime, music[2]])  # 재생시간과 제목 추가

    if not ans:
        return "(None)"
    elif len(ans) == 1:
        return ans[0][1]
    else:
        ans = sorted(ans, key=lambda x: (-x[0]))  # 여러개 있다면 재생시간 긴 순으로 정렬
        return ans[0][1]