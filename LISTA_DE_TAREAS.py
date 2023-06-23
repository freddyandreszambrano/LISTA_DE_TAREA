import sys
import os
from pathlib import Path
from datetime import date
import time
import shutil



def error():
    print(" ██████  ██████╗    ██████╗")
    print(" ███     ██╔══██╗   ██╔══██╗")
    print(" ██████  ██████╔╝   ██████╔╝")
    print(" ███     ██╔══██╗   ██╔══██╗")
    print(" ██████  ██║  ██║   ██║  ██║")
    print("         ╚═╝  ╚═╝   ╚═╝  ╚═╝")



def visto_bueno():
    print("           ██")
    print("          ██")
    print("  ██     ██ ")
    print("    ██  ██")
    print("      ██")

def agregar_nueva_tarea():

    print()
    print("¿Que tarea desea agregar?")
    Lv_tarea = input()
    Ln_fecha = date.today()
    nueva_tarea = [Lv_tarea, Ln_fecha.isoformat(), "False"]

    # Verificar si la tarea ya existe en la lista
    tarea_existente = False
    for tarea in Lista_tarea:
        if tarea[:2] == nueva_tarea[:2]:
            tarea_existente = True
            break

    if not tarea_existente:
        #si La tarea que agrega es nueva
        Lista_tarea.append(nueva_tarea)
        print(" ✓✓✓ Su tarea se ha creado con éxito. ✓✓✓")
        print()
        with open(Lf_ruta_file, "a") as archivo:
            archivo.write(f"{','.join(nueva_tarea)}\n")
    else:
        # La tarea se está repitiendo
        print("La tarea ya existe en la lista.")
        print()
    menu_principal()

def marcar_tarea():

    if not Lista_tarea:
        print("Lo sentimos, no podemos ejecutar este procedimiento.")
        print("La lista se encuentra vacía.")
        error()
        print()
    else:
        print("Ingrese el número de la tarea que desea marcar como completada:")
        Ln_num_tarea_completada = int(input())

        if Ln_num_tarea_completada <= 0 or Ln_num_tarea_completada > len(Lista_tarea):
            print("Se ha seleccionado mal el dato, por favor inténtelo de nuevo.")
            error()
            print()
        else:
            new_tarea = Lista_tarea[Ln_num_tarea_completada - 1]

            if new_tarea[2] == 'True':
                print("✓✓✓ La tarea ya se encuentra completada. ✓✓✓")
                print()
            else:
                tarea_temporal = [new_tarea[0], new_tarea[1], "True"]
                Lista_tarea[Ln_num_tarea_completada - 1] = tarea_temporal
                print("¡¡¡Felicidades!!! Has completado la tarea:")
                print(f"tarea completada=> {new_tarea[0]}")
                visto_bueno()
                print()
                # Crear un nuevo archivo txt temporal
                with open('temporal.txt', "w+") as archivo_temporal:
                    # Escribir los datos en el archivo temporal
                    for tarea in Lista_tarea:
                        archivo_temporal.write(f"{','.join(tarea)}\n")

                # Mover el archivo temporal a su ubicación final
                shutil.move('temporal.txt', 'lista_tarea.txt')
        menu_principal()

def imprimir_tarea():
    if not Lista_tarea:
        print("Lo sentimos, no hay tareas que se puedan mostrar.")
        error()
        print()
    else:
        ln_indi = 0
        for lista in Lista_tarea:
            if len(lista) >= 3 and lista[2] == "True":
                lv_estado = "Completo"
            else:
                lv_estado = "Pendiente"
            fecha = lista[1]
            try:
                nueva_fecha = time.strftime("%d/%m/%Y", time.strptime(fecha, "%Y-%m-%d"))
            except ValueError:
                nueva_fecha = "Fecha inválida"
            print()
            print("{:>2} {:>20} {:>10} {:>10}".format(ln_indi + 1, lista[0], nueva_fecha, lv_estado))
            print()
            ln_indi += 1

    menu_principal()


def eliminar_tarea():
    if not Lista_tarea:
        print("Lo sentimos, no podemos ejecutar este procedimiento.")
        print("La lista se encuentra vacía.")
        error()
        print()
    else:
        print("Ingrese el número de la tarea que desea eliminar:")
        Ln_num_eliminar = int(input())

        if Ln_num_eliminar <= 0 or Ln_num_eliminar > len(Lista_tarea):
            print("Se ha seleccionado mal el dato, por favor inténtelo de nuevo.")
            error()
            print()
        else:
            tarea_eliminada = Lista_tarea.pop(Ln_num_eliminar - 1)
            print("Se ha eliminado la siguiente tarea:")
            print(f"Tarea eliminada: {tarea_eliminada[0]}")

            with open(Lf_ruta_file, "w") as archivo:
                for tarea in Lista_tarea:
                    archivo.write(f"{','.join(tarea)}\n")
            print("✓✓✓✓✓✓✓✓✓")
            print("La tarea ha sido eliminada correctamente.")
            print("✓✓✓✓✓✓✓✓✓")
            print()

    menu_principal()

def menu_principal():
    print()
    print("     LISTA DE TAREAS     ")
    print("¿Qué desea realizar?")
    print("1 - Marcar tarea como completada")
    print("2 - Agregar nueva tarea")
    print("3 - Ver lista de tareas")
    print("4 - Eliminar tarea")
    print("5 - Salir")
    Ln_respuesta = int(input("---"))

    if Ln_respuesta == 1:
        # Marcar tarea como completada

        marcar_tarea()
    elif Ln_respuesta == 2:
        # Agregar nueva tarea
        agregar_nueva_tarea()
    elif Ln_respuesta == 3:
        # Ver lista de tareas
        imprimir_tarea()
    elif Ln_respuesta == 4:
        # Eliminar tarea
        eliminar_tarea()
    elif Ln_respuesta == 5:
        # Finalizar el programa
        print("Agradecemos su participación, vuelva pronto.")
        print("Finalizando programa.... =)")
        sys.exit()
    else:
        print("La opción que ingresó no es válida")
        error()

# Creación de la lista de tareas
Lista_tarea = []

# Obtención de la ruta del directorio actual del script
directorio_actual = Path.cwd()
Nombre_archivo = "lista_tarea.txt"
Lf_ruta_file = directorio_actual / Nombre_archivo

# Verificar si el archivo existe
Lb_existe = Lf_ruta_file.exists()
print(Lb_existe)

if Lb_existe:
    modo = "r"
else:
    modo = "a+"

with open(Lf_ruta_file, modo) as archivo:
    for linea in archivo:
        # Convertimos la línea en una lista
        tarea = linea.strip().split(',')
        # Agregamos la tarea a la lista
        Lista_tarea.append(tarea)


menu_principal()
