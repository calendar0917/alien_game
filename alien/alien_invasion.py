import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings,screen,"Play")
    sb = Scoreboard(ai_settings,screen,stats)

    gf.create_fleet(ai_settings,screen,ship,aliens)

    #开始游戏的主循环
    while True:    
        
        #监视键盘和鼠标事件
        gf.check_event(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        if stats.game_active:
            #船的位置更新
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets  )
        
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
        
        
        
run_game()