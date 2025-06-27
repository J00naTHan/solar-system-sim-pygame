import pygame
import random
import math
from typing import List, Tuple


class StarBackground:
    def __init__(self, width: int, height: int, num_stars: int = 500):
        self.width = width
        self.height = height
        self.stars = self._generate_stars(num_stars)
        self.twinkle_speed = 0.05

    def _generate_stars(self, num_stars: int) -> List[Tuple]:
        stars = []
        for _ in range(num_stars):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)

            brightness = random.randint(100, 255)
            size = random.uniform(0.5, 2.5)
            twinkle_factor = random.uniform(0.8, 1.2)
            speed = random.uniform(0.01, 0.03)

            if random.random() < 0.1:
                color_variation = random.choice(
                    [
                        (255, 200, 150),
                        (200, 200, 255),
                        (255, 150, 150),
                    ]
                )
                color = (
                    min(255, int(color_variation[0] * (brightness / 255))),
                    min(255, int(color_variation[1] * (brightness / 255))),
                    min(255, int(color_variation[2] * (brightness / 255))),
                )
            else:
                color = (brightness, brightness, brightness)

            stars.append(
                {
                    "pos": (x, y),
                    "size": size,
                    "color": color,
                    "original_color": color,
                    "twinkle_factor": twinkle_factor,
                    "speed": speed,
                    "phase": random.uniform(0, 2 * math.pi),
                }
            )
        return stars

    def update(self):
        for star in self.stars:
            star["phase"] += star["speed"]
            twinkle = math.sin(star["phase"]) * 0.2 + 0.8

            r, g, b = star["original_color"]
            star["color"] = (
                min(255, int(r * twinkle * star["twinkle_factor"])),
                min(255, int(g * twinkle * star["twinkle_factor"])),
                min(255, int(b * twinkle * star["twinkle_factor"])),
            )

    def draw(self, surface: pygame.Surface):
        for star in self.stars:
            pygame.draw.circle(surface, star["color"], star["pos"], star["size"])

            if star["size"] > 1.5:
                glow_surf = pygame.Surface(
                    (int(star["size"] * 4), int(star["size"] * 4)), pygame.SRCALPHA
                )
                pygame.draw.circle(
                    glow_surf,
                    (*star["color"][:3], 50),
                    (int(star["size"] * 2), int(star["size"] * 2)),
                    int(star["size"] * 2),
                )
                surface.blit(
                    glow_surf,
                    (
                        star["pos"][0] - star["size"] * 2,
                        star["pos"][1] - star["size"] * 2,
                    ),
                )
