import pygame

# Basic constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5
JUMP_STRENGTH = 15
GRAVITY = 0.8

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, SCREEN_HEIGHT - PLAYER_HEIGHT - 100, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.velocity_y = 0
        self.on_ground = False

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.on_ground = False

    def apply_gravity(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

    def collide_platforms(self, platforms):
        # Simple collision with platforms (assume axis-aligned)
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.velocity_y > 0:  # falling
                    self.rect.bottom = platform.top
                    self.velocity_y = 0
                    self.on_ground = True

    def update(self, platforms):
        self.apply_gravity()
        self.collide_platforms(platforms)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Platformer Skeleton")
    clock = pygame.time.Clock()

    player = Player()

    # Simple ground platform
    ground = pygame.Rect(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40)
    platforms = [ground]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        player.update(platforms)

        # Drawing
        screen.fill((135, 206, 235))  # sky blue background
        for platform in platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
