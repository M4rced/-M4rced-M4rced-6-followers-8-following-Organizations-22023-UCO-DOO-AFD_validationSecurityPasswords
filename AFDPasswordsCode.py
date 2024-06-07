import re
import msvcrt

def mostrar_reglas():
    print("Reglas para crear una contraseña:")
    print("1. La contraseña debe tener entre 8 y 12 caracteres.")
    print("2. La contraseña debe contener al menos una letra (mayúscula o minúscula).")
    print("3. La contraseña debe contener al menos un número (del 1 al 9).")
    print("4. La contraseña debe contener al menos un símbolo especial [#, %, &, $, ¿, ?, *].")
    print("{Nota: Una contraseña de 12 caracteres es más segura que una de 8 caracteres.}")
    print()

def es_contrasena_segura(contrasena):
    # Evaluar la seguridad de la contraseña
    longitud = len(contrasena)
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_minuscula = any(c.islower() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    tiene_simbolo = any(c in "#%&$¿?*" for c in contrasena)
    
    # Condiciones de seguridad
    if longitud == 8 and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
        return "segura"
    elif longitud > 8 and longitud <= 12 and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
        return "muy segura"
    else:
        return "insegura"

def validar_contrasena(contrasena):
    # Validar que la contraseña solo contenga los caracteres permitidos
    if not re.fullmatch(r"[a-zA-ZñÑ1-9#%&$¿?*]{8,12}", contrasena):
        return False
    if not (any(c.isalpha() for c in contrasena) and any(c.isdigit() for c in contrasena) and any(c in "#%&$¿?*" for c in contrasena)):
        return False
    return True

def input_contrasena():
    contrasena = ""
    print("Crea una contraseña (8-12 caracteres): ", end="", flush=True)
    while True:
        char = msvcrt.getch()
        if char == b'\r':  # Enter key
            if len(contrasena) >= 8:
                break
            else:
                print("\nContraseña demasiado corta. Debe tener al menos 8 caracteres.")
                return ""
        elif char == b'\x08':  # Backspace key
            if len(contrasena) > 0:
                contrasena = contrasena[:-1]
                print("\b \b", end="", flush=True)
        elif len(contrasena) < 12:
            contrasena += char.decode()
            print("*", end="", flush=True)
    print()
    return contrasena

def main():
    mostrar_reglas()
    while True:
        contrasena = input_contrasena()
        if not contrasena:
            continue
        if validar_contrasena(contrasena):
            print(f"Tu contraseña es: {contrasena}")
            seguridad = es_contrasena_segura(contrasena)
            if seguridad == "segura":
                print(f"La seguridad de tu contraseña es: {seguridad}")
                print ("Te sugerimos crear una contraseña más larga para mayor seguridad.")
            else:
                print(f"La seguridad de tu contraseña es: {seguridad}")
            break
        else:
            print(f"Tu contraseña es: {contrasena}")
            print("Contraseña: insegura")
            print("Asegúrate de seguir las reglas especificadas para mayor seguridad.\n")

if __name__ == "__main__":
    main()
