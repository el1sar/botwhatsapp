import pywhatkit

with open("config.txt", "r", encoding="utf-8") as archivo:
    lineas = [l for l in archivo.read().split("\n") 
              if l.strip() and not l.strip().startswith("#")]

numero = lineas[0].strip()
mensaje = "\n".join(lineas[1:]).strip() if len(lineas) > 1 else ""

pywhatkit.sendwhatmsg_instantly(numero, mensaje)