import pygame as pg
import sys
from random import randint


def check_bound(obj_rct, scr_rct):
    yoko, tate = 1, 1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
         yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def check_bound2(obj_rct, scr_rct):
    yoko2, tate2 = 1, 1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
         yoko2 = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate2 = -1
    return yoko2, tate2


def main():
    #練習1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    
    # 練習3
    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    # 練習5
    bomb_sfc = pg.Surface((20, 20)) # 空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(0, scrn_rct.width), randint(0, scrn_rct.height)

    bomb2_sfc = pg.Surface((20, 20)) # 空のSurface
    bomb2_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb2_sfc, (0, 0, 255), (10, 10), 10) # 円を描く
    bomb2_rct = bomb2_sfc.get_rect()
    bomb2_rct.centerx, bomb2_rct.centery = randint(0, scrn_rct.width), randint(0, scrn_rct.height)


    # 練習6
    vx, vy = 1, 1
    vx_blue, vy_blue = 1, 1

    clock = pg.time.Clock()
    
    # 練習2
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        

        for  event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_states[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if key_states[pg.K_RSHIFT]:
            fonto = pg.font.Font(None, 80)
            txt = fonto.render("MISTAKE", True, (0, 0, 0))
            scrn_sfc.blit(txt, (300, 200))
        if key_states[pg.K_RCTRL]:
            fonto = pg.font.Font(None, 80)
            txt = fonto.render("MISTAKE", True, (0, 0, 0))
            scrn_sfc.blit(txt, (300, 200))


        
        # 練習7
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1:
            if key_states[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1

        if tate == -1:
            if key_states[pg.K_UP]:
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1
        

        scrn_sfc.blit(tori_sfc, tori_rct) # 練習3
        

        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= 1.001
        vy *= 1.001
        vx *= yoko
        vy *= tate

        yoko2, tate2 = check_bound2(bomb2_rct, scrn_rct)
        vx_blue *= 1.0001
        vy_blue *= 1.0001
        vx_blue *= yoko2
        vy_blue *= tate2


        bomb_rct.move_ip(vx, vy) # 練習6
        bomb2_rct.move_ip(vx2, vy2)
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5
        scrn_sfc.blit(bomb2_sfc, bomb2_rct)

        # fonto = pg.font.Font(None, 80)
        # txt = fonto.render("あ", True, (0, 0, 0))
        # scrn_sfc.blit(txt, (300, 200))
        # 練習8
        if tori_rct.colliderect(bomb_rct):
            return
            # fonto = pg.font.Font(None, 80)
            # txt = fonto.render("あ", True, (0, 0, 0))
            # scrn_sfc.blit(txt, (300, 200))
        if tori_rct.colliderect(bomb2_rct):
            tori_sfc = pg.image.load("fig/7.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
            tori_rct = tori_sfc.get_rect() 

        pg.display.update()

        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()