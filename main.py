import pygame
import sys

from sim_components.background import StarBackground


from sim_components.celestial import Planet, Moon, Sun

pygame.init()

WIDTH, HEIGHT = 1200, 900
CENTER = (WIDTH // 2, HEIGHT // 2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sistema Solar Completo - HUD Interativa")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 14)
info_font = pygame.font.SysFont("arial", 18, bold=True)
ui_font = pygame.font.SysFont("arial", 16, bold=True)

background = StarBackground(WIDTH, HEIGHT, num_stars=1000)


sol = Sun(
    name="Sol",
    color=(255, 255, 0),
    size=25,
    info="A estrela no centro do nosso sistema.",
)


mercury = Planet(
    name="Mercúrio",
    color=(128, 128, 128),
    distance=50,
    speed=0.04,
    size=4,
    info="Planeta rochoso.",
)
venus = Planet(
    name="Vênus",
    color=(218, 214, 183),
    distance=80,
    speed=0.025,
    size=7,
    info="Atmosfera densa e tóxica.",
)
earth = Planet(
    name="Terra",
    color=(100, 149, 237),
    distance=120,
    speed=0.017,
    size=8,
    info="Nosso lar.",
)
mars = Planet(
    name="Marte",
    color=(188, 39, 50),
    distance=160,
    speed=0.013,
    size=6,
    info="O Planeta Vermelho.",
)
jupiter = Planet(
    name="Júpiter",
    color=(216, 202, 157),
    distance=240,
    speed=0.008,
    size=18,
    info="Gigante gasoso.",
)
saturn = Planet(
    name="Saturno",
    color=(234, 214, 184),
    distance=320,
    speed=0.006,
    size=15,
    info="Famoso por seus anéis.",
    has_rings=True,
)
uranus = Planet(
    name="Urano",
    color=(173, 216, 230),
    distance=380,
    speed=0.004,
    size=12,
    info="Gigante de gelo inclinado.",
)
neptune = Planet(
    name="Netuno",
    color=(63, 81, 181),
    distance=430,
    speed=0.003,
    size=11,
    info="Ventos supersônicos.",
)
planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
the_moon = Moon(
    name="Lua",
    color=(200, 200, 200),
    distance=15,
    speed=0.1,
    size=2,
    info="Satélite natural da Terra.",
)
earth.add_moon(the_moon)
phobos = Moon(
    name="Phobos",
    color=(100, 90, 80),
    distance=10,
    speed=0.2,
    size=1,
    info="Lua de Marte.",
)
deimos = Moon(
    name="Deimos",
    color=(120, 110, 100),
    distance=16,
    speed=0.15,
    size=2,
    info="Lua de Marte.",
)
mars.add_moon(phobos)
mars.add_moon(deimos)
io = Moon(
    name="Io",
    color=(255, 255, 0),
    distance=30,
    speed=0.18,
    size=3,
    info="Vulcanicamente ativa.",
)
europa = Moon(
    name="Europa",
    color=(180, 160, 140),
    distance=40,
    speed=0.14,
    size=3,
    info="Oceano sob o gelo.",
)
ganymede = Moon(
    name="Ganímedes",
    color=(140, 120, 100),
    distance=55,
    speed=0.1,
    size=4,
    info="A maior lua do sistema.",
)
callisto = Moon(
    name="Calisto",
    color=(80, 70, 60),
    distance=70,
    speed=0.08,
    size=4,
    info="Superfície com crateras.",
)
jupiter.add_moon(io)
jupiter.add_moon(europa)
jupiter.add_moon(ganymede)
jupiter.add_moon(callisto)


all_bodies = [sol] + planets

paused = False
running = True
time_multiplier = 0.5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

            if event.key == pygame.K_UP:
                if time_multiplier < 1.0:
                    time_multiplier += 0.05
                else:
                    time_multiplier += 0.1
            if event.key == pygame.K_DOWN:
                step = 0.05 if time_multiplier <= 1.0 else 0.1
                time_multiplier = max(0.05, time_multiplier - step)

    mouse_pos = pygame.mouse.get_pos()

    for body in all_bodies:
        body.update(paused, time_multiplier)

    screen.fill((0, 0, 0))
    background.draw(screen)

    for planet in planets:
        pygame.draw.circle(screen, (50, 50, 50), CENTER, planet.orbit_radius, 1)

    info_to_display = None

    if sol.draw(screen, CENTER, mouse_pos):
        info_to_display = sol

    for planet in planets:
        if planet.draw(screen, CENTER, mouse_pos):
            info_to_display = planet
        for moon in planet.moons:
            if moon.mouse_over:
                info_to_display = moon

    top_ui_rect = pygame.Rect(0, 0, WIDTH, 30)
    screen.fill((0, 0, 0), top_ui_rect)

    if paused:
        pause_text = ui_font.render("PAUSADO", True, (255, 255, 0))
        screen.blit(pause_text, (10, 5))

    speed_text_val = f"{round(time_multiplier, 2)}x"
    speed_text = ui_font.render(f"Velocidade: {speed_text_val}", True, (255, 255, 255))
    screen.blit(speed_text, (WIDTH - 150, 5))

    if info_to_display:
        name_text = info_font.render(info_to_display.name, True, (255, 255, 255))
        info_text = font.render(info_to_display.info, True, (255, 255, 255))

        text_rect = pygame.Rect(mouse_pos[0] + 15, mouse_pos[1], 250, 60)
        s = pygame.Surface((text_rect.width, text_rect.height), pygame.SRCALPHA)
        s.fill((0, 0, 0, 128))
        screen.blit(s, (text_rect.left, text_rect.top))

        screen.blit(name_text, (text_rect.left + 10, text_rect.top + 5))
        screen.blit(info_text, (text_rect.left + 10, text_rect.top + 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
