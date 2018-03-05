n = 0

def move(me, enemies, bullets, bonuses, m):
    global n

    n += 1

    if me['pos'][0]==25:
        for k in range(100):
            if (n // 110) % 2:
                m.up()
            else:
                m.down()
    if me['pos'][0] == 775:
        for k in range(100):
            if (n // 110) % 2:
                m.down()
            else:
                m.up()
    m.shot(400, 300)
