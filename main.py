import pyxel

p = pyxel

player1 = [False,0,0]
player2 = [False,0,0]
player3 = [False,0,0]
player4 = [False,0,0]





pyxel.init(160, 120)

def update():
    global player1
    if pyxel.btnp(pyxel.KEY_P):
        print(player1)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if p.btnp(p.KEY_E):
        player1[0] = True
    if player1:
        if p.btnp(p.KEY_A):
            if not check_walkable(-10,0):
                player1[1] -= 10
        if p.btnp(p.KEY_W):
            if not check_walkable(0,-10):
                player1[2] -= 10
        if p.btnp(p.KEY_S):
            if not check_walkable(0,10):
                player1[2] += 10
        if p.btnp(p.KEY_D):
            if not check_walkable(10,0):
                player1[1] += 10


def draw():
    global player1
    pyxel.cls(0)
    #p.rect(10,10,10,10,13)
    dungeon_gen()
    if player1[0]:
        draw_player(1)


def draw_player(player):
    global player1
    if player == 1:
        p.rect(player1[1],player1[2],10,10,15)
    if player == 2:
        pass
    if player == 3:
        pass
    if player == 4:
        pass

def check_walkable(x,y):
    global player1
    if p.pget(player1[1]+x,player1[2]+y) == 13:
        return True
    else:
        return False

def dungeon_gen():
    for i in range(0,200,10):
        for j in range(0,200,10):
            p.rect(i, j, 10, 10, 13)


    '''
    p.rect(10,10,10,10,13)
    p.rect(20,10,10,10,13)
    p.rect(30,10,10,10,13)
    p.rect(40,10,10,10,13)
    p.rect(40,20,10,10,13)
    p.rect(40,30,10,10,13)
    p.rect(40,40,10,10,13)
    p.rect(30,40,10,10,13)
    p.rect(20,40,10,10,13)
    p.rect(10,40,10,10,13)
    p.rect(10,30,10,10,13)
    p.rect(10,20,10,10,13)
    '''

pyxel.run(update, draw)