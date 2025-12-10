import turtle

x = turtle.Turtle()
x.color('white')
x.shape('circle')
x.pencolor('black')
x.speed(0)

def dx():
    x.left(45)
    x.pendown()
    x.forward(60)
    x.right(180)
    x.forward(60)
    x.left(90)
    x.forward(60)
    x.right(180)
    x.forward(60)
    x.left(90)
    x.forward(60)
    x.right(180)
    x.forward(60)
    x.left(90)
    x.forward(60)
    x.right(180)
    x.forward(60)
    x.right(45)
    x.penup()

def do():
    x.penup()
    x.forward(60)
    x.right(90)
    x.pendown()
    x.forward(60)
    x.right(90)
    x.forward(120)
    x.right(90)
    x.forward(120)
    x.right(90)
    x.forward(120)
    x.right(90)
    x.forward(60)
    x.right(90)
    x.penup()
    x.forward(60)

def mbox():
    x.pensize(3)
    x.right(90)
    x.penup()
    x.forward(75)
    x.right(90)
    x.forward(225)
    x.right(180)
    x.pendown()
    x.forward(450)
    x.penup()
    x.left(90)
    x.forward(150)
    x.left(90)
    x.forward(450)
    x.right(180)
    x.pendown()
    x.forward(450)
    x.back(300)
    x.left(90)
    x.penup()
    x.forward(150)
    x.right(180)
    x.pendown()
    x.forward(450)
    x.left(90)
    x.penup()
    x.forward(150)
    x.left(90)
    x.pendown()
    x.forward(450)
    x.back(225)
    x.left(90)
    x.penup()
    x.forward(75)
    x.right(90)
    x.pendown()

def tlx():
    x.left(90)
    x.penup()
    x.forward(150)
    x.right(90)
    x.forward(150)
    dx()
    x.penup()
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.right(180)

def tlo():
    x.left(90)
    x.penup()
    x.forward(150)
    x.right(90)
    x.forward(150)
    do()
    x.left(90)
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.right(180)

def tmx():
    x.penup()
    x.forward(150)
    dx()
    x.penup()
    x.right(90)
    x.forward(150)
    x.right(180)
    x.pendown()

def tmo():
    x.penup()
    x.forward(150)
    do()
    x.forward(150)
    x.left(180)

def trx():
    x.penup()
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.left(90)
    dx()
    x.right(90)
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.right(90)

def tro():
    x.penup()
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.left(90)
    do()
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.right(90)

def mlx():
    x.left(90)
    x.penup()
    x.forward(150)
    x.right(90)
    dx()
    x.penup()
    x.forward(150)
    x.left(90)
    x.pendown()

def mlo():
    x.left(90)
    x.penup()
    x.forward(150)
    x.right(90)
    do()
    x.left(90)
    x.forward(150)
    x.left(90)
    x.pendown()

def mmx():
    dx()
    x.left(90)
    x.pendown()

def mmo():
    do()
    x.right(180)
    x.pendown()

def mrx():
    x.penup()
    x.right(90)
    x.forward(150)
    x.left(90)
    dx()
    x.left(180)
    x.forward(150)
    x.right(90)

def mro():
    x.penup()
    x.right(90)
    x.forward(150)
    x.left(90)
    do()
    x.right(90)
    x.forward(150)
    x.right(90)

def blx():
    x.penup()
    x.right(180)
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.right(90)
    dx()
    x.forward(150)
    x.left(90)
    x.forward(150)

def blo():
    x.penup()
    x.right(180)
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.right(90)
    do()
    x.left(90)
    x.forward(150)
    x.left(90)
    x.forward(150)

def bmx():
    x.penup()
    x.right(180)
    x.forward(150)
    x.right(180)
    dx()
    x.left(90)
    x.forward(150)

def bmo():
    x.penup()
    x.right(180)
    x.forward(150)
    x.right(180)
    do()
    x.left(180)
    x.forward(150)

def brx():
    x.penup()
    x.right(90)
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.right(180)
    dx()
    x.left(90)
    x.forward(150)
    x.left(90)
    x.forward(150)
    x.right(90)

def bro():
    x.penup()
    x.right(90)
    x.forward(150)
    x.right(90)
    x.forward(150)
    x.right(180)
    do()
    x.left(180)
    x.forward(150)
    x.left(90)
    x.forward(150)
    x.right(90)

mbox()
quit = ''
player_role = 'P1'
tlc = ''
tmc = ''
trc = ''
mlc = ''
mmc = ''
mrc = ''
blc = ''
bmc = ''
brc = ''


while quit.upper() != 'YES':
    print('Type tl for top left, tm for top middle and tr for top right and so on. second row is called middle(ml, mm, mr) and 3rd row is called bottom(bl, bm, br). Type quit to quit')
    pinput = input(f"Its {player_role}'s chance. Choose something: ")
    pinput = pinput.upper()

    if pinput == 'TL' and player_role == 'P1' and tlc == '':
        tlx()
        player_role = 'P2'
        tlc = 'x'
    elif pinput == 'TL' and player_role == 'P2' and tlc == '':
        tlo()
        player_role = 'P1'
        tlc = 'o'
    elif pinput == 'TM' and player_role == 'P1' and tmc == '':
        tmx()
        tmc = 'x'
        player_role = 'P2'
    elif pinput == 'TM' and player_role == 'P2' and tmc == '':
        tmo()
        tmc = 'o'
        player_role = 'P1'
    elif pinput == 'TR' and player_role == 'P1' and trc == '':
        trx()
        trc = 'x'
        player_role = 'P2'
    elif pinput == 'TR' and player_role == 'P2' and trc == '':
        tro()
        trc = 'o'
        player_role = 'P1'
    elif pinput == 'ML' and player_role == 'P1' and mlc == '':
        mlx()
        mlc = 'x'
        player_role = 'P2'
    elif pinput == 'ML' and player_role == 'P2' and mlc == '':
        mlo()
        mlc = 'o'
        player_role = 'P1'
    elif pinput == 'MM' and player_role == 'P1' and mmc == '':
        mmx()
        mmc = 'x'
        player_role = 'P2'
    elif pinput == 'MM' and player_role == 'P2' and mmc == '':
        mmo()
        mmc = 'o'
        player_role = 'P1'
    elif pinput == 'MR' and player_role == 'P1' and mrc == '':
        mrx()
        mrc = 'x'
        player_role = 'P2'
    elif pinput == 'MR' and player_role == 'P2' and mrc == '':
        mro()
        mrc = 'x'
        player_role = 'P1'
    elif pinput == 'BL' and player_role == 'P1' and blc == '':
        blx()
        blc = 'x'
        player_role = 'P2'
    elif pinput == 'BL' and player_role == 'P2' and blc == '':
        blo()
        blc = 'o'
        player_role = 'P1'
    elif pinput == 'BM' and player_role == 'P1' and bmc == '':
        bmx()
        bmc = 'x'
        player_role = 'P2'
    elif pinput == 'BM' and player_role == 'P2' and bmc == '':
        bmo()
        bmc = 'o'
        player_role = 'P1'
    elif pinput == 'BR' and player_role == 'P1' and brc == '':
        brx()
        brc = 'x'
        player_role = 'P2'
    elif pinput == 'BR' and player_role == 'P2' and brc == '':
        bro()
        brc = 'o'
        player_role = 'P1'
    elif pinput == 'QUIT':
        break
    else:
        print('Please rectify what you have entered, the box you chose could be occupied already or you may have entered an unrecognised word.')

    if tlc == 'x' and tmc == 'x' and trc == 'x':
        print('PLayer 1, that is, X has won the game')
        break
    elif tlc == 'x' and mmc == 'x' and brc == 'x':
        print('PLayer 1, that is, X has won the game')
        break
    elif tlc == 'x' and mlc == 'x' and blc == 'x':
        print('PLayer 1, that is, X has won the game')
        break
    elif trc == 'x' and mmc == 'x' and blc == 'x':
        print('PLayer 1, that is, X has won the game')
        break
    elif trc == 'x' and mrc == 'x' and brc == 'x':
        print('PLayer 1, that is, X has won the game')
        break
    elif blc == 'x' and bmc == 'x' and brc == 'x':
        print('PLayer 1, that is, X has won the game')
        break
    elif tlc == 'o' and tmc == 'o' and trc == 'o':
        print('PLayer 2, that is, O has won the game')
        break
    elif tlc == 'o' and mmc == 'o' and brc == 'o':
        print('PLayer 2, that is, O has won the game')
        break
    elif tlc == 'o' and mlc == 'o' and blc == 'o':
        print('PLayer 2, that is, O has won the game')
        break
    elif trc == 'o' and mmc == 'o' and blc == 'o':
        print('PLayer 2, that is, O has won the game')
        break
    elif trc == 'o' and mrc == 'o' and brc == 'o':
        print('PLayer 2, that is, O has won the game')
        break
    elif blc == 'o' and bmc == 'o' and brc == 'o':
        print('PLayer 2, that is, O has won the game')
        break
    elif tlc != '' and tmc != '' and trc != '' and mlc != '' and mmc != '' and mrc != '' and blc != '' and bmc != '' and brc != '':
        print("It's a draw, try again!")
        break
    else:
        continue


turtle.mainloop()