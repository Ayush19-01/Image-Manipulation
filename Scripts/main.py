from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import manipulation
import steganography
from tkinter import filedialog
import tkinter as tk
from kivy.app import App
from PIL import Image
import os
from kivy.properties import StringProperty

pwd = os.getcwd()
pwdl = pwd.split("\\")
dir_point = ""
for i in pwdl:
    if i == "Image Manipulation":
        dir_point += i + "\\"
        break
    else:
        dir_point +=  i + "\\"

class SuccessCon(FloatLayout):


    global popupWindow


    def showpopup():
        global popupWindow
        show = SuccessCon
        popupWindow = Popup(title="Success", content= show(), size_hint=(None, None), size=(400, 200))
        popupWindow.open()

        return None

    def quit1(self):

        global popupWindow
        popupWindow.dismiss()

        return None


class SuccessCom(FloatLayout):

    global popupWindow
    def showpopup():
        global popupWindow
        show = SuccessCom
        popupWindow = Popup(title="Success", content= show(), size_hint=(None, None), size=(400, 200))
        popupWindow.open()

        return None

    def quit1(self):
        global popupWindow
        popupWindow.dismiss()

        return None


class SuccessRes(FloatLayout):

    global popupWindow
    def showpopup():
        global popupWindow
        show = SuccessRes
        popupWindow = Popup(title="Success", content= show(), size_hint=(None, None), size=(400, 200))
        popupWindow.open()

        return None

    def quit1(self):
        global popupWindow
        popupWindow.dismiss()

        return None


class SuccessSteg(FloatLayout):

    global popupWindow
    def showpopup():
        global popupWindow
        show = SuccessSteg
        popupWindow = Popup(title="Success", content= show(), size_hint=(None, None), size=(400, 200))
        popupWindow.open()

        return None

    def quit1(self):
        global popupWindow
        popupWindow.dismiss()

        return None


# popup error messages block ends here
class MainScreen(Screen):
    def on_pre_enter(self):
        Window.size = (450,800)
        Window.resizable = False

class Convert(Screen):

    pass


class pngtojpg(Screen):

    filename1 = ObjectProperty(None)
    def get_filename(self):
        global filename
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Png", "*.png"),))
        self.filename1.text = str(filename.split("/")[-1])
        root.destroy()

    def get_saveas(event):
        global pb
        global filename
        root = tk.Tk()
        root.withdraw()
        filename2 = filedialog.asksaveasfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Jpg", ".jpg .jpeg"),))

        root.destroy()
        x = (filename2.split(".")[-1])
        if x == "jpg" or x == "jpeg":
            pass
        else:
            extension = filename.split(".")[-1]
            filename2 += "." + extension

        manipulation.conversion(filename, filename2)
        SuccessCon.showpopup()



class jpgtopng(Screen):

    filename1 = ObjectProperty(None)
    def get_filename(self):
        global filename
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Jpg", ".jpg .jpeg"),))
        self.filename1.text = str(filename.split("/")[-1])
        root.destroy()


    def get_saveas(event):
        global pb
        global filename
        root = tk.Tk()
        root.withdraw()
        filename2 = filedialog.asksaveasfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Png", ".png "),))
        root.destroy()

        x = (filename2.split(".")[-1])
        if x == "png" :
            pass
        else:
            filename2 += ".png"

        manipulation.conversion(filename, filename2)
        SuccessCon.showpopup()



class Resize(Screen):

    height_h = ObjectProperty(None)
    width_h = ObjectProperty(None)
    filename1 = ObjectProperty(None)
    filesize = ObjectProperty(None)
    def get_filename(self):
        global filename
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Image Files", ".png .jpg .jpeg"),))
        self.filename1.text = str(filename.split("/")[-1])
        im = Image.open(filename)
        width_x, height_x = im.size
        im.close()
        self.filesize.text = str(width_x)+" x "+str(height_x)
        root.destroy()

    def get_saveas(self):
        global pb
        global filename
        root = tk.Tk()
        root.withdraw()
        filename2 = filedialog.asksaveasfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Image Files", ".png . jpg .jpeg"),))
        root.destroy()
        x = (filename2.split(".")[-1])
        if x == "png" or x == "jpg" or x == "jpeg":
            pass
        else:
            extension = filename.split(".")[-1]
            filename2 += "." + extension
        tmp1 = self.width_h.text
        tmp2 = self.height_h.text
        if tmp2 == "":
            manipulation.resizer_scale(filename,filename2,int(tmp1))
        else:
            manipulation.resizer_fit(filename,filename2,int(tmp1),int(tmp2))
        SuccessRes.showpopup()


class Compress(Screen):

    filename1 = ObjectProperty(None)
    val = ObjectProperty(None)
    def get_filename(self):
        global filename
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Image Files", ".png .jpg .jpeg"),))
        self.filename1.text = str(filename.split("/")[-1])
        root.destroy()
    def get_saveas(self):
        global pb
        global filename
        root = tk.Tk()
        root.withdraw()

        filename2 = filedialog.asksaveasfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Image Files", ".png .jpg .jpeg"),))
        root.destroy()
        print(filename2)
        x = (filename2.split(".")[-1])
        if x == "png" or x == "jpg" or x == "jpeg":
            pass
        else:
            filename2 += "." + "jpg"
        print(filename2)
        com = 100 - int(self.val.value)
        manipulation.compression(filename,filename2,com)
        SuccessCom.showpopup()


class Steganography_Main(Screen):

    pass

class StegDe(Screen):

    datade = ObjectProperty(None)
    filename1 = ObjectProperty(None)
    def get_filename(self):
        global filename
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Png", ".png"),))
        self.filename1.text = str(filename.split("/")[-1])
        root.destroy()

    def get_decrypt(self):
        global filename
        tmp1 = steganography.decode(filename)
        self.datade.text = tmp1

class StegEn(Screen):
    dataen = ObjectProperty(None)
    filename1 = ObjectProperty(None)
    def get_filename(self):
        global filename
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Png", ".png"),))
        self.filename1.text = str(filename.split("/")[-1])
        root.destroy()

    def get_saveas(self):
        global pb
        global filename
        root = tk.Tk()
        root.withdraw()
        filename2 = filedialog.asksaveasfilename(initialdir="C:\\Users\\Ayush\\PycharmProjects\\DA\\", title="Select an image",filetype=(("Png", ".png"),))
        root.destroy()
        x = (filename2.split(".")[-1])
        if x == "png":
            pass
        else:
            filename2 += ".png"

        tmp1 = str(self.dataen.text)
        steganography.encode(filename,tmp1,filename2)
        SuccessSteg.showpopup()


#

# kv file and initialisation manager
class WindowManager(ScreenManager):
    global dir_point
    dir = StringProperty(dir_point)
    Window.set_title('Image')
    pass


class MainApp(App):
    def build(self):
        self.title = 'Image Manipulation'
        self.root_widget = Builder.load_file("my.kv")
        return self.root_widget


if __name__ == "__main__":
    MainApp().run()
