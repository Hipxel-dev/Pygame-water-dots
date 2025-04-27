import pygame

pygame.init()

screen = pygame.display.set_mode((1920 / 2, 1080 / 2))
clock = pygame.time.Clock()

class Poin:
    def __init__(self, x, y):
        self.posisi = pygame.Vector2(x, y)
        self.gerakan = pygame.Vector2(0, 0)
        self.posisi_semula = pygame.Vector2(x, y)
        self.tetangga = []
        self.tetangga_gambar = []
        self.waktu = 0

    def update(self, posisi_kursor, mouse_klik):
        self.waktu -= 0.01
        if self.waktu < 0:
            for tetangga in self.tetangga:
                self.gerakan += (tetangga.posisi - self.posisi) * 0.1
            if self.posisi.distance_squared_to(posisi_kursor) < 7700:  
                if mouse_klik:
                    self.gerakan += (self.posisi - posisi_kursor) * 0.2
                else:
                    self.gerakan += (posisi_kursor - self.posisi) * 0.02
            self.waktu = 0.05

        self.gerakan += (self.posisi_semula - self.posisi) * 0.03

        self.posisi += self.gerakan

        self.gerakan /= 1.05

    def draw(self, layar):
       pygame.draw.circle(layar,(255,255,255),self.posisi,2.0,2)

       # for tetangga in self.tetangga_gambar:
       #     pygame.draw.line(layar, (0, 100, 255), self.posisi, tetangga.posisi, 2)

jaringan = []
spacing = 14
kolum, barisan =72, 40

for y in range(barisan):
    row = []
    for x in range(kolum):
        p = Poin(-10 + x * spacing,-10 + y * spacing)
        row.append(p)
    jaringan.append(row)

font = pygame.font.SysFont(None, 24)

for y in range(barisan):
    for x in range(kolum):
        p = jaringan[y][x]
        if x > 0:
            p.tetangga.append(jaringan[y][x-1])
            p.tetangga_gambar.append(jaringan[y][x-1])
        if y > 0:
            p.tetangga.append(jaringan[y-1][x])
            p.tetangga_gambar.append(jaringan[y-1][x])
        if x < kolum - 1:
            p.tetangga.append(jaringan[y][x + 1])
        if y < barisan - 1:
            p.tetangga.append(jaringan[y + 1][x])
         


while True:
    posisi_mouse = pygame.Vector2(pygame.mouse.get_pos())
    klik_mouse = pygame.mouse.get_pressed()[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((20, 20, 30))

    for row in jaringan:
        for p in row:
            p.update(posisi_mouse, klik_mouse)
            p.draw(screen)


    pygame.display.flip()
    clock.tick(60)
