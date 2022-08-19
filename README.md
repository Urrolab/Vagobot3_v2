# Vagobot3_v2
# ######### VAGOBOT ##########

# Por favor no modificar ningun archivo o carpeta original del Script ya que el minimo cambio puede generar un error catastrófico y dar a lugar a mi inminente muerte.

# ############ DESCRIPCIÓN ################
# Este Script consta de 3 directorios  y 3 archivos

# ## README.md ##
# Es literalmente este mismo archivo noseabolu.

# ## VagobotBeta.py ###
# Es el Script Padre/Maestro escrito en Python3, utiliza librerias como, Pandas, OpenPyxl, Colorama, Glob2 y librerias del sistema como OS, csv y Subprocess, para más información, leer los comentarios dentro del mismo archivo.

# ## Contenedor_CSV ###
# Dentro de esta carpeta se almacenan los .CSV descargados del Smart-GIS, para luego ser leidos por el Script en Python.

# ## temp / usuarios / concat
# Dentro del directorio temp se almacenan archivos temporales y dos carpetas "usuarios" la cual almacena los archivos temporales .html que son eliminados una ves terminan su función dentro del script. "concat" almacena archivos basura generados por el Concatenador.sh.

# ## Vagobot_CORE ###
# En este directorio se almacenan 4archivos: cookies2.txt, autoArrayxtreme.sh, Concatenador.sh, y WebScrapping.sh. Para mas información, leer los comentarios dentro de los mismos archivos.

# ############ INSTRUCCIONES ################

# IMPORTANTE
# El script tiene que ser ejecutado en Python3 ya que la sintaxis que maneja es sobre esa version de Python, si se ejecuta con otra versión va a dar errores de sintaxis.

# REQUISITOS
# 1) Python 3.8 o superior, no funciona en versiones inferiores.

# 2) Se necesitan las siguientes librerias: OpenPyxl, Pandas, Colorama y Glob2.
# /// For dummies ///
# Debian
# sudo python3.x -m pip install Openpyxl
# sudo python3.x -m pip install Pandas
# sudo python3.x -m pip install Colorama
# sudo python3.x -m pip install Glob2

# 3) Se tiene que dar permisos de ejecucion a los scripts en bash dentro del directorio Vagobot_CORE/ y ejecutar VagobotBeta.py como sudo/root/administrador

# 4) No funciona fuera de la red interna de TelViso.

# ERRORES CONOCIDOS
# 1) Si no se ejecuta como administrador:
# 1a) En caso de tener que ejecutar la depuracion, no se realizara ya que se necesita ser root y el programa lo indicara
# 1b) En caso de no ejecutar la depuracion, el programa indicara un error al momento de finalizar el autoArrayxtreme.sh

# 2) Si se ejecuta fuera de la red de interna el programa llega hasta el WebScrapping y queda en loop ya que busca obtener informacion del codigo fuente atraves de CURL con una URL interna.

# 3) Si se carga otro archivo que no sea .csv el programa dara errores de sintaxis.

# COMO USAR
# 1) Se descarga el archivo .csv del Smart-GIS de la intranet
# Dentro del script hay varios .csv de prueba en el directorio Contenedor_CSV/

# 2) Se debe renombrar el archivo descargado por el NAP reemplazando caracteres y espacios con guin bajo ejemplo: NAP 01/02 DV a NAP_01_02_DV.csv. Luego, guardar el archivo en el Contenedor_CSV/

# 3) Ejecutar VagobotBeta.py
# En caso de tener archivos basura en la carpeta /temp el Script ejecutara una depuracion y preguntara al usuario si quiere realizar la depuración siempre y cuando no hayan archivos que querramos analizar, es altamente necesaria la depuracion para un nuevo Excel.

# 4) Ingresar el archivo
# Se debe ejecutar la primera Opción, el Script ya detecta que el archivo NAP o NAPS este dentro del directorio y lo visualiza, simplemente hay que escribir el nombre del archivo exceptuando la extensión .csv

# 5) Ejecutar el Script
# Una vez finalizada la carga del archivo .csv se ejecuta el Script que genera el Excel, el programa es bastante descriptivo a la hora de tener un error, si se siguieron todos los pasos, se tienen todas las dependencia necesarias y se ejecuto como root, no deberia haber ningun inconveniente.

# 6) ExcelFinal.xlsx
# Al final del Script se entrega este archivo, con el excel ya formulado, con toda la información que fuimos recopilando, en este repositorio hay un Excel de prueba para ser analizado.
