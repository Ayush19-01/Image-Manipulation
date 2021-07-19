from PIL import Image

def encode(image_dir,data,savename):

    open1=Image.open(image_dir)
    rgb_im = open1.convert('RGB')
    img_copy = rgb_im.copy()
    encode_act(img_copy,data)
    img_copy.save(savename)

    return None


def decode(image_dir):

    open1 = Image.open(image_dir)
    rgb_im = open1.convert('RGB')
    data = ''
    imgdata = iter(rgb_im.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +imgdata.__next__()[:3] + imgdata.__next__()[:3]]

        thebinstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                thebinstr += '0'
            else:
                thebinstr += '1'

        data += chr(int(thebinstr, 2))
        if (pixels[-1] % 2 != 0):

            return data


def genData(data):

    al_bin = []
    for i in data:
        al_bin.append(format(ord(i),'08b'))

    return al_bin


def encode_act(newimg, data):

    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in pixel_act(newimg.getdata(), data):
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

    return None


def pixel_act(pixels, data):

    data_bin = genData(data)
    lendata = len(data_bin)
    imdata = iter(pixels)

    for i in range(lendata):
        pixels = [value for value in imdata.__next__()[:3] +imdata.__next__()[:3] + imdata.__next__()[:3]]
        for j in range(0, 8):
            if (data_bin[i][j] == '0' and pixels[j]% 2 != 0):
                pixels[j] -= 1

            elif (data_bin[i][j] == '1' and pixels[j] % 2 == 0):
                if(pixels[j] != 0):
                    pixels[j] -= 1
                else:
                    pixels[j] += 1

        if (i == lendata - 1):
            if (pixels[-1] % 2 == 0):
                if(pixels[-1] != 0):
                    pixels[-1] -= 1
                else:
                    pixels[-1] += 1

        else:
            if (pixels[-1] % 2 != 0):
                pixels[-1] -= 1

        pixels = tuple(pixels)
        yield pixels[0:3]
        yield pixels[3:6]
        yield pixels[6:9]