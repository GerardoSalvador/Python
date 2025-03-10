
#!/usr/bin/env python3
import os, re
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 


texto = "Mi gato está en el tejado y mi otro gato está en el jardin"
texto_1 = "Hoy estamos a fecha 10/10/2025, mañana estaremos a 11/10/2025"
texto_2 = "Los usuarios pueden contactarnos a soporte@hack.io o a sistemas@hack.io"
texto_3 = "Mi gato está en el tejado y mi perro está en el jardin"
texto_4 = "Campo1, Campo2, Campo3, Campo4, Campo5, Campo6"

texto = re.findall("gato", texto)
texto_1 = re.findall("\d{2}\/\d{2}\/\d{4}", texto_1)
texto_2 = re.findall("(\w+)@(\w+\.\w{2,})", texto_2)
texto_3 = re.sub("gato", "perro", texto_3)
texto_4 = re.split(",", texto_4)

print(texto)
print(texto_1)
print(texto_2)
print(texto_3)
print(texto_4)
print(texto_4[1])

# Validador de un correo electrónico

def validar_correo(correo):
    
    patron = "[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}"

    if re.findall(patron, correo):
        return True
    else:
        return False

print(validar_correo("soporte@hack4u.io"))

################################################################

patrones = "car, carro, cart, masticar, magicarp"

print(re.findall("car", patrones))
print(re.findall(r"\bcar", patrones))
print(re.findall(r"car\b", patrones))
print(re.findall(r"\bcar\b", patrones))

################################################################

texto_5 = "Hoy estamos a dia 10/10/2023 mañana será 11/10/2023"
patron = r"\b(\d{2}\/\d{2}\/\d{4})\b"
print(re.findall(patron, texto_5))

for match in re.finditer(patron, texto_5):
    print(f"La fecha es: {match.group(0)}, la cual comienza en la posicion {match.start()} y termina en la posicion {match.end()}")