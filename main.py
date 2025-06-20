import pygame
import math
import sys
from sim_components.background import StarBackground

# Inicialização do pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação de Sistema Solar")
clock = pygame.time.Clock()

# Definição de plano de fundo
background = StarBackground(WIDTH, HEIGHT, num_stars=800)

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 100, 255)
RED = (255, 50, 50)

# Planetas com raio da órbita e velocidade angular
planets = [
    {"color": BLUE, "radius": 100, "angle": 0, "speed": 0.02, "size": 10},
    {"color": RED, "radius": 200, "angle": 0, "speed": 0.01, "size": 14}
]

# Loop principal
running = True
while running:
    clock.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza o fundo
    background.update()
    
    # Desenha o fundo
    screen.fill(BLACK)  # Limpa a tela
    background.draw(screen)

    pygame.draw.circle(screen, YELLOW, CENTER, 30)
    
    for planet in planets:
        planet['angle'] += planet['speed']
        x = CENTER[0] + planet['radius'] * math.cos(planet['angle'])
        y = CENTER[1] + planet['radius'] * math.sin(planet['angle'])
        pygame.draw.circle(screen, planet['color'], (int(x), int(y)), planet['size'])

    pygame.display.flip()

pygame.quit()
sys.exit()
