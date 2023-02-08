def countvowles(data):
    cnt = 0

    for i in data:
        if i.upper() in ('A', 'E', 'I', 'O', 'U'):
            cnt += 1
    return cnt