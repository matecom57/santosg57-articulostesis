Optimal control problems with delays in state and control variables subject to mixed control–state constraints art05 - 2008
=============================================================

Optimal control problems with delays in state and control variables are studied. Constraints are imposed
as mixed control–state inequality constraints. Necessary optimality conditions in the form of Pontryagin’s
minimum principle are established. The proof proceeds by augmenting the delayed control problem to a
nondelayed problem with mixed terminal boundary conditions to which Pontryagin’s minimum principle
is applicable. Discretization methods are discussed by which the delayed optimal control problem is
transformed into a large-scale nonlinear programming problem. It is shown that the Lagrange multipliers
associated with the programming problem provide a consistent discretization of the advanced adjoint
equation for the delayed control problem. An analytical example and numerical examples from chemical
engineering and economics illustrate the results.

Se estudian problemas de control óptimo con retrasos en las variables de estado y control. Se imponen 
restricciones como restricciones mixtas de desigualdad control-estado. Se establecen las condiciones de 
optimalidad necesarias mediante el principio del mínimo de Pontryagin. La demostración procede ampliando el 
problema de control retardado a un problema sin retraso con condiciones de contorno terminales mixtas, al que se 
aplica el principio del mínimo de Pontryagin. Se discuten métodos de discretización que transforman el problema 
de control óptimo retardado en un problema de programación no lineal a gran escala. Se demuestra que los 
multiplicadores de Lagrange asociados al problema de programación proporcionan una discretización consistente de 
la ecuación adjunta avanzada para el problema de control retardado. Un ejemplo analítico y ejemplos numéricos de 
ingeniería química y economía ilustran los resultados.

 KEY WORDS: retarded optimal control problems; delays in 
state and control; 
mixed control–state inequality constraints; Pontryagin’s minimum principle; discretization methods; optimal
control of a CSTR reactor; optimal fishing

1. INTRODUCTION
---------------

Differential control systems with delays in state or control variables play an important role in
the modelling of real-life phenomena in various fields of applications. Many papers have been
devoted to delayed (other terminology: time lag, retarded, hereditary) optimal control problems and
the derivation of necessary optimality conditions. Let us briefly review some papers concerning
different classes of control problems. An introduction to time delay control problems can be found
in Oguzt ˇ oreli  ̈ [1]. Kharatishvili [2] was first to provide a maximum principle for optimal control
problems with a constant state delay. In [3], he gave similar results for control problems with pure
control delays. Halany [4] proves a maximum principle for optimal control problems with multiple
constant delays in state and control variables that, however, are chosen to be equal for state and
control. 

Los sistemas de control diferencial con retardos en las variables de estado o de control desempeñan un papel 
importante en el modelado de fenómenos de la vida real en diversos campos de aplicación. Se han dedicado 
numerosos artículos a problemas de control óptimo retardado (otra terminología: retardado, hereditario) y a la 
derivación de las condiciones de optimalidad necesarias. Repasemos brevemente algunos artículos sobre diferentes 
clases de problemas de control. Una introducción a los problemas de control con retardo temporal se puede 
encontrar en Oguzt ˇ oreli ̈ [1]. Kharatishvili [2] fue el primero en proporcionar un principio máximo para 
problemas de control óptimo con un retardo de estado constante. En [3], presentó resultados similares para 
problemas de control con retardos de control puros. Halany [4] demuestra un principio máximo para problemas de 
control óptimo con múltiples retardos constantes en las variables de estado y de control que, sin embargo, se 
eligen para que sean iguales para el estado y el control.

Similar results were obtained by Ray and Soliman [5]. Guinn [6] sketches a simple method
for obtaining necessary conditions for control problems with a constant delay in the state variable.
He suggests to augment the delayed control problem that yields a higher-dimensional undelayed
control problem to which the standard maximum principle is applicable. Banks [7] derives a
maximum principle for control systems with a time-dependent delay in the state variable. Delays
in the control are admitted for systems linear in the control variable. Colonius and Hinrichsen [8]
provide a unified approach to control problems with delays in the state variable by applying the
theory of necessary conditions for optimization problems in function spaces. All articles mentioned
so far do not consider general control or state inequality constraints.

Ray y Soliman [5] obtuvieron resultados similares. Guinn [6] describe un método simple para obtener las 
condiciones necesarias para problemas de control con un retraso constante en la variable de estado. Sugiere 
ampliar el problema de control retrasado para obtener un problema de control sin retraso de mayor dimensión al 
que se aplica el principio del máximo estándar. Banks [7] deriva un principio del máximo para sistemas de control 
con un retraso dependiente del tiempo en la variable de estado. Se admiten retrasos en el control para sistemas 
lineales en la variable de control. Colonius y Hinrichsen [8] proporcionan un enfoque unificado para controlar 
problemas con retrasos en la variable de estado aplicando la teoría de las condiciones necesarias para problemas 
de optimización en espacios de funciones. Todos los artículos mencionados hasta ahora no consideran restricciones 
generales de control o desigualdad de estado.

Angell and Kirsch [9] treat functional differential equations with function-space state inequality
constraints. However, they do not discuss the regularity of the multiplier associated with the state
constraint and do not provide a numerical example with a pure state space constraint. To our
knowledge, optimal control problems with constant delays in state and control variables and mixed
control–state inequality constraints have not yet been considered in the literature. The first goal in
this paper is to derive a Pontryagin-type minimum (maximum) principle for this class of delayed
control problems. 

Angell y Kirsch [9] tratan ecuaciones diferenciales funcionales con restricciones de desigualdad de estado en el 
espacio de funciones. Sin embargo, no analizan la regularidad del multiplicador asociado con la restricción de 
estado ni proporcionan un ejemplo numérico con una restricción pura en el espacio de estados. Hasta donde 
sabemos, los problemas de control óptimo con retardos constantes en las variables de estado y control, y 
restricciones mixtas de desigualdad de control-estado, aún no se han considerado en la literatura. El primer 
objetivo de este trabajo es derivar un principio de mínimo (máximo) de tipo Pontryagin para esta clase de 
problemas de control retardado.

Concerning the development of numerical methods and the numerical treatment
of practical examples, our impression is that this topic has not yet been adequately addressed in the
literature. Bader [10] uses collocation methods to solve the boundary value problem for the retarded
state variable and advanced adjoint variable. He successfully solves several academic examples, but
his method does not give accurate results for the more difficult CSTR reactor problem described in
Soliman and Ray [5, 11]. A similar CSTR reactor problem is considered in Oh and Luus [12] and
Dadebo and Luus [13], who use the differential dynamic programming method with a moderate
number of stages. Therefore, the second goal of this paper is the presentation of discretization and
nonlinear programming methods that provide the optimal state, control and adjoint functions and
allow for an accurate check of the necessary conditions.

Con respecto al desarrollo de métodos numéricos y el tratamiento numérico de ejemplos prácticos, nuestra 
impresión es que este tema aún no se ha abordado adecuadamente en la literatura. Bader [10] utiliza métodos de 
colocación para resolver el problema del valor en la frontera para la variable de estado retardada y la variable 
adjunta avanzada. Resuelve con éxito varios ejemplos académicos, pero su método no proporciona resultados 
precisos para el problema más complejo del reactor CSTR descrito en Soliman y Ray [5, 11]. Un problema similar 
del reactor CSTR es considerado por Oh y Luus [12] y Dadebo y Luus [13], quienes utilizan el método de 
programación dinámica diferencial con un número moderado de etapas. Por lo tanto, el segundo objetivo de este 
artículo es la presentación de métodos de discretización y programación no lineal que proporcionen las funciones 
óptimas de estado, control y adjuntas y permitan una verificación precisa de las condiciones necesarias.

The organization of this paper is as follows. Section 2 presents the statement of the delayed
control problem with mixed state–control constraints. In Section 3, we recall the minimum principle
for nondelayed control problems with control–state constraints. Here, a crucial feature is that
the initial and the terminal boundary conditions must be considered in a general mixed form.
Section 4 is devoted to the derivation of first-order necessary optimality conditions for the delayed
optimal control problem given in Section 2. Essentially, the augmentation approach of Guinn [6]
is generalized, which allows to use the minimum principle in Section 3. For technical reasons, we
need the assumption that the ratio of the time delays in state and control is a rational number. The
analysis in this section is based on the theses of Gollmann  ̈ [14] and Kern [15]. 

Este artículo se organiza de la siguiente manera. La Sección 2 presenta el planteamiento del problema de control 
retardado con restricciones mixtas de estado-control. En la Sección 3, recordamos el principio de mínimo para 
problemas de control sin retardo con restricciones de estado-control. Aquí, una característica crucial es que las 
condiciones de contorno inicial y terminal deben considerarse en una forma mixta general. La Sección 4 está 
dedicada a la derivación de las condiciones de optimalidad necesarias de primer orden para el problema de control 
óptimo retardado dado en la Sección 2. Esencialmente, el enfoque de aumento de Guinn [6] es generalizado, lo que 
permite utilizar el principio de mínimo en la Sección 3. Por razones técnicas, necesitamos la suposición de que 
la relación de los retardos de tiempo en el estado y el control es un número racional. El análisis en esta 
sección se basa en las tesis de Gollmann ̈ [14] y Kern [15].

In Section 5, the
Euler discretization for the delayed control problem is discussed, which leads to a high-dimensional
nonlinear programming problem. As in the nondelayed case, it can be shown that the Lagrange
multipliers corresponding to the optimization problem constitute an Euler discretization for the
advanced adjoint equations. In Section 6, we discuss an analytical example that allows to test
the accuracy of the numerical solution for various step sizes. Sections 7 and 8 are devoted to the
numerical solution and the verification of the minimum principle for two practical examples. The
first example is taken from [5, 11] and describes the optimal control of a chemical tank reactor
(CSTR reactor), whereas the second example arises in the optimal harvesting of a resource (optimal
fishing).

En la Sección 5, se analiza la discretización de Euler para el problema de control retardado, lo que da lugar a 
un problema de programación no lineal de alta dimensión. Al igual que en el caso no retardado, se puede demostrar 
que los multiplicadores de Lagrange correspondientes al problema de optimización constituyen una discretización 
de Euler para las ecuaciones adjuntas avanzadas. En la Sección 6, se presenta un ejemplo analítico que permite 
comprobar la precisión de la solución numérica para diferentes tamaños de paso. Las Secciones 7 y 8 se dedican a 
la solución numérica y a la verificación del principio de mínimos para dos ejemplos prácticos. El primer ejemplo, 
tomado de [5, 11], describe el control óptimo de un reactor de tanque químico (reactor CSTR), mientras que el 
segundo se presenta en la explotación óptima de un recurso (pesca óptima).


2. OPTIMAL CONTROL PROBLEMS WITH DELAYS IN STATE AND CONTROL 
------------------------------------------------------------

We consider retarded optimal control problems with constant delays :math:`r \geg 0` in the state variable
:math:`x(t) \in  \mathbb{R}^n` and  :math:`s \geg 0` in the control variable :math:`u(t) \in \mathbb{R}^n`. 
The following retarded control problem with
mixed control–state inequality constraints will be referred to as problem (ROCP):

Minimize J (u, x)=g(x(b))+
 b
a
L(t, x(t), x(t −r),u(t),u(t −s))dt (1)
subject to the retarded differential equation, boundary conditions and mixed control–state inequality
constraints

x ̇(t) = f (t, x(t), x(t −r),u(t),u(t −s)), a.e. t ∈ [a,b] (2)
x(t) = (t), t ∈ [a−r,a] (3)
u(t) = (t), t ∈ [a−s,a) (4)
w(x(b)) = 0 (5)
C(t, x(t),u(t))  0, t ∈ [a,b] (6)

For convenience, all functions
g : Rn →R
L : [a,b]×Rn ×Rn ×Rm ×Rm →R
f : [a,b]×Rn ×Rn ×Rm ×Rm →Rn
w : Rn →Rq , 0qn
C : Rn ×Rm →Rp

are assumed to be twice continuously differentiable w.r.t. all arguments. A pair of functions
(u, x)∈ L∞([a,b],Rm)×W1,∞([a,b],Rn) is called an admissible pair for problem (ROCP), if
the state x and control u satisfy restrictions (2)–(6). An admissible pair (uˆ, xˆ) is called a locally
optimal pair or weak minimum for (ROCP), if
J (uˆ, xˆ)J (u, x)

holds for all (u, x) admissible in a neighborhood of (uˆ, xˆ) with u(t)− ˆu(t), x(t)− ˆx(t)< for
all t ∈ [a,b] and >0 sufficiently small. Instead of considering a weak minimum, we could use
the more general notion of a Pontryagin minimum, thus admitting neighborhoods of (uˆ, xˆ) in the
L1-norm; cf. Milyutin and Osmolovskii [16].

3. FIRST-ORDER NECESSARY OPTIMALITY CONDITIONS FOR UNDELAYED OPTIMAL CONTROL PROBLEMS WITH MIXED CONSTRAINTS
-----------------------------------------------------------------

Formally, any undelayed control problem is contained in the retarded problem (ROCP) by choosing
r =s =0. Owing to the absence of delays, the initial value profiles given by conditions (3) and (4)


are omitted. However, the continuity of the state variables in the augmented problem necessitates
to introduce a general boundary condition of mixed type,

w(x(a), x(b))=0 (7)
which replaces the terminal boundary condition (5). This condition is indispensable in the proof
of the necessary conditions presented in Section 4. The Hamiltonian or Pontryagin function for
the nondelayed control problem without any constraints (6) is given by

H(t, x,u,):= L(t, x,u)+∗ f (t, x,u) (8)
The augmented Hamiltonian is defined by adjoining the mixed control–state constraint (6) by a
multiplier ∈Rp to the Hamiltonian (8):

H(t, x,u,,):= L(t, x,u)+∗ f (t, x,u)+∗C(t, x,u) (9)
Here and in the sequel, ∗ denotes the transposition. The extension of the classical Pontryagin’s
minimum principle to the mixed control–state constraints (6) requires a regularity condition
or constraint qualification. For a locally optimal pair (uˆ, xˆ) and t ∈ [a,b], let J0(t):= {j ∈
{1,..., p}|Cj(t, xˆ(t),uˆ(t))=0} denote the set of active indices for the inequality constraint (6).
Then, we assume the rank condition:

rank Cj(t, xˆ(t),uˆ(t)
u

j∈J0(t)
=#J0(t) (10)
The following necessary optimality conditions are to be found in Hestenes [17, Chapter 7,
Theorem 3.1] and Neustadt [18, Chapter VI.3, p. 296].
Theorem 3.1 (Pontryagin’s Minimum Principle)
Let (uˆ, xˆ) be a locally optimal pair for the control problem (ROCP) without delays, i.e.r =s =0, and
the mixed boundary condition (7). Assume that the regularity condition (10) is satisfied. Then there
exist a costate (adjoint) function ˆ

∈W1,∞([a,b],Rn), a multiplier function ˆ ∈ L∞([a,b],Rp) and

a multiplier ˆ ∈Rq , such that the following conditions hold for a.e. t ∈ [a,b]:
(i) adjoint differential equation:
 ̇
ˆ
(t)
∗ =−Hx (t, xˆ(t),uˆ(t), ˆ

(t),ˆ(t)) (11)

(ii) transversality conditions:
ˆ
(a)
∗ = −ˆ
∗
wxa (xˆ(a), xˆ(b)) (12)

ˆ
(b)
∗ = gx (xˆ(b))+ ˆ
∗
wxb (xˆ(a), xˆ(b)) (13)

(iii) minimum condition for Hamiltonian:
H(t, xˆ(t),uˆ(t), ˆ

(t))H(t, xˆ(t),u, ˆ

(t)) (14)

for all u ∈Rm satisfying C(t, xˆ(t),u)0;

(iv) local minimum condition for augmented Hamiltonian:
Hu(t, xˆ(t),uˆ(t), ˆ

(t),ˆ(t))=0 (15)

(v) nonnegativity of multiplier and complementarity condition:

ˆ(t)0 and ˆi(t)Ci(t, xˆ(t),uˆ(t))=0, i =1,..., p (16)

In (12) and (13), wxa and wxb denote partial derivatives of w=w(xa, xb) with respect to its
first and second arguments. In the following section, Theorem 3.1 will be used to derive necessary
conditions for the retarded control problem (ROCP).

4. NECESSARY OPTIMALITY CONDITIONS FOR DELAYED OPTIMAL CONTROL PROBLEMS WITH MIXED CONTROL–STATE CONSTRAINTS
------------------------------------------------------

Now we study the retarded control problem (ROCP) with constant delays r,s0 and (r,s)=(0,0).
We shall use a transformation technique that requires the technical assumption that the ratio of the
delays is a rational number.
Assumption 4.1 (rationality assumption)
Assume that r,s0, (r,s)=(0,0) and
r
s
∈Q for s>0 or
s
r
∈Q for r>0 (17)
In particular, this assumption holds for any couple of rational numbers (r,s), where at least one
number is nonzero.
The Hamiltonian H and the augmented Hamiltonian H for the delayed control problem (ROCP)

are defined in analogy to nondelayed problems. However, in contrast to the nondelayed Hamilto-
nians, two additional arguments y ∈Rn and v∈Rm denoting the delayed state and control variables

are needed:

H(t, x, y,u,v,) := L(t, x, y,u,v)+∗ f (t, x, y,u,v)
H(t, x, y,u,v,,) := L(t, x, y,u,v)+∗ f (t, x, y,u,v)+∗C(t, x,u)

(18)

where ∈Rn, ∈Rp.
We shall obtain necessary optimality conditions for the retarded control problem (ROCP) by first
transforming (augmenting) problem (ROCP) to a higher-dimensional nondelayed control problem.
To further study the augmented problem, we need Pontryagin’s minimum principle for nondelayed
control problems with mixed control–state constraints, which will be reviewed in the following
section.
The following first-order necessary conditions can be found in Gollmann  ̈ [14]; a precise proof
under Assumption 4.1 has been given by Kern [15].

Theorem 4.2 (minimum principle for the retarded optimal control problem (ROCP))
Let (uˆ, xˆ) be locally optimal for (ROCP) with delays satisfying Assumption 4.1. Then there exist
a costate (adjoint) function ˆ

∈W1,∞([a,b],Rn), a multiplier function ˆ ∈ L∞([a,b],Rp) and a

multiplier ˆ ∈Rq , such that the following conditions hold for a.e. t ∈ [a,b]:
(i) adjoint differential equation:
 ̇
ˆ
(t)
∗ = −Hˆ x (t)−[a,b−r](t)Hˆ y (t +r)
= −Hx (t, xˆ(t), xˆ(t −r),uˆ(t),uˆ(t −s), ˆ
(t),ˆ(t))
−[a,b−r](t)Hy (t+r, xˆ(t+r), xˆ(t),uˆ(t+r),uˆ(t+r−s), ˆ

(t+r),ˆ(t+r)) (19)
where Hˆ x (t) and Hˆ y (t) denote the evaluation of the partial derivatives Hx and Hy along
xˆ(t), xˆ(t −r),uˆ(t),uˆ(t −s), ˆ
(t),ˆ(t);

(ii) transversality condition:
ˆ
(b)
∗ =gx (xˆ(b))+ ˆ
∗
wx (xˆ(b)) (20)

(iii) minimum condition for Hamiltonian:
Hˆ(t)+[a,b−s](t)Hˆ(t +s)
= H(t, xˆ(t), xˆ(t −r),uˆ(t),uˆ(t −s), ˆ
(t))

+[a,b−s](t)H(t +s, xˆ(t +s), xˆ(t +s−r),uˆ(t +s),uˆ(t), ˆ

(t +s)) (21)

H(t, xˆ(t), xˆ(t −r),u,uˆ(t −s), ˆ
(t))

+[a,b−s](t)H(t +s, xˆ(t +s), xˆ(t +s−r),uˆ(t +s),u, ˆ
(t +s))

for all u ∈Rm satisfying C(t, xˆ(t),u)0;
(iv) local minimum condition for augmented Hamiltonian:

Hˆ u(t)+[a,b−s](t)Hˆ v(t +s)=0 (22)

(v) nonnegativity of multiplier and complementarity condition:

ˆ(t)0 and ˆi(t)Ci(t, xˆ(t),uˆ(t))=0, i =1,..., p (23)

Proof
The proof uses a transformation technique suggested by Guinn [6] to derive first-order necessary
conditions for unconstrained optimal control problems with pure state delays. In view of the
rationality assumption (17), there exist integers k,l ∈N with

r
s
= k
l
for s =0, s
r = l
k
for r =0


Without loss of generality, we may assume the first case. Then the delays r,s are integer multiples
of the interval length h :=s/l:

r =k ·h, s =l ·h, k,l ∈N

The time interval [a,a+h] will be used below as the basis time interval for the augmented control
problem. Without loss of generality, we may further assume that the interval length b−a represents
an integer multiple of h, i.e. we have b−a = N h with N ∈N+.
Now we introduce the state variable ∗ =(∗
0,...,∗
N−1)∈RN n,i ∈Rn, and control variable

∗ =( ∗
0,..., ∗
N−1)∈RNm, i ∈Rm, which are defined by
i(t):=x(t +i h), i(t):=u(t +i h) for t ∈ [a,a+h], i =0,..., N −1 (24)
The continuity of the state x(t) in [a,b] implies the following boundary conditions for the
augmented state (t):

i(a+h)=i+1(a), i =0,..., N −2

which can be expressed as

Vi(i+1(a),i(a+h)):=i(a+h)−i+1(a)=0, i =0,..., N −2 (25)
In terms of the new state and control variables  and , the retarded control problem (ROCP) is
equivalent to the following undelayed optimal control problem on the time interval [a,a+h]:
Minimize J (,)=g(N−1(a+h))+
 a+h
a
N
−1
i=0
L(t+i h,i(t),i−k (t), i(t), i−l(t))dt (26)

subject to
 ̇
i(t)= f (t +i h,i(t),i−k (t), i(t), i−l(t)), i =0,..., N −1, t ∈ [a,a+h] (27)

Vi(i+1(a),i(a+h)) = 0, i =0,..., N −2
VN−1(N−1(a+h)) := w(N−1(a+h))=0

(28)
C(t +i h,i(t), i(t))0, i =0,..., N −1, t ∈ [a,a+h] (29)
The fixed starting profiles (3) and (4) are included in this notation by considering the variables
−k ,...,−1 and −l,..., −l defined by

i(t) := (t +i h), i =−k,...,−1
i(t) := (t +i h), i =−l,...,−1

However, note that −k ,...,−1 and −l,..., −1 do not represent optimization variables. Intro-
ducing adjoint variables and multipliers for the augmented problem by (26)–(29) by

=(0,...,N−1)

∗ ∈RN·n, M =(M0,..., MN−1)
∗ ∈RN·p

the Hamiltonian functions (8) and (9) for the nondelayed augmented control problem are given by
K(t,,,, M) = N
−1
i=0
[L(t +i h,i,i−k , i, i−l)+∗

i L(t +i h,i,i−k , i, i−l)] (30)

K(t,,,, M) = N
−1
i=0
[L(t +i h,i,i−k , i, i−l)+∗

i L(t +i h,i,i−k , i, i−l)]

+
N
−1
i=0
M∗
i C(t +i h,i, i) (31)
Every locally optimal pair (uˆ(·), xˆ(·)) for (ROCP) defines a pair (ˆ (·),ˆ(·)) that minimizes
the augmented problem (26)–(29). Pontryagin’s minimum principle for nondelayed problems
(Theorem 3.1) assures the existence of a costate (adjoint) function ˆ ∈W1,∞([a,a+h],RN·n), a
multiplier function Mˆ ∈ L∞([a,a+h],RN·p) and a vector ∈R(N−1)n+q , ˆ =(ˆ
∗
0,..., ˆ
∗
N−2, ˆ
∗
N−1)∗
where ˆ0,... ˆN−2 ∈Rn and ˆN−1 ∈Rq , such that the following conditions hold for almost every
t ∈ [a,a+h]:
1. adjoint differential equation:
d
dt
ˆ (t)
∗ =−K(t,ˆ(t),ˆ (t),ˆ (t), Mˆ (t)) (32)

2. transversality condition:
ˆ i(a)
∗ = −ˆ
∗
i

i
Vi(ˆ
i+1(a), ˆ
i(a+h)), i =0,..., N −2 (33)

ˆ i(a+h)
∗ = ˆ
∗
i

i+1
Vi(ˆ
i+1(a), ˆ
i(a+h)), i =0,..., N −2 (34)

ˆ N−1(a+h)
∗ = gx (ˆ
N−1(a+h))+ ˆ
∗
N−1wx (ˆ
N−1(a+h)) (35)

3. minimum condition for Hamiltonian:

K(t,ˆ(t),ˆ (t),ˆ (t))K(t,ˆ(t),,ˆ (t)) (36)

for all admissible =( ∗
0,..., ∗
N−1)∗ ∈RNm satisfying C(t +i h, ˆ

i(t), i)0 for i =

0,..., N −1;
4. local minimum condition for augmented Hamiltonian:

K(t,ˆ(t),ˆ (t),ˆ (t), M(t))=0 (37)

5. nonnegativity of multiplier and complementarity condition:

Mˆ (t)0, Mˆi(t)
∗C(t +i h, ˆ
i(t), ˆ
i(t))=0, i =0,..., N −1 (38)

Evaluating the adjoint equation for the component ˆ j (0 jN −1) yields
d
dt
ˆ j(t)
∗ = −Lx (t + j h, ˆ
j(t), ˆ
j−k (t), ˆ
j(t), ˆ
j−l(t))
−{0,...,N−1−k}(j)Ly (t +(j +k)h, ˆ
j+k (t), ˆ
j(t), ˆ
j+k (t), ˆ
j+k−l(t))

−ˆ j(t)
∗ fx (t + j h, ˆ
j(t), ˆ
 j−k (t), ˆ
j(t), ˆ
j−l(t))

−{0,...,N−1−k}(j)ˆ j+k (t)

∗ f y (t +(j +k)h, ˆ
j+k (t), ˆ
j(t), ˆ
j+k (t), ˆ
j+k−l(t))

−Mˆ j(t)
∗Cx (t + j h, ˆ
j(t), ˆ
j(t))
Now we are able to define the adjoint function ˆ

∈W1,∞([a,b],Rn) and multiplier function ˆ ∈
L∞([a,b],Rp) for the retarded control problem (ROCP) in the following way. For t ∈ [a,b], there
exists 0 jN −1 with a+ j hta+(j +1)h. We substitute

ˆ
(t):=ˆ j(t − j h), ˆ(t):= Mˆ (t − j h) (39)

and obtain from the previous adjoint equation:
 ̇
ˆ
(t) = d
dt
ˆ j(t − j h)
= −Lx (t, xˆ(t), xˆ(t −kh),uˆ(t),uˆ(t −lh))
−{0,...,N−1−k}(j)Ly (t +kh, xˆ(t +kh), xˆ(t),uˆ(t +kh),uˆ(t +kh−lh))
−ˆ
(t)
∗ fx (t, xˆ(t), xˆ(t −kh),uˆ(t),uˆ(t −lh))
−{1,...,N−1−k}(j)ˆ
(t +kh)
∗ f y (t +kh, xˆ(t +kh), xˆ(t),uˆ(t +kh),uˆ(t +kh−lh))

− ˆ(t)
∗Cx (t, xˆ(t),uˆ(t))
= −H(t, xˆ(t), xˆ(t −r),uˆ(t),uˆ(t −s), ˆ
(t),ˆ(t))
−[a,b−r](t)H(t +r, xˆ(t +r), xˆ(t),uˆ(t +r),uˆ(t +r −s), ˆ

(t +r)ˆ(t +r))
Thus, we have found the adjoint equation (19). The transversality condition (34) for N−1

ˆ N−1(a+h)
∗ =gx (ˆ
N−1(a+h))+ ˆ
∗
N−1wx (ˆ
N−1(a+h))
gives the desired transversality condition (20) for (ROCP) in view of b=a+N h:

ˆ
(a+N h)=gx (xˆ(a+N h))+ ˆ
∗
wx (xˆ(a+N h)), ˆ:= ˆN−1 ∈Rq

To verify the minimum condition for the Hamiltonian H, we consider t ∈ [a,b] and the corre-
sponding index j ∈ {0,..., N −1} with a+ j hta+(j +1)h. Substituting t :=t − j h ∈ [a,a+h],

the minimum condition (36) gives
K(t

,ˆ(t

),ˆ (t

),ˆ (t

))K(t

,ˆ(t

),,ˆ (t

)) (40)

for all admissible ∈RNm satisfying (29). The local minimum condition (37) yields K(t
)=0.

Now we define an admissible control policy (·)=( ∗
0,..., ∗
N−1)∗ ∈RNm by

i :=
uˆ(t

+i h), i = j
u, i = j , i =0,..., N −1

where the control vector u ∈Rm is admissible for (ROCP), i.e. C(t, xˆ(t),u)0. Evaluating
inequality (40) for this vector  and removing equal expressions on both sides, we obtain for the
remaining terms associated with j and j +l:
L(t

+ j h, ˆ
j(t

), ˆ
j−k (t

),uˆ(t

+ j h),uˆ(t

+(j −l)h))

+ˆ j(t

)
∗ f (t

+ j h, ˆ
j(t

), ˆ
j−k (t

),uˆ(t

+ j h),uˆ(t

+(j −l)h))

+{0,...,N−1−l}(j)L(t

+(j +l)h, ˆ
j+l(t

), ˆ
j+l−k (t

),uˆ(t

+(j +l)h),uˆ(t

+ j h))

+{0,...,N−1−l}(j)ˆ j+l(t

)
∗ f (t

+(j +l)h, ˆ
j+l(t

), ˆ
 j+l−k (t

),uˆ(t

+(j +l)h),uˆ(t

+ j h))

L(t

+ j h, ˆ
j(t

), ˆ
j−k (t

),u,uˆ(t

+(j −l)h))

+ˆ j(t

)
∗ f (t

+ j h, ˆ
j(t

), ˆ
j−k (t

),u,uˆ(t

+(j −l)h))

+{0,...,N−1−l}(j)L(t

+(j +l)h, ˆ
j+l(t

), ˆ
j+l−k (t

),uˆ(t

+(j +l)h),u)

+{0,...,N−1−l}(j)ˆ j+l(t

)
∗ f (t

+(j +l)h, ˆ
j+l(t

), ˆ
j+l−k (t

),uˆ(t

+(j +l)h),u)

Redefining the adjoint and multiplier function in (39) with t =t − j h, we obtain the desired
minimum condition (21) for the Hamiltonian H, respectively, the local minimum condition (22)

for the augmented Hamiltonian. Condition (38) immediately implies the multiplier and comple-
mentarity condition (23) in view of (39). 

Remark
Soliman, Ray [5] have discussed bang-bang and singular controls that appear in control problems,
where the control u ∈Rm is partitioned into controls u1 ∈Rm1 and u2 ∈Rm2 with control u1 appearing
linearly in the system. The control–state constraint (6) then reduces to bounds for u1:
u1,minu1(t)u1,max for t ∈ [a,b], u1,min,u1,max ∈Rm1

The minimum condition (21) shows that the control u1(t) is determined by the sign of the
components of the switching vector function

(t)= Hu1 (t)+[a,b](t +s)Hv1 (t +s) (41)

whereas the control u2 satisfies the local minimum condition (22)

Hu2 (t)+[a,b](t +s)Hv2 (t +s)=0 (42)

The CSTR control problem in Section 6 provides an example with such a partitioning of the control
vector. Soliman and Ray [5] study junction phenomena for bang-bang and singular arcs. They not
only give conditions under which junction results for control systems without delay carry over to
delayed systems, but also give examples for delayed systems that exhibit unusual features. Some
examples illustrating these unusual features have been worked out by Kern [15]. Further work is
needed to fully develop the theory.

5. DISCRETIZATION, OPTIMIZATION AND CONSISTENCY OF ADJOINT EQUATIONS
--------------------------------------------------------------



