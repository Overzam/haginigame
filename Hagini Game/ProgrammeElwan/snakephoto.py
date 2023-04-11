
import pygame

tilesize = 24
class Snake(pygame.sprite.Sprite):
    images = None
    def __init__(self, grp, pos, length, parent=None):
        super().__init__(grp)
        self.parent = parent
        self.child = None
        self.direction = 'N'

        if not self.parent: self.image = Snake.images['tete_N']
        elif length == 1: self.image = Snake.images['queue_N']
        else: self.image = Snake.images['corps_NN']

        self.pos = pos
        self.rect = self.image.get_rect(x=self.pos[0]+55, y=self.pos[1]+55)
        if length > 1:
            self.child = Snake(grp, (pos[0], pos[1]+1), length-1, self)

    def move(self):
        # if we have a parent, let's look were it moves
        parent_direction = self.parent.direction if self.parent else None

        if self.direction == 'N': self.pos = self.pos[0], self.pos[1] - 1
        elif self.direction == 'S': self.pos = self.pos[0], self.pos[1] + 1
        elif self.direction == 'E': self.pos = self.pos[0] - 1, self.pos[1]
        elif self.direction == 'W': self.pos = self.pos[0] + 1, self.pos[1]

        self.rect = self.image.get_rect(x=self.pos[0]*tilesize, y=self.pos[1]*tilesize)

        # move the child
        if self.child:
            self.child.move()

        if not self.parent: self.image = Snake.images['tete_' + self.direction]
        elif not self.child: self.image = Snake.images['queue_' + parent_direction]
        else: self.image = Snake.images['corps_' + parent_direction + self.direction]

        # follow the parent
        if parent_direction:
            self.direction = parent_direction

    def update(self):
        # no parent means we're the tete of the snake
        # and we should move we a key is pressed
        if not self.parent:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]: self.direction = 'N'
            if pressed[pygame.K_DOWN]: self.direction = 'S'
            if pressed[pygame.K_LEFT]: self.direction = 'E'
            if pressed[pygame.K_RIGHT]: self.direction = 'W'


def build_images():
    load = lambda part: pygame.image.load(f'images/snake/{part}.png').convert_alpha()
    parts = ('tete', 'corps', 'queue', 'coin')
    tete_img, corps_img, queue_img, coin_img = [load(p) for p in parts]

    return {
        'tete_N': tete_img,
        'tete_S': pygame.transform.rotate(tete_img, 180),
        'tete_E': pygame.transform.rotate(tete_img, 90),
        'tete_W': pygame.transform.rotate(tete_img, -90),
        'corps_NN': corps_img,
        'corps_SS': corps_img,
        'corps_WW': pygame.transform.rotate(corps_img, 90),
        'corps_EE': pygame.transform.rotate(corps_img, 90),
        'corps_NE': pygame.transform.rotate(coin_img, 180),
        'corps_WS': pygame.transform.rotate(coin_img, 180),
        'corps_WN': pygame.transform.rotate(coin_img, 90),
        'corps_SE': pygame.transform.rotate(coin_img, 90),
        'corps_ES': pygame.transform.rotate(coin_img, -90),
        'corps_NW': pygame.transform.rotate(coin_img, -90),
        'corps_EN': pygame.transform.rotate(coin_img, 0),
        'corps_SW': pygame.transform.rotate(coin_img, 0),
        'queue_N': queue_img,
        'queue_S': pygame.transform.rotate(queue_img, 180),
        'queue_E': pygame.transform.rotate(queue_img, 90),
        'queue_W': pygame.transform.rotate(queue_img, -90)
    }

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 480))
    Snake.images = build_images()

    # let's trigger the MOVE event every 500ms
    MOVE = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVE, 100)

    all_sprites = pygame.sprite.Group()
    snake = Snake(all_sprites, (4, 4), 8)
    clock = pygame.time.Clock()
    dt = 0
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
            if e.type == MOVE:
                snake.move()

        screen.fill((30, 30, 30))

        all_sprites.update()
        all_sprites.draw(screen)

        dt = clock.tick(60)
        pygame.display.flip()

main()