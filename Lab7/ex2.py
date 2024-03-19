import pygame

pygame.init()
pygame.mixer.init()

done = False
screen = pygame.display.set_mode((600, 400))

songs = ['s1.mp3', 's2.mp3','s3.mp3'] 
current_index = 0
current_playing_music = songs[current_index]

def play():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(current_playing_music)
        pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next():
    global current_playing_music, current_index, songs
    next_index = (current_index + 1) % len(songs)
    current_playing_music = songs[next_index]
    pygame.mixer.music.load(current_playing_music)
    pygame.mixer.music.play()
    current_index = next_index

def previous():
    global current_playing_music, current_index, songs
    previous_index = (current_index - 1) % len(songs)
    current_playing_music = songs[previous_index]
    pygame.mixer.music.load(current_playing_music)
    pygame.mixer.music.play()
    current_index = previous_index

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop()
            elif event.key == pygame.K_p:
                play()
            elif event.key == pygame.K_LEFT:
                previous()
            elif event.key == pygame.K_RIGHT:
                next()
    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
