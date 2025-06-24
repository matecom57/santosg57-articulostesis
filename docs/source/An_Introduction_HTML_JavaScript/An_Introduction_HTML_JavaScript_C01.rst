An_Introduction_HTML_JavaScript_C01
===================================

David R. Brooks


Introductory Concepts

Chapter 1 provides a very brief introduction to using HTML and JavaScript for creating simple Web pages. It presents examples that illustrate the way 
in which JavaScript interfaces with an HTML document to display some printed output in a Web browser window, and introduces the concept of an HTML 
document as an object, with certain methods and properties accessible through JavaScript to act on that object. There are also some examples that show 
how to modify the appearance of a document by using HTML tags and their attributes, including as part of a text string passed as a calling argument to 
JavaScript’s write() method.

El Capítulo 1 proporciona una introducción muy breve al uso de HTML y JavaScript para crear páginas web simples. Presenta ejemplos que ilustran la 
forma en que JavaScript interactúa con un documento HTML para mostrar algunos resultados impresos en una ventana del navegador web e introduce el 
concepto de un documento HTML como un objeto, con ciertos métodos y propiedades accesibles a través de JavaScript para actuar sobre eso. objeto. 
También hay algunos ejemplos que muestran cómo modificar la apariencia de un documento mediante el uso de etiquetas HTML y sus atributos, incluso como 
parte de una cadena de texto pasada como argumento de llamada al método write() de JavaScript.


**1.1 Introducing the Tools**

**1.1.1 What Is an HTML Document?**

HTML is an acronym for HyperText Markup Language. HTML documents, the foundation of all content appearing on the World Wide Web (WWW), consist of two 
essential parts: information content and a set of instructions that tells a computer how to display that content. The instructions—the “markup,” in 
editorial jargon—comprise the HTML language. It is not a programming language in the traditional sense, but rather a set of instructions about how to 
display content. The computer application that translates this description is called a Web browser. Ideally, online content should always look the same 
regardless of the browser used or the operating system on which it resides, but the goal of platform independence is achieved only approximately in 
practice.

HTML es un acrónimo de lenguaje de marcado de hipertexto. Los documentos HTML, la base de todo el contenido que aparece en la World Wide Web (WWW), 
constan de dos partes esenciales: contenido informativo y un conjunto de instrucciones que le indican a una computadora cómo mostrar ese contenido. Las 
instrucciones (el "marcado", en la jerga editorial) comprenden el lenguaje HTML. No es un lenguaje de programación en el sentido tradicional, sino más 
bien un conjunto de instrucciones sobre cómo mostrar contenido. La aplicación informática que traduce esta descripción se llama navegador web. 
Idealmente, el contenido en línea debería tener siempre el mismo aspecto independientemente del navegador utilizado o del sistema operativo en el que 
resida, pero el objetivo de la independencia de la plataforma sólo se logra de forma aproximada en la práctica.


A basic HTML document requires a minimum of four sets of elements:

<html> … </html>
<head> … </head>
<title> … </title>
<body> … </body>

These elements define the essential parts of an HTML document: the document itself, a heading section, a title section, and a body. Each of the 
elements is defined by two tags—a start tag and an end tag. Tags are always enclosed in angle brackets: <…>. End tags start with a slash (/). As is 
shown later, some HTML elements have only one tag. Most tags are supposed to occur in pairs, although this rule is only loosely enforced in HTML. In 
order to support a scripting language such as JavaScript (much more about that later!), another element must be added:

Estos elementos definen las partes esenciales de un documento HTML: el documento en sí, una sección de encabezado, una sección de título y un cuerpo. 
Cada uno de los elementos está definido por dos etiquetas: 

una etiqueta de inicio y una etiqueta de finalización. 

Las etiquetas siempre están entre corchetes angulares: <…>. Las etiquetas finales comienzan con una barra (/). Como se muestra más adelante, algunos 
elementos HTML tienen una sola etiqueta. Se supone que la mayoría de las etiquetas aparecen en pares, aunque esta regla sólo se aplica de manera laxa 
en HTML. Para admitir un lenguaje de secuencias de comandos como JavaScript (¡mucho más sobre esto más adelante!), se debe agregar otro elemento:


<script> … </script>

For our purposes, a script element always contains JavaScript code. These elements are organized as follows within an HTML document:

<html>
<head>
<title> … </title>
…
<!-- Optional script elements as needed. -->
<script> … </script>
</head>
<body>
…
</body>
</html>

The html tag encloses all other tags and defines the boundaries of the HTML document. We will return to all the other tags later. script tags are often 
found inside the <head> tag, but they can appear elsewhere in a document as well. The indenting used to set off pairs of tags is optional, but it makes 
documents easier to create, read, and edit. This style is part of good programming practice in all languages.

La etiqueta html encierra todas las demás etiquetas y define los límites del documento HTML. Volveremos a todas las demás etiquetas más adelante. Las 
etiquetas de script a menudo se encuentran dentro de la etiqueta <head>, pero también pueden aparecer en otras partes de un documento. La sangría 
utilizada para resaltar pares de etiquetas es opcional, pero facilita la creación, lectura y edición de documentos. Este estilo es parte de buenas 
prácticas de programación en todos los lenguajes.


Owing to the fact that JavaScript is so tightly bound to HTML documents, you must learn JavaScript along with at least a subset of HTML. Unfortunately 
for anyone trying to learn and use HTML and JavaScript, each of the several available browsers is free to implement and support JavaScript in its own 
way. A browser does not even have to support JavaScript at all, although it is hard to imagine why it would not do so. Browsers can and do incorporate 
some proprietary HTML and JavaScript features that may not be supported by other browsers. Newer versions of any browser may support features that will 
not be recognized by earlier versions.

Debido al hecho de que JavaScript está tan estrechamente vinculado a los documentos HTML, debes aprender JavaScript junto con al menos un subconjunto 
de HTML. Desafortunadamente para cualquiera que intente aprender y utilizar HTML y JavaScript, cada uno de los distintos navegadores disponibles es 
libre de implementar y admitir JavaScript a su manera. Un navegador ni siquiera tiene que soportar JavaScript, aunque es difícil imaginar por qué no lo 
haría. Los navegadores pueden incorporar, y de hecho lo hacen, algunas características patentadas de HTML y JavaScript que pueden no ser compatibles 
con otros navegadores. Las versiones más recientes de cualquier navegador pueden admitir funciones que las versiones anteriores no reconocerán.


Fortunately, it is possible to work with what is essentially a de facto standardized subset of HTML and JavaScript. As a result, some of the 
descriptions of the details of HTML and JavaScript in this book are incomplete. This is not necessarily bad!

Afortunadamente, es posible trabajar con lo que es esencialmente un subconjunto estandarizado de facto de HTML y JavaScript. Como resultado, algunas de 
las descripciones de los detalles de HTML y JavaScript en este libro están incompletas. ¡Esto no es necesariamente malo!


Although we tend to think of HTML documents as a way to distribute information for remote access on the Web, they are equally useful when used locally 
on any computer that has a browser. Thus, in conjunction with JavaScript, you can create a self-contained problem-solving environment that can be used 
locally as well as (literally) globally.

Aunque solemos pensar en los documentos HTML como una forma de distribuir información para el acceso remoto en la Web, son igualmente útiles cuando se 
utilizan localmente en cualquier ordenador que tenga un navegador. Por tanto, junto con JavaScript, se puede crear un entorno de resolución de 
problemas autónomo que se puede utilizar tanto localmente como (literalmente) globalmente.


Good programming technique often involves separating the input/output (I/O) interface from the underlying calculations that do the work of a program, 
using appropriate modularization. The programming environment provided by HTML/JavaScript provides a conceptually elegant means of implementing this 
strategy. An HTML document provides the I/O interface and JavaScript handles the calculations. An advantage of HTML is that it provides a wealth of 
interface possibilities that far surpass those of text-based languages such as C.

Una buena técnica de programación a menudo implica separar la interfaz de entrada/salida (E/S) de los cálculos subyacentes que realizan el trabajo de 
un programa, utilizando una modularización adecuada. El entorno de programación proporcionado por HTML/JavaScript proporciona un medio conceptualmente 
elegante para implementar esta estrategia. Un documento HTML proporciona la interfaz de E/S y JavaScript maneja los cálculos. Una ventaja de HTML es 
que proporciona una gran cantidad de posibilidades de interfaz que superan con creces las de los lenguajes basados en texto como C.


1.1.2 What Is JavaScript?

JavaScript is an interpreted (rather than a compiled) object-oriented programming language, with roots in C/C++, that has been developed for use with 
other Web tools. It does not operate as a standalone language, but rather is designed to work together with HTML for creating interactive Web pages. 
JavaScript is not the same as Java, which is a compiled object-oriented language.

JavaScript es un lenguaje de programación orientado a objetos interpretado (en lugar de compilado), con raíces en C/C++, que ha sido desarrollado para 
su uso con otras herramientas web. No funciona como un lenguaje independiente, sino que está diseñado para trabajar junto con HTML para crear páginas 
web interactivas. JavaScript no es lo mismo que Java, que es un lenguaje compilado orientado a objetos.


JavaScript is used to write client side applications, which means that its code is sent to a user’s computer when a Web page is loaded. The code is 
then executed, basically line by line, by a JavaScript interpreter included as part of the user’s (client’s) Web browser. This arrangement minimizes 
security issues that can arise when a client computer interacts with the computer that sent the page. It also makes it easy to package an entire 
problem—with its own user interface and solution—self-contained within a single document. However, the inability to interact dynamically with 
information on the server does impose limitations on the kinds of tasks that JavaScript can accomplish.

JavaScript se utiliza para escribir aplicaciones del lado del cliente, lo que significa que su código se envía a la computadora de un usuario cuando se 
carga una página web. Luego, el código se ejecuta, básicamente línea por línea, mediante un intérprete de JavaScript incluido como parte del navegador 
web del usuario (cliente). Esta disposición minimiza los problemas de seguridad que pueden surgir cuando una computadora cliente interactúa con la 
computadora que envió la página. También facilita empaquetar un problema completo (con su propia interfaz de usuario y solución) en un solo documento. 
Sin embargo, la incapacidad de interactuar dinámicamente con la información del servidor impone limitaciones en los tipos de tareas que JavaScript 
puede realizar.


It is commonplace to refer to any set of written computer instructions as a “program,” but this term should perhaps be more rigorously applied to a 
separate entity that can be executed on its own. As JavaScript is interpreted rather than compiled, a separately executable entity is never created. 
Rather, JavaScript code statements are interpreted and executed one at a time, essentially “on the fly.” Although this may seem inefficient, there is 
rarely any discernible time lag associated with executing JavaScript commands on modern computers.

Es un lugar común referirse a cualquier conjunto de instrucciones escritas de computadora como “programa”, pero este término tal vez debería aplicarse 
con más rigor a una entidad separada que puede ejecutarse por sí sola. Como JavaScript se interpreta en lugar de compilarse, nunca se crea una entidad 
ejecutable por separado. Más bien, las declaraciones del código JavaScript se interpretan y ejecutan una a la vez, esencialmente "sobre la marcha". 
Aunque esto puede parecer ineficiente, rara vez hay un retraso perceptible asociado con la ejecución de comandos JavaScript en computadoras modernas.


JavaScript is one of a class of scripting languages whose purpose is to access and modify components of an existing information interface. (Microsoft’s 
VBScript is another scripting language.) In this case, the interface is an HTML document. Something like JavaScript became necessary as soon as HTML 
documents on the Web evolved from one-way delivery systems for displaying fixed content. One of JavaScript’s first applications arose from the need to 
check values entered by users into the fields of HTML forms that can be sent back to the originator. (Forms are discussed in a later chapter.) 
JavaScript can be used to compare input values against an expected range or set of values and to generate appropriate messages and other actions based 
on those comparisons.

JavaScript pertenece a una clase de lenguajes de secuencias de comandos cuyo propósito es acceder y modificar componentes de una interfaz de 
información existente. (VBScript de Microsoft es otro lenguaje de programación). En este caso, la interfaz es un documento HTML. Algo como JavaScript 
se hizo necesario tan pronto como los documentos HTML en la Web evolucionaron a partir de sistemas de entrega unidireccionales para mostrar contenido 
fijo. Una de las primeras aplicaciones de JavaScript surgió de la necesidad de verificar los valores ingresados por los usuarios en los campos de los 
formularios HTML que se pueden enviar al creador. (Los formularios se analizan en un capítulo posterior). JavaScript se puede utilizar para comparar 
valores de entrada con un rango o conjunto de valores esperado y para generar mensajes apropiados y otras acciones basadas en esas comparaciones.


JavaScript has evolved into a complete programming language with extensive capabilities for manipulating text and handling mathematical operations, 
useful for a wide range of computing problems. The possible applications include many self-contained scientific and engineering calculations, which 
provide the primary motivation for this book. As noted above, the utility of JavaScript is restricted to problems that do not have to access external 
data sources, such as would reside on a host computer and would not be available to a client computer.

JavaScript ha evolucionado hasta convertirse en un lenguaje de programación completo con amplias capacidades para manipular texto y realizar 
operaciones matemáticas, útil para una amplia gama de problemas informáticos. Las posibles aplicaciones incluyen muchos cálculos científicos y de 
ingeniería autónomos, que constituyen la motivación principal de este libro. Como se señaló anteriormente, la utilidad de JavaScript está restringida a 
problemas que no tienen que acceder a fuentes de datos externas, como las que residirían en una computadora host y no estarían disponibles para una 
computadora cliente.


The major challenge in learning HTML/JavaScript is that it is not a completely standardized environment. The various dialects of HTML and JavaScript 
pose problems even for experienced programmers. These kinds of problems can be minimized by focusing on an appropriate subset of HTML/JavaScript, which 
is feasible because there is little reason to use browser-specific subsets of HTML/JavaScript in the context of the topics dealt with in this book.

El mayor desafío al aprender HTML/JavaScript es que no es un entorno completamente estandarizado. Los distintos dialectos de HTML y JavaScript plantean 
problemas incluso a los programadores experimentados. Este tipo de problemas se pueden minimizar centrándose en un subconjunto apropiado de 
HTML/JavaScript, lo cual es factible porque hay pocas razones para utilizar subconjuntos de HTML/JavaScript específicos del navegador en el contexto de 
los temas tratados en este libro.


1.1.3 How Do You Create HTML/JavaScript Documents?

Since HTML/JavaScript documents are just text documents, they can be created with any text editor. Even Windows’ very basic Notepad application is a 
workable choice for simple tasks.1 Once they are created, you can open HTML files in your computer’s browser—hopefully without regard to which browser 
you are using. As long as you give such documents an .htm or .html file name extension, they should automatically open in your browser when you 
double-click on the file name. The three-letter extension is standard for Windows-based documents. The four-letter extension is commonly used on UNIX 
systems.2

Dado que los documentos HTML/JavaScript son sólo documentos de texto, se pueden crear con cualquier editor de texto. Incluso la aplicación Bloc de 
notas muy básica de Windows es una opción viable para tareas simples.1 Una vez creados, puede abrir archivos HTML en el navegador de su computadora, 
con suerte sin importar qué navegador esté utilizando. Siempre que proporcione a dichos documentos una extensión de nombre de archivo .htm o .html, 
deberían abrirse automáticamente en su navegador cuando haga doble clic en el nombre del archivo. La extensión de tres letras es estándar para los 
documentos basados ​​en Windows. La extensión de cuatro letras se usa comúnmente en sistemas UNIX.2


There is one other consequence of using Windows computers for creating all the examples in this text (and the text itself, for that matter): Windows 
file names are case-insensitive, whereas in UNIX, all spellings, including file names and commands, are case-sensitive. This should not cause problems, 
but it is something to keep in mind. In Windows, you can name a document newDocument.htm. Later, you can spell it newdocument.htm, NEWDOCUMENT.HTM, or 
any other combination of uppercase and lowercase letters and it will not matter. However, on a UNIX system, that file can be accessed only with the 
original spelling.

Hay otra consecuencia del uso de computadoras con Windows para crear todos los ejemplos en este texto (y el texto mismo, de hecho): los nombres de 
archivos de Windows no distinguen entre mayúsculas y minúsculas, mientras que en UNIX, toda la ortografía, incluidos los nombres de archivos y los 
comandos, no se distinguen entre mayúsculas y minúsculas. distingue mayúsculas y minúsculas. Esto no debería causar problemas, pero es algo a tener en 
cuenta. En Windows, puede nombrar un documento como nuevoDocumento.htm. Luego, podrás deletrearlo newdocument.htm, NEWDOCUMENT.HTM o cualquier otra 
combinación de letras mayúsculas y minúsculas y no importará. Sin embargo, en un sistema UNIX, sólo se puede acceder a ese archivo con la ortografía 
original.


Although you can create text (and, therefore, HTML) documents with a full-featured word processor such as Microsoft Word, this is not recommended. When 
you save a word processor document it no longer contains just the text you have typed, but also all the layout and formatting information that goes 
with along with it. You can choose to save a document as just text with an .htm extension, but it is easy to forget to do it.

Aunque puede crear documentos de texto (y, por lo tanto, HTML) con un procesador de textos con todas las funciones como Microsoft Word, no se 
recomienda. Cuando guarda un documento de procesador de textos, ya no contiene solo el texto que ha escrito, sino también toda la información de diseño 
y formato que lo acompaña. Puede optar por guardar un documento solo como texto con una extensión .htm, pero es fácil olvidarse de hacerlo.


Microsoft Word and other modern word-processing applications can also format any document as an HTML document, but this is also not recommended. These 
converted documents may include a huge quantity of extraneous information and HTML instructions that make the resulting file much larger and more 
complex than it needs to be. (Try saving a Word document as an HTML document and then look at the result in a text editor such as Notepad!)

Microsoft Word y otras aplicaciones modernas de procesamiento de textos también pueden formatear cualquier documento como documento HTML, pero tampoco 
se recomienda. Estos documentos convertidos pueden incluir una gran cantidad de información superflua e instrucciones HTML que hacen que el archivo 
resultante sea mucho más grande y complejo de lo necesario. (¡Intente guardar un documento de Word como documento HTML y luego observe el resultado en 
un editor de texto como el Bloc de notas!)


RTF (“rich text format”) documents are also unacceptable, as they still retain some formatting information that is inappropriate for an HTML document. 
Any document that contains “smart quotes” rather than “straight quotes” can also cause problems, because smart quotes may not be displayed properly by 
browsers. (This is much less of a problem on current browsers than it was in the past.)

Los documentos RTF (“formato de texto enriquecido”) también son inaceptables, ya que aún conservan cierta información de formato que no es apropiada 
para un documento HTML. Cualquier documento que contenga “comillas tipográficas” en lugar de “comillas simples” también puede causar problemas, porque 
es posible que los navegadores no muestren correctamente las comillas tipográficas. (Esto es un problema mucho menor en los navegadores actuales que en 
el pasado).


There are commercial Web development applications that allow you to create Web pages without actually knowing anything about HTML or JavaScript, but 
these applications are not suitable for use with this book. The obvious reason is that the primary purpose of the book is to show you how to write your 
own HTML instructions and JavaScript code.

Existen aplicaciones comerciales de desarrollo web que le permiten crear páginas web sin saber nada sobre HTML o JavaScript, pero estas aplicaciones no 
son adecuadas para usar con este libro. La razón obvia es que el propósito principal del libro es mostrarle cómo escribir sus propias instrucciones 
HTML y código JavaScript.


Moreover, these applications will probably create HTML files that are much larger and more complex than they need to be for our purposes. Finally, they 
do not include the kind of JavaScript code you will need for the topics discussed here. Thus, they are better suited for Web development projects that 
involve a lot of graphics and the other “bells and whistles” that make commercial Web pages attractive.

Además, estas aplicaciones probablemente crearán archivos HTML mucho más grandes y complejos de lo necesario para nuestros propósitos. Finalmente, no 
incluyen el tipo de código JavaScript que necesitará para los temas tratados aquí. Por lo tanto, son más adecuados para proyectos de desarrollo web que 
involucran muchos gráficos y otras "campanas y silbatos" que hacen atractivas las páginas web comerciales.


Creating an HTML/JavaScript document that works properly inevitably involves switching back and forth between a text editor and a browser—making 
changes and observing the effects of those changes. Once you create a basic HTML document, you can open it in your browser and move back and forth 
between this document and your text editor, and whenever you change the document, you can reload or refresh it in your browser. It is certainly 
possible, but not particularly convenient, to do this with a simple text editor such as Notepad.

Crear un documento HTML/JavaScript que funcione correctamente implica inevitablemente alternar entre un editor de texto y un navegador, realizar 
cambios y observar los efectos de esos cambios. Una vez que crea un documento HTML básico, puede abrirlo en su navegador y avanzar y retroceder entre 
este documento y su editor de texto, y cada vez que cambie el documento, puede recargarlo o actualizarlo en su navegador. Ciertamente es posible, pero 
no particularmente conveniente, hacer esto con un editor de texto simple como el Bloc de notas.


There are many commercial software tools whose purpose is to facilitate writing and editing HTML documents by integrating document creation, editing, 
and viewing. Some of them are intended for large and complicated projects and may be “overkill” for use with this book. For several years, for creating 
this book and in my own day-to-day work, I have used AceHTML Freeware V.5 (see www.visicommedia.com). This software provides an HTML/JavaScript editor 
with some automatic color based text formatting that makes HTML instructions and JavaScript code easy to read. There is an integrated Web page viewer, 
so it is easy to switch back and forth between creating and editing a document and seeing the results of your work. It also has a JavaScript syntax 
checker. As is typically the case, the checker is not very good at telling you how to fix a syntax error, but it at least tells you where the error was 
detected. The freeware version of this editor may or may not be currently available, and it may require installation of other software that you may or 
may not want on your computer. In any event, during the time I was writing this book, there were versions of AceHTML available for purchase.3

Existen muchas herramientas de software comerciales cuyo propósito es facilitar la escritura y edición de documentos HTML integrando la creación, 
edición y visualización de documentos. Algunos de ellos están pensados ​​para proyectos grandes y complicados y pueden ser “exagerados” para su uso con 
este libro. Durante varios años, para crear este libro y en mi trabajo diario, he utilizado AceHTML Freeware V.5 (ver www.visicommedia.com). Este 
software proporciona un editor HTML/JavaScript con formato de texto automático basado en colores que hace que las instrucciones HTML y el código 
JavaScript sean fáciles de leer. Hay un visor de páginas web integrado, por lo que es fácil alternar entre crear y editar un documento y ver los 
resultados de su trabajo. También tiene un verificador de sintaxis de JavaScript. Como suele ser el caso, el verificador no es muy bueno para decirle 
cómo corregir un error de sintaxis, pero al menos le dice dónde se detectó el error. La versión gratuita de este editor puede o no estar disponible 
actualmente y puede requerir la instalación de otro software que quizás desee o no en su computadora. En cualquier caso, durante el tiempo que escribí 
este libro, había versiones de AceHTML disponibles para su compra.3


Although, in principle, it should not make any difference which browser you use, the outputs I have displayed in this text come from either AceHTML’s 
internal browser or Mozilla’s Firefox, which I use as the default browser on my Windows computers. When you display content in an “alert” box, as will 
be described later in this book, the appearance of this box is different for different browsers, and hence may be different from what is shown here.

Aunque, en principio, no debería haber ninguna diferencia qué navegador utilice, los resultados que he mostrado en este texto provienen del navegador 
interno de AceHTML o de Firefox de Mozilla, que uso como navegador predeterminado en mis computadoras con Windows. Cuando muestra contenido en un 
cuadro de "alerta", como se describirá más adelante en este libro, la apariencia de este cuadro es diferente para diferentes navegadores y, por lo 
tanto, puede ser diferente de lo que se muestra aquí.


1.1.4 Some Typographic Conventions Used in This Book

HTML tags and JavaScript code are printed in a monospaced (Courier) font in document examples and whenever they are referred to in the text. Thus, 
document is interpreted as a reference to an HTML object, as opposed to its general use as a term identifying a body of text. Some technical terms used 
for the first time are printed in bold font. Their definitions can be found in the Glossary. Within descriptions of HTML document features and 
JavaScript code, user-supplied text is denoted by {italicized text in braces (curly brackets)}. In the code examples, HTML tags are printed in bold 
font.
Las etiquetas HTML y el código JavaScript se imprimen en una fuente monoespaciada (Courier) en los ejemplos de documentos y siempre que se haga 
referencia a ellos en el texto. Por tanto, documento se interpreta como una referencia a un objeto HTML, a diferencia de su uso general como un término 
que identifica un cuerpo de texto. Algunos términos técnicos utilizados por primera vez están impresos en negrita. Sus definiciones se pueden encontrar 
en el Glosario. En las descripciones de las características de los documentos HTML y el código JavaScript, el texto proporcionado por el usuario se 
indica con {texto en cursiva entre llaves (llaves)}. En los ejemplos de código, las etiquetas HTML están impresas en negrita.



The renderings of HTML documents and other output as displayed in a browser window have been captured and edited on a Windows computer by pressing the 
PrtScn (or Print Screen) key and copying the resulting screen image into the freeware IrfanView image editing program (www.irfanview.com).

Las representaciones de documentos HTML y otros resultados tal como se muestran en una ventana del navegador se han capturado y editado en una 
computadora con Windows presionando la tecla PrtScn (o Imprimir Pantalla) y copiando la imagen de pantalla resultante en el programa gratuito de 
edición de imágenes IrfanView (www.irfanview.com).


Owing to the small format of this book, line breaks in document examples may sometimes be misleading. I have tried to make necessary line breaks as 
logical as possible, but you may want to remove some breaks when you reproduce these documents for your own use.

Debido al pequeño formato de este libro, los saltos de línea en los ejemplos de documentos pueden ser a veces engañosos. He intentado que los saltos de 
línea necesarios sean lo más lógicos posible, pero es posible que desee eliminar algunos saltos cuando reproduzca estos documentos para su propio uso.


1.1.5 Where Should I Look for More Information about HTML and JavaScript?

By now, it should be clear that this book is in no way intended as a reference source for either HTML or JavaScript. Any attempt to provide complete 
coverage for either language would thoroughly confound its purpose and is far beyond my capabilities! Therefore, you must look elsewhere for exhaustive 
treatments of HTML and JavaScript. I used three sources:

A estas alturas, debería quedar claro que este libro de ninguna manera pretende ser una fuente de referencia ni para HTML ni para JavaScript. 
¡Cualquier intento de proporcionar una cobertura completa para cualquiera de los idiomas confundiría completamente su propósito y está mucho más allá 
de mis capacidades! Por lo tanto, debe buscar en otra parte tratamientos exhaustivos de HTML y JavaScript. Utilicé tres fuentes:


Thomas Powell, HTML: The Complete Reference, Third Edition, 2001, Osborne/McGraw-Hill, Berkeley, CA. ISBN 0-07-212951-4.
Thomas Powell and Dan Whitworth, HTML Programmer’s Reference, Second Edition, 2001, Osborne/McGraw-Hill, Berkeley, CA. ISBN 0-07-213232-9.8
Thomas Powell and Fritz Schneider, JavaScript: The Complete Reference, 2001, Osborne/McGraw-Hill, Berkeley, CA. ISBN 0-07-219127-9.

If you are at all serious about creating your own online applications (“serious” perhaps being defined as anything past the bare minimum needed to 
survive a course based on this text), there is no substitute for these or similar references.

Si realmente desea crear sus propias aplicaciones en línea (“serio” tal vez definido como cualquier cosa que supere el mínimo necesario para sobrevivir 
a un curso basado en este texto), no hay sustituto para estas referencias u otras similares.


The first HTML book I ever read (and still consult from time to time) is out of print, but it is worth looking for in libraries or remaindered book 
stores (which is where I found my copy). Even though it addresses an older (and simpler!) version of HTML, it is still an excellent resource for the 
kinds of problems discussed here.

El primer libro HTML que leí (y que sigo consultando de vez en cuando) está agotado, pero vale la pena buscarlo en bibliotecas o librerías restantes 
(que es donde encontré mi copia). Aunque aborda una versión anterior (¡y más simple!) de HTML, sigue siendo un recurso excelente para los tipos de 
problemas que se analizan aquí.


Todd Stauffer, Using HTML 3.2, Second Edition, 1996, Que Corporation, Indianapolis, IN. ISBN 0-7897-0985-6.

1.2 Your First HTML/JavaScript Documents

A typical first goal in learning any programming language is to display a simple message. With HTML, this is trivially simple: Just type the message in 
the body of the document, as shown in Document 1.1. (Appendix 1 contains an index to all the documents in the text.)

Un primer objetivo típico al aprender cualquier lenguaje de programación es mostrar un mensaje simple. Con HTML, esto es trivialmente simple: 
simplemente escriba el mensaje en el cuerpo del documento, como se muestra en el Documento 1.1. (El Apéndice 1 contiene un índice de todos los 
documentos del texto).


Document 1.1 (HelloWorldHTML.htm)

<html>
<head>
<title>First HTML Document</title>
</head>
<body>
Hello, world!
</body>
</html>

Most document examples presented in this book will include a browser’s rendering of the screen output produced by the document. When a border appears 
around the output, as it does for the output from Document 1.1, the purpose is to distinguish the output from the rest of the text—the document does 
not generate that border. In the text, renderings are always in black and white or grayscale. In some cases, as noted, color renderings are printed on 
separate color plates. In other cases (such as for Document 1.3) you will have to try the code yourself.

La mayoría de los ejemplos de documentos presentados en este libro incluirán la representación en un navegador de la salida de pantalla producida por 
el documento. Cuando aparece un borde alrededor de la salida, como ocurre con la salida del Documento 1.1, el propósito es distinguir la salida del 
resto del texto; el documento no genera ese borde. En el texto, las representaciones son siempre en blanco y negro o en escala de grises. En algunos 
casos, como se señaló, las reproducciones de color se imprimen en placas de color separadas. En otros casos (como en el Documento 1.3) tendrás que 
probar el código tú mismo.


Document 1.1 is certainly not very exciting. But the point is that an HTML document simply displays the static content you provide. As you will learn 
in Chapter 2, HTML provides many facilities for changing the appearance of this content, but not the content itself.

El documento 1.1 ciertamente no es muy interesante. Pero el punto es que un documento HTML simplemente muestra el contenido estático que usted 
proporciona. Como aprenderá en el Capítulo 2, HTML proporciona muchas posibilidades para cambiar la apariencia de este contenido, pero no el contenido 
en sí.


You can also display content with JavaScript. With JavaScript, input and output always pass through an HTML document. Instructions (code) you write in 
JavaScript are called a script. The capability to interpret JavaScript instructions must be built into your browser. Document 1.2 uses JavaScript to 
generate a simple text message, which is displayed in the document. There is no good reason to use JavaScript simply to display fixed content, but this 
exercise will provide an introduction to JavaScript syntax. Do not worry if the details of this and following examples seem obscure—hopefully, future 
chapters will clarify all these details!

También puedes mostrar contenido con JavaScript. Con JavaScript, la entrada y la salida siempre pasan por un documento HTML. Las instrucciones (código) 
que escribe en JavaScript se denominan script. La capacidad de interpretar instrucciones de JavaScript debe estar integrada en su navegador. El 
Documento 1.2 utiliza JavaScript para generar un mensaje de texto simple, que se muestra en el documento. No existe una buena razón para utilizar 
JavaScript simplemente para mostrar contenido fijo, pero este ejercicio proporcionará una introducción a la sintaxis de JavaScript. No se preocupe si 
los detalles de este ejemplo y los siguientes parecen oscuros; ¡con suerte, los capítulos futuros aclararán todos estos detalles!


Document 1.2 (HelloWorld.htm)

<html>
<head>
<title>Hello, world!</title>
<script language="javascript" type="text/javascript">
// These statements display text in a document.
document.write("Hello, world!");
document.write("<br />It's a beautiful day!");
</script>
</head>
<body>
<!-- No content in the body of this document. -->
</body>
</html>

A browser must be instructed to interpret certain parts of an HTML document as JavaScript code. To accomplish this, all text appearing inside the 
script element will be interpreted by a browser as one or more JavaScript statements. This means that HTML elements cannot appear inside the script 
element, as then the JavaScript interpreter would attempt (inappropriately) to interpret them as JavaScript code. This will generate a JavaScript 
error. In Document 1.2, the <br /> tag, which generates a line break, is an HTML element, but it is included inside a quoted string of text. This is 
allowed, but

Se debe indicar a un navegador que interprete ciertas partes de un documento HTML como código JavaScript. Para lograr esto, un navegador interpretará 
todo el texto que aparece dentro del elemento de secuencia de comandos como una o más declaraciones de JavaScript. Esto significa que los elementos 
HTML no pueden aparecer dentro del elemento script, ya que entonces el intérprete de JavaScript intentaría (inapropiadamente) interpretarlos como 
código JavaScript. Esto generará un error de JavaScript. En el Documento 1.2, la etiqueta <br />, que genera un salto de línea, es un elemento HTML, 
pero se incluye dentro de una cadena de texto entre comillas. Esto está permitido, pero


document.write("Hello, world!");
<br /> document.write("It's a beautiful day!");

is not allowed.

As noted previously, JavaScript is an object-based language. In programming terminology, an HTML document is an object. Using JavaScript, pre-defined 
methods can be used to act on a specified object. (Objects are discussed in more detail starting in Chapter 4.) Document 1.2 accesses (“calls” or 
“invokes”) the write() method of the document object to display text. A method is associated with its object by using “dot notation,” as in 
document.write().

Como se señaló anteriormente, JavaScript es un lenguaje basado en objetos. En terminología de programación, un documento HTML es un objeto. Usando 
JavaScript, se pueden usar métodos predefinidos para actuar sobre un objeto específico. (Los objetos se analizan con más detalle a partir del Capítulo 
4.) El documento 1.2 accede (“llama” o “invoca”) al método write() del objeto del documento para mostrar texto. Un método se asocia con su objeto 
mediante el uso de “notación de puntos”, como en document.write().




Methods such as write() often, but not always, require one or more inputs, referred to as calling arguments. In Document 1.2, the text strings "Hello, 
world!" and "<br />It's a beautiful day! "; are calling arguments for the write() method. Calling arguments provide the values on which a method acts.

Los métodos como write() a menudo, pero no siempre, requieren una o más entradas, denominadas argumentos de llamada. En el Documento 1.2, las cadenas 
de texto "¡Hola, mundo!" y "<br />¡Es un hermoso día! "; están llamando argumentos para el método write(). Los argumentos de llamada proporcionan los 
valores sobre los que actúa un método.


As we will see, most HTML elements include attributes that are used to assign properties to the element. The script element should include values for 
the language and type attributes, as shown:

Como veremos, la mayoría de los elementos HTML incluyen atributos que se utilizan para asignar propiedades al elemento. El elemento script debe incluir 
valores para los atributos de idioma y tipo, como se muestra:


<script language="javascript" type="text/javascript">

Comments within an HTML document are indicated by a very specific sequence of symbols:

<!-- {comments} -->

In keeping with the style adopted in this book, italicized text enclosed in curly brackets indicates text that is entered by the user. The curly 
brackets could be part of the comment, but are not needed and would normally not be included.

De acuerdo con el estilo adoptado en este libro, el texto en cursiva encerrado entre llaves indica el texto ingresado por el usuario. Las llaves 
podrían ser parte del comentario, pero no son necesarias y normalmente no se incluirían.


Inside a script element, single-line comments begin with two slashes, as in the fifth line of Document 1.2. Comments are a basic part of good 
programming style, no matter what the language. Some authors prefer not to use many comments in HTML/JavaScript because it increases the size of the 
file that is sent to the client computer. However, when you are learning the material presented in this book, there is no excuse for not making liberal 
use of comments to remind yourself of what you are doing.

Dentro de un elemento de script, los comentarios de una sola línea comienzan con dos barras, como en la quinta línea del Documento 1.2. Los comentarios 
son una parte básica de un buen estilo de programación, sin importar el lenguaje. Algunos autores prefieren no utilizar muchos comentarios en 
HTML/JavaScript porque aumenta el tamaño del archivo que se envía a la computadora cliente. Sin embargo, cuando esté aprendiendo el material presentado 
en este libro, no hay excusa para no hacer un uso liberal de los comentarios para recordar lo que está haciendo.


One use of HTML comments is to hide JavaScript code from browsers that do not have a JavaScript interpreter, but this is much less of a problem today 
than it might have been several years ago. It is also irrelevant for now because, of course, your browser must support JavaScript in order to be useful 
for this book. In any event, hiding JavaScript is accomplished as follows:

Un uso de los comentarios HTML es ocultar el código JavaScript de los navegadores que no tienen un intérprete de JavaScript, pero esto es un problema 
mucho menor hoy que hace varios años. También es irrelevante por ahora porque, por supuesto, su navegador debe soportar JavaScript para que sea útil 
para este libro. En cualquier caso, ocultar JavaScript se logra de la siguiente manera:


<script language="javascript" type="text/javascript">
<!-- Start hiding JavaScript code here.
{Put JavaScript statements here.}
// Stop hiding code here. -->
</script>

Although these HTML comment tags appear to be out of place because we have already stated that HTML elements cannot appear inside a script element, any 
browser that includes a JavaScript interpreter will be able to sort things out, basically by ignoring the comment tags.

Aunque estas etiquetas de comentarios HTML parecen estar fuera de lugar porque ya hemos dicho que los elementos HTML no pueden aparecer dentro de un 
elemento de script, cualquier navegador que incluya un intérprete de JavaScript podrá solucionar las cosas, básicamente ignorando las etiquetas de 
comentarios.


HTML syntax is case-insensitive, which means that <html> is equivalent to <HTML> or even <hTmL>. Some HTML document authors favor uppercase spellings 
for tags because they stand out from the text content. However, XHTML (extended HTML), the apparent successor to HTML, requires that tags be in 
lowercase letters.4 Hence, I always use lowercase letters for tag names here. Note that, despite previous warnings that file names and commands are 
case-sensitive in some systems, browsers should not be case-sensitive in their interpretation of HTML tags, regardless of the underlying operating 
system.

La sintaxis HTML no distingue entre mayúsculas y minúsculas, lo que significa que <html> es equivalente a <HTML> o incluso a <hTmL>. Algunos autores de 
documentos HTML prefieren escribir las etiquetas en mayúsculas porque se destacan del contenido del texto. Sin embargo, XHTML (HTML extendido), el 
aparente sucesor de HTML, requiere que las etiquetas estén en letras minúsculas.4 Por lo tanto, aquí siempre uso letras minúsculas para los nombres de 
las etiquetas. Tenga en cuenta que, a pesar de las advertencias anteriores de que los nombres de archivos y los comandos distinguen entre mayúsculas y 
minúsculas en algunos sistemas, los navegadores no deberían distinguir entre mayúsculas y minúsculas en su interpretación de las etiquetas HTML, 
independientemente del sistema operativo subyacente.


JavaScript syntax is always case-sensitive, regardless of the computer system on which it runs, like the C/C++ languages from which it is derived. So, 
when you write JavaScript code, you have to be very careful about case. For example, document is an object name recognized by JavaScript, but Document 
is not. (Try this in Document 1.2 if you need convincing.)

La sintaxis de JavaScript siempre distingue entre mayúsculas y minúsculas, independientemente del sistema informático en el que se ejecuta, como los 
lenguajes C/C++ de los que se deriva. Entonces, cuando escribes código JavaScript, debes tener mucho cuidado con las mayúsculas y minúsculas. Por 
ejemplo, documento es un nombre de objeto reconocido por JavaScript, pero Documento no. (Pruebe esto en el Documento 1.2 si necesita convencerse).


Note that each of the two JavaScript statements (the calls to document.write()) is terminated with a semicolon. JavaScript interprets a semicolon as 
“end of statement.” As a matter of syntax, a line feed at the end of a statement will also be interpreted as marking the end of that statement. 
However, it is poor programming practice to use this “implied semicolon,” and all JavaScript statements used in this book should terminate with 
semicolons. (Authors are not perfect!)

Tenga en cuenta que cada una de las dos declaraciones de JavaScript (las llamadas a document.write()) termina con un punto y coma. JavaScript 
interpreta un punto y coma como "fin de declaración". Por una cuestión de sintaxis, un salto de línea al final de una declaración también se 
interpretará como una marca del final de esa declaración. Sin embargo, es una mala práctica de programación utilizar este “punto y coma implícito” y 
todas las declaraciones de JavaScript utilizadas en este libro deben terminar con punto y coma. (¡Los autores no son perfectos!)



You can make Document 1.2 a little fancier by using other HTML elements and their attributes to control the appearance of the text. (Chapter 2 presents 
much more information about elements and attributes.) In Document 1.3, font (font description), h1 (heading), and hr (horizontal rule) are elements, 
and color, size, and align are attributes. Of these, the hr element requires only a single tag because it does not enclose any HTML content. Single-tag 
elements should include a forward slash at the end: <hr /> rather than <hr>.

Puede hacer que el Documento 1.2 sea un poco más sofisticado utilizando otros elementos HTML y sus atributos para controlar la apariencia del texto. 
(El Capítulo 2 presenta mucha más información sobre elementos y atributos). En el Documento 1.3, font (descripción de fuente), h1 (encabezado) y hr 
(regla horizontal) son elementos, y color, tamaño y alineación son atributos. De estos, el elemento hr requiere solo una etiqueta porque no incluye 
ningún contenido HTML. Los elementos de etiqueta única deben incluir una barra diagonal al final: <hr /> en lugar de <hr>.



Document 1.3 (HelloWorld2.htm)

<html>
<head>
<title>Hello, world!</title>
</head>
<body>
<h1 align="center">First JavaScript</h1>
<hr />
<script language="javascript" type="text/javascript">
document.write("<font size='5'
color='red'><center>Hello, world!</font>");
document.write("<br /><font size='7' color='blue'>
It's a beautiful day!</center></font>");
</script>
</body>
</html>

(Try this yourself to see the colors displayed.)

As previously noted, there is no good reason to use JavaScript to display this fixed content, but Document 1.3 again makes the point that any HTML tags 
appearing as part of the calling argument passed to document.write()are treated as part of the text string—the characters enclosed in quote marks—and 
therefore do not violate the rule that HTML elements cannot be used inside a script element. The HTML tags are essentially “pasted” into the HTML 
document right along with the text. Within the string
Como se señaló anteriormente, no hay una buena razón para usar JavaScript para mostrar este contenido fijo, pero el Documento 1.3 nuevamente señala que 
cualquier etiqueta HTML que aparezca como parte del argumento de llamada pasado a document.write() se trata como parte del texto. cadena (los 
caracteres entre comillas) y, por lo tanto, no violan la regla de que los elementos HTML no se pueden usar dentro de un elemento de secuencia de 
comandos. Básicamente, las etiquetas HTML se "pegan" en el documento HTML junto con el texto. dentro de la cuerda



"<br /><font size='7' color='blue'>
It's a beautiful day!</center></font>"

the attribute values are enclosed in single rather than double quotes. Otherwise, it would not be clear where the quoted string begins and ends.

los valores de los atributos están entre comillas simples en lugar de comillas dobles. De lo contrario, no quedaría claro dónde comienza y termina la 
cadena entrecomillada.



Another difference between Document 1.2 and Document 1.3 is that in 1.3, the script element is inside the body element. This is all right, although we 
would normally try to keep the script element inside the head element, thus ensuring that the JavaScript code is interpreted before the rest of the 
page is loaded. This detail is of no concern in this example, the sole purpose of which is to display some text.

Otra diferencia entre el Documento 1.2 y el Documento 1.3 es que en 1.3, el elemento de secuencia de comandos está dentro del elemento del cuerpo. Esto 
está bien, aunque normalmente intentaríamos mantener el elemento script dentro del elemento head, asegurando así que el código JavaScript se interprete 
antes de que se cargue el resto de la página. Este detalle no importa en este ejemplo, cuyo único propósito es mostrar texto.


As expected, this attempted modification of the script, which contains HTML tags in a context where a browser expects to see only JavaScript code, will 
produce an error:

Como era de esperar, este intento de modificación del script, que contiene etiquetas HTML en un contexto donde un navegador espera ver sólo código 
JavaScript, producirá un error:


<script language="javascript" type="text/javascript">
<font size="5" color="red"><center> // ERROR!!
document.write("Hello, world");
</font>
</script>

You can include more than one script element within an HTML document, as shown in Document 1.4a, in which there are two separate script sections, 
arbitrarily divided into a section above the horizontal rule (see the <hr /> tag) and another below the rule.

Puede incluir más de un elemento de secuencia de comandos dentro de un documento HTML, como se muestra en el Documento 1.4a, en el que hay dos 
secciones de secuencia de comandos separadas, divididas arbitrariamente en una sección encima de la regla horizontal (consulte la etiqueta <hr />) y 
otra debajo la regla.


Document 1.4a (HelloWorld3.htm)

<html>
<head>
<title>Hello, world! (v.3)</title>
</head>
<body bgcolor="lightgreen" text="magenta">
<h1 align="center">First JavaScript</h1>

<script language="javascript" type="text/javascript">
document.write("<font color='green'>
This document was last modified on
"+document.lastModified+"</font>");
</script>

<hr />

<script language="javascript" type="text/javascript">
document.write("background = "+document.bgColor);
document.write("<br />font = " + document.fgColor);
document.write("<font size='5'
color='red'><center>Hello,world!</font><br />");
document.write("<font size='7' color='blue'>
He said, &quot;It's a beautiful day!&quot;
</center></font>");
</script>

</body>
</html>

(See Color Example 1 for full-color output.)

Document 1.4a contains an answer to this question: How do you display double quote marks with the document.write() method if you cannot use double 
quotes inside a quoted string? One way is to use the escape sequence &quot;. Escape sequences always start with an ampersand (&) and end with a 
semicolon (;). There are many escape sequences for displaying characters that are not available directly from the keyboard or would be misinterpreted 
by HTML if entered directly, and they will be discussed later as needed. A list of commonly used escape sequences appears in Appendix 2.

El documento 1.4a contiene una respuesta a esta pregunta: ¿Cómo se muestran comillas dobles con el método document.write() si no se pueden utilizar 
comillas dobles dentro de una cadena entre comillas? Una forma es utilizar la secuencia de escape &quot;. Las secuencias de escape siempre comienzan 
con un signo (&) y terminan con un punto y coma (;). Hay muchas secuencias de escape para mostrar caracteres que no están disponibles directamente 
desde el teclado o que HTML malinterpretaría si se ingresaran directamente, y se analizarán más adelante según sea necesario. En el Apéndice 2 aparece 
una lista de secuencias de escape comúnmente utilizadas.


JavaScript objects have properties as well as methods. Like methods, properties are associated with objects through the use of dot notation. One useful 
property of the document object is lastModified, used in Document 1.4a. As its name suggests, this property accesses the time and date stamp 
automatically stored along with a document whenever it is modified and saved, based on the calendar and clock on the computer used to create the 
document. This stamp is automatically attached to the document, without any special action required by the creator of the document. The lastModified 
property is useful for documents that contain time-sensitive information, or just to give users some idea of whether a page displayed in a browser is 
current.

Los objetos JavaScript tienen propiedades además de métodos. Al igual que los métodos, las propiedades se asocian con objetos mediante el uso de 
notación de puntos. Una propiedad útil del objeto documento es lastModified, utilizada en el Documento 1.4a. Como sugiere su nombre, esta propiedad 
accede a la marca de fecha y hora almacenada automáticamente junto con un documento cada vez que se modifica y guarda, según el calendario y el reloj 
de la computadora utilizada para crear el documento. Este sello se adjunta automáticamente al documento, sin que el creador del documento requiera 
ninguna acción especial. La propiedad lastModified es útil para documentos que contienen información urgente o simplemente para dar a los usuarios una 
idea de si una página mostrada en un navegador es actual.


Document 1.4a contains the following two statements, which access two more document properties:

document.write("background = "+document.bgColor);
document.write("<br />font = " + document.fgColor);

These display a code for the background and font colors.

Attributes such as size and color have values. These values are supposed to be enclosed in quotes, although this is not actually required in HTML. 
Quotes are required in XHTML, and we will always use them. You can use either double or single quotes. In HTML documents, double quotes are generally 
accepted as the standard. However, when HTML elements with attributes are included inside quoted strings, as in

Atributos como el tamaño y el color tienen valores. Se supone que estos valores deben estar entre comillas, aunque en realidad esto no es necesario en 
HTML. Las cotizaciones son obligatorias en XHTML y siempre las usaremos. Puede utilizar comillas dobles o simples. En los documentos HTML, las comillas 
dobles se aceptan generalmente como estándar. Sin embargo, cuando se incluyen elementos HTML con atributos dentro de cadenas entrecomilladas, como en


document.write("<font size='5'
color='red'><center>Hello,world!</font><br />");

document.write("<font size='7' color='blue'>
He said, &quot;It's a beautiful day!&quot;
</center></font>");

then single quotes are required for the values in order to avoid conflict with the double quotes around the string.

A more reasonable approach to generating the output shown for Document 1.4a is to use JavaScript only as required to access desired document properties 
(and perhaps display some related text) and to use HTML for everything else. Document 1.4b is a modified version of Document 1.4a that does the content 
formatting with HTML tags inside the document. There is no need to show the output, as it is identical to that for Document 1.4a.

Un enfoque más razonable para generar el resultado que se muestra para el Documento 1.4a es usar JavaScript sólo cuando sea necesario para acceder a 
las propiedades deseadas del documento (y tal vez mostrar algún texto relacionado) y usar HTML para todo lo demás. El Documento 1.4b es una versión 
modificada del Documento 1.4a que formatea el contenido con etiquetas HTML dentro del documento. No es necesario mostrar el resultado, ya que es 
idéntico al del Documento 1.4a.


Document 1.4b (HelloWorld3HTML.htm)

<html>
<head>
<title>Hello, world! (with HTML)</title>

<script language="javascript" type="text/javascript">
document.write(
"<font color=©green©> This document was last modified on
"+document.lastModified+"</font>");
</script>

</head>
<body bgcolor="lightgreen" text="magenta">
<h1 align="center">First JavaScript</h1>
<hr />

<script language="javascript" type="text/javascript">
document.write("background = "+document.bgColor);
document.write("<br />font = " + document.fgColor);
</script>

<font size="5" color="red"><center>Hello,world!</font><br />
<font size="7" color="blue">
He said, "It's a beautiful day! "</center></font>"
</body>
</html>

In this case, there is actually a justification for putting one of the script sections inside the body of the document: This script is used to display 
codes for the background and text colors, which are known only after they are set inside the body element.

En este caso, en realidad existe una justificación para colocar una de las secciones del script dentro del cuerpo del documento: este script se utiliza 
para mostrar códigos para los colores de fondo y del texto, que se conocen sólo después de que se configuran dentro del elemento del cuerpo.


A summary of some properties and methods of the document object is given in Table 1.1. The bgColor and fgColor properties are not used to set the 
colors, but merely to tell you what they are. (You are right to conclude that this is normally not terribly important information.) Note that bgcolor 
is an HTML attribute used to set the background color of the body element and is supposed to be (but does not have to be in case-insensitive HTML) 
spelled in lowercase letters. bgColor is a property of the JavaScript document object and must be spelled with a capital C, as shown.

En la Tabla 1.1 se proporciona un resumen de algunas propiedades y métodos del objeto de documento. Las propiedades bgColor y fgColor no se utilizan 
para establecer los colores, sino simplemente para indicarle cuáles son. (Tiene razón al concluir que normalmente esta no es información muy 
importante). Tenga en cuenta que bgcolor es un atributo HTML que se utiliza para establecer el color de fondo del elemento del cuerpo y se supone que 
lo es (pero no tiene que serlo en HTML que no distingue entre mayúsculas y minúsculas). ) escrito en letras minúsculas. bgColor es una propiedad del 
objeto de documento JavaScript y debe escribirse con C mayúscula, como se muestra.


Table 1.1. Some properties and methods of the document object
Property or Method
Property
document.bgColor
Property
document.fgColor
Property
document.lastModified
Method
document.write("Hello! ")
Method
document.writeln("Hello!")
Action
Returns current value of back-
ground (page) color. Returns
"#ffffff" for
<body bgcolor="white">
Returns current value of font color.
Returns "#0000ff" for
<body text="blue">
Returns text string containing date
the document was last modified.
Prints quoted string on document
page.
Prints quoted string on document
page, followed by line feed.*
*

As HTML ignores line feeds, the writeln() method will not normally produce any noticeable difference in output. If the text to be displayed is within a 
pre element, then the line feed will be displayed.

Como HTML ignora los cambios de línea, el método writeln() normalmente no producirá ninguna diferencia notable en la salida. Si el texto que se 
mostrará está dentro de un elemento previo, se mostrará el avance de línea.


1.3 Accessing HTML Documents on the Web

Documents intended for access by others on the World Wide Web are posted on a Web server, a computer system connected to the Internet. Colleges and 
universities typically provide Web servers for use by their faculty and students. Individuals not affiliated with an institution may have to purchase 
space on a commercial Web server. In any case, access to Web pages is universal in the sense that any computer with an Internet connection and a 
browser can be connected to a Web site through its Internet address—its Uniform Resource Locator (URL).

Los documentos destinados al acceso de otras personas en la World Wide Web se publican en un servidor web, un sistema informático conectado a Internet. 
Los colegios y universidades suelen proporcionar servidores web para uso de sus profesores y estudiantes. Es posible que las personas no afiliadas a 
una institución tengan que comprar espacio en un servidor web comercial. En cualquier caso, el acceso a las páginas web es universal en el sentido de 
que cualquier computadora con una conexión a Internet y un navegador puede conectarse a un sitio web a través de su dirección de Internet: su 
localizador uniforme de recursos (URL).


Not all HTML documents have to be publicly accessible on the Web. They can be protected with logon identifications and passwords, or they can be 
available only locally through an intranet (as opposed to the Internet). The Internet is a global network of interconnected computers, whereas an 
intranet is a local network that may or may not also provide connections to the Internet. For example, a company can provide an intranet with no 
external access, exclusively for internal use by its own employees.

No todos los documentos HTML tienen que ser accesibles públicamente en la Web. Pueden protegerse con identificaciones de inicio de sesión y 
contraseñas, o pueden estar disponibles sólo localmente a través de una intranet (a diferencia de Internet). Internet es una red global de computadoras 
interconectadas, mientras que una intranet es una red local que puede o no proporcionar también conexiones a Internet. Por ejemplo, una empresa puede 
proporcionar una intranet sin acceso externo, exclusivamente para uso interno de sus propios empleados.


Internet addresses look something like this:

http://www.myUniversity.edu/~myName/index.htm

They start with the http:// prefix, to indicate that the Hypertext Transfer Protocol (HTTP) is being used. There are some variations, such as https, 
which indicates that the address that follows resides on a secure server, as required for financial transactions, for example. The rest of the address 
identifies a Web server and then a folder or directory on a computer system at myUniversity for someone named myName. The .edu extension identifies 
this site as belonging to an educational institution, in the same way as .gov and .com identify government and commercial sites. The ~ symbol is often 
used to specify a folder (or directory) set aside for Web pages, but there are many ways to specify the location of Web pages. Sometimes names in URLs 
are case-sensitive, depending on the operating system installed on the computer system containing the Web page. Thus, if you type myname instead of 
myName in the above URL, it may not work. Users of Windows computers should note the use of forward slashes rather than backslashes to separate folders 
(or directories).

Comienzan con el prefijo http://, para indicar que se está utilizando el Protocolo de transferencia de hipertexto (HTTP). Existen algunas variaciones, 
como https, que indica que la dirección que sigue reside en un servidor seguro, como se requiere para transacciones financieras, por ejemplo. El resto 
de la dirección identifica un servidor web y luego una carpeta o directorio en un sistema informático en myUniversity para alguien llamado myName. La 
extensión .edu identifica este sitio como perteneciente a una institución educativa, de la misma manera que .gov y .com identifican sitios 
gubernamentales y comerciales. El símbolo ~ se utiliza a menudo para especificar una carpeta (o directorio) reservada para páginas web, pero hay muchas 
formas de especificar la ubicación de las páginas web. A veces, los nombres en las URL distinguen entre mayúsculas y minúsculas, según el sistema 
operativo instalado en el sistema informático que contiene la página web. Por lo tanto, si escribe myname en lugar de myName en la URL anterior, es 
posible que no funcione. Los usuarios de computadoras con Windows deben tener en cuenta el uso de barras diagonales en lugar de barras invertidas para 
separar carpetas (o directorios).


The index.htm (or index.html) file contains the home page for this individual. By default, the index.htm file is automatically opened, if it exists, 
whenever this URL is accessed. That is, the address

El archivo index.htm (o index.html) contiene la página de inicio de esta persona. De forma predeterminada, el archivo index.htm se abre 
automáticamente, si existe, cada vez que se accede a esta URL. Es decir, la dirección


http://www.myUniversity.edu/~myName/

is equivalent to the address that includes the index.htm file name.

As they were being developed, the documents discussed in this book resided neither on the Internet nor on an intranet. Rather, they were simply stored 
in a folder on a computer and accessed through the file menu in a browser, just as you would access a file with any other software application. For 
example, the “address” on my computer for the first document in this text is

Mientras se desarrollaban, los documentos analizados en este libro no residían ni en Internet ni en una intranet. Más bien, simplemente se almacenaban 
en una carpeta de una computadora y se accedía a ellos a través del menú de archivos de un navegador, tal como se accedería a un archivo con cualquier 
otra aplicación de software. Por ejemplo, la “dirección” en mi computadora para el primer documento de este texto es


file:///C:/Documents%20and%20Settings/David/Desktop/
JavaScript/JavaScriptCode/HelloWorld.htm

(Spaces are represented by the hexadecimal code %20 and, yes, there are three forward slashes following file:)

You should create a separate folder on your computer as you work through the examples in this book and write your own documents. You could make 
documents you create yourself accessible on the Internet or an intranet by placing them on a Web server. For example, if you are taking a course based 
on this book, your instructor may require you to post homework assignments on a Web site.

Debe crear una carpeta separada en su computadora mientras trabaja con los ejemplos de este libro y escribe sus propios documentos. Puede hacer que los 
documentos que cree usted mismo sean accesibles en Internet o en una intranet colocándolos en un servidor web. Por ejemplo, si está tomando un curso 
basado en este libro, su instructor puede pedirle que publique las tareas en un sitio web.


1.4 Another Example

The following example shows how to include an image in an HTML
document.

Document 1.5 (house.htm)

<html>
<head>
<title>Our New House</title>
<script language="javascript" type="text/javascript">
document.write("<font color='green'>This document was
last modified on "+document.lastModified+"</font>");
</script>
</head>
<body>
<h1>Our New House</h1>
<p>
Here's the status of our new house. (We know you're
fascinated!)</p>
<!—Link to your image goes here. -->
<img src="house.jpg" align="left" /><br />
</body>
</html>

1.4 Another Example
19

There are several image formats that are widely used in HTML documents, including image bitmaps (.bmp), Graphics Interchange Format (.gif), and Joint 
Photographic Experts Group (.jpg).

The original .jpg file has been compressed to reduce its size, and this compression can result in jagged edges where edges should be straight. This 
effect is visible in the house framing and roof lines.

El archivo .jpg original se ha comprimido para reducir su tamaño y esta compresión puede dar como resultado bordes irregulares donde los bordes 
deberían ser rectos. Este efecto es visible en la estructura de la casa y en las líneas del techo.


Within the img element, height and width attributes allow you to control the size of the image display (in pixels). This is not equivalent to actually 
“resizing” the image, as is possible with image-(See Color Example 2 for full-color output.) editing software.5 Hence, it is important to use images 
that initially are sized appropriately. If a very large high-resolution image file is displayed as a very small image, using the height and width 
attributes, the original large file must still be transmitted to the client computer. In view of the fact that high-resolution images can produce very 
large files (>10 Mb), it is important to consider appropriate resolution for images included in HTML documents, even in an age of high-speed broadband 
Internet connections. (The size of the compressed grayscale house.jpg image printed here is about 93 Kb.)

Dentro del elemento img, los atributos de alto y ancho le permiten controlar el tamaño de visualización de la imagen (en píxeles). Esto no equivale a 
“cambiar el tamaño” de la imagen, como es posible con el software de edición de imágenes (consulte el Ejemplo de color 2 para obtener resultados a todo 
color).5 Por lo tanto, es importante utilizar imágenes que inicialmente tengan el tamaño adecuado. Si un archivo de imagen muy grande de alta 
resolución se muestra como una imagen muy pequeña, utilizando los atributos de alto y ancho, el archivo grande original aún debe transmitirse a la 
computadora cliente. En vista del hecho de que las imágenes de alta resolución pueden producir archivos muy grandes (>10 Mb), es importante considerar 
la resolución adecuada para las imágenes incluidas en documentos HTML, incluso en una era de conexiones a Internet de banda ancha de alta velocidad. 
(El tamaño de la imagen house.jpg comprimida en escala de grises impresa aquí es de aproximadamente 93 Kb).


Document 1.5 could be made into a default home page simply by changing its name to index.htm.

Here is a final admonition that I hope does not sound too preachy: Intellectual honesty and fairness in the use of other people’s material is 
important, no matter what the setting. The image displayed in Document 1.5 was taken by me, of my own house under construction. In other words, I “own” 
this image. Whenever you post images (or other material, for that matter) online, please be careful to respect intellectual property rights. Your 
default approach should be that online materials are copyrighted and cannot be used freely without permission. If you are in doubt about whether you 
have permission to use an image or other material, don’t!

He aquí una advertencia final que espero no suene demasiado sermoneadora: la honestidad intelectual y la justicia en el uso del material de otras 
personas son importantes, sin importar el entorno. La imagen que se muestra en el Documento 1.5 fue tomada por mí, de mi propia casa en construcción. 
En otras palabras, soy "dueño" de esta imagen. Siempre que publique imágenes (u otro material, de hecho) en línea, tenga cuidado de respetar los 
derechos de propiedad intelectual. Su enfoque predeterminado debería ser que los materiales en línea tengan derechos de autor y no puedan usarse 
libremente sin permiso. Si tiene dudas sobre si tiene permiso para usar una imagen u otro material, ¡no lo haga!




