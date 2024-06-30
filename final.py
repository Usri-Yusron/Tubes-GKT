import pygame
import sys
import random
import math  # Tambahkan baris ini untuk mengimpor modul math

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 800
screen_height = 600

# Warna
white = (255, 255, 255)
blue = (135, 206, 250)
green = (34, 139, 34)

# Inisialisasi layar
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lanskap Animasi")

# Fungsi untuk menggambar gunung
def draw_mountains():
    pygame.draw.polygon(screen, (0, 128, 0), [(0, 400), (150, 200), (300, 400)])
    pygame.draw.polygon(screen, (0, 128, 0), [(300, 400), (450, 200), (600, 400)])
    pygame.draw.rect(screen, (34, 139, 34), (0, 400, screen_width, screen_height - 400))



# Fungsi untuk menggambar awan
def draw_cloud(x, y):
    pygame.draw.circle(screen, white, (x, y), 20)
    pygame.draw.circle(screen, white, (x + 30, y), 30)
    pygame.draw.circle(screen, white, (x + 60, y), 20)

# Fungsi untuk menggambar matahari
def draw_sun(x, y, angle):
    # Buat salinan gambar matahari
    sun_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
    
    # Gambar lingkaran matahari
    pygame.draw.circle(sun_surface, (255, 255, 0), (50, 50), 50)

    # Gambar garis-garis di sekitar lingkaran matahari
    line_color = (255, 255, 0)
    line_length = 400  # Panjang garis-garis
    for i in range(0, 360, 10):
        start_pos = (50 + int(45 * math.cos(math.radians(i))), 50 + int(45 * math.sin(math.radians(i))))
        end_pos = (50 + int((45 + line_length) * math.cos(math.radians(i))), 50 + int((45 + line_length) * math.sin(math.radians(i))))
        pygame.draw.line(sun_surface, line_color, start_pos, end_pos, 2)

    # Rotasi gambar matahari
    rotated_sun = pygame.transform.rotate(sun_surface, angle)

    # Ambil rect dari gambar yang telah dirotasi
    sun_rect = rotated_sun.get_rect(center=(x, y))

    # Gambar matahari yang telah dirotasi
    screen.blit(rotated_sun, sun_rect)


# Fungsi untuk menggambar jalan dengan marka putus-putus
def draw_dashed_road():
    road_color = (47, 79, 79)
    line_color = (255, 255, 255)

    # Gambar jalan
    pygame.draw.rect(screen, road_color, (0, 500, screen_width, screen_height - 500))

    # Gambar marka putus-putus
    line_width = 10
    gap = 20  # Jarak antar marka putus-putus

    for i in range(0, screen_width, gap * 2):
        pygame.draw.rect(screen, line_color, (i, 550, gap, line_width))

# Fungsi untuk menggambar rumah
def draw_house(x, y):
    pygame.draw.rect(screen, (139, 69, 19), (x, y, 80, 80))
    pygame.draw.polygon(screen, (255, 0, 0), [(x, y), (x + 40, y - 40), (x + 80, y)])


# Fungsi untuk menggambar mobil
def draw_car(x, y, color):
    pygame.draw.rect(screen, color, (x, y, 80, 40))
    pygame.draw.rect(screen, (0, 0, 0), (x + 10, y - 20, 60, 30))
    pygame.draw.circle(screen, (0, 0, 0), (x + 20, y + 40), 15)
    pygame.draw.circle(screen, (0, 0, 0), (x + 60, y + 40), 15)

# Fungsi untuk menggambar pohon apel
def draw_apple_tree(x, y):
    # Batang pohon
    pygame.draw.rect(screen, (139, 69, 19), (x + 1, y + 20, 13, 60))

    # Daun berbentuk ikal
    pygame.draw.circle(screen, (0, 128, 0), (x, y), 30)
    pygame.draw.circle(screen, (0, 128, 0), (x + 20, y - 10), 30)
    pygame.draw.circle(screen, (0, 128, 0), (x - 20, y - 10), 30)
    pygame.draw.circle(screen, (0, 128, 0), (x + 10, y - 30), 30)
    pygame.draw.circle(screen, (0, 128, 0), (x - 10, y - 30), 30)

    # Buah apel
    pygame.draw.circle(screen, (255, 0, 0), (x + 20, y - 40), 10)
    pygame.draw.circle(screen, (255, 0, 0), (x - 15, y - 45), 10)
    pygame.draw.circle(screen, (255, 0, 0), (x + 10, y - 60), 10)


# Main loop
clock = pygame.time.Clock()

clouds = [(random.randint(0, screen_width), random.randint(50, 150)) for _ in range(5)]
car_x = 800
car2_x = 0  # Posisi awal mobil kedua
sun_angle = 0  # Sudut rotasi matahari

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill(blue)

    # Gambar elemen-elemen lanskap
    draw_mountains()
    draw_sun(700, 100, sun_angle)
    draw_dashed_road()
    draw_house(600, 350)
    draw_car(car_x, 490, (255, 0, 0))
    draw_car(car2_x, 550, (0, 0, 255)) # Gambar mobil kedua
    draw_apple_tree(730, 330)
    draw_apple_tree(330, 530)
    draw_apple_tree(730, 530)
    draw_apple_tree(130, 420)
    draw_apple_tree(530, 420)
    
        # Update rotasi matahari
    sun_angle += 1
    if sun_angle > 360:
        sun_angle = 0
        
        # Update posisi mobil 1 warna merah
    car_x -= 2
        
        # Update posisi mobil 2            
    car2_x += 2


    # perulangan untuk Gambar awan supaya bisa bergerak 
    for i, cloud in enumerate(clouds):
        cloud_x, cloud_y = cloud
        draw_cloud(cloud_x, cloud_y)
        # masuk ke bagian inti penggerak awan
        cloud_x -= 1
        clouds[i] = (cloud_x, cloud_y)
        # Jika awan mencapai batas layar kiri, reset posisi
        if cloud_x < -60:
            clouds[i] = (screen_width, random.randint(50, 150))


    # Jika mobil mencapai batas layar kiri, reset posisi
    if car_x < -80:
        car_x = screen_width


    # Jika mobil kedua mencapai batas layar kanan, reset posisi
    if car2_x > screen_width:
        car2_x = -80

    # Update display
    pygame.display.flip()

    # Atur FPS
    clock.tick(60)
