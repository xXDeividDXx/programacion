if __name__ == "__main__":
   try:
      archivo = open("archivo_2.txt", "r")
      print(archivo.read())
   except:
      print("lol")  