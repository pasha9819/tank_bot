import math
import game
from random import choice


prev_action = ''
magic_counter = 0
prev_enem_x = 0
prev_enem_y = 0
inb = -1


def is_bullet_can_kill_me(bullet, me):

    x_me = me['pos'][0]
    x_bullet = bullet['pos'][0]
    y_me = me['pos'][1]
    y_bullet = bullet['pos'][1]
    b_dir_x = bullet['dir'][0]
    b_dir_y = bullet['dir'][1]

    temp = (x_bullet - x_me) * b_dir_x + (y_bullet - y_me) * b_dir_y

    temp /= math.sqrt(pow(x_bullet - x_me, 2)+ pow(y_bullet - y_me, 2))
    if distance_to_obj(bullet, me) < 80 and temp > 0.7:
        return True
    if temp < 0.9:
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
    min_distance = 80
    index = -1
    for i in range(len(bullets)):
        temp = distance_to_obj(bullets[i], me)
        if temp < min_distance and is_bullet_can_kill_me(bullets[i], me):
            min_distance = temp
            index = i
    return index


def index_of_nearest_bonus(bonuses, me):
    min_distance = 700
    index = -1
    for i in range(len(bonuses)):
        temp = distance_to_obj(bonuses[i], me)
        if temp < min_distance:
            min_distance = temp
            index = i
    return index


def shot_to_advance(me, enemies, m):
    global prev_enem_x
    global prev_enem_y
    x_en = enemies[0]['pos'][0]
    y_en = enemies[0]['pos'][1]

    en_dir_x = prev_enem_x - x_en
    en_dir_y = prev_enem_y - y_en

    prev_enem_y = y_en
    prev_enem_x = x_en

    dist_to_enem = distance_to_obj(enemies[0], me)

    time = dist_to_enem / game.BULLET_SPEED

    #time /= 10

    next_enem_x = x_en - en_dir_x * time
    next_enem_y = y_en - en_dir_y * time

    # print(next_enem_y, next_enem_x, sep=' ')
    m.shot(next_enem_x, next_enem_y)


def need_to_survive(me, bullets):
    global inb
    inb = check_bullet(bullets, me)
    if inb != -1:
        return True
    return False


def get_perpendicular_line(dir_x, dir_y):
    m_y = 0
    m_x = 0
    magic = choice([-1, 1])
    magic = 1
    if dir_x != 0:
        m_y = magic * 100  # * randint(1,5)
        m_x = (-1 * dir_y * m_y) / dir_x  # * randint(1,5)
    elif dir_y != 0:
        m_x = magic * 100  # * randint(1,5)
        m_y = (-1 * dir_x * m_x) / dir_y  # * randint(1,5)
    return m_x, m_y


def player_in_corner(x, y):
    return x < 50 and y < 50 or x > 750 and y > 550 or x < 50 and y > 550 or x > 750 and y < 50


def player_near_the_border(x, y):
    return x < 30 or y < 30 or x > 770 or y > 570


def move(me, enemies, bullets, bonuses, m):
    try:
        global prev_action
        global magic_counter
        global inb

        shot_to_advance(me, enemies, m)

        x = me['pos'][0]
        y = me['pos'][1]

        if need_to_survive(me, bullets):
            prev_action = 'def'
            m_x, m_y = get_perpendicular_line(bullets[inb]['dir'][0], bullets[inb]['dir'][1])
            m.dir(m_x, m_y)
        elif distance_to_obj(enemies[0], me) < 200:
            if abs(400 - x) < 50 and abs(300 - y) < 50:
                m.dir(x - 400, y - 300)
            else:
                m.dir(400 - x, 300 - y)
        elif player_in_corner(x, y):
            m.dir(400 - x, 300 - y)
        else:
            index = index_of_nearest_bonus(bonuses, me)
            m.dir(bonuses[index]['pos'][0] - x, bonuses[index]['pos'][1] - y)
    except:
        pass

