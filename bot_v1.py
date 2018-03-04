import math

from random import choice
from random import randint


def is_bullet_can_kill_me(bullet, me):
    x_me = me['pos'][0]
    x_bullet = bullet['pos'][0]
    y_me = me['pos'][1]
    y_bullet = bullet['pos'][1]
    b_dir_x = bullet['dir'][0]
    b_dir_y = bullet['dir'][1]
    if abs((x_bullet - x_me) * b_dir_x + (y_bullet - y_me) * b_dir_y) < 0.8:
        return False
    return True


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


def go_to_bonus(bonuses, me, m):
    min_distance = 1000
    index = -1
    for i in range(len(bonuses)):
        temp = distance_to_obj(bonuses[i], me)
        if temp < min_distance:
            min_distance = temp
            index = i
    if index != -1 and min_distance < 300:
        m.dir(bonuses[index]['pos'][0] - me['pos'][0], bonuses[index]['pos'][1] - me['pos'][1])


prev_action = ''
magic_counter = 0

def move(me, enemies, bullets, bonuses, m):
    global prev_action
    global magic_counter

    if prev_action == 'def' or prev_action == '':
        go_to_bonus(bonuses, me, m)
        prev_action = 'bonus'
    else:
        # индекс ближайшей пули
        inb = check_bullet(bullets, me)

        if inb != -1:
            prev_action = 'def'
            b_x = bullets[inb]['pos'][0]
            b_y = bullets[inb]['pos'][1]
            m_y = 0
            m_x = 0
            magic = choice([-1, 1])
            if b_x != 0:
                m_y = magic * 100 * randint(1,5)
                m_x = (-1 * b_y * m_y) // b_x * randint(1,5)
            elif b_y != 0:
                m_x = magic * 100 * randint(1,5)
                m_y = (-1 * b_x * m_x) // b_y * randint(1,5)
            m.dir(m_x, m_y)
    m.dir(randint(-10,10), randint(-10,10))
    m.shot(enemies[0]['pos'][0], enemies[0]['pos'][1])