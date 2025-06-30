Tutorial de SPM n.° 1: Descarga de datos
=====================================

.. _SPM_01_Descarga de datos:

=====================================
Tutorial de SPM n.° 1: Descarga de datos
=====================================

---------------

Descripción general
--------

En este curso, analizaremos un conjunto de datos de fMRI que utilizó la tarea Flanker. El conjunto de datos se puede encontrar 
aquí <https://openneuro.org/datasets/ds000102/versions/00001> en el sitio web OpenNeuro <https://openneuro.org>, un repositorio en 
línea de datos de neuroimagen.


.. figura:: OpenNeuro_Flanker.png

    La página de OpenNeuro para el conjunto de datos Flanker incluye un árbol de archivos del conjunto de datos, que incluye las 
carpetas «anat» (que contiene la imagen anatómica) y «func» (que contiene las imágenes funcionales y las horas de inicio de cada 
ejecución). Hay archivos adicionales que contienen datos del sujeto, como sexo y edad («participants.tsv») y parámetros de escaneo 
(«task-flanker_bold.json»). Estos datos están en un formato llamado BIDS (Estructura de Datos de Imágenes Cerebrales). Un árbol de 
directorios estandarizado como este facilita enormemente la creación de scripts, como veremos en un tutorial posterior.
    
    
Descargue el conjunto de datos haciendo clic en el botón "Descargar" en la parte superior de la página. El conjunto de datos ocupa 
aproximadamente 2 GB y viene en una carpeta comprimida. Extráigalo haciendo doble clic en la carpeta.

.. figura:: OpenNeuro_DownloadButton.png


Después de haber descargado y descomprimido el conjunto de datos, haga clic en el botón Siguiente para obtener una descripción 
general de la tarea experimental utilizada en este estudio.

Opciones de descarga alternativas
****************************

Si el botón de descarga no funciona, prueba la opción `Amazon Web Services (AWS) <https://aws.amazon.com/>`__. Ve a `esta página 
<https://aws.amazon.com/cli/>`__ y descarga el cliente de AWS adecuado para tu sistema operativo. Una vez instalado, abre una 
terminal, ve al escritorio y escribe lo siguiente:

::

    sincronización de aws s3: sin solicitud de firma s3://openneuro.org/ds000102 ds000102-download/

La descarga debería tardar aproximadamente media hora.


Video
*****

Para ver un videotutorial sobre cómo descargar los datos, haz clic aquí: <https://www.youtube.com/watch?v=4Y0LfKNj8Ns>. (El video 
se titula "Tutorial AFNI n.° 1", pero como es básicamente lo mismo que harás para SPM, he decidido usar el mismo video para ambos 
tutoriales).


