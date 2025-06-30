Descripción general de SPM
==========================

¿Qué es SPM?

SPM (Mapeo Paramétrico Estadístico) es un paquete de software de análisis fMRI que se ejecuta en Matlab . Además del análisis 
fMRI, SPM incluye herramientas para realizar morfometría basada en volumen y conectividad efectiva.

../_images/spm12_logo.png

Los siguientes tutoriales le mostrarán cómo analizar un conjunto de datos de muestra con SPM. Comenzará aprendiendo los 
fundamentos del preprocesamiento de fMRI y luego creará un modelo estadístico para estimar la actividad cerebral en respuesta a 
diferentes condiciones. Tras aprender sobre los resultados a nivel de grupo y cómo programar su análisis, finalizaremos 
aprendiendo sobre los diferentes tipos de análisis de grupo y cómo realizar análisis de región de interés (ROI).

Análisis de principio a fin con SPM

* Introducción a SPM
* Tutorial de SPM n.° 1: Descarga de datos
* Tutorial de SPM n.° 2: La tarea de flanqueo
* Tutorial de SPM n.º 3: Análisis de los datos
* Tutorial de SPM n.° 4: Preprocesamiento
* Tutorial de SPM n.° 5: Estadísticas y modelado
* Tutorial de SPM n.° 6: Creación de scripts
* Tutorial de SPM n.° 7: Establecer el origen
* Tutorial de SPM n.° 8: Análisis de grupo
* SPM Intermezzo: Cajas de herramientas
* Tutorial de SPM n.° 9: Análisis del ROI
* Apéndice A: Resumen estadístico
* Apéndice B: Interacciones psicofisiológicas (PPI) en SPM
* Apéndice C: Modulación paramétrica
* Apéndice D: Optimización del diseño

.. _SPM_fMRI_Introducción:

===================
Introducción a SPM
===================

------------

Este curso te mostrará cómo analizar un conjunto de datos de fMRI de principio a fin. Comenzaremos **descargando un conjunto de 
datos de muestra** e inspeccionando las imágenes anatómicas y funcionales de cada sujeto. A continuación, **preprocesaremos los 
datos**, lo que elimina el ruido y mejora la señal en las imágenes. Una vez preprocesadas las imágenes, crearemos un modelo que 
represente cómo creemos que debería verse la señal BOLD <BOLD_Response>`, una medida de la actividad neuronal, en nuestras 
imágenes. Durante el **ajuste del modelo**, comparamos este modelo con la señal en diferentes áreas de la imagen. Este ajuste del 
modelo mide la intensidad de la señal en diferentes condiciones; por ejemplo, podemos tomar la diferencia de la señal entre las 
condiciones A y B del experimento para ver qué condición produce una respuesta BOLD mayor.

Una vez creado un modelo para cada sujeto y estimada la respuesta BOLD para cada condición, podemos realizar cualquier tipo de 
análisis de grupo: pruebas t pareadas, pruebas t intergrupales, interacciones, etc. El objetivo de este curso es calcular un 
contraste intrasujeto simple entre dos condiciones y comprobar su significancia entre sujetos. También aprenderá a crear figuras 
que muestren análisis de cerebro completo, similares a las publicadas en revistas de neuroimagen, y a realizar un análisis de 
región de interés (ROI).

Este curso está diseñado para desarrollar su confianza al trabajar con datos de fMRI, mejorar su dominio de los términos básicos 
del análisis de fMRI y ayudarle a tomar decisiones informadas en cada paso. Algunos capítulos incluyen ejercicios para ayudarle a 
practicar lo aprendido y prepararle para el siguiente capítulo. Una vez que domine los fundamentos de este curso, podrá aplicarlos 
a otros conjuntos de datos de su elección.


Descarga e instalación de SPM
******************************

A diferencia de AFNI o FSL, SPM puede ejecutarse en cualquier sistema operativo siempre que tenga Matlab instalado. Matlab es un 
software propietario bastante caro, pero si eres estudiante o empleado universitario, puedes obtener una copia gratuita. Una vez 
instalado Matlab, el sitio web de SPM <https://www.fil.ion.ucl.ac.uk/spm/software/spm12/>`__ contiene instrucciones sobre cómo 
instalar el paquete de software. Haz clic en el botón "Descargar formulario" para completar algunos datos personales, como tu 
puesto y el uso que le darás al software, lo que te permitirá descargarlo.

Una vez descargado el paquete SPM, colóquelo en su directorio personal. Abra Matlab, haga clic en la pestaña "Inicio" y luego en 
el botón "Establecer ruta". Seleccione el directorio "spm12" y haga clic en "Agregar con subcarpetas". Haga clic en el botón 
"Guardar" para asegurarse de que la ruta se configure cada vez que abra Matlab y cierre la ventana.

.. figura:: SPM_SetPath.png

Después de haber establecido la ruta, escriba lo siguiente desde la terminal de Matlab:

::

  spm
  
Lo cual abrirá la siguiente ventana:

.. figura::Tipo_SPM.png

Haga clic en el botón fMRI para abrir la GUI de fMRI de SPM.

.. nota::

  Suponiendo que solo está utilizando la parte fMRI del paquete SPM, puede escribir ``spm fmri`` desde la línea de comando para 
abrir la GUI de análisis fMRI.
  
Ya está listo para descargar el conjunto de datos Flanker, al que nos referiremos ahora.

.. nota::
    Este curso no profundizará en la física de la resonancia magnética. Para una revisión de este tema, recomiendo los capítulos 1 
a 5 del libro *Functional Magnetic Resonance Imaging*, de Huettel, Song y McCarthy (3.ª edición). Consulte también el excelente 
sitio web de Allen Elster, "MRI Questions <http://mriquestions.com/index.html>`__, para obtener ejemplos útiles de conceptos de 
resonancia magnética.


Video
******

Para obtener una descripción general de SPM y cómo descargarlo e instalarlo, consulte este video 
<https://www.youtube.com/watch?v=qbcBLXJhzZg>`__.

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

.. _SPM_02_Flanquero:

=================================
Tutorial de SPM n.° 2: La tarea de flanqueo
=================================

------------------

El conjunto de datos que descargaste utiliza la tarea Flanker, diseñada para aprovechar un proceso mental conocido como control 
cognitivo. En este curso, definiremos el control cognitivo como la capacidad de ignorar estímulos irrelevantes para realizar una 
tarea correctamente.

En la tarea Flanker, las flechas apuntan a la izquierda o a la derecha, y se le indica al sujeto que presione uno de los dos 
botones que indican la dirección de la flecha central. Si apunta a la izquierda, el sujeto presiona el botón "izquierda"; si 
apunta a la derecha, el botón "derecha". La flecha central está flanqueada por otras flechas que apuntan en la misma dirección o 
en la dirección opuesta.

.. figura:: 02_Flanker_Example.png

	Un ejemplo de las dos condiciones de la tarea Flanker. En la condición Incongruente, la flecha central (en la que se 
centra el sujeto) apunta en dirección opuesta a las flechas flanqueantes; en la condición Congruente, la flecha central apunta en 
la misma dirección que las flechas flanqueantes. En este ejemplo, la respuesta correcta en la condición Incongruente sería pulsar 
el botón "izquierda", y la respuesta correcta en la condición Congruente sería pulsar el botón "derecha". Para realizar una 
versión de la tarea Flanker, haga clic aquí <http://cognitivefun.net/test/6>.

Como puede imaginar, la tarea es más sencilla si la flecha central apunta en la misma dirección que la flecha lateral, y más 
difícil si apunta en la dirección opuesta. Llamaremos a la primera condición "Congruente" y a la segunda "Incongruente". Los 
sujetos suelen ser más lentos y menos precisos en la condición Incongruente, y más rápidos y precisos en la condición Congruente. 
Dado que la diferencia en los tiempos de reacción es robusta y fiable, en nuestros datos de fMRI también deberíamos observar una 
diferencia notable en la señal :ref:`BOLD <BOLD_Response>`.

.. figura:: 02_Flanker_Design.png

Ilustración de la tarea de Flanker para este estudio, adaptada de Kelly et al. (2008). Se muestra al sujeto una cruz de fijación 
para que enfoque el centro de la pantalla, y luego se presenta una prueba de Flanker congruente o incongruente durante 2000 ms. 
Durante la prueba, el sujeto presiona el botón izquierdo o derecho. A continuación, se produce un intervalo de fluctuación que 
dura entre 8000 ms y 14 000 ms. (Tenga en cuenta que los intervalos de fluctuación suelen aumentar en segundos; en este caso, la 
fluctuación para una prueba dada sería una selección aleatoria de uno de los siguientes: 8000 ms, 9000 ms, 10 000 ms, 11 000 ms, 
12 000 ms, 13 000 ms y 14 000 ms). Se presenta otra cruz de fijación para comenzar la siguiente prueba.

Nuestro objetivo es estimar la magnitud de la señal BOLD para cada condición y luego **contrastar** (es decir, tomar la diferencia 
de) las dos condiciones para ver si son significativamente diferentes entre sí.

.. nota::
	Esta descripción de la tarea plantea un punto importante sobre las buenas prácticas para diseñar estudios de fMRI: si 
puede diseñar una tarea conductual que produzca un efecto fuerte y confiable, aumentará sus probabilidades de encontrar un efecto 
en sus datos de imágenes. Los datos de fMRI son notoriamente ruidosos: si no ve un efecto conductual en su estudio, lo más 
probable es que tampoco encuentre un efecto en sus datos de imágenes.

Video
*****

Para ver un video resumen de la tarea Flanker, haga clic aquí <https://www.youtube.com/watch?v=SKuYVFgyWf8>`__. (El título del 
video dice "Tutorial AFNI n.° 2", pero los principios de la tarea Flanker son los mismos independientemente del paquete que use).

https://andysbrainbook.readthedocs.io/en/latest/SPM/SPM_Short_Course/SPM_02_Flanker.html




