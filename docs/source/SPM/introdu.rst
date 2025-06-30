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


