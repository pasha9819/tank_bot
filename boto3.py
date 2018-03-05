import game
import math

n = 0


def distance_to_obj(obj, me):
    """возвращает дистанцию до пули"""
    x_me = me['pos'][0]
    x_obj = obj['pos'][0]
    y_me = me['pos'][1]
    y_obj = obj['pos'][1]
    return math.sqrt(math.pow(x_me - x_obj, 2) + math.pow(y_me - y_obj, 2))

prev_enem_x = 0
prev_enem_y = 0


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

    next_enem_x = x_en - en_dir_x * time
    next_enem_y = y_en - en_dir_y * time

    # print(next_enem_y, next_enem_x, sep=' ')
    m.shot(next_enem_x, next_enem_y)

def move(me, enemies, bullets, bonuses, m):
    global n


    n += 1
    if me['pos'][1]<575:
        m.down()
    elif me['pos'][1]==575:
        m.right()
    if me['pos'][0]==775 and not me['pos'][1]==25:
        m.up()
    elif me['pos'][1]==25 and me['pos'][0]!=25:
        m.left()
    enemy=enemies[0]
   #m.shot(enemy['pos'][0], enemy['pos'][1])
    shot_to_advance(me, enemies, m)

