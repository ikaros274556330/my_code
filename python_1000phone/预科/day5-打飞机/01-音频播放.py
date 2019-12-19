"""__author:吴佩隆__"""
import pygame

pygame.init()
window = pygame.display.set_mode((400,600))
window.fill((255,255,255))
pygame.display.set_caption('音频播放')

# ======音频播放=======
# 方法一：mixer_music/mixer.music播放器-只有一个播放器，同一时间播放一个音频
# 1.加载音频文件
pygame.mixer_music.load('./plane/sound/game_music.mp3')
# 2.播放音频
# pygame.mixer_music.play(循环次数)-1，无限，-0/1，播放一次,大于1，指定次数
pygame.mixer_music.play(-1)
# 3.停止播放
# pygame.mixer_music.stop()

# 方法二:通过Sound创建播放器对象播放指定音频（播放音效:wav）
# 1.加载音频文件 - 返回一个播放器对象
sound1 = pygame.mixer.Sound('./plane/sound/achievement.wav')
sound2 = pygame.mixer.Sound('./plane/sound/get_bomb.wav')
# 2.播放音频
# sound1.play(-1)
# sound2.play(-1)
# 3.停止播放
# sound1.stop()
# sound2.stop()

pygame.display.flip()
flag = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            # 按空格暂停和播放背景音乐
            if event.key == pygame.K_SPACE:
                if flag:
                    pygame.mixer_music.stop()
                    flag = False
                else:
                    pygame.mixer_music.play()
                    flag = True





