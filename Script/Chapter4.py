import pygame
from PIL import Image, ImageFilter

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("DP(MJ) Game")

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.flip()
    
pygame.quit()


# image = pygame.image.load('/workspaces/multimedia-python/Gambar/DP.jpg')

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
            
#     screen.blit(image, (100, 100))
#     pygame.display.flip()
# pygame.quit()


# sound = pygame.mixer.Sound('/workspaces/multimedia-python/Video/Deadpool_Intro.mp4')
# sound.play()

# x = 0
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Memperbarui posisi
#     x += 5
#     if x > 800:
#         x = 0

#     # Menggambar gambar di posisi baru
#     screen.fill((0, 0, 0))
#     screen.blit(Image, (x, 100))

#     # Memperbarui tampilan
#     pygame.display.flip()

# pygame.quit()