def formula(cnt_rooms: int, cnt_winds: list, lights: dict):
    lights = list(lights.values())
    ans = set()

    for i in range(len(lights)):
        for j in range(len(lights[i])):
            if lights[i][j] == True:
                p = j
                room_num = (3 * i) + 1
                wids_idx = 0
                while p - cnt_winds[wids_idx] >= 0 and wids_idx < len(cnt_winds):
                    p -= cnt_winds[wids_idx]
                    wids_idx += 1
                    room_num += 1
                ans.add(room_num)
    return sorted(list(ans))

