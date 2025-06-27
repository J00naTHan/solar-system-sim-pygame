import pygame
import math


class Planet:
    def __init__(self, name, color, distance, speed, size, info, has_rings=False):
        self.name = name
        self.color = color
        self.orbit_radius = distance
        self.speed = speed
        self.size = size
        self.info = info
        self.angle = 0
        self.mouse_over = False
        self.trail_positions = []
        self.max_trail_length = 200

        self.moons = []
        self.has_rings = has_rings

    def add_moon(self, moon):
        self.moons.append(moon)

    def update(self, paused, time_multiplier):
        if not paused:
            self.angle += self.speed * time_multiplier

        for moon in self.moons:
            moon.update(paused, time_multiplier)

    def _draw_rings(self, surface, planet_pos):
        ring_rect = pygame.Rect(
            planet_pos[0] - self.size * 2,
            planet_pos[1] - self.size,
            self.size * 4,
            self.size * 2,
        )

        ring_color = (210, 180, 140, 150)

        s = pygame.Surface((self.size * 4, self.size * 4), pygame.SRCALPHA)
        pygame.draw.ellipse(
            s, ring_color, (0, self.size, self.size * 4, self.size * 2), 2
        )

        rotated_s = pygame.transform.rotate(s, 30)
        rect = rotated_s.get_rect(center=planet_pos)

        surface.blit(rotated_s, rect.topleft)

    def draw(self, surface, center, mouse_pos):
        planet_x = center[0] + self.orbit_radius * math.cos(self.angle)
        planet_y = center[1] + self.orbit_radius * math.sin(self.angle)
        planet_pos = (int(planet_x), int(planet_y))

        if (
            len(self.trail_positions) == 0
            or (planet_x, planet_y) != self.trail_positions[-1]
        ):
            self.trail_positions.append((planet_x, planet_y))
            if len(self.trail_positions) > self.max_trail_length:
                self.trail_positions.pop(0)

        if len(self.trail_positions) > 1:
            for i, pos in enumerate(self.trail_positions):
                alpha = int(255 * (i / len(self.trail_positions)))
                trail_color = (*self.color, alpha)
                trail_surface = pygame.Surface((2, 2), pygame.SRCALPHA)
                pygame.draw.circle(trail_surface, trail_color, (1, 1), 1)
                surface.blit(trail_surface, (int(pos[0]) - 1, int(pos[1]) - 1))

        if self.has_rings:
            self._draw_rings(surface, planet_pos)

        distance = math.sqrt(
            (mouse_pos[0] - planet_x) ** 2 + (mouse_pos[1] - planet_y) ** 2
        )
        self.mouse_over = distance <= self.size

        if self.mouse_over:
            highlight_color = (
                min(255, self.color[0] + 70),
                min(255, self.color[1] + 70),
                min(255, self.color[2] + 70),
            )
        else:
            highlight_color = self.color

        pygame.draw.circle(surface, highlight_color, planet_pos, self.size)

        for moon in self.moons:
            moon.draw(surface, planet_pos, mouse_pos)

        return self.mouse_over


class Moon(Planet):
    def __init__(self, name, color, distance, speed, size, info):
        super().__init__(name, color, distance, speed, size, info)
        self.max_trail_length = 50

    def _draw_rings(self, surface, planet_pos):
        pass

    def draw(self, surface, center, mouse_pos):
        super().draw(surface, center, mouse_pos)
        return self.mouse_over


class Sun:
    def __init__(self, name, color, size, info):
        self.name = name
        self.color = color
        self.size = size
        self.info = info
        self.mouse_over = False

    def update(self, paused, time_multiplier):
        pass

    def draw(self, surface, center, mouse_pos):
        distance = math.sqrt(
            (mouse_pos[0] - center[0]) ** 2 + (mouse_pos[1] - center[1]) ** 2
        )
        self.mouse_over = distance <= self.size

        pygame.draw.circle(surface, self.color, center, self.size)

        if self.mouse_over:
            glow_color = (255, 255, 150, 60)

            glow_surf = pygame.Surface((self.size * 4, self.size * 4), pygame.SRCALPHA)
            pygame.draw.circle(
                glow_surf,
                glow_color,
                (self.size * 2, self.size * 2),
                self.size * 1.5,
            )
            surface.blit(
                glow_surf, (center[0] - self.size * 2, center[1] - self.size * 2)
            )

        return self.mouse_over
