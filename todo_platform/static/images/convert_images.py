import base64


class Funcoes():
     def convert_to_base64(self, image_file):
          with open(image_file, "rb") as img_file:
               my_string_base64 = base64.b64encode(img_file.read())
          return my_string_base64
     

if __name__ == '__main__':
     funcs = Funcoes()
     image_converted = funcs.convert_to_base64('ANIVERSARIO_MISSA.jpg')
     print(image_converted)
