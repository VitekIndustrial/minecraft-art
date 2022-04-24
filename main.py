import render, os

def start():
    listimg = os.listdir(path='input')
    if str(listimg) == '[]':
        print('Изображения не найдены!')
        input('Press Enter')
        exit()
    print('Список имеющихся изображений:')
    for images in listimg:
        print(images)
    name_img = input('Введите полное название фотографии: ')
    name_model = 'new_db_learn2'
    file_name = input('Название конечного файла: ')
    height = int(input('Высота конечного изображения(в блоках): '))
    try:
        render.render(file_name, render.loadimg('input\{}'.format(name_img), height), name_model)
    except:
        print('Фото не найдено!')
        start()
    input('Press Enter')
if __name__ == '__main__':
    print('''      g    g   Æ▄                                   ╓██▀ ▄           ╓▄         ,▄  
      █▌  ╒█▌ ╒▄▄ ╔▄▄▄▄▄   ▄▄▄▄,  ,▄▄▄▄ ▄▄▄▄m╓▄▄▄, &██▄j▄█▄▄        ┌██▄   ▄▄▄▄▄██▄▄
     ▐█▀▌ ▓▀▓  ▐█ ▐▌   █▌ █▌▄▄▄█▌▓▌     ▓▌   ,▄▄▄▓  █▌   █   ,▄▄,   █` █L  ▓▌   ▐▌  
     ▓▌ ▓█▌ ▐▌ ▐█ ▐▌   ▐▌ █▌     ▓▌     ▓▌  ]█   ▓▌ ▓▌   █   `""`  ██████, ▓▌   ▐▌  
    ╩▀  └▀  ╙▀─╨▀ ╚▀   ▀▀ `▀▀▀▀╜  ▀▀▀▀▀`▀▀   ▀▀▀▀▀╝ ▀▀   ▀▀▀╜     ▀▀    ╚▀╩▀╛    ▀▀▀''')
    start()