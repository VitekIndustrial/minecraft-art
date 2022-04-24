from PIL import Image
import joblib, threading

def loadimg(name, h):
    try:
        img = Image.open(name)
        razm = img.size
        weight = int(h * razm[0] // razm[1]) // 2 * 2
        img = img.resize((weight, h))
        return img
    except FileNotFoundError:
        print("Файл не найден")

def pollisttetracasr(img):
    global listc1, listc2
    listcolor = []
    pix = img.load()
    h, w = img.size[1], img.size[0]
    t1 = threading.Thread(target=multiThreading_listcolor1, args=(pix, 0, h//2, w,))
    t2 = threading.Thread(target=multiThreading_listcolor2, args=(pix, h//2, h, w,))
    t1.start(); t2.start()
    t1.join()
    listcolor += listc1
    t2.join()
    listcolor += listc2
    return listcolor

def multiThreading_listcolor1(pix, h1, h2, w):
    global listc1
    for y in range(h1, h2):
        for x in range(w):
            rgb = (pix[x, y][0], pix[x, y][1], pix[x, y][2])
            listc1.append(rgb)

def multiThreading_listcolor2(pix, h1, h2, w):
    global listc2
    for y in range(h1, h2):
        for x in range(w):
            rgb = (pix[x, y][0], pix[x, y][1], pix[x, y][2])
            listc2.append(rgb)

def getMCP(img, model):
    listcolor = pollisttetracasr(img)
    size = img.size
    model = joblib.load('models\{}.pkl'.format(model))
    pr = model.predict(listcolor)
    listblc = []
    i = 0
    for b in range(size[1]):
        stro = []
        for c in range(size[0]):
            stro.append(int(pr[i]))
            i += 1
        listblc.append(stro)
    return listblc, size[0], size[1]

def render(file_name, img, model):
    list, w, h = getMCP(img, model)
    img = Image.new("RGB", (w * 16, h * 16), (255, 255, 255))
    t3 = threading.Thread(target=multiThreading_render3, args=(img, list,))
    t4 = threading.Thread(target=multiThreading_render4, args=(img, list,))
    t3.start(); t4.start()
    t3.join(); t4.join()
    img.save('output\{}.jpg'.format(file_name), quality=100)
    print('Фото готово, проверьте папку output')

def multiThreading_render3(img, list):
    for a in range(len(list)//2):
        line = list[a]
        y = a*16
        x = 0
        for block in line:
            block_img = Image.open('textures\{}.png'.format(block))
            img.paste(block_img, (x, y))
            x += 16

def multiThreading_render4(img, list):
    for a in range(len(list)//2, len(list)):
        line = list[a]
        y = a*16
        x = 0
        for block in line:
            block_img = Image.open('textures\{}.png'.format(block))
            img.paste(block_img, (x, y))
            x += 16