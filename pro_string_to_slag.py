#programa para convertir una cadena de texto en formato uwl slag valido
from slugify import slugify

f = open("lista_texto.txt","r")
for line in f:

    v_string = line
    f2 = open ("lista_texto_salida.txt","a")
    v_url = slugify(v_string)
    v_string = line[:-1]
    f2.write(v_string+";;"+v_url+"\n")
    f2.close

f.close()
print("finish")
