#!/bin/bash

# Este script realmente no crea un ARRAY, lo que hace es generar un archivo .txt
# Que mas adelante va a ser usado como ARRAY en el Script de WebScrapping.sh

tput setaf 3; echo 'Verificando archivos'; tput sgr0
echo
Directorio=$PWD/edit*
if [ -f $Directorio ];
    then
    mv $Directorio $PWD/temp/concat/
    tput setaf 2; echo '¡PERFECTO!'; tput sgr0 
    echo -e 'Existe el archivo\n'
    tput setaf 3; echo -e 'Generando array.txt\n'; tput sgr0
    cat $PWD/temp/concat/edit* | cut -s -d ',' -f2 | sed '1d' > array.txt
    mv array.txt $PWD/temp/concat/
    tput setaf 3; echo -e 'Visualizando array.txt\n'; tput sgr0
    tput setaf 5; cat $PWD/temp/concat/array.txt; tput sgr0
    echo

    else
    tput setaf 1; echo '¡ERROR!'; tput sgr0
    echo -e 'No se generó el archivo EditNAP.csv para generar array.txt\n'

fi

# nap=$PWDv2/edit* Es igual a cualquier archivo que empiece con edit
# tput setaf Agrega color al script
# tput sgr0 Indica hasta donde pinta el tput setaf

