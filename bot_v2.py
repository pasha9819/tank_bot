import math

def is_bullet_can_kill_me(bullet, me):
    x_me = me['pos'][0]
    x_bullet = bullet['pos'][0]
    y_me = me['pos'][1]
    y_bullet = bullet['pos'][1]
    b_dir_x = bullet['dir'][0]
    b_dir_y = bullet['dir'][1]

    temp = (x_bullet - x_me) * b_dir_x + (y_bullet - y_me) * b_dir_y

    temp /= math.sqrt(pow(x_bullet - x_me, 2)+ pow(y_bullet - y_me, 2))
    if temp > 0.9:
        return True
    return False


def distance_to_obj(obj, me):
    """возвращает дистанцию до пули"""
    x_me = me['pos'][0]
    x_obj = obj['pos'][0]
    y_me = me['pos'][1]
    y_obj = obj['pos'][1]
    return math.sqrt(math.pow(x_me - x_obj, 2) + math.pow(y_me - y_obj, 2))


def check_bullet(bullets, me):
    """функция возвращает индекс ближайшей пули летящей на нас"""
    min_distance = 1000
    index = -1
    for i in range(len(bullets)):
        temp = distance_to_obj(bullets[i], me)
        if temp < min_distance and is_bullet_can_kill_me(bullets[i], me):
            min_distance = temp
            index = i
    return index

def move(me, enemies, bullets, bonuses, m):
    #m.dir(enemies[0]['pos'][0] - me['pos'][0], enemies[0]['pos'][1] - me['pos'][1])
    m.shot(400, 300)
    m.left()
    m.shot(400, 30)