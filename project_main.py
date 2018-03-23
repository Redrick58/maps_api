import pygame, requests, os, sys
coords = '45.666,43.1123'
spn = 0.005
map_api_server = "http://static-maps.yandex.ru/1.x/"
map_file = "map.png"
def create_image(): 
    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": coords,
        "spn": str(spn) + ',' + str(spn),
        "l": "map"
    }
    
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)
    # Запишем полученное изображение в файл.
    
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    

create_image()    
# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN and event.key == 280:
            if spn * 1.6 < 100:
                spn *= 1.6
                create_image()
        
        elif event.type == pygame.KEYDOWN and event.key == 281:
            if spn * 0.6 > 0.001:
                spn *= 0.6
                create_image()
        
    screen.fill((0,0,0))
    screen.blit(pygame.image.load(map_file), (0, 0))
    # Переключаем экран и ждем закрытия окна.
    pygame.display.flip()         

pygame.quit()
    
# Удаляем за собой файл с изображением.
os.remove(map_file)