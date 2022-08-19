#!/bin/bash

# En este Script se genera el ARRAY atraves del array.txt
# Una vez generado el Array en el Script, se deshecha el archivo.

DIRECTORIO="$PWD"
mapfile -t usuarios < $DIRECTORIO/temp/concat/array.txt

for usuario in "${usuarios[@]}";
    do
    curl --cookie $DIRECTORIO/Vagobot_CORE/cookies2.txt -s http://192.168.5.11/Matrix360/matrix_verhistorial.php?username=$usuario > "$usuario"_temp.html
    mv "$usuario"_temp.html $DIRECTORIO/temp/usuarios
        if grep -q 'Conexion activa' $DIRECTORIO/temp/usuarios/"$usuario"_temp.html;
        #### MODULO DE CONEXIÓN #####
            then
            tput setaf 2; echo "$usuario conectado"; tput sgr0
            cat $DIRECTORIO/temp/usuarios/"$usuario"_temp.html | grep 'Conexion activa' | cut -s -d ">" -f35 | sed 's!</TD!!g' | sed "1s/^/Conectado,/"> $DIRECTORIO/temp/usuarios/"$usuario"_conectado.txt
            tput setaf 3; cat $DIRECTORIO/temp/usuarios/"$usuario"_conectado.txt | sed "1s/^/Ubicacion /"; tput sgr0
            cat $DIRECTORIO/temp/usuarios/"$usuario"_conectado.txt | sed "1s/^/$usuario,/" | sed "s/:/,/g" | sed "s!/!,!g" >> $DIRECTORIO/temp/concat/Conectados.txt
            #rm $DIRECTORIO/temp/usuarios/"$usuario"_temp.html # Comentar esta linea en caso de querer guardar los archivos .html 
            #rm $DIRECTORIO/temp/usuarios/"$usuario"_conectado.txt # Comentar esta linea en caso de querer gaurdar los archivos _conectado.txt

            #### MODULO DE DESCONEXION ####
            else
            tput setaf 1; echo "$usuario desconectado"; tput sgr0
            curl --cookie $DIRECTORIO/Vagobot_CORE/cookies2.txt -s http://192.168.5.11/Matrix360/matrix_verusuario.php?username=$usuario > "$usuario"_temp.html
            mv "$usuario"_temp.html $DIRECTORIO/temp/usuarios
            cat $DIRECTORIO/temp/usuarios/"$usuario"_temp.html | grep OLT | cut -s -d ">" -f9 | sed 's!</TD!!g' | sed "1s/^/Desconectado,/" > $DIRECTORIO/temp/usuarios/"$usuario"_desconectado.txt
            cat $DIRECTORIO/temp/usuarios/"$usuario"_temp.html | grep 'callerid' | cut -s -d '>' -f16 | sed 's!</td!!g' > $DIRECTORIO/temp/usuarios/"$usuario"_sininfo.txt
            tput setaf 3; cat $DIRECTORIO/temp/usuarios/"$usuario"_desconectado.txt | sed "1s/^/Ubicacion /"; tput sgr0
            tput setaf 5; cat $DIRECTORIO/temp/usuarios/"$usuario"_sininfo.txt | sed "1s/^/Sin registro /" | sed 's/conecciones con callerid/posible vinculo o linea suspendida/g'; tput sgr0
            cat $DIRECTORIO/temp/usuarios/"$usuario"_desconectado.txt | sed "1s/^/$usuario,/" | sed "s/:/,/g" | sed "s!/!,!g" >> $DIRECTORIO/temp/concat/Desconectados.txt
            cat $DIRECTORIO/temp/usuarios/"$usuario"_sininfo.txt | sed "1s/^/$usuario,/" | sed 's/conecciones con callerid/Sin registro/g' | sed -e '1s|$|,,,,,,|' >> $DIRECTORIO/temp/concat/Sin_info.txt
            #rm $DIRECTORIO/temp/usuarios/"$usuario"_temp.html # Comentar esta linea en caso de querer guardar los archivos .html
            #rm $DIRECTORIO/temp/usuarios/"$usuario"_desconectado.txt # Comentar esta linea en caso de querer guardar los archivos _desconectado.txt
            #rm $DIRECTORIO/temp/usuarios/"$usuario"_sininfo.txt
        fi
    done
rm $DIRECTORIO/temp/concat/array.txt

# INFO
# Este escript es posiblemente el más complejo de entender, es un Web Scrapping basado en CURL desarrollado por mi mismo
# la funcionalidad de este Script es descargar el codigo fuente de ciertas pestañas de la Matrix
# Primero se establece un bucle sobre el array, el cual es generado gracias a la funcionalidad de mapfile que permite generar un array
# atraves de un archivo de texto, luego pasa a un bucle "For" para validar cada una de esas variables, dentro del bucle se ejecuta una
# condición, si dentro de la primera extracción del codigo fuente se encuentra la palabra clave 'Conexion activa', se ejecuta una condición
# que da a lugar a todo el Web Scrapping para los usuarios conectados, si no, se ejecuta la segunda condición que sustrae la información
# de otra url donde solamente podemos sacar la ubicación de la linea, ya que por descarte ese usuario esta Desconectado.
# al final de cada condicion se eliminan archivos temporales de cada Usuario como _temp y _esconectado/_conectado dejando dos unicos archivos
# Conectados.txt y Desconectados.txt los cuales serán concatenados en la proxima ejecucion del Script.
