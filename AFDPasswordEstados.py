import msvcrt

class AutomataPassword:
    def __init__(self):
        self.state = 'q0'
        self.has_letter = False
        self.has_digit = False
        self.has_symbol = False

    def transition(self, char):
        if self.state == 'q0':
            if char.isdigit():
                self.state = 'q1'
                self.has_digit = True
            elif char.isalpha():
                self.state = 'q2'
                self.has_letter = True
            elif char in '#%&$¿?*':
                self.state = 'q3'
                self.has_symbol = True
        elif self.state == 'q1':
            if char.isdigit():
                self.state = 'q1'
            elif char.isalpha():
                self.state = 'q4'
                self.has_letter = True
            elif char in '#%&$¿?*':
                self.state = 'q5'
                self.has_symbol = True
        elif self.state == 'q2':
            if char.isdigit():
                self.state = 'q4'
                self.has_digit = True
            elif char.isalpha():
                self.state = 'q2'
            elif char in '#%&$¿?*':
                self.state = 'q6'
                self.has_symbol = True
        elif self.state == 'q3':
            if char.isdigit():
                self.state = 'q5'
                self.has_digit = True
            elif char.isalpha():
                self.state = 'q6'
                self.has_letter = True
            elif char in '#%&$¿?*':
                self.state = 'q3'
        elif self.state == 'q4':
            if char.isdigit():
                self.state = 'q4'
            elif char.isalpha():
                self.state = 'q4'
            elif char in '#%&$¿?*':
                self.state = 'q7'
                self.has_symbol = True
        elif self.state == 'q5':
            if char.isdigit():
                self.state = 'q5'
            elif char.isalpha():
                self.state = 'q7'
                self.has_letter = True
            elif char in '#%&$¿?*':
                self.state = 'q5'
        elif self.state == 'q6':
            if char.isdigit():
                self.state = 'q7'
                self.has_digit = True
            elif char.isalpha():
                self.state = 'q6'
            elif char in '#%&$¿?*':
                self.state = 'q6'
        elif self.state == 'q7':
            if char.isdigit():
                self.state = 'q7'
            elif char.isalpha():
                self.state = 'q7'
            elif char in '#%&$¿?*':
                self.state = 'q7'

    def is_valid(self):
        return self.has_letter and self.has_digit and self.has_symbol

def mostrar_reglas():
    print("Reglas para crear una contraseña:")
    print("1. La contraseña debe tener entre 8 y 12 caracteres.")
    print("2. La contraseña debe contener al menos una letra (mayúscula o minúscula).")
    print("3. La contraseña debe contener al menos un número (del 1 al 9).")
    print("4. La contraseña debe contener al menos un símbolo especial [#, %, &, $, ¿, ?, *].")
    print("{Nota: Una contraseña de 12 caracteres es más segura que una de 8 caracteres.}")
    print()

def es_contrasena_segura(contrasena):
    longitud = len(contrasena)
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_minuscula = any(c.islower() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    tiene_simbolo = any(c in "#%&$¿?*" for c in contrasena)
    
    if longitud == 8 and tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo:
        return "segura"
    elif longitud > 8 and longitud <= 12 and tiene_mayuscula and tiene_minuscula and tiene_numero:
        return "muy segura"
    else:
        return "insegura"

def validar_contrasena(contrasena):
    automata = AutomataPassword()
    for char in contrasena:
        automata.transition(char)
    return automata.is_valid()

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
                print("Te sugerimos crear una contraseña más larga para mayor seguridad.")
            else:
                print(f"La seguridad de tu contraseña es: {seguridad}")
            break
        else:
            print(f"Tu contraseña es: {contrasena}")
            print("Contraseña: insegura")
            print("Asegúrate de seguir las reglas especificadas para mayor seguridad.\n")

if __name__ == "__main__":
    main()


