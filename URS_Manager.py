import time
import random
import os
import ctypes
import webbrowser

# Función para cambiar el color del texto en la consola de Windows
def set_cmd_text_color(color):
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleTextAttribute(kernel32.GetStdHandle(-11), color)

# Función para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_welcome_message():
    set_cmd_text_color(14)  # Amarillo claro para simular naranja
    clear_screen()
    print("BIENVENIDO AL SISTEMA DE LA UNION SOVIETICA")
    print("======================================")
    print("Versión 1.0 - 1985")
    print("======================================")
    time.sleep(2)

def show_login_screen():
    clear_screen()
    set_cmd_text_color(14)  # Amarillo claro para simular naranja
    print("======================================")
    print("ACCESO RESTRINGIDO AL SISTEMA SOVIETICO")
    print("======================================")
    attempts = 3
    while attempts > 0:
        username = input("Usuario: ")
        password = input("Contraseña: ")
        if username == "Adolfo" and password == "KKJS":
            clear_screen()
            print("======================================")
            print("ACCESO CONCEDIDO")
            print("======================================")
            print("Bienvenido Sr. Adolfo")
            print("======================================")
            time.sleep(2)
            return True
        else:
            attempts -= 1
            clear_screen()
            print("======================================")
            print("ACCESO DENEGADO")
            print("======================================")
            if attempts > 0:
                if attempts == 2:
                    print("PISTA: El usuario es el nombre de un líder histórico soviético")
                elif attempts == 1:
                    print("PISTA: La contraseña es un código de cuatro letras mayúsculas")
                print(f"Intentos restantes: {attempts}")
                print("======================================")
            else:
                print("ACCESO BLOQUEADO. CONTACTE AL ADMINISTRADOR")
                print("======================================")
                time.sleep(2)
                return False

def show_main_menu():
    while True:
        clear_screen()
        print("SISTEMA DE LA UNION SOVIETICA")
        print("===========================")
        print("1. Iniciar Proceso Nuclear")
        print("2. Decodificar Mensaje Secreto")
        print("3. Simulación de Apagón")
        print("4. Estado de las Reservas")
        print("5. Informe de Producción")
        print("6. Plan Espacial")
        print("7. Abrir Bunker Nuclear")
        print("8. Control de Central Nuclear")
        print("9. Salir")
        print("===========================")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            clear_screen()
            print("INICIANDO PROCESO NUCLEAR...")
            for i in range(5):
                print(f"Progreso: {i*20}%")
                time.sleep(1)
            print("PROCESO COMPLETADO. LA UNION SOVIETICA AHORA ES UNA SUPERPODER")
            input("Presione Enter para continuar...")
        elif opcion == '2':
            clear_screen()
            print("DECODIFICANDO MENSAJE SECRETO...")
            time.sleep(2)
            mensaje_secreto = "EL ENEMIGO PLANEA UNA INVASION USANDO A BELINDA-98"
            mensaje_encriptado = ['X'] * len(mensaje_secreto)
            for i in range(len(mensaje_secreto)):
                clear_screen()
                print("DECODIFICANDO MENSAJE SECRETO...")
                print("".join(mensaje_encriptado))
                mensaje_encriptado[i] = mensaje_secreto[i]
                time.sleep(0.2)
            print("MENSAJE SECRETO: " + "".join(mensaje_encriptado))
            input("Presione Enter para continuar...")
        elif opcion == '3':
            clear_screen()
            print("SIMULANDO APAGÓN...")
            for i in range(3):
                print(f"Apagón en {3-i} segundos...")
                time.sleep(1)
            print("APAGÓN SIMULADO. TODO EL SISTEMA ESTÁ FUERA DE SERVICIO")
            input("Presione Enter para continuar...")
        elif opcion == '4':
            clear_screen()
            print("ESTADO DE LAS RESERVAS")
            print("======================")
            reservas = {
                "Uranio": "Insuficientes",
                "Combustible Nuclear": "Críticos",
                "Trigo": "Disminuido",
                "Armas": "Suficientes"
            }
            for clave, valor in reservas.items():
                print(f"{clave}: {valor}")
            input("Presione Enter para continuar...")
        elif opcion == '5':
            clear_screen()
            print("INFORME DE PRODUCCIÓN")
            print("======================")
            produccion = {
                "Trigo": "Bajo",
                "Maquinaria": "Malo",
                "Armamento": "Medio",
                "Textiles": "Alto"
            }
            for clave, valor in produccion.items():
                print(f"{clave}: {valor}")
            input("Presione Enter para continuar...")
        elif opcion == '6':
            clear_screen()
            print("PLAN ESPACIAL")
            print("================")
            print("Estado: Fracaso")
            print("Razones: Problemas en el lanzador, fallos en las pruebas")
            input("Presione Enter para continuar...")
        elif opcion == '7':
            clear_screen()
            print("ABRIENDO BUNKER NUCLEAR")
            print("======================")
            print("1. Acceso al Control de Reacciones Nucleares")
            print("2. Acceso a los Archivos de Inteligencia")
            print("======================")
            bunker_opcion = input("Seleccione una opción: ")
            if bunker_opcion == '1':
                webbrowser.open("https://www.anygame.net/en/?id=421726850000")
            elif bunker_opcion == '2':
                webbrowser.open("https://filecr.com/en/")
            else:
                print("OPCIÓN INVÁLIDA. INTENTE NUEVAMENTE")
                time.sleep(2)
        elif opcion == '8':
            clear_screen()
            print("CONTROL DE CENTRAL NUCLEAR")
            print("==========================")
            print("1. Apagar el reactor")
            print("2. Abrir válvula de enfriamiento")
            print("==========================")
            control_opcion = input("Seleccione una opción: ")
            if control_opcion == '1':
                clear_screen()
                print("APAGANDO EL REACTOR...")
                for i in range(11):
                    print(f"Progreso: {i*10}%")
                    time.sleep(0.5)
                print("REACTOR APAGADO")
                input("Presione Enter para continuar...")
            elif control_opcion == '2':
                clear_screen()
                print("ABIERTO VALVULA DE ENFRIAMIENTO...")
                for i in range(11):
                    print(f"Progreso: {i*10}%")
                    time.sleep(0.5)
                print("VALVULA ABIERTA")
                input("Presione Enter para continuar...")
            else:
                clear_screen()
                print("OPCIÓN INVÁLIDA. INTENTE NUEVAMENTE")
                time.sleep(2)
        elif opcion == '9':
            clear_screen()
            print("SALIENDO DEL SISTEMA...")
            time.sleep(1)
            print("HASTA LUEGO")
            time.sleep(1)
            break
        else:
            clear_screen()
            print("OPCIÓN INVÁLIDA. INTENTE NUEVAMENTE")
            time.sleep(2)

def main():
    show_welcome_message()
    if show_login_screen():
        show_main_menu()

if __name__ == "__main__":
    main()
