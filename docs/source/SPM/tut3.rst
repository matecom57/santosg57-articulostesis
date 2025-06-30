Tutorial de SPM n. 3: Análisis de los datos
====================================

.. _SPM_03_MirandoDatos:

====================================
Tutorial de SPM n.º 3: Análisis de los datos
====================================

----------------

Descripción general: la interfaz gráfica de usuario de SPM
*******************************************

Ahora que ha descargado el conjunto de datos, querrá **mirar sus datos**; por ejemplo, querrá saber si hay algún artefacto o 
problema con sus datos y si estos pueden solucionarse con :ref:`preprocessing <SPM_04_Preprocessing>`.

Primero, renombremos el conjunto de datos con un nombre claro e informativo. Si el conjunto de datos se ha descargado en el 
directorio de Descargas, use la terminal de Matlab para navegar al Escritorio y escriba lo siguiente:

::

    movefile('~/Descargas/ds000102_0001/', 'Flanker')
    
Esto cambiará el nombre de la carpeta a «Flanker» y la colocará en su escritorio.


    
    
Como se vio en la página anterior de descarga de datos <SPM_01_DataDownload>, el conjunto de datos tiene una estructura 
estandarizada: cada carpeta de sujeto contiene un directorio anatómico y un directorio funcional denominados ``anat`` y ``func``, 
que a su vez contienen las imágenes anatómicas y funcionales recopiladas durante el experimento. (El directorio ``func`` también 
contiene las **horas de inicio**, o marcas de tiempo que indican cuándo el sujeto se sometió a una prueba congruente o 
incongruente). Este formato se conoce como `BIDS <http://bids.neuroimaging.io/>`__, o Estructura de Datos de Imágenes Cerebrales, 
y facilita la organización y el análisis de los datos.


.. figura:: 03_Flanker_DataStructure.png

    Ejemplo del formato BIDS. Tenga en cuenta que el directorio ``func`` contiene datos funcionales (en este caso, dos ejecuciones 
de datos funcionales) y los archivos "events.tsv" correspondientes, que contienen **onsets**, o marcas de tiempo de qué condición 
se produjo y a qué hora. Puede abrirlos como archivo de texto o como hoja de cálculo. Los usaremos más adelante al crear nuestro 
Modelo Lineal General.
    
Para ver e inspeccionar los datos, utilizaremos la **Interfaz Gráfica de Usuario SPM**, o GUI. Puede abrir la GUI abriendo una 
nueva terminal de Matlab, escribiendo ``spm fmri`` desde la línea de comandos y presionando Enter.



--------

Inspección de la imagen anatómica
*******************************
    
Siempre que descargue datos de imágenes, revise las imágenes anatómicas y funcionales para detectar cualquier **artefacto**: picos 
en el escáner, orientación incorrecta, contraste deficiente, etc. Tomará tiempo acostumbrarse a estos problemas, pero con la 
práctica será más rápido y fácil.

Para empezar, veamos la imagen anatómica en la carpeta "anat" para "sub-08". Si aún no ha abierto SPM, navegue a la carpeta sub-08 
y escriba

::

    resonancia magnética funcional spm
    
Presione Enter para abrir la interfaz gráfica de usuario de SPM. Si hace clic en el botón "Mostrar", se le pedirá que seleccione 
una imagen.

.. nota::

  SPM puede leer cualquier imagen que esté en formato NIFTI, pero no se pueden comprimir; es decir, si los conjuntos de datos 
terminan con una extensión ``.gz``, primero deberá descomprimirlos navegando al directorio que contiene las imágenes y luego 
escribir

  ::

    gunzip('*.gz')
    
  Lo cual expandirá las imágenes y eliminará la extensión ".gz".


.. figura:: 03_Inspección_Anatómica.png

    La imagen anatómica mostrada en el visor SPM en vistas axial, sagital y coronal. Puede cerrar cualquiera de las ventanas si 
solo desea centrarse en un subconjunto de las vistas.
    
   
Inspeccione la imagen haciendo clic en una de las ventanas de visualización. Observe cómo cambian las demás ventanas y la cruceta. 
Esto se debe a que los datos de resonancia magnética se recopilan como una imagen tridimensional, y al desplazarse por una de las 
dimensiones, también cambian las demás ventanas.

.. nota::

    Quizás haya notado que a este sujeto parece faltarle el rostro. Esto se debe a que los datos de OpenNeuro.org han sido 
**desidentificados**: No solo se ha eliminado del encabezado información como el nombre y la fecha del escaneo, sino que también 
se han borrado los rostros. Esto se hace para garantizar el anonimato del sujeto.
    

A medida que continúe inspeccionando la imagen, hay dos cosas que debe tener en cuenta:

1. Líneas que parecen ondas en un estanque. Estas ondas pueden deberse a que el sujeto se mueve demasiado durante el escaneo y, si 
son lo suficientemente grandes, pueden provocar fallos en los pasos de preprocesamiento, como la extracción cerebral o la 
normalización.

.. figura:: 03_Gibbs.png

    Crédito de la foto: Sundar Amartur


2. Diferencias anormales de intensidad en la sustancia gris o blanca. Estas pueden indicar patologías como aneurismas o 
cavernomas, y deben reportarse a su radiólogo de inmediato. Asegúrese de familiarizarse con los protocolos de su laboratorio para 
reportar artefactos. Para ver una galería de patologías que puede observar en una imagen de resonancia magnética, haga clic aquí 
<http://www.mrishark.com/brain1.html>.

----------

Inspección de las imágenes funcionales
********************************
    
Cuando haya terminado de ver la imagen anatómica, haga clic nuevamente en el botón "Mostrar", navegue hasta el directorio "func" y 
seleccione la imagen funcional "run-1".

Se mostrará una nueva imagen en las ventanas de visualización ortogonales. Esta imagen también se asemeja a un cerebro, pero no 
está tan claramente definida como la imagen anatómica. Esto se debe a que la **resolución** es menor. Es habitual que un estudio 
recopile una imagen ponderada en T1 de alta resolución (es decir, anatómica) e imágenes funcionales de menor resolución, que, en 
parte, tienen una resolución menor debido a su rápida obtención. Una de las disyuntivas en la investigación con imágenes es la que 
existe entre la resolución espacial y la resolución temporal: las imágenes obtenidas con mayor resolución temporal tendrán menor 
resolución espacial, y viceversa.

.. figura:: 03_Inspección_Funcional.png


Muchos de los controles de calidad de la imagen funcional son los mismos que los de la imagen anatómica: Preste atención a las 
manchas extremadamente brillantes o extremadamente oscuras en la materia gris o blanca, así como a las distorsiones de la imagen, 
como estiramientos o deformaciones anormales. Un lugar donde es común observar una ligera distorsión es en la región orbitofrontal 
del cerebro, justo encima de los globos oculares. Hay maneras de «reducir esta distorsión 
<https://andysbrainbook.readthedocs.io/en/latest/FrequentlyAskedQuestions/FrequentlyAskedQuestions.html#how-can-i-unwarp-my-data>», 
pero por ahora la ignoraremos.

.. Consulte el glosario de series de tiempo

Otra comprobación de calidad consiste en asegurar que no haya movimiento excesivo. Las imágenes funcionales suelen recopilarse 
como series temporales; es decir, se concatenan varios volúmenes en un único conjunto de datos. Para ver las series temporales de 
volúmenes en rápida sucesión, haga clic en el botón "Check Reg" y cargue los datos "sub-01_task-flanker_run-1_bold.nii". Esto 
mostrará un único volumen en tres planos: coronal, sagital y axial. Haga clic con el botón derecho en cualquiera de los planos y 
haga clic en el botón "Browse". Se le pedirá que seleccione una imagen; haga clic en el archivo seleccionado para eliminarlo e 
introduzca la cadena "run-1" en el campo "Filtro" y "1:146" en el campo "Fotogramas". Seleccione todas las imágenes resultantes y 
haga clic en "Listo".

Ahora verá una barra de desplazamiento horizontal en la parte inferior de la ventana. Al hacer clic en las flechas derecha o 
izquierda, avanzará o retrocederá un volumen; también puede hacer clic y arrastrar la barra de desplazamiento para ver los 
volúmenes más rápidamente. Al hacer clic en el botón ``>`` en la esquina inferior derecha, se iniciará el **modo película**, que 
recorre los volúmenes rápidamente. Al hacer clic de nuevo, se detendrá la película. Para ver un gráfico de la activación de la 
serie temporal en el vóxel bajo la cruceta, haga clic derecho de nuevo en cualquiera de los planos, seleccione "Explorar" y luego 
"Perfil de visualización". Esto abrirá otra figura que puede ver simultáneamente mientras recorre los volúmenes.

.. figura:: 03_SPM_ViewTimeSeries.gif

Además, durante el paso de preprocesamiento de realineación <01_SPM_Realign_Unwarp>, se generará un archivo de parámetros de 
movimiento que muestra el movimiento entre cada volumen. Para comenzar a aprender sobre los pasos de preprocesamiento, haga clic 
en el botón "Siguiente".


--------

Ceremonias
*********

1. Observe la serie temporal de los datos de la "serie 2" para "sub-08", siguiendo los pasos descritos anteriormente. ¿Observa 
algún cambio repentino en el movimiento? Observe la serie temporal de la "serie 1" y compárela con la de la "serie 2". ¿Qué 
volúmenes, si los hay, muestran cambios repentinos en el movimiento?

2. Examine algunas de las demás exploraciones anatómicas y funcionales de otros sujetos, asegurándose de descomprimir las imágenes 
antes de cargarlas en el visor. ¿Cómo cambian el contraste y el brillo al arrastrar la cruz por diferentes secciones de la imagen? 
¿Qué cree que afecta el brillo de una sección determinada?

3. Si está visualizando una de las imágenes funcionales con el botón "Mostrar", al hacer clic derecho en cualquiera de los paneles 
de visualización, se mostrará un menú con el nombre del archivo actual en la parte superior. Coloque el cursor sobre el nombre del 
archivo y observe los valores que se presentan en un submenú a la derecha. ¿Cómo se comparan con los valores que ve en la mitad 
inferior de la ventana de visualización?

4. SPM lee la **información del encabezado** al cargar un archivo. La versión de línea de comandos se llama ``spm_vol``. Desde la 
terminal de Matlab, navegue al directorio ``sub-01/func``, asegúrese de que los datos estén descomprimidos y escriba lo siguiente:

::

    ejecución1 = spm_vol('sub-01_tarea-flanker_ejecución-1_bold.nii')
    
Tenga en cuenta que esta estructura devuelve varios campos, como fname, dim y dt. Puede examinar el contenido de cada uno 
escribiendo, por ejemplo,

::

    run1.fname
    
En este caso, ¿por qué se devuelven 146 respuestas? ¿Cuál de los campos contiene las dimensiones de los vóxeles de cada volumen? 
¿Cuál de los campos contiene las dimensiones del volumen total (es decir, ancho, largo y alto)? ¿Cuántos volúmenes se devolverían 
si se aplicara el comando ``spm_vol`` a la imagen anatómica? ¿Por qué?

5. Abra la imagen anatómica de sub-08 en el visor de imágenes y haga clic derecho en cualquiera de los tres paneles. Seleccione 
"Superposición -> Agregar imagen -> Esta imagen" y seleccione el archivo funcional "sub-08_task-flanker_run-1_bold.nii". La imagen 
funcional se superpondrá a la imagen anatómica y se mostrará en un mapa de calor rojo-naranja, mostrando una alineación inicial 
relativamente buena entre las imágenes.

.. figura:: 03_ImageOverlay.png

Ahora realice el mismo procedimiento para las imágenes anatómicas y funcionales para sub-01, lo que debería darle una figura como 
la siguiente:

.. figura:: 03_ImageOverlay_sub01.png

¿Qué observas? Esta desalineación entre las imágenes se abordará en un capítulo posterior sobre :ref:`Configuración del origen 
<SPM_07_SettingTheOrigin>`.

Video
--------

Para ver una descripción general en video sobre cómo verificar la calidad de sus datos, haga clic `aquí 
<https://www.youtube.com/watch?v=j0AEAOghD7w>`__.


