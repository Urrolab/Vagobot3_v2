import os, re, pandas as pd, subprocess, glob, openpyxl, csv
from os import path, remove
from colorama import Fore, Style
from openpyxl.styles import Alignment
from openpyxl import load_workbook


####################################### VagobotBeta.Py ##########################################
#################################################################################################
#### NUEVA VERSION DEL SCRIPT "Vagobot.py" ESTA NUEVA VERSION INTEGRA LAS SIGUIENTES FUNCIONES: #
#### *- MENU INTERACTIVO                                                                        #
#### *- VERIFICADOR DE ESCRITURA PARA UBICAR ConcatDir                                          #
#### *- DEPURADOR                                                                               #
#### *- Y UNA MEJOR SINTAXIS EN EL CODIGO DEL SCRIPT PARA LECTURA HUMANA.                       #
#################################################################################################

os.system('clear') # Limpiador

# VARIABLES GLOBALES --------------------------------------------------------------------------------------------------------------------
DirectorioRaiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/Vagobot3_v2/"
print(Fore.MAGENTA + f'Inicializando en: {DirectorioRaiz}\n' + Style.RESET_ALL)

# DEPURACION VERIFICA QUE NO EXISTAN ConcatDir BASURA ------------------------------------------------------------------------------------
def Depuracion():
    while True:
        try:
            print(Fore.YELLOW + 'Ejecutando depuracion' + Style.RESET_ALL)
            print()
            ConcatDir = glob.glob(f'{DirectorioRaiz}temp/concat/*'
            ) or glob.glob(f'{DirectorioRaiz}temp/usuarios/*'
            ) or glob.glob(f'{DirectorioRaiz}/edit*'
            ) or glob.glob(f'{DirectorioRaiz}/*.html')
            if ConcatDir:
                print(Fore.YELLOW + '¡CUIDADO!' + Style.RESET_ALL ,'La depuracion encontro archivos basuras, se recomienda depuración\n')
                print('Ejecutar depuracion?\n')
                Opc = str(input(Fore.CYAN + "Si / No: " + Style.RESET_ALL))
                if Opc == 'Si':
                    print(Fore.YELLOW + 'Removiendo archivos basura\n' + Style.RESET_ALL)
                    for Basura in ConcatDir:
                        remove(Basura)
                else:
                    print(Fore.YELLOW + 'Saliendo\n' + Style.RESET_ALL)
            else:
                print(Fore.GREEN + '¡PERFECTO!' + Style.RESET_ALL, 'No se encontraron archivos basuras')
                print()
                print(Fore.YELLOW + 'Ejecutando Menu\n' + Style.RESET_ALL)
            break
        except PermissionError:
            print(Fore.RED + '¡ERROR!' + Style.RESET_ALL, 'No se ejecuto el Script como Administrador/Root\n')
Depuracion()

# FUNCIONES DEL MENU --------------------------------------------------------------------------------------------------------------------
def MostrarMenu(Opciones):
    print(Fore.YELLOW + 'Seleccione una opcion: \n' + Style.RESET_ALL)
    for Clave in sorted(Opciones):
        print(f' {Clave}) {Opciones[Clave][0]}')

# VALIDADOR DE OPCIONES DEL MENU --------------------------------------------------------------------------------------------------------
def LeerOpcion(Opciones):
    while (a := input(Fore.CYAN + 'Opcion: ' + Style.RESET_ALL)) not in Opciones:
        print(Fore.RED + 'Opcion incorrecta, vuelva a intentarlo. \n' + Style.RESET_ALL)
    return a

# EJECUCION DE LA OPCION ----------------------------------------------------------------------------------------------------------------
def EjecutarOpcion(Opcion, Opciones):    Opciones[Opcion][1]()

# BUCLE PARA EL MENU --------------------------------------------------------------------------------------------------------------------
def GenerarMenu(Opciones, OpcionSalida):
    Opcion = None
    while Opcion != OpcionSalida:
        MostrarMenu(Opciones)
        Opcion = LeerOpcion(Opciones)
        EjecutarOpcion(Opcion, Opciones)
        print()

# ARRAY DEL MENU Y VISUALIZACIÓN --------------------------------------------------------------------------------------------------------
def MenuPrincipal():
    Opciones = {
        '1': ('Ingresar archivo', Opcion1),
        '2': ('Ejecutar Script', Opcion2),
        '3': ('Salir\n', salir),
    }

    GenerarMenu(Opciones, '3')

#### COMIENZO DEL DESARROLLO DE CADA OPCION DEL MENU ####

# FUNCION DE LA PRIMERA OPCION DEL MENU -------------------------------------------------------------------------------------------------
def Opcion1():
    print()
    Valido = False
    print(Fore.YELLOW + 'Visualizando carpeta\n' + Style.RESET_ALL)
    NapList = glob.glob(f'{DirectorioRaiz}Contenedor_CSV/*')
    for Nap in NapList:
        print(Nap.replace(f'{DirectorioRaiz}Contenedor_CSV/', ''))
    print()
    print(Fore.YELLOW + 'Ingrese un archivo: ' + Style.RESET_ALL , end='')

# BUCLE PARA VERIFICAR SINTAXIS ---------------------------------------------------------------------------------------------------------
    def Validar(NapNombre): # Funcion anidada sobre Opcion1()
        Patron = '^NAP'
        Resultado = re.search(Patron, NapNombre)
        return Resultado
   
    while not Valido:
        global NapCsv # Variable global de la ubicacion del archivo .csv
        global NapNombre # Variable glolal del nombre del archivo .csv

        NapNombre = input()
        Valido = Validar(NapNombre)
        if not Valido:
            print(Fore.RED + 'Formato incorrecto, ingrese de nuevo: ' + Style.RESET_ALL , end='')
    print(Fore.YELLOW + f'Verificando archivo {NapNombre}' + Style.RESET_ALL , "\n")

    NapCsv = DirectorioRaiz + 'Contenedor_CSV/' + NapNombre + ".csv"
    NapCsvBool = (path.exists(NapCsv))

    if NapCsvBool == True: # Este condicional verifica que el archivo exista realmente.
        print(Fore.GREEN + "¡PERFECTO!" + Style.RESET_ALL , "Archivo cargado, ejecute el Script para", Fore.MAGENTA + NapNombre + ".csv\n" + Style.RESET_ALL)
    else:
        print(Fore.RED + "¡ERROR!" + Style.RESET_ALL , "No existe" + NapCsv + "\n")
        Opcion1()

# MODULO DE PANDAS -----------------------------------------------------------------------------------------------------------------------
def Opcion2():
    print()
    while True:
        try:
            print("Se va a ejecutar un cut a ", Fore.MAGENTA + NapNombre + Style.RESET_ALL + "\n")

            CsvData = pd.read_csv(NapCsv)
            CsvData_drop = CsvData.drop(["Nombre y Apellido", "Nro. Cliente"], axis=1)
            CsvData_sort = CsvData_drop.sort_values(['Usuario Internet'], ascending=True)
            CsvData_index = CsvData_sort.set_index('Nro. Telefono')
            CsvData_index.to_csv('edit' + NapNombre)

            print(Fore.YELLOW + "Pasando archivo cortado a autoArrayxtreme.sh \n" + Style.RESET_ALL)
            print(Fore.YELLOW + "Ejecutando autoArrayxtreme.sh \n" + Style.RESET_ALL)

            subprocess.call(f'{DirectorioRaiz}Vagobot_CORE/autoArrayxtreme.sh' ) # Se ejecuta el Script en BASH para generar el array.txt
            subprocess.call(f'{DirectorioRaiz}Vagobot_CORE/WebScrapping.sh')
            subprocess.call(f'{DirectorioRaiz}Vagobot_CORE/Concatenador.sh')

            with open(DirectorioRaiz + "temp/concat/ProcesoFINAL.csv") as f:
                reader = csv.reader(f)
                next(f)
                for row in reader:
                    print(
                        Fore.YELLOW + "Cargando la siguiente información: ", Fore.CYAN + "NUMERO: {0}, USUARIO: {1}, NAP: {2}, PUERTO: {3}, ESTADO: {4}, PPOE: {5}, OLT: {6}, VLAN: {7}, SHELF: {8}, PLACA: {9}, PUERTO: {10}, ONU: {11}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11] + Style.RESET_ALL) # VISUALIZADOR DE ARCHIVOS CARGADOS AL .CSV
                        )
            convert = pd.read_csv(DirectorioRaiz + "temp/concat/ProcesoFINAL.csv")
            convert.to_excel('ExcelLectura.xlsx', sheet_name='Reporte')
        
            wb = load_workbook('ExcelLectura.xlsx')
            pestaña = wb['Reporte']
        
            pestaña['A1'] = 'INDEX'
            pestaña['A1'].style = 'Headline 2'
            pestaña.column_dimensions['A'].width = 10
            pestaña['A1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['B1'] = 'NRO. TELEFONO'
            pestaña['B1'].style = 'Headline 2'
            pestaña.column_dimensions['B'].width = 18
            pestaña['B1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['C1'] = 'USUARIO'
            pestaña['C1'].style = 'Headline 2'
            pestaña.column_dimensions['C'].width = 17
            pestaña['C1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['D1'] = 'NAP'
            pestaña['D1'].style = 'Headline 2'
            pestaña.column_dimensions['D'].width = 25
            pestaña['D1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['E1'] = 'PUERTO'
            pestaña['E1'].style = 'Headline 2'
            pestaña.column_dimensions['E'].width = 9.5
            pestaña['E1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['F1'] = 'PPOE'
            pestaña['F1'].style = 'Headline 2'
            pestaña.column_dimensions['F'].width = 15
            pestaña['F1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['G1'] = 'ESTADO'
            pestaña['G1'].style = 'Headline 2'
            pestaña.column_dimensions['G'].width = 17
            pestaña['G1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['H1'] = 'OLT'
            pestaña['H1'].style = 'Headline 2'
            pestaña.column_dimensions['H'].width = 25
            pestaña['H1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['I1'] = 'VLAN'
            pestaña['I1'].style = 'Headline 2'
            pestaña.column_dimensions['I'].width = 10
            pestaña['I1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['J1'] = 'SHELF'
            pestaña['J1'].style = 'Headline 2'
            pestaña.column_dimensions['J'].width = 10
            pestaña['J1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['K1'] = 'PLACA'
            pestaña['K1'].style = 'Headline 2'
            pestaña.column_dimensions['K'].width = 10
            pestaña['K1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['L1'] = 'PUERTO'
            pestaña['L1'].style = 'Headline 2'
            pestaña.column_dimensions['L'].width = 10
            pestaña['L1'].alignment = Alignment(horizontal="center", vertical="center")
            pestaña['M1'] = 'ONU'
            pestaña['M1'].style = 'Headline 2'
            pestaña.column_dimensions['M'].width = 10
            pestaña['M1'].alignment = Alignment(horizontal="center", vertical="center")
        
            wb.save('ExcelFinal.xlsx')

            print(Fore.GREEN + 'Se realizo con exito' + Style.RESET_ALL)
        
            remove(DirectorioRaiz + "temp/concat/ProcesoFINAL.csv")
            remove(DirectorioRaiz + "temp/concat/Procesado.csv")
            remove(DirectorioRaiz + "ExcelLectura.xlsx")
            break

        except NameError:
            print(Fore.RED + '¡ERROR!' + Style.RESET_ALL, 'No se definio ningun archivo .csv\n')
            break

def salir():
    print()
    print(Fore.YELLOW + "Saliendo." + Style.RESET_ALL)

if __name__ == '__main__':
    MenuPrincipal()