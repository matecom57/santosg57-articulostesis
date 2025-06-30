Curve Propagation, Level Set Methods
===================================

and Grouping
N. Paragios

Abstract Image segmentation and object extraction are among the most
well addressed topics in computational vision. In this chapter we present a
comprehensive tutorial of level sets towards a flexible frame partition paradigm that
could integrate edge-drive, regional-based and prior knowledge to object extraction.
The central idea behind such an approach is to perform image partition through the
propagation planar curves/surfaces. To this end, an objective function that aims to
account for the expected visual properties of the object, impose certain smoothness
constraints and encode prior knowledge on the geometric form of the object to be
recovered is presented. Promising experimental results demonstrate the potential of
such a method.

1 Introduction

Image segmentation has been a long term research initiative in computational vision.
Extraction of prominent edges [14] and discontinuities between in-homogeneous
image regions was the first attempt to address segmentation. Statistical methods
that aim to separate regions according to their visual characteristics was an attempt
to better address the problem [11], while the snake/active contour model [16] was a
breakthrough in the the domain.
Objects are represented using parametric curves and segmentation is obtained
through the deformation of such a curve towards the lowest potential of an objective
function. Data-driven as well as internal smoothness terms were the components of
such a function. Such a model refers to certain limitations like, the initial conditions,
the parameterisation of the curve, the ability to cope with structures with multiple
components, and the estimation of curve geometric properties.


Balloon models [8] where a first attempt to make the snake independent with
respect to the initial conditions, while the use of regional terms forcing visual
homogeneity [45] was a step further towards this direction. Prior knowledge was
also introduced at some later point [37] through a learning stage of the snake
coefficients. Geometric alternatives to snakes [3] like the geodesic active contour
model [4] were an attempt to eliminate the parameterisation issue.

Curves are represented in an implicit manner through the level set method [24].
Such an approach can handle changes of topology and provide sufficient support to
the estimation of the interface geometric properties. Furthermore, the use of such
a space as an optimisation framework [44], and the integration of visual cues of
different nature [25] made these approaches quite attractive to numerous domains
[23]. One can also point recent successful attempts to introduce prior knowledge
[19, 32] within the level set framework leading to efficient object extraction and
tracking methods [33].

To conclude, curve propagation is an established technique to perform object
extraction and image segmentation. Level set methods refer to a geometric
alternative of curve propagation and have proven to be a quite efficient optimisation
space to address numerous problems of computational vision. In this chapter, first
we present the notion of curve optimisation in computer vision, then establishes
a connection with the level set method and conclude with the introduction of
ways to perform segmentation using edge-driven, statistical clustering and prior
knowledge terms.

2 On the Propagation of Curves

Let us consider a planar curve  : [0, 1] ! R  R defined at a plane . The most
general form of the snake model consists of:

E./ D
1
s
0
. ̨Eint..p// C ˇEimg.I ..p/// C

Eext..p///dp (1)

where I is the input image, Eint [Dw1j0 j C w2j00j] imposes smoothness constraints (smooth derivatives), Eimg [D  jrI j] makes the curve to be attracted
from the image features (strong edges), Eext encodes either user interaction or prior
knowledge and  ̨, ˇ, are coefficients that balance the importance of these terms.

The calculus of variations can be used to optimise such a cost function. To this
end, a certain number of control points are selected along the curve, and the their
positions are updated according to the partial differential equation that is recovered
through the derivation of E() at a given control point of . In the most general case
a flow of the following nature is recovered:

.pI
/ D . ̨Fgm./ C ˇFimg.I / C

where N is the inward normal and Fgm depends on the spatial derivatives of the
curve, the curvature, etc. On the other hand, Fimg is the force that connects the
propagation with the image domain and Fpr() is a speed term that compares the
evolving curve with a prior and enforces similarity with such a prior. The tangential
component of this flow has been omitted since it affects the internal position of the
control points and doesn’t change the form of the curve itself.

Such an approach refers to numerous limitations. The number and the sampling
rule used to determined the position of the control points can affect the final
segmentation result. The estimation of the internal geometric properties of the
curve is also problematic and depends on the sampling rule. Control points move
according to different speed functions and therefore a frequent re-parameterisation
of the contour is required. Last, but no least the evolving contour cannot change the
topology and one cannot have objects that consist of multiple components that are
not connected.

2.1 Level Set Method

The level set method was first introduced in [10] and re-invented in [24] to
track moving interfaces in the community of fluid dynamics and then emerged in
computer vision [3, 21]. The central idea behind these methods is to represent the
(closed) evolving curve  with an implicit function that has been constructed as
follows:

.s/ D
8
<
:
0; s 2 
 –; s 2 i n
C –; s 2 out

where epsilon is a positive constant, in the area inside the curve and out the area
outside the curve as shown in [Fig. (1)]. Given the partial differential equation that
dictates the deformation of  one now can derive the one for using the chain rule
according to the following manner:

@
@
. .pI
// D
. .pI
//
@
@ .pI
/ 
@
„ ƒ‚ ... F N
C @
@
D F .r
 N / C
D 0 (3)

Let us consider the arc-length parameterisation of the curve (c). The values of
along the curve are 0 and therefore taking the derivative of along the curve 
will lead to the following conditions:

@
..c//
@c D 0 ! @
@ ..c// 
@
@c D 0 ! r

.c/  T .c/ D 0 (4)

where T (c) is the tangential vector to the contour. Therefore one can conclude that
r is orthogonal to the contour and can be used (upon normalisation) to replace the
inward normal h N D  r jr j i leading to the following condition on the deformation
of

:

F j
j C
D 0 !
D F j
j (5)

Such a flow establishes a connection between the family of curves  that have
been propagated according to the original flow and the ones recovered through the
propagation of the implicit function . The resulting flow is parameter free, intrinsic,
implicit and can change the topology of the evolving curve under certain smoothness
assumptions on the speed function F. Last, but not least, the geometric properties of
the curve like its normal and the curvature can also be determined from the level set
function [24]. One can see a demonstration of such a flow in [Fig. (2)].

In practice, given a flow and an initial curve the level set function is constructed
and updated according to the corresponding motion equation in all pixels of the
image domain. In order to recover the actual position of the curve, the marching
cubes algorithm [20] can be used that is seeking for zero-crossings. One should pay
attention on the numerical implementation of such a method, in particular on the
estimation of the first and second order derivatives of, where the ENO schema
[24] is the one to be considered. One can refer to [36] for a comprehensive survey
of the numerical approximation techniques.

In order to decrease computational complexity that is inherited through the
deformation of the level set function in the image domain, the narrow band
algorithm [7] was proposed. The central idea is update the level set function only
within the evolving vicinity of the actual position of the curve. The fast marching
algorithm [35, 40] is an alternative technique that can be used to evolve curves
in one direction with known speed function. One can refer to earlier contribution
in this book [Chap. 7] for a comprehensive presentation of this algorithm and its
applications. Last, but not least semi-implicit formulations of the flow that guides
the evolution of were proposed [12, 42] namely the additive operator splitting.
Such an approach refers to a stable and fast evolution using a notable time step
under certain conditions.

2.2 Optimisation and Level Set Methods

The implementation of curve propagation flows was the first attempt to use the level
set method in computer vision. Geometric flows or flows recovered through the
optimisation of snake-driven objective functions were considered in their implicit
nature. Despite the numerous advantages of the level set variant of these flows,
their added value can be seen as a better numerical implementation tool since the
definition of the cost function or the original geometric flow is the core part of the
solution. If such a flow or function does not address the desired properties of the
problem to be solved, its level set variant will fail. Therefore, a natural step forward
for these methods was their consideration in the form of an optimisation space.

Such a framework was derived through the definition of simple indicator func-
tions as proposed in [44] with the following behaviour

ı .
/ D
 0;
¤ 0
1;
D 0 ; H .
/ D
8
<
:
1;
> 0
0;
D 0
0;
< 0

(6)

Once such indicator functions have been defined, an evolving interface  can be
considered directly on the level set space as

 D fs 2 W ı .

/ D 1g (7)

while one can define a dual image partition using the H indicator functions as:

i n D fs 2 W H .
/ D 1g
out D fs 2 W H .

/ D 0g ; i n [ out D (8)

Towards continuous behaviour of the indicator function [H ] , as well as well-
defined derivatives [ı] in the entire domain a more appropriate selection was
proposed in [44], namely the DIRAC and the HEAVISIDE distribution:

ı ̨ .
/ D
( 0 ; j
j >  ̨

1
2 ̨ 
1 C cos 
 ̨
 ; j
j <  ̨ (9)

H ̨ .
/ D
8
ˆ<
ˆ:
1 ;
> ̨
0 ;
< – ̨

1
2

1 C
 ̨ C 1
sin 
 ̨
 ; j
j <  ̨

Such an indicator function has smooth, continuous derivatives and the following
nice property:

@
@
H ̨ .
/ D ı ̨ .
/

Last, but not least one consider the implicit function to be a signed distance transform D(s, ),

.s/ D
8
<
:
0; s 2 
D .s; / ; s 2 i n
 D .s; / ; s 2  i n D out




Such a selection is continuous and supports gradient descent minimisation tech-
niques. On the other hand it has to be maintained, and therefore frequent re-
initialisations using either the fast marching method [35] or PDE-based approaches

[38] were considered. In [13] the problem was studied from a different perspective.
The central idea was to derive the same speed function for all level lines - the one of
the zero level set - an approach that will preserve the distance function constraint.

3 Data-driven Segmentation
The first attempt to address such task was made in [21] where a geometric flow
was proposed to image segmentation. Such a flow was implemented in the level set
space and aimed to evolve an initial curve towards strong edges constrained by the
curvature effect. Within the last decade numerous advanced techniques have taken
advantage of the level set method for object extraction.

3.1 Boundary-based Segmentation
The geodesic active contour model [4, 17] - a notable scientific contribution in the
domain - consists of
E ./ D
Z 1
0
g .jrI ..p//j /
ˇ
ˇ0
.p/ˇ
ˇ dp (11)
where I is the output of a convolution between the input image and a Gaussian
kernel and g is a decreasing function of monotonic nature. Such a cost function
seeks a minimal length geodesic curve that is attracted to the desired image features,
and is equivalent with the original snake model once the second order smoothness
component was removed. In [4] a gradient descent method was used to evolve
an initial curve towards the lowest potential of this cost function and then was
implemented using the level set method.
A more elegant approach is to consider the level set variant objective function of
the geodesic active contour;
E .
/ D
“
ı ̨ .
.!// g .jrI .!/j/jr

.!/j d! (12)
where  is now represented in an implicit fashion with the zero-level set of
. One

can take take the derivative of such a cost function according to
:

D ı ̨.
/ div 
g.I/ r
jr
j


(13)

where ! and jr I  (!)j were omitted from the notation. Such a flow aims to shrink
an initial curve towards strong edges. While the strength of image gradient is a solid
indicator of object boundaries, initial conditions on the position of the curve can
be issue. Knowing the direction of the propagation is a first drawback (the curve
has either to shrink or expand), while having the initial curve either interior to the
objects or exterior is the second limitation. Numerous provisions were proposed to
address these limitations, some of them aimed to modify the boundary attraction
term [29], while most of them on introducing global regional terms [45].

3.2 Region-based Segmentation

In [26] the first attempt to integrate edge-driven and region-based partition com-
ponents in a level set approach was reported, namely the geodesic active region

model. Within such an approach, the assumption of knowing the expected intensity
properties (supervised segmentation) of the image classes was considered. Without
loss of generality, let us assume an image partition in two classes, and let rin(I ),
rout(I ) be regional descriptors that measure the fit between an observed intensity
I and the class interior [rin(I )] and exterior to [rout(I )] the curve. Under such an
assumption one can derive a cost function that separates the image domain into two
regions:
• according to a minimal length geodesic curve attracted by the regions boundaries,
• according to an optimal fit between the observed image and the expected
properties of each class,

E .
/ D w
“
ı ̨ .
.!// g .jrI .!/j/ jr
.!/j d!

C
“
H ̨ .
.!// ri n .I /d! C
“
.1  H ̨ .

.!/// rout .I /d!
(14)

where w is a constant balancing the contributions of the two terms. One can see this

framework as an integration of the geodesic active contour model [4] and the region-
based growing segmentation approach proposed in [45]. The objective is to recover

a minimal length geodesic curve positioned at the object boundaries that creates
an image partition that is optimal according to some image descriptors. Taking the
partial derivatives with respect to

, one can recover the flow that is to be used

towards such an optimal partition:
D ı ̨.
/.ri n.I /  .rout.I // C !ı ̨.
/ div 
g.I/ r
jr
j

(15)

Fig. 3 Multi-class image segmentation [27] through integration of edge-driven and region-based
image metrics; The propagation with respect to the four different image classes as well as the final
presentation result is presented
where the term ı ̨(

) was replaced with ı ̨(

) since it has a symmetric behaviour.
In [26] such descriptor function was considered to be the -log of the intensity
conditional density [pin (I ), pin (I )] for each class
ri n .I / D  log .pi n .I // ; rout .I / D  log .pout .I //
In [34] the case of supervised image segmentation for more than two classes
was considered using the frame partition concept introduced in [44]. One can also
refer to other similar techniques [1]. Promising results were reported from such
an approach for the case of image in [27] [Figure (3)] and for supervised texture
segmentation in [28].
However, segmentation often refers to unconstrained domains of computational
vision and therefore the assumption of known appearance properties for the objects
to be recovered can be unrealistic. Several attempts were made to address this
limitation. To this end, in [5, 43] an un-supervised region based segmentation

approach based on the Mumford-Shah [22] was proposed. The central idea behind
these approaches of bi-modal [5] and tri-modal [43] segmentation was that image
regions are piece-wise constant intensity-wise.
The level set variant of the Mumford-Shah [22] framework consists of minimising

E .
; i n; out/ D

w
“
ı ̨ .
.!//jr
.!/j d! C
“
H ̨ .
.!// .I .!/  i n/
2
d!

C
“

1  H ̨ .

.!// .I .!/  out/
2
d!
(16)

where both the image partition [

] and the region descriptors [in, out] for the inner
and the outer region are to be recovered. The calculus of variations with respect to
the curve position and the piece-wise constants can be consider to recover the lowest
potential of such a function,

i n D
“
H .
/I .!/d!
“
H .
/d!
; out D
“
.1  H .
//I .!/d!

“
.1  H .
// d!
;

D ı ̨ .
/ h
..I .!/  i n//2  .I .!/  out/

2 // C w div  r
jr
j
i
(17)

Such a framework was the basis to numerous image segmentation level set
approaches, while certain provisions were made to improve its performance. In [18]
the simplistic Gaussian assumption of the image reconstruction term (piece-wise
constant) was replaced with a non-parametric approximation density function while
in [31] a vectorial unsupervised image/texture segmentation approach was proposed.

Last, but not least in [41] the same framework was extended to deal with multi-
class segmentation. The most notable contribution of this approach is the significant

reduction of the computational cost and the natural handling (opposite to [44]) of
not forming neither vacuums nor overlapping regions. Such an approach can address
the N -class partition problem, using log2(N)
level set functions.

4 Prior Knowledge
Computational vision tasks including image segmentation often refer to constrained
environments. Medical imaging is an example where prior knowledge exists on the
structure and the form of the objects to be recovered. One can claim that the level
set method is among the most promising framework to model-free segmentation.

Introducing prior knowledge within such a framework is a natural extension that
could make such level sets an adequate selection to numerous applications like
object extraction, recognition, medical image segmentation, tracking, etc. In [19]
a first attempt to perform knowledge-based segmentation was reported, while later
numerous authors have proposed various alternatives [6, 9, 32, 39].
4.1 Average Models
Statistical representation of shapes is the first step of such an approach. Given a set
of training examples, one would like to recover a representation of minimal length
that can be used to reproduce the training set. To this end, all shapes of the training
set should be registered to the same pose. Numerous methods can be found in the
literature for shape registration, an adequate selection for building shape models in
the space of implicit functions is the approach proposed in [15] where registration is
addressed on this space. Without loss of generality we can assume that registration
problem has been solved.
Let SA D f
1,
2, ::: ,
ng be the implicit representations of n training samples
according to a signed Euclidean distance transform. Simple averaging of the shape
belonging to the training set can be used to determine a mean model

M D 1
n
Xn
iD1
i (18)
that was considered in [9, 19, 39]. Such a model is a not an signed Euclidean implicit
function, an important limitation. However, one can recover a mean model in the
form of a planar curve M through the marching cubes algorithm [20]. Once such
a model has been determined, one can impose shape prior knowledge through the
constraint that the object to be recovered at the image plane  that is a clone of the
average shape M according to some transformation:

 D A .M / (19)
where A can be a linear or non-linear transformation. In [6] prior knowledge has
been considered in the form of a mean represented with a signed distance function.
Once such a model was recovered, it was used [6] within the geodesic active contour
model [4] to impose prior knowledge in the level set space:
E .
; A / D
“
ı ̨ .
/ 
g .jrI j/jr
j C 
2
M .A .!// d! (20)
where A D (s, , (T x, T y)) is a similarity transformation that consists of a scale
factor [s], a rotation component [] and a translation vector (T x, T y).
M is an
implicit representation of the mean model according to a distance function and 
is a constant that determines the importance of the prior term. Such an objective

function aims at finding a minimal length geodesic curve that is attracted to the
object boundaries and is not far from being a similarity transformation of the prior
model:

M .A .M / ! 0

Such an approach can be very efficient when modelling shapes of limited variation.
On the other hand, one can claim that for shapes with important deviation from
the mean model the method could fail. Furthermore, given the small number of
constraints when determining the transformation between the image and the model
space the estimation [A ] could become a quite unstable task.
Towards a more stable approach to determine the optimal transformation between
the evolving contour and the average model, in [32] a direct comparison between the
contour implicit function and the model distance transform was used to enforce prior
knowledge:

.!/ D
M .A .!//

Despite the fact that distance transforms are robust to local deformations, invariant

to translation and rotation, they are not invariant to scale variations. Slight modifi-
cation of the above condition [30] could also lead to scale invariant term:

s
.!/ D
M .A .!//

The minimisation of the SSD between the implicit representations of the evolving
contour and the distance transform of the average prior model can be considered to
impose prior knowledge, or
E .
; A / D
“
ı ̨ .
/ .s
.!/ 
M .A .!///2

d! (21)
a term that is evaluated within the vicinity of the zero level-set contour (modulo
the selection of  ̨). The calculus of variations within a gradient descent method can
provide the lowest potential of the cost function. Two unknown variables are to be
recovered, the object position (form of function
),

d
d
D  @
@
ı ̨ .
/
.. s

M .A /
2
„ ƒ‚ ... area force
 2ı ̨ .
/ s .s

M .A // „ ƒ‚ ... shape consistency force
(22)

This flow consists of two terms: (i) a shape consistency force that updates the
interface towards a better local much with the prior and (ii) a force that aims at
updating the level set values such that the region on which the objective functions is
evaluated ( ̨,  ̨) becomes smaller and smaller in the image plane. In order to better

understand the influence of this force, one can consider a negative

value, within
the range of ( ̨,  ̨); Such a term does not change the position of the interface and
therefore it could be omitted:
d
d
D 2ı ̨ .
/ s .s

M .A // (23)
Towards recovering the transformation parameters [A ] between the evolving
contour and the average model, a gradient descent approach could be considered
in parallel: A
8
ˆˆˆˆˆˆ<
ˆˆˆˆˆˆ:
d
dt  D 2
R
ı– .
/ .s

M . A // .r
M . A 
 @
@ A 
d

d
dt Tx D 2
R
ı– .
/ .s

M . A // .r
M . A

 @
@Tx A

d

d
dt Ty D 2
R
ı– .
/ .s

M . A // .r
M . A

 @
@Ty A

d

d
dt s D 2
R
ı– .
/ .s

M . A // .–
C r
M . A 
 @
@s A 
d
(24)

One can refer to very promising results - as shown in [Fig. (4)] - on objects that
refer to limited shape variability using such a method [32]. However, often the object
under consideration presents important shape variations that cannot be accounted for
with simple average models. Decomposition and representation of the training set
through linear shape spaces is the most common method to address such a limitation.
4.2 Prior Knowledge through Linear Shape Spaces
In [19] a principal component analysis on the registered set of the space of distance
functions (training examples) was considered to recover a model that can account for
important shape variations. Similar approach was consider in [2, 33, 39]. Principal
component analysis refers to a linear transformation of variables that retains - for
a given number n of operators - the largest amount of variation within the training
data.
Let
iD1 ::: n be a column vector representation of the training set of n implicit
function elements registered to the same pose. We assume that the dimensionality
of this vector is d. Using the technique introduced in [32] one can estimate a mean
vector
M that is part of the space of implicit functions and subtract it from the
input to obtain zero mean vectors f
Qi D
i –
M g.

Given the set of training examples and the mean vector, one can define the d d
covariance matrix:

X
Q D E  ̊
Qi
Q
i
(25)
It is well known that the principal orthogonal directions of maximum variation
are the eigenvectors of P
Q .

One can approximate P

Q with the sample covariance matrix that is given by

QN
Q
N
where
QN is the matrix formed by concatenating the set of implicit

functions  ̊
Q
i
iD1:::n: Then, the eigenvectors of P

Q can be computed through the

singular value decomposition (SVD) of
Q
N :
QN D UDUT (26)

The eigenvectors of the covariance matrix P

Q are the columns of the matrix U
(referred to as the basis vectors henceforth) while the elements of the diagonal
matrix D are the square root of the corresponding eigenvalues and refer to the
variance of the data in the direction of the basis vectors. Such information can
be used to determine the number of basis vectors (m) required to retain a certain
percentage of the variance in the data.
Then, one can consider a linear shape space that consists of the (m) basis vectors
required to retain a certain percentage of the training set:

D
M C Xm
j D1
j Uj (27)

Fig. 5 Level set methods, prior knowledge, linear shape spaces and Object Extraction [33];
segmentation of lateral brain ventricles (Top Left) surface evolution, (Top Right) projected surface
in the learning space and ground-truth surface (from the training set), (Bottom) surface cut and its
projection in the learning space during surface evolution

Such linear space can now be used as prior model that refers to a global transfor-
mation A of the average model

M and its local deformation  D (1 ,..., m)
through a linear combination of the the basis vectors Uj. Then, object extraction is
equivalent with finding a shape for which there exists such a transformation that
will map each value of current representation to the “best” level set representation
belonging to the class of the training shapes:

E .
; A ; / D
Z
ı– .
/
0
@s

0
@
M .A / CXm
j D1
j Uj .A /
1
A
1
A
2
d (28)
where the rotation factor Uj (A ) has to be accounted for when applying the principal
modes of variations to deform the average shape.
In order to minimise the above functional with respect to the evolving level set
representation, the global linear transformation A and the modes weights j, we
use the calculus of variations. The deformation of

is guided by a flow similar to
(1.22) that is also the case with respect to the pose parameters A as shown in ().
Last, but not least he differentiation with respect to the coefficients  D (1,...,
m) leads to a linear system that has a closed form solution V  D b with:


V .i; j / D R
ı– .
/ Ui .A / Uj .A /

b.i / D R
ı– .
/ .s

M . A // Ui .A / (29)
where V is a m  m positive definite matrix. Such an approach as shown
in [Fig. (5)] - can cope with important shape variations under the assumption that
the distribution of the training set is Gaussian and therefore its PCA is valid.

5 Discussion
In this chapter, we have presented an approach to object extraction through the
level set method that is implicit, intrinsic, parameter free and can account for
topological changes. First, we have introduced a connection between the active
contours, propagation of curves and their level set implementation. Then, we have
considered the notion of implicit functions to represent shapes and define objective

functions in such spaces to perform object extraction and segmentation. Edge-
driven as well as global statistical-based region-defined segmentation criteria were

presented. In the last part of the chapter we have presented prominent techniques to
account for prior knowledge on the object to be recovered. To this end, we have
introduced constraints of increasing complexity proportional to the spectrum of
expected shape deformations that constraints the evolving interface according to
the prior knowledge. Therefore one can conclude that the level set method is an
efficient technique to address object extraction, is able to deal with important shape
deformations, topological changes, can integrate visual cues of different nature and
can account for corrupted, incomplete and occluded data.

References
1. O. Amadieu, E. Debreuve, M. Barlaud, and G. Aubert. Inward and Outward Curve Evolution
Using Level Set Method. In IEEE International Conference on Image Processing, volume III,
pages 188–192, 1999.
2. X. Bresson, P. Vandergheynst, and J. Thiran. A Priori Information in Image Segmentation:
Energy Functional based on Shape Statistical Model and Image Information. In IEEE
International Conference on Image Processing, volume 3, pages 428–428, Barcelona, Spain,
2003.
3. V. Caselles, F. Catté, B. Coll, and F. Dibos. A geometric model for active contours in image
processing. Numerische Mathematik, 66(1):1–31, 1993.
4. V. Caselles, R. Kimmel, and G. Sapiro. Geodesic Active Contours. In IEEE International
Conference in Computer Vision, pages 694–699, 1995.
5. T. Chan and L. Vese. An Active Contour Model without Edges. In International Conference
on Scale-Space Theories in Computer Vision, pages 141–151, 1999.
6. Y. Chen, H. Thiruvenkadam, H. Tagare, F. Huang, and D. Wilson. On the Incorporation of
Shape Priors int Geometric Active Contours. In IEEE Workshop in Variational and Level Set
Methods, pages 145–152, 2001.

7. D. Chopp. Computing Minimal Surfaces via Level Set Curvature Flow. Journal of Computa-
tional Physics, 106:77–91, 1993.

8. L. Cohen. On active contour models and balloons. CVGIP: Image Understanding, 53:211–218,
1991.
9. D. Cremers, N. Sochen, and C. Schnorr. Multiphase Dynamic Labeling for Variational
Recognition-driven Image Segmentation. In European Conference on Computer Vision, pages
74–86, Prague, Chech Republic, 2004.
10. A. Dervieux and F. Thomasset. A finite element method for the simulation of rayleigh-taylor
instability. Lecture Notes in Mathematics,771:145–159, 1979.
11. S. Geman and D. Geman. Stochastic Relaxation, Gibbs Distributions, and the Bayesian
Restoration of Images. IEEE Transactions on Pattern Analysis and Machine Intelligence,
6:721–741, 1984.

12. R. Goldenberg, R. Kimmel, E. Rivlin, and M. Rudzsky. Fast Geodesic Active Contours. IEEE
Transactions on Image Processing, 10:1467–1475, 2001.
13. J. Gomes and O. Faugeras. Reconciling distance functions and level sets. Journal of Visual
Communication and Image Representation, 11:209–223, 2000.
14. R. Haralick. Digital step edges from zero crossing of second directional derivatives. IEEE
Transactions on Pattern Analysis and Machine Intelligence, 6:58–68, 1984.
15. X. Huang, N. Paragios, and D. Metaxas. Registration of Structures in Arbitrary Dimensions:
Implicit Representations, Mutual Information & Free-Form Deformations. Technical Report
DCS-TR-0520, Division of Computer & Information Science, Rutgers University, 2003.

16. M. Kass, A. Witkin, and D. Terzopoulos. Snakes: Active Contour Models. In IEEE Interna-
tional Conference in Computer Vision, pages 261–268, 1987.

17. S. Kichenassamy, A. Kumar, P. Olver, A. Tannenbaum, and A. Yezzi. Gradient flows and
geometric active contour models. In IEEE International Conference in Computer Vision, pages
810–815, 1995.

18. J. Kim, J. Fisher, A. Yezzi, M. Cetin, and A. Willsky. Non-Parametric Methods for Image Seg-
mentation using Information Theory and Curve Evolution. In IEEE International Conference

on Image Processing, 2002.
19. M. Leventon, E. Grimson, and O. Faugeras. Statistical Shape Influence in Geodesic Active
Controus. In IEEE Conference on Computer Vision and Pattern Recognition, pages I:316–322,
2000.
20. W. Lorensen and H. Cline. Marching cubes: a high resolution 3D surface construction
algorithm. In ACM SIGGRAPH, volume 21, pages 163–170, 1987.
21. R. Malladi, J. Sethian, and B. Vemuri. Evolutionary fronts for topology independent shape
modeling and recovery. In European Conference on Computer Vision, pages 1–13, 1994.
22. D. Mumford and J. Shah. Boundary detection by minimizing functionals. In IEEE Conference
on Computer Vision and Pattern Recognition, pages 22–26, 1985.
23. S. Osher and N. Paragios. Geometric Level Set Methods in Imaging, Vision and Graphics.
Springer Verlag, 2003.
24. S. Osher and J. Sethian. Fronts propagating with curvature-dependent speed : Algorithms based
on the Hamilton-Jacobi formulation. Journal of Computational Physics, 79:12–49, 1988.
25. N. Paragios. Geodesic Active Regions and Level Set Methods: Contributions and Applications
in Artificial Vision. PhD thesis, I.N.R.I.A./ University of Nice-Sophia Antipolis, 2000. http://
www.inria.fr/RRRT/TU-0636.html.
26. N. Paragios and R. Deriche. A PDE-based Level Set approach for Detection and Tracking
of moving objects. In IEEE International Conference in Computer Vision, pages 1139–1145,
1998.
27. N. Paragios and R. Deriche. Geodesic Active Contours and Level Sets for the Detection and
Tracking of Moving Objects. IEEE Transactions on Pattern Analysis and Machine Intelligence,
22:266–280, 2000.
28. N. Paragios and R. Deriche. Geodesic Active Regions: A New Framework to Deal with
Frame Partition Problems in Computer Vision. Journal of Visual Communication and Image
Representation, 13:249–268, 2002.
29. N. Paragios, O. Mellina-Gottardo, and V. Ramesh. Gradient Vector Flow Fast Geodesic Active
Contours. In IEEE International Conference in Computer Vision, pages I:67–73, 2001.
30. N. Paragios, M. Rousson, and V. Ramesh. Non-Rigid Registration Using Distance Functions.
Computer Vision and Image Understanding, 2003. to appear.
31. M. Rousson and R. Deriche. A Variational Framework for Active and Adaptative Segmentation
of Vector Valued Images. Technical Report 4515, INRIA, France, 2002.
32. M. Rousson and N. Paragios. Shape Priors for Level Set Representations. In European
Conference on Computer Vision, pages II:78–93, Copenhangen, Denmark, 2002.
33. M. Rousson, N. Paragios, and R. Deriche. Implicit Active Shape Models for 3D Segmentation
in MR Imaging. In Medical Imaging Copmuting and Computer-Assisted Intervention, 2004.
34. C. Samson, L. Blanc-Feraud, G. Aubert, and J. Zerubia. A Level Set Model for Image
Classification. International Journal of Computer Vision, 40:187–197, 2000.

35. J. Sethian. A Review of the Theory, Algorithms, and Applications of Level Set Methods for
Propagating Interfaces. Cambridge University Press, pages 487–499, 1995.
36. J. Sethian. Level Set Methods. Cambridge University Press, 1996.
37. L. Staib and S. Duncan. Boundary finding with parametrically deformable models. IEEE
Transactions on Pattern Analysis and Machine Intelligence, 14:1061–1075, 1992.
38. M. Sussman, P. Smereka, and S. Osher. A Level Set Method for Computing Solutions to
Incomprenissible Two-Phase Flow. Journal of Computational Physics, 114:146–159, 1994.
39. A. Tsai, A. Yezzi, W. Wells, C. Tempany, D. Tucker, A. Fan, A. Grimson, and A. Willsky.
Model-based Curve Evolution Technique for Image Segmentation. In IEEE Conference on
Computer Vision and Pattern Recognition, volume I, pages 463–468, 2001.
40. J. Tsitsiklis. Efficient Algorithms for Globally Optimal Trajectories. In 33rdConference on
Decision and Control, pages 1368–1373, 1994.
41. L. Vese and T. Chan. A Multiphase Level Set Framework for Image Segmentation Using the
Mumford and Shah Model. International Journal of Computer Vision, 50:271–293, 2002.
42. J. Weickert and G. Kuhne. Fast Methods for Implicit Active Contours. In S. Osher and
n. Paragios, editors, Geometric Level Set Methods in Imaging, Vision and Graphics, pages
43–58. Springer, 2003.
43. A. Yezzi, A. Tsai, and A. Willsky. A Statistical Approach to Snakes for Bimodal and Trimodal
Imagery. In IEEE International Conference in Computer Vision, pages 898–903, 1999.
44. H.-K. Zhao, T. Chan, B. Merriman, and S. Osher. A variational Level Set Approach to
Multiphase Motion. Journal of Computational Physics, 127:179–195, 1996.
45. S. Zhu and A. Yuille. Region Competition: Unifying Snakes, Region Growing, and
Bayes/MDL for Multiband Image Segmentation. IEEE Transactions on Pattern Analysis and
Machine Intelligence, 18:884–900, 1996.


