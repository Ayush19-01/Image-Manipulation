from PIL import Image
def compression(filename,filename2,val):
    im = Image.open(filename)
    im.save(filename2,optimize=True,quality=val)

    im.close()
    return None


def conversion(filename,filename2):

    extension = filename.split(".")
    if extension[1] == "png":
        im = Image.open(filename)
        im.save(filename2)

    else:
        im = Image.open(filename)
        im.save(filename2)

    im.close()
    return None


def resizer_scale(filename,filename2,width_h,):

    im = Image.open(filename)
    width_t,height_t = im.size
    height_h = int(width_h*height_t/width_t)
    im = im.resize((width_h, height_h), Image.ANTIALIAS)
    im.save(filename2)

    im.close()
    return None


def resizer_fit(filename,filename2,width_h,height_h):

    im = Image.open(filename)
    im = im.resize((width_h,height_h), Image.ANTIALIAS)
    im.save(filename2)

    im.close()
    return None
