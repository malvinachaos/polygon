import pygame
import sys

from collections import defaultdict

# Ядро игры
class Game:
    # Инициализирует сам PyGame, шрифты, звуковой микшер, фоновое изображение,
    # игровую поверхность и игровой таймер с правильной частотой кадров
    def __init__(self, 
                 caption, 
                 width, 
                 height, 
                 back_image_filename, 
                 frame_rate):
        # загрузка фонового изображения
        self.background_image = \
            pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        # хранит в себе все объекты, которые должны рендериться и обновляться
        self.objects = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []

    # Следующие два метода проходятся по всем управляемым игровым объектам
    # и вызывают соответствующие им методы
    def update(self):
        for o in self.objects:
            o.update()
    
    def draw(self):
        for o in self.objects:
            o.draw(self.surface)
    
    # Данный метод слушает события, генерируемые PyGame(к примеру, события
    # клавиш и мыши). Для каждого события он вызывает все функции-обработчики
    # соответствующих типов
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN():
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            
            elif event.type == pygame.KEYUP():
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            
            elif event.type == (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)
    
    # Данный метод выполняет основной цикл до тех пор, пока game_over равно 
    # False
    def run(self):
        while not self.game_over:
            self.surface.blit(self.background_image, (0, 0))

            # По очереди рендерит фоновое изображениеи вызывает по порядку эти 
            # методы
            self.handle_events()
            self.update()
            self.draw()

            # Обновляет экран, записывая на дисплей всё содержимое, которое 
            # было отрендерено на текущей итерации
            pygame.display.update()
            # Метод управляет тем, когда будет вызвана следующая итерация
            self.clock.tick(self.frame_rate)