from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty

class Widgets(FloatLayout):

    def cifra(self, s, clave):
        clave = round(clave)
        buff = []
        for c in s:
            num = ord(c)
            if 65 <= num < 91:
                new_num = ((num - 65 + clave) % 26) + 65
                buff.append(str(chr(new_num)))
            elif 97 <= num < 123:
                new_num = ((num - 97 + clave) % 26) + 97
                buff.append(str(chr(new_num)))
            else:
                buff.append(c)
        return ''.join(buff)

    val = StringProperty('0')

    def slider_value(self, widget):
        self.val = f'{round(widget.value)}'

    def cambio_texto(self, widget):
        print(widget.state)
        if widget.state == 'down':
            self.ids.text_label.text = self.cifra(self.ids.input.text, self.ids.slider.value)



class ShieldApp(App):
    pass

def main():
    app = ShieldApp()
    app.run()

if __name__ == '__main__':
    main()