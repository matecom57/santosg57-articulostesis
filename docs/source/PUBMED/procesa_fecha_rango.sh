#!/bin/bash

mes=4

dia=7
 
yy=26

filo="fecha_rango_M"${mes}"D"${dia}"y"${yy}
echo $filo

python fecha_rango.py $mes $dia $yy > ${filo}".txt"

filt=${filo}"_titulos" 
cat ${filo}".txt" | grep \"title\": > ${filt}".txt" 



