#!/bin/bash

# Este script concatena los archivos temp/concatorales Desconectado.txt, Conectado.txt y edit*.csv.

nap=$PWD/temp/concat/edit*
cd $PWD/temp/concat
if [ -f $nap ];
    then
    cat $nap | sed '1d' > napcut
    cat Conectados.txt Desconectados.txt Sin_info.txt > Concatenado.txt
    cat Concatenado.txt | sort > ConcatenadoFINAL.csv
    paste -d "," napcut ConcatenadoFINAL.csv > Procesado.csv
    cat Procesado.csv | sed "1s/^/,,,,,,,,,,,\n/" > ProcesoFINAL.csv
    #rm -r Concatenado.txt
    #rm -r napcut
    #rm -r Conectados.txt
    #rm -r Desconectados.txt
    #rm -r Sin_info.txt
    #rm -r ConcatenadoFINAL.csv

    else
    echo "ERROR no se encontre el archivo edit*.csv para concatenar."
fi
rm $nap

