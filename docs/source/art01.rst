A Study of Intuitionistic Fuzzy Graph Using Morphological Operators and Its Application
=======================================================================================

Abstract The study focuses on some properties of **mathematical morphological operators** on **intuitionistic fuzzy graphs**(IFG). Morphological 
operators like 
dilation and erosion and its composition are useful in the application of intuitionistic fuzzy graph. It is extended to study the topological 
properties using the topological data analysis(TDA) with the help of bar codes and betti numbers obtained by constructing minimal spanning trees(MST) 
which extracts topological properties of intuitionistic fuzzy graph. Finally, an algorithm for analyzing spread of disease is presented in this study.

Resumen El estudio se centra en algunas propiedades de los operadores morfológicos matemáticos en grafos difusos intuicionistas (IFG). Operadores 
morfológicos como la dilatación y la erosión, así como su composición, son útiles en la aplicación de grafos difusos intuicionistas. Se amplía el 
estudio de las propiedades topológicas mediante el análisis topológico de datos (TDA) con la ayuda de códigos de barras y números de Betti obtenidos 
mediante la construcción de árboles de expansión mínima (MST), que extraen las propiedades topológicas de los grafos difusos intuicionistas. 
Finalmente, se presenta un algoritmo para analizar la propagación de enfermedades. Keywords Morphological operators · Fuzzy graphs · Betti numbers

**1 Introduction**

**1.1 Mathematical Morphology**

The main idear behind mathematical morphology(MM) [6, 12, 13, 20] is to study the geometric structure of an image by probing or matching it with tiny 
patterns, named structuring elements, at different locations of the image sothat extraction of different parts of the image and their 
interrelations.Nonlinearity of the MM operators,dilation and erosion„makes them suitable for the study of geometric and topological structure of the 
image.

La idea principal detrás de la morfología matemática (MM) [6, 12, 13, 20] es estudiar la estructura geométrica de una imagen sondeándola o comparándola 
con pequeños patrones, llamados elementos estructurantes, en diferentes ubicaciones de la imagen para extraer diferentes partes de la imagen y sus 
interrelaciones. La no linealidad de los operadores MM, dilatación y erosión, los hace adecuados para el estudio de la estructura geométrica y 
topológica de la imagen.

At the initial stage, MM was used to study binary images using set theory.To consider the grey scale or color images,it was necessary to generalize set 
theoretic approach. Ronse and Heijmans in 1990 developed MM operators using complete lattice structure. In this, partial orders are used to indicate 
the relationship between the images. Supremum and inﬁmum are two operations used in this structure. Any operator ∈  : M 1 → M 2 where M 1 and M 2 
are complete lattices is called erosion if it is anti-extensive (that is, ∈ (X) ⊆ X, for X ∈ M 1 ),increasing and distributive over inﬁmum. Any 
operator δ : M 2 → M 1 where M 1 and M 2 are complete lattices is called dilation if it is extensive (that is, X ⊆ δ(Y) for Y ∈ M 2 ),increasing and 
distributive over supremum. The operators δ and ∈  form an adjunction if δ(Y) ≤ X ⇐⇒ Y ≤ ∈ (X), for X ∈ M 1 , Y ∈ M 2 .An operator φ : M 1 → M 
1 is known as opening if it is anti-extensive, increasing and idempotent(φ 2 = φ). Any operator ψ : M 2 → M 2 is known as closing if it is 
extensive,increasing and idempotent. For an adjunction (∈ , δ) between the operators M 1 and M 2 ,opening is the composition δ∈  and the closing is 
the compostion ∈ δ.

En la etapa inicial, MM se utilizó para estudiar imágenes binarias mediante la teoría de conjuntos. Para considerar la escala de grises o las imágenes 
a color, fue necesario generalizar el enfoque de la teoría de conjuntos. En 1990, Ronse y Heijmans desarrollaron operadores MM utilizando una 
estructura reticular completa. En esta, se utilizan órdenes parciales para indicar la relación entre las imágenes. El supremo y el ínfimo son dos 
operaciones utilizadas en esta estructura. Cualquier operador ∈ : M 1 → M 2 donde M 1 y M 2 son reticulados completos se denomina erosión si es 
antiextensivo (es decir, ∈ (X) ⊆ X, para X ∈ M 1 ), creciente y distributivo sobre el ínfimo. Cualquier operador δ : M 2 → M 1 donde M 1 y M 2 son 
redes completas se llama dilatación si es extensivo (es decir, X ⊆ δ(Y) para Y ∈ M 2 ), creciente y distributivo sobre supremo. Los operadores δ y ∈ 
forman una adjunción si δ(Y) ≤ X ⇐⇒ Y ≤ ∈ (X), para X ∈ M 1 , Y ∈ M 2 . Un operador φ : M 1 → M 1 se conoce como apertura si es antiextensivo, 
creciente e idempotente (φ 2 = φ). Cualquier operador ψ : M 2 → M 2 se conoce como cierre si es extensivo, creciente e idempotente. Para una adjunción 
(∈ , δ) entre los operadores M 1 y M 2 , la apertura es la composición δ∈ y el cierre es la composición ∈ δ.

**1.2 Fuzzy Mathematical Morphology**

Authors like Di Gesu, De Baets, Bloch [9–11], Maitre and Nachtegeal [17] explained basic mathematical morphology operators based on fuzzy set theory 
[2, 3, 23], intuitionistic fuzzy set theory and bipolay set theory [1]. This provides alternative methods to extend binary morphology to greyscale 
morphology.

The erosion of fuzzy set μ by fuzzy structural element ϑ in the spatial domain S is given by

.f or all x∈ S, ∈  ϑ (μ) (x) = inf y∈S T [c (ϑ (y − x)) , μ(y)]

The dilation of fuzzy set μ by fuzzy structural element ϑ in the spatial domain S is given by

.f or all x∈ S, ∈  ϑ (μ) (x) = sup y∈S t [ϑ (x − y) , μ(y)]

1.3 Mathematical Morphology and Graphs

Impotance of graphs with vertices and edges are well established in various ﬁelds like decision making. Graphs describe the relationship between the 
members of the set. Neighbours of each data point or vertex is obtained by the edges to which the data point is linked. Vincent [7, 16, 22] deﬁned 
mathematical morphology operators,dilation and erosion, on graphs with vertices and edges. Fuzzy graph [19], extension of graphs to fuzzy sets,can 
manage imprecision and uncertainty in the information. A fuzzy graph is a pair G : (μ, γ ) where μ is a fuzzy subset of a

set S and γ is a fuzzy relation on μ. In fuzzy graph, each vertex and edge have membership functions which lie in the interval [0, 1]. Also sum of 
membership function and its complement of each vertex and edge of a fuzzy graph is unity. In many real situations, the sum will lie in [0,1] so that 
indetermination is possible. In such situations, fuzzy graph is replaced by intuitionistic fuzzy graph (IFG).

1.4 Intuitionistic Fuzzy Graph

An Intuitionistic fuzzy graph (IFG) is of the form [14, 15, 18, 21] G = (G 1 , G 2 = { v1 , μ 1 , γ 1 , μ 2 , γ 2 ), where G 1 , v 2 . . . v n } such 
that μ 1 : G 1 → [0, 1] and γ 1 : G 1 → [0, 1], the membership function and non membership function of the element v i ∈ G 1 respectively and 0 ≤ μ 
1 (v i ) + γ 1 (v i ) ≤ 1 for every v i ∈ G 1 ,

i = 1, 2, . . . n.

G 2 ⊆ G 1 × G 1 where μ 2 : G 2 → [0, 1] and γ 2 : G 2 → [0, 1] are such that

(a) μ 2 ( e v i v j ) ≤ min ( μ 1 (v i ) , μ 1 ( v j )) .

(b) γ 2 ( e v i v j ) ≤ max ( γ 1 (v i ) , γ 1 ( v j )) .

(c) 0 ≤ μ 2 ( e v i v j ) 2, . . . n.

+

γ2 

( e v i v j )

≤

1 for every edges ev i v j 

.

∈

G 2 ., i = 1, 2, . . . n, j = 1,

In the case of IFG, sum of membership function and non-membership function of each vertices and edges in IFG should lie in the interval [0, 1]. So 
there is a space for indetermination.

A Intuitionistic fuzzy graph G i = ( G 1 i , G 2 i ) . is said to be IF subgraph of IFG

G = (G 1 , G 2 ) of G 1 i ⊆ G 1 . and G 2 i ⊆ G2 . 

.μ 1i (v k ) ≤ μ 1 (v k ) , γ 1i (v k ) ≥ γ 1 (v k ) for all v k ∈ G1 i 

.μ 2i e v k v l ≤ μ 2 e v k v l , γ 2i e v k v l ≥ γ 2 e v k v l for all e v k v l ∈ G 2 i . ( ) ( ) ( ) ( )

1.5 Spanning Tree

Let G be a connected graph. A tree is a spanning tree of G if it is a subgraph of G and it contains all vertices of G. A spanning tree with the 
smallest weight in a weighted fuzzy graph is a minimal spanning tree(MST).

Example 1.1 Consider the intuitionistic fuzzy graph G = (G 1 , G 2 , μ 1 , γ 1 , μ 2 , γ 2 ) with vertex set G 1 = { v 1 , v 2 , v 3 , v 4 , v 5 , v 6 
, v 7 } and edge set G 2 == } e v 1 v 2 , e v 2 v 3 , e v 1 v 4 , e v 3 v 4 , e v 4 v 5 , e v 4 v 7 , e v 5 v 6 ., e v 6 v 7 { . in Fig. 1. For v 1 , 
sum of membership and nonmembership functions = .2 + .5 = .7 which lies inside [0,1]. This true for each vertices in the IFG G in Fig. 1. Member ship 
function of the edge e v 1 v 2 . is the less than or equal to the minimum of membership functions of its end vertices v 1 and v 2 and Non-

member ship function of the edge e v 1 v 2 . is the less than or equal to the maximum of the non-membership functions of its end vertices v 1 and v 2 .

.μ 2 e v 1 v 2 ≤ min { μ 1 (v 1 ) , μ 1 (v 2 ) } = min { .2, .3 } = .2. ( )

.γ 2 e v 1 v 2 ≤ max { γ 1 (v 1 ) , γ 1 (v 2 ) } = max { .5, .2 } = .5 ( )

This is true for all other edges of given IFG in Fig. 1. Therefore G is a n IFG.

Information of data from graph can be done using topological data analysis. Now topological data analysis is brifed below.

1.6 Topological Data Analysis

Topological data analysis (TDA) [8] focuses on analyzing shapes and topological structures of dataset by which one can extract information [4, 5]. It 
is good enough to infer high dimensional structure from low dimensional representations. With the help of theories of algebraic topology and persistent 
homology, it is good enough to change the data set into simplicial complexes and encode this into barcodes named betti numbers.

1.7 Betti Numbers

A set consisting of points, line segments, triangles or tetrahedron to arbitrary dimensions is termed as simplicial complexes. Betti numbers are used 
to distinguish topological spaces based on the connectivity of simplicial complexes.

1. Betti number for 0-dimensional simplicial complexes b 0 is the number of connected components.

2. Betti number for 1-dimensional simplicial complexes b 1 is the number of one-dimensional or “circular” holes

IFG with no holes. b 1 = 0, b 0 = 1

3. Betti number for 2-dimensional simplicial complexes b 2 is the number of two-dimensional “voids” or “cavities”.

IFG with no holes. b 1 = 1, b 0 = 1, b 2 = 0

The Poincaré polynomial is the generating function of its Betti numbers which is of the form b 0 + b 1 x + b 2 x 2 .

1.8 Barcodes

A parameter,cut off distance ∈ , has to be selected for converting data point to simplicial complex.If parameter is too small,all points are separated 
and so no structure is not clear.If it is too large,then data points are all connected and complex is a single high dimensional simplex and no 
topological holes exist.Selecting appropriate scale for datapoint is a difﬁcult task.Each bar represents a hole and length of bar represents the 
persistence. With barcode, we can ﬁlter out the short bars as topological noise and long bars as persistence topological features.

In the next section,we deﬁne neighbouring vertices and edges as p n adjacency vertices and p n adjacency edges. We also explain mathematical 
morphology operators dilation, erosion, opening and closing with example.

2

Mathematical Morphology Operators on IFG

Deﬁnition 2.1 Two vertices v l and v k in G i in F . are p n adjacency vertices (n path adjacency vertices) if they are connected by almost n edges. 
We represent it as v l p n adjv k . Two edges e v l v k . and e v m v n . in G i in F . are p n adjacency edges if either v l or v k is connected to v 
m or v n by at most n edges.

References

1. Atanassov, K.: Intuitionistic Fuzzy Sets: Theory and Applications. Springer, Heidelberg (1999)

2. Baets, D., Kerre, E., Gadan, M.: The fundamentals of fuzzy mathematical morphology part 1:

basic concepts. Int. J. Gen. Syst. 23, 155–171 (1995)

3. De Baets, B., Kerre, E., Gupta, M.: The fundamentals of fuzzy mathematical morphology: part 2: Idempotence, convexity and Decoposition. Int. J. Gen. 
Syst. 23, 307–322 (1995)

4. Carlsson, G., Zomorodian, A., Collins, A., Guibas, L.: Persistence barcodes for shapes. Intl. J.

Shape Modeling. 11, 149–187 (2005)

5. Edelsbrunner, H., Letscher, D., Zomorodian, A.: Topological persistence and simpliﬁcation.

Discrete Comput. Geom. 28(4), 511–533 (2002)

6. Heijmans, H.J.A.M., Ronse, C.: The algebraic basis of mathematical morphology. I dilations and erosions. Comput. Vision Gr. Image Process. 50, 
245–295 (1990)

7. Henk Heijmans & Luc Vincent: Graph morphology in image analysis. In: Mathematical Morphology in Image Processing, pp. 171–203 (1992)

8. He-Liang Huang, Xi-Lin Wang, Peter P. Rohde, Yi-Han Luo, You-Wei Zhao, Chang Liu, Li Li, Nai-Le Liu, Chao-Yang Lu, and Jian-Wei Pan, Demonstration 
of Topological Data Analysis on a Quantum Processor 2022

9. Bloch, I.: Fuzzy sets for image processing and understanding. Fuzzy Sets Syst. 281, 280–291 (2015)

10. Bloch, I.: Mathematical morphology on bipolar fuzzy sets: general algebraic framework. Int.

J. Approx. Reason. 53, 1031–1060 (2012)

11. Bloch, I., Blusseau, S., Perez, R.P., Puybareau, E., Tochon, G.: On some Association between Mathematical Morphology and Artiﬁcial Intelligence, 
Discrete Geometry and Mathematical Morphology, pp. 457–469 (2021)

12. Serra, J.: Image Analysis and Mathematical Morphology, vol. 1. Academic, London (1982)

13. Serra, J.: Image Analysis and Mathematical Morphology, vol. 2. Academic, London (1988)

14. Karunambigai, K.G., Parvathi, R.: Intuitionistic fuzzy graphs. Int. J. Comput. Intell. Theory Appl. 20, 139–150 (2006)

15. Karunambigai, M.G., Parvathi, R., Kalaivani, O.K.: A study on Atanassov’s intuitionistic fuzzy graphs. In: IEEE International Conference on Fuzzy 
Systems (2011)

16. Najman, L., Cousty, J.: A Graph-Based Mathematical Morphology Reader. Elsevier (2014)

17. Sussner, P., Nachtegael, M., Mélange, T., Deschrijver, G., Esmi, E., Kerre, E.: Interval-valued and intuitionistic fuzzy mathematical morphologies 
as special cases of LL-fuzzy mathematical morphology. J. Math. Imaging Vision. 43, 50–71 (2012)

18. Parvathi, R, Karunambigai, M.G.: Intuitionistic Fuzzy Graphs, Computational Intelligence, Theory and Applications (2006)

19. Rosenfeld, A.: Fuzzy Graphs. In: Zadeh, L.A., Fu, K.S., Tanka, K., Shimura, M. (eds.) Fuzzy Sets and their Applications to Cognitive and Decision 
Process, pp. 75–95. Academic, New York (1975)

20. Ronse, C., Serra, J.: Algebraic foundations of morphology. In: Najman, L., Talbot, H. (eds.) Mathematical Morphology: from Theory to Applications, 
pp. 35–80. ISTE / Wiley (2010)

21. Shannon, A., Atanassov, K.: A ﬁrst step to a theory of the intuitionistic fuzzy graphs. In: Lakov,

D. (ed.) Soﬁa, 28–30Proc. of the First Workshop on Fuzzy Based Expert Systems, pp. 59–61 (1994)

22. Vincent, L.: Graphs and mathematical morphology. Signal Process. 16, 365–388 (1989)

23. Zadeh, L.A.: Fuzzy sets. Inf. Control. 8, 338–353 (1965)


