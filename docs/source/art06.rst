OPTIMAL CONTROL PROBLEMS WITH TIME DELAYS: TWO CASE STUDIES IN BIOMEDICINE . art06 - 2018
=============================================================

Abstract. There exists an extensive literature on delay differential models
in biology and biomedicine, but only a few papers study such models in the
framework of optimal control theory. In this paper, we consider optimal control
problems with multiple time delays in state and control variables and present
two applications in biomedicine. After discussing the necessary optimality con-
ditions for delayed optimal control problems with control-state constraints, we
propose discretization methods by which the delayed optimal control problem
is transformed into a large-scale nonlinear programming problem. The first
case study is concerned with the delay differential model in [21] describing the
tumour-immune response to a chemo-immuno-therapy. Assuming L1 -type objectives, which are linear in control, we obtain optimal controls of bang-bang
type. In the second case study, we introduce a control variable in the delay
differential model of Hepatitis B virus infection developed in [7]. For L1 -type
objectives we obtain extremal controls of bang-bang type.

1. Introduction. 
----------------

Differential dynamic systems with time delays play an important
role in the modeling of real-life phenomena in various fields of applications. There
exists an extensive literature on delay differential models in biology and biomedicine;
see e.g., [6, 7, 16, 18, 24, 26, 27]. Though there is a vast literature on optimal control
problems with time delays in control and state variables, so far only a few papers
have applied the framework of optimal control with delays to biomedicine; cf. the
recent papers [15, 21, 23]. The aim of this paper is to present two case studies in
biomedicine which illustrate the application of delayed optimal control problems and
demonstrate that there exist efficient numerical techniques to solve such problems.

In Section 2, we consider optimal control problems with multiple time delays in
control and state variables The control process can be subject to mixed control-
state constraints. We review the necessary optimality conditions that were derived
in [10] in the form of a Pontryagin type Minimum Principle. It is assumed that the
so-called commensurability assumption holds which requires that the time delays
and the terminal time are integer multiples of a joint stepsize. This assumption
also underlies the discretization and nonlinear programming techniques that are
briefly reviewed in Section 3. In Section 4, we study the delay differential model for
tumour-immune-response with chemo-immunotherapy in Rihan et al. [21]. Aside
from the state delay in this model we introduce a time delay in the control variable
representing the immune therapy. The delay accounts for the fact that the human
immune system needs some time to respond to the immune therapy. In contrast
to the L2 -type objectives in [21] we consider L1 -type objectives characterized by
linearly appearing controls which seem to be more appropriate in the biological
framework; cf. the remarks in [22]. The computations show that all controls are
of bang-bang type. For the non-delayed problem, we can verify the second-order
sufficient conditions in [19, 17] and thus show that the computed solution provides
a strict strong minimum.

Section 5 considers the delay differential model in [7] describing the spread of
Hepatitis B virus (HBV). The dynamical model exhibits a delay in the state vari-
ables. We introduce a control variable into this model and formulate an optimal
control problem using L1 -type objectives. Again, all controls are of bang-bang type.
We show that the non-delayed bang-bang control provides a strict strong minimum,
whereas the delayed controls are extremal solutions that satisfy the necessary con-
ditions with high accuracy.

2. Optimal control problems with multiple time-delays in state and control variables.
------------------------------------------------------------------------------------

2.1. Problem statement. 
-----------------------

Let x(t) ∈ Rn denote the state variable and u(t) ∈ Rm
the control variable at time t ∈ [0, tf ] with fixed terminal time tf > 0. The time-
delays in the state and control variables are given by a constant vector (τ1 , . . . , τd ) ∈
Rd satisfying

0 =: τ0 < τ1 < . . . < τd .

Thus τ0 represents the non-delayed variables. In [9, 10] we have studied the fol-
lowing optimal control problem with multiple time-delays and mixed control-state
constraints (MDOCP): determine a pair of functions (x, u) ∈ W 1,∞ ([0, tf ], Rn ) ×
L∞ ([0, tf ], Rm ) that minimize the functional in Mayer form

J(x, u) = g(x(tf ))

(1)

subject to the delayed (retarded) differential equation, boundary conditions and
mixed control-state inequality constraints

ẋ(t) = f (t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τd )), a.e. t ∈ [0, tf ], (2)
x(t) = x0 (t),t ∈ [−τd , 0],(3)
u(t) = u0 (t),t ∈ [−τd , 0),(4)
ψ(x(T )) = 0,(5)
C(t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τd )) ≤ 0, a.e. t ∈ [0, tf ].(6)

The functions g : Rn → R, f : [0, tf ] × R(d+1)·n × R(d+1)·m → Rn , ψ : Rn → Rq
(0 ≤ q ≤ n), and C : [0, tf ] × R(d+1)·n × R(d+1)·m → Rp are assumed to be continu-
ously differentiable, while the functions x0 : [−τd , 0] → Rn , u0 : [−τd , 0] → Rm only
need to be continuous.

Without lack of generality we have assumed that the cost functional is given in
Mayer form (1). It is well known that an objective in Bolza form,

Ztf
L(t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τd )) dt,
J(x, u) = g(x(tf )) +
0

can be reduced to Mayer form by introducing an additional state variable xn+1
defined by

ẋn+1 (t) = L(t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τd )),
xn+1 (0) = 0.
˜ xn+1 , u) = g(x(tf )) + xn+1 (tf ).

Then we have to minimize the functional J(x,

In the following, we shall use the placeholder variables y0 , y1 , . . . , yd for the de-
layed state variables and v0 , v1 , . . . , vd for the delayed control variables. The delayed
variables are defined by

yδ (t) = x(t − τδ ),
vδ (t) = u(t − τδ )
(δ = 0, 1, . . . , d).
(7)

Note that we do not necessarily assume an equal number of state and control delays.
The case of an unequal number of delays in state and control variables is included
in this formulation as we admit that

∂h
∂h
= 0 or
= 0, h ∈ {f, C, L}, for some δ ∈ {0, . . . , d}.
∂yδ
∂vδ

2.2. Minimum principle: First-order necessary conditions. 
---------------------------------------------------------

A Pontryagin-
type minimum principle for problem (MDOCP) has been derived in [9, 10]. The
main result requires that all positive time delays τ1 , . . . , rd can be expressed as
integer multiples of a sufficiently small positive constant (stepsize).

**Assumption 2.1** (Commensurability Condition). Assume that there exist a con-
stant h > 0 and integers k1 , . . . , kd , N with

τδ = k δ h
(δ = 1, . . . , d)
and
tf = N h.
(8)

In view of 0 = τ0 < τ1 < . . . < τd we have 0 < k1 < . . . < kd . Then in analogy
to the non-delayed case we define the Hamiltonian function by

H(t, y0 , . . . , yd , v0 , . . . , vd , λ) = λ f (t, y0 , . . . , yd , v0 , . . . , vd ),
λ ∈ Rn ,
(9)
n

where the adjoint variable λ ∈ R is a row vector. The augmented Hamiltonian func-
tion is defined by adjoining the mixed control-state constraint (6) to the Hamiltonian
using a multiplier µ ∈ Rp (row vector):

H(t, y0 , . . . , yd , v0 , . . . , vd , λ, µ)
= H(t, y0 , . . . , yd , v0 , . . . , vd , λ)
+µ C(t, y0 , . . . , yd , v0 , . . . , vd ).
(10)

For ease of notation we refrain from denoting an optimal pair

(x, u) ∈ W 1,∞ ([0, tf ], Rn ) × L∞ ([0, tf ], Rm )

by a hat or a similar symbol. We require the following regularity condition for the
active control-state constraints.

**Assumption 2.2** (Regularity Condition). Let (x, u) be a locally optimal pair and
let

J0 (t) := {j ∈ {1, . . . , p} | Cj (t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τd )) = 0}1140

denote the set of active indices for the inequality constraints (6). Assume that the
gradients

∂Cj (t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τd ))
,
∂(v0 , . . . , vd )
j ∈ J0 (t),
(11)

are linearly independent.

The following theorem summarizes the first-order necessary conditions for opti-
mality for the control problem (MDOCP) [10].

**Theorem 2.3.** (Minimum Principle for Optimal Control Problems with Multiple
Time-Delays [10]): Let (x, u) be a locally optimal pair for (MDOCP) with delays 0 =
τ0 < τ1 < . . . τd that satisfies the commensurability condition (8) and the regularity
condition 2.2. Then there exist an adjoint (costate) function λ ∈ W 1,∞ ([0, tf ], Rn ),
a number λ0 ≥ 0, a multiplier function µ ∈ L∞ ([0, tf ], Rp ) and a multiplier ν ∈ Rq ,
such that the following conditions hold for a.e. t ∈ [0, tf ]:

1. Advanced Adjoint Differential Equation:

λ̇(t) = −
d
X
χ[0,tf −τδ ] (t)Hyδ (t + τδ ),
(12)
δ=0

where Hyδ [t] = Hyδ (t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τd ), λ(t), µ(t))
and χ[0,tf −τδ ] is the characteristic function of the interval [0, tf − τδ ].

2. Transversality Condition:

λ(tf ) = λ0 gx (x(tf )) + ν ψx (x(tf )).
(13)

3. Minimum Condition for the Hamiltonian:

d
X
χ[0,tf −τδ ] (t)H[t + τδ ]
δ=0
≤ H(t, . . . , u, u(t − τ1 ), . . . , u(t − τd ), λ(t))
+
d−1
X
(14)
χ[0,tf −τδ ] (t) H(t + τδ , . . . , u(t + τδ − τδ−1 ), u, u(t + τδ − τδ+1 ), . . .)
δ=1
+ χ[0,tf −τd ] (t) H(t + τd , . . . , u(t + τd − τ1 ), . . . , u(t + τd − τd−1 ), u, λ(t))
for all u ∈ Rm satisfying
C(t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τδ−1 ), u,
u(t − τδ+1 ), . . . , u(t − τd )) ≤ 0
for
δ = 0, . . . , d,
where H[t] = H(t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τd ), λ(t)).

4. Local Minimum Condition for the Augmented Hamiltonian Function:

d
X
χ[0,tf −τδ ] (t)Hvδ [t + τδ ] = 0.
(15)
δ=0

5. Non-negativity of Multiplier and Complementarity Condition: for t ∈ [0, tf ],

µ(t) ≥ 0, µ(t)C(t, x(t − τ0 ), . . . , x(t − τd , u(t − τ0 ), . . . , u(t − τd )) = 0.
(16)

**3. Numerical discretization methods.** Similar to the case of non-delayed dif-
ferential equations, we can employ integration methods of Runge-Kutta type or
multistep methods, e.g., the Euler method and trapezoidal rule, to discretize the
delay differential equation

ẋ(t) = f (t, x(t − τ0 ), . . . , x(t − τd ), u(t − τ0 ), . . . , u(t − τd )).

Any integration method based on an equidistant discretization scheme utilizes a
uniform step size h > 0. Due to the presence of time-delays it is crucial to match
the delays τ1 , . . . , τd to the grid. This is ensured by the commensurability condition
(8) in Assumption 2.1. For this purpose, let h > 0 be a step size satisfying (8), i.e.

τδ = kδ h (δ = 0, . . . , d),
tf = N h,

with integers 0 = k0 < k1 < . . . < kd and N . Note that this grid can be refined
by use of any integer fraction of h, This defines an equidistant discretization mesh
with grid points ti = ih for i = 0, 1, ..., N .

Let xi ∈ Rn and ui ∈ Rm denote approximations of x(ti ) and u(ti ) at the grid
points ti for i = 0, 1, . . . , N . For convenience, we shall use the abbreviations

fi = f (ti , xi , xi−k1 , . . . , xi−kδ , ui , ui−k1 , . . . , ui−kδ ).

The initial value profiles x0 (·) and u0 (·) provide the values

x−i = x0 (−ih)
(i = 0, .., kd ),
u−i = u0 (−ih)
(i = 1, .., kd ).
(17)

Since the focus in this paper is not on discussing various numerical methods, we
present only two integration methods that can be easily implemented. The simplest
method is the first order method of Euler which is defined by the recursion

xi+1 = xi + hfi ,
i = 0, 1, . . . , N − 1.

The trapezoidal rule is an implicit method of second order:

1
xi+1 = xi + h (fi + fi+1 ) , i = 0, 1, . . . , N − 1.
2

Then for the Euler method and the optimization variable
(18)
(19)

z := (u0 , x1 , u1 , x2 , ..., uN −1 , xN ) ∈ RN (m+n)

we obtain the following nonlinear programming problem (NLP) with equality and
inequality constraints:

Minimize
J(z) = g(xN )
(20)

subject to

xi+1 = xi + hf (ti , xi−k0 , . . . , xi−kd , ui−k0 , . . . , ui−kd ),i = 0, . . . , N − 1,(21)
C(ti , xi−k0 , . . . , xi−kd , ui−k0 , . . . , ui−kd ) ≤ 0,i = 0, . . . , N − 1,(22)
ψ(xN ) = 0,
(23)

and initial values (17). Using the trapezoidal method (19) we simply replace the
equations (21) by the equations defined in (19).

Let λ = (λ0 , λ1 , . . . , λN −1 ) ∈ Rn·N , λi ∈ Rn (i = 0, . . . , N − 1), be the Lagrange
multipliers for equations (21) and let µ = (µ0 , µ1 , . . . , µN −1 ) ∈ Rp·N , µi ∈ Rp
(i = 0, . . . , N −1), be the multipliers for the inequality constraints (22) and νN ∈ Rq
be the multiplier for the boundary condition (23). In [9, 10] we have discussed the
Karush-Kuhn-Tucker (KKT) necessary optimality conditions for the (NLP) using
the Euler scheme (18) and showed that the property of consistency holds. This
means that the Lagrange multipliers provide approximations for the adjoint variable
λ(t), the multiplier µ(t) and ν according to

λ(ti ) ≈ λi ∈ Rn ,
µ(ti ) ≈ µi /h ∈ Rp
(i = 0, ..., N − 1),
νN ≈ ν.
(24)

This follows from the fact that the Lagrange multipliers λi satisfy the advanced
adjoint equations using the same discretization scheme in a backward mode.

To solve the optimization problem (NLP) in (20)–(22) numerically, we employ
the Applied Modeling Programming Language (AMPL) developed by Fourer, Gay
and Kernighan [8] which can be linked to the interior-point optimization solver
IPOPT developed by Wächter et al. [28] or to the SQP solver WORHP by Büskens
and Gerdts [4]. Every solver provides the Lagrange multipliers and therefore gives
access to approximations of adjoint variables and multiplier functions for the control
problem (MDOCP) according to (24). Thus we can test whether the numerical
solution is an extremal solution which satisfies the necessary optimality conditions
in Theorem 2.3.

4. Optimal control of chemo-immuno-therapy.
------------------------------------------

4.1. Optimal control problem. 
-----------------------------

We consider the delay differential model in Ri-
han et al. [21] that proposes a chemo-immuno-therapy of cancer. The authors
introduce a time delay only in the state variable and present a stability analysis
of drug free steady states. We shall extend the model by including also a control
delay in the control u2 of immune therapy. The delay accounts for the fact that the
human immune system takes some time to respond to the immune therapy. The
state and variables have the following meaning:

E: concentration of effector cells (plasma B cells, producing antibodies).
T : concentration of tumour cells.
N : concentration of healthy cells.
U : concentration of cytostatic agent for chemotherapy.
u1 : dose control for chemotherapy,
u2 : dose control for immune therapy of the effector cells.

Denoting the state delay by τ1 and the control delay by τ2 , the dynamical system
is given by

ρ
−
µ
E(t − τ1 )T (t − τ1 )
Ė(t) = σ + η+T (t−τ
e
1)
−(δ + a1 (1 − e−U (t) ))E(t) + u2 (t − τ2 )s1 ,
␁
Ṫ (t) = r2 (1 − βT (t)) − nT E(t) − c1 N (t) − a2 (1 − e−U (t) ) T (t),
␁
Ṅ (t) = r3 (1 − β2 N (t)) − c2 T (t) − a3 (1 − e−U (t) ) N (t),
U̇ (t) = u1 (t) − d1 U (t).
(25)

The initial values and initial functions for the delayed state and control variables
are as follows:

E(0) =
T (0) =
N (0) =
U (0) =
E0 = 0.3,
T0 = 300,
N0 = 0.9,
U0 = 0.0.
E(t) = E0
T (t) = T0
u2 (t) = 0
∀ − τ1 ≤ t ≤ 0,
∀ − τ1 ≤ t ≤ 0,
∀ − τ2 ≤ t < 0.
(26)

We shall consider the control constraints

0 ≤ uk (t) ≤ uk,max
∀ t ∈ [0, tf ]
(k = 1, 2).

Let us denote the state and control variables by

x = (E, T, N, U ) ∈ R4 ,
u = (u1 , u2 ) ∈ R2 .

For notational convenience, we simplify the notations (7) for the delayed state and
control variables. In the context of the dynamical system (25) it is more convenient
to consider the delayed state variables y1 , y2 and control variable v2 defined by

y1 (t) = x1 (t − τ1 ) = E(t − τ1 ), y2 (t) = x2 (t − τ1 ) = T (t − τ1 ),
v2 (t) = u2 (t − τ2 ).
(28)

With these notations the dynamical system (25) can be written as

ẋ(t) = f (x(t), y1 (t), y2 (t), u(t), v2 (t)).
(29)

Then the optimal control problem is as follows: determine a control function u =
(u1 , u2 ) ∈ L∞ ([0, tf ], R2 ) that minimizes the objective functional

Z tf
Jp (x, u) =
(T (t) − E(t) + B1 (u1 (t))p + B2 (u2 (t))p ) dt (p = 1, 2)
(30)
0

subject to the dynamic constraints (25), initial conditions (26) and control con-
straints (27). The objective functional (30) represents a trade-off between minimiz-
ing the tumour cells and the total doses of the cytotoxic and immunologic agents
on one hand and maximizing the plasma cells on the other hand. The constants
B1 > 0, B2 > 0 are appropriate weights which are listed in Table 1 together with
the system parameters.

Rihan et al. [21] consider only the L2 -type functional J2 (x, u) in (30) which is
quadratic in the control variable u. L2 -type functionals are often used in economics
to describe, e.g., production costs, but are mostly not appropriate in a biological
framework; cf. the remarks in [22]. The L1 functional J1 (x, u) incorporates the
total amount of drugs used as a penalty and thus appears to be more realistic. For
that reason, we shall mainly focus on the functional J1 (x, u) in the sequel.

Now we apply the necessary optimality conditions in the form of a Minimum
Principle as stated in Theorem 2.3. Denoting the adjoint variable by the row vector
λ = (λE , λT , λN , λU ) ∈ R4 , the Hamiltonian for the objective J1 (x, u) and the
control system (29) is given by

H(x, y1 , y2 , u, v2 , λ) = T − E + B1 u1 + B2 u2 + λf (x, y1 , y2 , u, v2 ).
(31)

According to Theorem 2.3 (1), the advanced adjoint equations are given by

λ̇E (t) = −HE [t] − χ [0,tf −τ1 ] (t) Hy1 [t + τ1 ],
λ̇T (t) = −HT [t] − χ [0,tf −τ1 ] (t) Hy2 [t + τ1 ],
λ̇N (t) = −HN [t],
(32)
λ̇U (t) = −HU [t].

We do not write out the adjoint variables explicitly, since the adjoint variables can
be computed as Lagrange multipliers of the discretized control problem as explained
in the preceding section. Due to the free terminal state, the transversality condition
(13) is

λ(tf ) = (0, 0, 0, 0).
(33)

The optimal control u(t) minimizes the sum of Hamiltonians in (14). Since both
controls appear linearly in the Hamiltonian, the minimizing controls are determined
by the switching functions

φ1 (t) = Hu1 [t] = B1 + λU (t),
φ2 (t) = Hu2 (t) + χ[0,tf −τ2 ] (t)Hv2 [t + τ2 ] = B2 + χ[0,tf −τ2 ] (t)λE (t + τ2 )s1 ,
(34)

Table 1. Parameters in the control problem of chemoimmunotherapy [21].

ParameterDescriptionValue
tf
τ1
τ2
(uk,min , uk,max )
(a1 , a2 , a3 )
(β, β2 )final time
state delay
control delay
control bounds
cell kill rate response
reciprocal carrying capacities of tumour
and host cells
scaling parameters
drug decay rate
immune cell death rate
steepness of immune response
uninfected effector cell decrease rate
immune cell influx and decay rate resp.
cell growth rates
immune effector cell decrease rate
weights30 d (days)
1.5 d
3.0 d
(0, 1) for k = 1, 2
(0.2, 0.4, 0.1)
(c1 , c2 )
d1
δ
η
µe
(σ, ρ)
(s1 , r2 , r3 )
nT
(B1 , B2 )
(0.002, 1.0)
(3 × 10−5 , 3 × 10−8 )
0.01
0.2
0.3
0.003611
(0.2, 0.2)
(0.3, 1.03, 1.0)
1.0
(5, 10)

according to the control law



if φk (t) > 0

 0,
uk,max ,
if φk (t) < 0
,
uk (t) =


singular, if φk (t) = 0 ∀ t ∈ Is ⊂ [0, tf ]
k = 1, 2.
(35)

Singular controls will not be discussed further, since our computations only yield
bang-bang controls. Due to the transversality condition λ(tf ) = 0 the switching
functions satisfy φk (tf ) = Bk > 0 for k = 1, 2. Hence, the control law (35) shows
that uk (t) = 0 holds on a terminal interval [tk , tf ] for k = 1, 2. Parameters for the
subsequent computations are given in the Table 1.

4.2. Optimal solution of the non-delayed control problem. 
---------------------------------------------------------

First, we present
the solution for the non-delayed control problem with τ1 = τ2 = 0 and the functional
J1 (x, u). Recall the upper control bounds u1,max = u2,max = 1, the terminal time
tf = 30 (days) and the weights B1 = 5 and B2 = 10 from Table 1. Applying
AMPL/IPOPT with N = 3000 grid points and the trapezoidal rule (19) we find
the following bang-bang controls uk (t) with only one switch at tk ,

1 for 0 ≤ t < tk
uk (t) =
(k = 1, 2), 0 < t1 < t2 < tf .
(36)
0 for tk ≤ t ≤ tf

To obtain a refinement of the solution, we solve the Induced Optimization Problem
(IOP) with the switching times t1 and t2 as optimization variables; cf. [17, 19]). The
arc-parametrization method [17] and the optimal control package NUDOCCCS due
to Büskens [2] yield the following numerical results

J1 (x, u) = 1399.02,
E(tf ) = 0.640303,
U (tf ) = 2.96962.
t1 = 3.93031,
T (tf ) = 0.180726,
t2 = 9.76562,
N (tf ) = 0.904968,

The initial values of the adjoint variables are

λE (0) = −770.13, λT (0) = 2.9980, λN (0) = −0.027548, λU (0) = −281.11.

The non-delayed solution is shown in Figure 1. A common strategy in medical
practise is the administration of a pulse therapy or a blockwise application of drugs.
Such a strategy is promoted by the controls in Figure 1.

Now we show that the second-order sufficient conditions in [19], Chapter 7, are
satisfied for the bang-bang control (36). For that purpose, we have to check two
further conditions. First, notice that the objective J1 (x, u) becomes a function
J1 (t1 , t2 ) of the two switching times t1 , t2 , if we assume the control structure (36).
The Hessian of J1 (t1 , t2 ) is computed as the positive definite 2 × 2 matrix


19.167 11.120
D2 J1 (t1 , t2 ) =
.
11.120 10.887

Furthermore, as can be seen in Figure 2, the following strict bang-bang property
with respect to the Minimum Principle holds for k = 1, 2:

φk (t) < 0
∀ 0 ≤ t < tk ,
φ̇k (tk ) > 0,
φk (t) > 0
∀ tk < t ≤ tf .
(37)

Hence, the solution shown in Figure 1 provides a strict strong minimum.

We briefly compare the solutions for the functionals J1 (x, u) and J2 (x, u). The
controls u1 and u2 for the functional J2 (x, u) are continuous, since the strict
Legendre-Clebsch condition holds and the Hamiltonian has a unique minimum with
respect to u1 and u2 . Figure 3 displays a comparison of the controls u1 and u2 for
both functionals. The state variables for the functional J2 (x, u) are very similar to
those shown in Figure 1 and thus are not displayed here. The functional value is
J2 (x, u) = 1392.88 versus J1 (x, u) = 1399.02 and the final state is computed as

E(tf ) = 0.615728, T (tf ) = 0.108124, N (tf ) = 0.903899, U (tf ) = 3.20922.

4.3. Numerical solution of the delayed control problem. 
-------------------------------------------------------

We choose the state
delay τ1 = 1.5 and the control delay τ2 = 3. To obtain a rather precise reference solu-
tion, we apply AMPL/IPOPT with N = 6000 grid points and tolerance tol = 10−8 .
As in the non-delayed case we obtain a bang-bang control u(t) = (u1 (t), u2 (t)),
where each uk (t) has only one switch at tk :

1 for 0 ≤ t < tk
uk (t) =
(k = 1, 2), 0 < t1 < t2 < tf .
(38)
0 for tk ≤ t ≤ tf

We obtain the numerical results

J1 (x, u) = 2126.69,
E(tf ) = 0.661258,
U (tf ) = 3.55546.
t1 = 4.692,
T (tf ) = 0.136262,
t2 = 10.42,
N (tf ) = 0.902747,

The initial values of the adjoint variables are

λE (0) = −485.41, λT (0) = 2.2403, λN (0) = −0.022090, λU (0) = −248.50.

Using the Euler method (18) with the same number N = 6000 grid points, the nu-
merical results are less accurate by two decimals. The control and state trajectories
are shown in Figure 4. Figure 5 displays the controls and the switching functions
in a neighborhood of the switching times. The zoom into the controls confirms that
the control law (35) is precisely satisfied and that the strict bang-bang property
(37) holds as well for the delayed solution. Unfortunately, we can not check any
kind of sufficient conditions for the delayed solution, since numerically verifiable
sufficient conditions are not available in the literature.


Finally, as in the non-delayed case we briefly compare the solutions for the func-
tionals J1 (x, u) and J2 (x, u). The controls u1 and u2 for the functional J2 (x, u) are
continuous, since the strict Legendre-Clebsch condition holds and the Hamiltonian
has a unique minimum with respect to u1 and u2 . Figure 6 displays a comparison
of the controls u1 and u2 for both functionals.

4.4. Numerical solution of the delayed control problem with mixed control-state constraint 
-----------------------------------------------------

U (t) + u2 (t) ≤ 3. We add the following mixed control-
state constraint to the delayed optimal control problem:

U (t) + u2 (t) ≤ 3
∀ t ∈ [0, tf ].
(39)

This constraint means that sum of the cytotoxic agent and the immune dose is
bounded from above. Here we consider the augmented Hamiltonian

H(x, y1 , y2 , u, v2 , λ, µ) = H(x, y1 , y2 , u, v2 , λ) + µ(U + u2 ),
(40)

where the mixed constraint is adjoined to the Hamiltonian (31) by a multiplier
µ ≥ 0. The local minimum condition (15) yields

0 = Hu2 [t] + χ[0,tf −τ2 ] (t) Hv2 [t + τ2 ] = φ2 (t) + µ(t),
(41)

where φ2 (t) = B2 +χ[0,tf −τ2 ] (t) λE (t+τ2 )s1 is the switching function defined in (34).
The multiplier satisfies the complementarity condition µ(t)(U (t) + u2 (t) − 3) = 0
for t ∈ [0, tf ]. Hence, on a boundary arc with U (t) + u2 (t) = 3 for t ∈ [t1 , t2 ] we
obtain an explicit formula of the multiplier in view of (41):

µ(t) = −φ2 (t) = −B2 − χ[0,tf −τ2 ] (t)λE (t + τ2 )s1
∀ t ∈ [t1 , t2 ].
(42)

Computations show that the control u2 (t) is constant on a boundary arc and
thus we obtain by differentiation

0 = U̇ (t) = u1 (t) − d1 U (t) = u1 (t) − d1 (3 − u2 (t)).

Since we have u2 (t) = 1 on a boundary arc, the control u1 (t) on the boundary arc
is given by

u1 (t) = d1 (3 − u2 (t)) = 0.02
(d1 = 0.01).

Using the trapezoidal method (19) with N = 3000 grid points we find the control
structure



␚
␛
for 0 ≤ t < t1 
 1
1 for 0 ≤ t < t3
0.02 for t1 ≤ t < t2
u1 (t) =
, u2 (t) =
(43)
0 for t3 ≤ t ≤ tf


0
for t2 ≤ t ≤ tf


with 0 < t1 < t2 < t3 < tf and the boundary arc [t1 , t2 ]. We obtain the numerical
results:

J1 (x, u) = 2236.06,
t1 = 2.045,
t3 = 10.98,
E(tf ) = 0.725265,
N (tf ) = 0.919108, U (tf ) = 1.63720.
t2 = 9.95,
T (tf ) = 0.100546,

5. Optimal control of a delay model of Hepatitis B virus infection.
------------------------------------------------

5.1. Optimal control model. 
---------------------------

Eikenberry et al. [7] report that currently about
two billion people - roughly 30% of the human population - have been infected by
Hepatitis B virus (HBV). The disease has attracted considerable attention from
mathematical biologists who have developed various models to study the HBV dynamics. Eikenberry et al. [7] present a dynamical model with state variables

x: number of healthy cells,
p: number of exposed cells,
y: number of infected cells,
v: free virion load.

The model (4.1)–(4.4) in [7] does not yet involve a control variable. We choose
the control variable u as the effect of treatment which corresponds to the coefficient
γ in the dynamic equation (4.4) in [7]. Denoting the time by t ∈ [0, tf ] with fixed
final time tf > 0 and the delay in the state variable by τ ≥ 0, the dynamic system
(4.1)–(4.4) in [7] reads as follows:

ẋ(t) = r x(t) 1 − TK(t) − d x(t) − β v(t) Tx(t)
(t) ,
ṗ(t)
)
−d τ
v(t − τ ) Tx(t−τ
= −d p(t) + β v(t) Tx(t)
(t) − βe
(t−τ ) ,
)
ẏ(t) = βe−d τ v(t − τ ) Tx(t−τ
(t−τ ) − a y(t),
v̇(t) = k(1 − u(t)) y(t) − µ y(t).
(44)

The variable T denotes the total number of cells defined by

T = x+p+y.

The delay τ appears in all three variables x, p, y. Hence, the initial conditions are
given by initial functions for x, p, y and an initial value for v:

x(t) = x0 , p(t) = p0 , y(t) = y0
for − τ ≤ t ≤ 0,
v(0) = v0 .
(45)

We impose the control constraint

0 ≤ u(t) ≤ 1
∀ t ∈ [0, tf ].
(46)

9999

Denoting the state vector by X := (x, p, y, v) ∈ R4 and the delayed variable by Y ,
where Y (t) = X(t − τ ), the dynamical system can be written as
Ẋ = f (X, Y, u)
(47)
with initial functions and conditions given in (45).
The optimal control problem then consists in determining a control function
u ∈ L1 ([0, tf ], R) that minimizes the cost functional
Z tf
J(X, u) =
(−x(t) + B u(t)) dt (B > 0),
(48)
0
subject to the dynamics (44) with initial conditions (45) and the control constraint
(46). The objective functional represents a trade-off between maximizing the num-
ber of healthy cells and minimizing the treatment cost.
5.2. Necessary optimality conditions: Minimum principle. We briefly dis-
cuss the necessary optimality conditions in Theorem 2.1. The Hamiltonian is given
by
H(X, Y, u, λ) = −x + Bu + λ f (X, Y, u),
λ = (λx , λp , λy , λv ) ∈ R4 .
(49)
We do not explicitly write out the advanced adjoint equation (12):
λ̇(t) = −HX [t] − χ [0,tf −τ ] (t) HY [t + τ ].
(50)
The control variable u appears linearly in the Hamiltonian and does not involve a
delay. Hence, defining the switching functions by
φ(t) = Hu [t] = B − λv (t) k y(t),
(51)OPTIMAL CONTROL PROBLEMS WITH TIME DELAYS IN BIOMEDICINE
1151
the minimizing control is characterized by the control law


if φ(t) > 0
 0,

1,
if φ(t) < 0
u(t) =
.


singular, if φ(t) = 0 ∀ t ∈ Is ⊂ [0, tf ]
(52)
Singular controls will not be discussed further, because we only found bang-bang
controls. The following parameters from [7], page 294 below, will be used in our
computations:
a = 0.011,
K = 2,
d = 0.0039, β = 4.8 · 10−5 ,
r = 1,
µ = 0.693.
k = 200,
(53)
The state variable X = (x, p, y, v) is scaled by 10−11 so that we can choose, e.g.,
the following initial conditions:
x(t) = 1.4,
p(t) = 0.3,
y(t) = 0.2
∀ − τ ≤ t ≤ 0,
v(0) = 500.
(54)
The time horizon is tf = 500 (days) and the weight parameter in the objective (48)
is taken as B = 0.05 .
5.3. Comparison of solutions for several delays. We compare the solutions
for the delays τ = 0 (non-delayed solution), τ = 10 and τ = 15. Applying
AMPL/IPOPT with N = 5000 grid points and using the trapezoidal rule (19),
we find a bang-bang control u(t) with only one switch at t1 ,
␚
␛
1 for 0 ≤ t < t1
u(t) =
.
(55)
0 for t1 ≤ t ≤ tf
τ=0 : control u and switching function φ
u
φ
1
τ=10 : control u and switching function φ
u
φ
1
0.50.5
00
u
φ
1
0.5
0
-0.5
-0.5
-0.5
τ=15 : control u and switching function φ
-1
-1
-1
0
100
200
300
time t (days)
400
500
-1.5
0
100
200
300
time t (days)
400
500
0
100
200
300
time t (days)
400
500
Figure 8. Controls and switching functions (51) for delays τ = 0,
τ = 10 and τ = 15. For all delays the control law (52) is satisfied
and the strict bang-bang property holds.
In the non-delayed case, a refinement of the solution is obtained by solving the
Induced Optimization Problem (IOP) with respect to the switching time [17, 19].
We get the numerical results:
τ =0
τ = 10
τ = 15
: J(X, u) = 893.072,
: J(X, u) = 913.388,
: J(X, u) = 923.032,
t1 = 261.70,
t1 = 293.50,
t1 = 304.10.
A comparison of the controls and switching functions for the delays τ = 0, 10, 15
is shown in Figure 8. The bang-bang control for τ = 0 provides a strict strong
minimum, since second-order sufficient conditions (SSC) in [17, 19] are satisfied.
The numerical test of SSC proceeds as follows. Since the bang-bang control (55)
has only one switch at t1 , the objective functional becomes a function J = J(t1 )1152
LAURENZ GÖLLMANN AND HELMUT MAURER
healthy cells x
2.3
2.2
2.1
2
1.9
1.8
1.7
1.6
1.5
1.4
exposed cells p
0.3
τ=0
τ=10
τ=15
τ=0
τ=10
τ=15
0.25
0.2
0.15
0.1
0.05
0
0
100
200
300
400
500
200
300
infected cells yvirions v
τ=0
τ=10
τ=15
100
100
time t (days)
0.45
0.4
0.35
0.3
0.25
0.2
0.15
0.1
0.05
0
0
0
time t (days)
200
300
500
500
400500
τ=0
τ=10
τ=15
12
10
8
6
4
2
0
400
400
100
time t (days)
200
300
time t (days)
Figure 9. Comparison of state variables for delays τ = 0, 10, 15.
Top row: (a) healthy cells x, (b) exposed cells p. Bottom row: (a)
infected cells y, (b) free virions v.
of the scalar optimization variable t1 . One verifies numerically that the second
derivative is positive: d2 J/dt21 = 0.005028 > 0. Moreover, the following strict
bang-bang property [17, 19] for the switching function φ(t) holds; cf. Figure 8, left:
φ(t) < 0
for 0 ≤ t < t1 ,
φ̇(t1 ) > 0 ,
φ(t) > 0
for t1 < t ≤ tf = 500 .
Note that the strict bang-bang property is also satisfied for the delayed control with
delays τ = 10 and τ = 15. However, as in the preceding section we can not conclude
that the delayed controls in Figure 8 provide a strict strong minimum. Figure 9
displays a comparison of the state variables for delays τ = 0, τ = 10, τ = 15.
6. Conclusion. We presented two applications of delayed optimal control prob-
lems in biomedicine. In the first case study, we extended the delay differential
model of tumour-immune-response in Rihan et al. [21] by including a time delay in
the control variable u2 which represents the immune therapy. The delay is due to
the delayed response of the human immune system to the immune therapy. Rihan
et al. [21] considered a L2 -type objective which is quadratic in the control variables.
From a numerical point of view, the control solution in [21] remained a bit obscure.
Therefore, we improved the results in this paper in two regards. First, we consid-
ered a more realistic L1 -type objective which is linear in the two control variables.
Secondly, we applied the discretization and nonlinear programming methods [10]OPTIMAL CONTROL PROBLEMS WITH TIME DELAYS IN BIOMEDICINE
1153
(see Section 3) to obtain extremal solutions that satisfy the necessary optimality
conditions in Theorem 2.1 with high accuracy. The computations showed that both
controls u1 and u2 are of bang-bang type with only one switch from the upper
bound uk (t) = uk,max to the zero control uk (t) = 0 for k = 1, 2. Apparently, it
is much easier to administer the therapy protocol induced by a bang-bang control
then applying a treatment plan resulting from a L2 -type objective; cf. Figure 3.
In the non-delayed case we could show that the bang-bang controls are indeed op-
timal, since they satisfy the second-order sufficient conditions in [19, 17]. To our
knowledge, sufficient conditions for delayed bang-bang controls are not available
in the literature. We have also studied the solution under the mixed control-state
constraint (39) which combines the cytostatic agent U (t) and the immune control
u2 (t). The computations gave very accurate extremal solutions.
The second delay differential model, which describes the spread of Hepatitis B
virus, was taken from Eikenberry at al. [7]. We introduced a control variable into
the originally uncontrolled model and considered L1 -type objectives. For different
delays we obtained only bang-bang controls as in the first case study. Sufficient
optimality conditions [19, 17] could only be verified for the non-delayed bang-bang
control.
REFERENCES
[1] B. Buonomo and M. Cerasuolo, The effect of time delay in plant-pathogen interactions with
host demography, Math. Biosciences and Engineering, 12 (2015), 473–490.
[2] C. Büskens, Optimierungsmethoden und Sensitivitätsanalyse für optimale Steuerprozesse mit
Steuer- und Zustands-Beschränkungen, PhD thesis, Institut für Numerische Mathematik,
Westfälische Wilhelms-Universität Münster, Germany, 1998.
[3] C. Büskens and H. Maurer, SQP methods for solving optimal control problems with control
and state constraints: adjoint variables, sensitivity analysis and real-time control, J. Comput.
Appl. Math., 120 (2000), 85–108.
[4] C. Büskens and M. Gerdts, WORHP: Large-Scale Sparse Nonlinear Optimization Solver,
http://www.worhp.de.
[5] Q. Chai, R. Loxton, K. L. Teo and C. Yang, A class of optimal state-delay control Problems,
Nonlinear Analysis: Real World Applications, 14 (2013), 1536–1550.
[6] R. V. Culshaw and S. Ruan, A delay-differential equation model of HIV infection of CD4+
T-cells, Mathematical Biosciences, 165 (2000), 27–39.
[7] S. Eikenberry, S. Hews, J. D. Nagy and Y. Kuang, The dynamics of a delay model of Hepatitis
B virus infection with logistic hepatocyte growth, Mathematical Biosciences, 6 (2009), 283–
299.
[8] R. Fourer, D. M. Gay and B. W. Kernighan, AMPL: A Modeling Language for Mathemati-
calProgramming, The Scientific Press, South San Francisco, California, 1993.
[9] L. Göllmann, D. Kern and H. Maurer, Optimal control problems with delays in state and
control and mixed control-state constraints, Optimal Control Applications and Methods, 30
(2009), 341–365.
[10] L. Göllmann and H. Maurer, Theory and applications of optimal control problems with mul-
tiple time-delays, Journal of Industrial and Management Optimization, 10 (2014), 413–441.
[11] T. Guinn, Reduction of delayed optimal control problems to nondelayed problems, Journal
of Optimization Theory and Applications, 18 (1976), 371–377.
[12] R. F. Hartl, S. P. Sethi and R. G. Vickson, A survey of the maximum principles for optimal
control problems with state constraints, SIAM Review, 37 (1995), 181–218.
[13] M. R. Hestenes, Calculus of Variations and Optimal Control Theory, John Wiley, New York,
1966.
[14] S. C. Huang, Optimal Control problems with retardations and restricted phase coordinates,
Journal of Optimization Theory and Applications, 3 (1969), 316–360.
[15] J. Klamka, H. Maurer and A. Swierniak, Local controllability and optimal control for a
model of combined anticancer therapy with control delays, Mathematical Biosciences and
Engineering, 14 (2017), 195–216.1154
LAURENZ GÖLLMANN AND HELMUT MAURER
[16] Y. Kuang, Delay Differential Equations with Applications in Population Dynamics, Academic
Press, San Diego, 1993.
[17] H. Maurer, C. Büskens, J.-H. R. Kim and Y. Kaya, Optimization methods for the verification
of second-order sufficient conditions for bang-bang controls, Optimal Control Methods and
Applications, 26 (2005), 129–156.
[18] R. M. May, Time-delay versus stability in population models with two and three tropic levels,
Ecology, 54 (1973), 315–325.
[19] N. P. Osmolovskii and H. Maurer, Applications to Regular and Bang-Bang Control: Second-
Order Necessary and Sufficient Optimality Conditions in Calculus of Variations and Optimal
Control, SIAM Advances in Design and Control, Vol. DC 24, SIAM Publications, Philadel-
phia, 2012.
[20] L. S. Pontryagin, V. G. Boltyanskii, R. V. Gamkrelidze and E. F. Mishchenko, The Math-
ematical Theory of Optimal Processes, Translation by K. N. Trirogoff, Wiley, New York,
1962.
[21] F. Rihan, D. H. Abdelrahman, F. Al-Maskari, F. Ibrahim and M. A. Abdeen, Delay differ-
ential model for tumour-immune-response with chemoimmunotherapy and optimal control.
Computational and Mathematical Methods in Medicine, Hindawi Publishing Corporation,
Vol. 2014, Article ID 982978, (2014).
[22] H. Schättler, U. Ledzewicz and H. Maurer, Sufficient conditions for strong local optimality in
optimal control problems with L2 -type objectives and control constraints, Discrete Contin.
Dyn. Syst. Ser. B 19 (2014), 2657–2679.
[23] C. Silva, H. Maurer and D.F.M. Torres, Optimal control of a tuberculosis model with state
and control delays, Mathematical Biosciences and Engineering, 14 (2017), 321–337.
[24] C. T. Sreeramareddy, K. V. Panduru, J. Menten and J. V. den Ende, Time delays in diagnosis
of pulmonary tuberculosis: A systematic review of literature, BMC Infectious Diseases, 9
(2009), 91–100.
[25] J. Stoer and R. Bulirsch, Introduction ot Numerical Analysis, Third Edition, Texts in Applied
Mathematics, Springer-Verlag, Berlin, 1990.
[26] D. G. Storla, S. Yimer, and G. A. Bjune, A systematic review in delay in the diagnosis and
treatment of tuberculosis, BMC Public Health, 8 (2008), p15.
[27] P. van den Driessche, Some Epidemiological Models with Delays, Report DMS-679-IR, Uni-
versity of Victoria, Department of Mathematics, 1994.
[28] A. Wächter and L. T. Biegler, On the implementation of an interior–point filter line-search
algorithm for large-scale nonlinear programming, Mathematical Programming, 106 (2006),
25–57.
[29] H. Yang and J. Wei, Global behaviour of a delayed viral kinetic model with general incidence
rate, Discrete Contin. Dyn. Syst. Ser. B, 20 (2015), 1573–1582.
Received April 30, 2017; Accepted March 18, 2018.
E-mail address: goellmann@fh-muenster.de
E-mail address: maurer@math.uni-muenster.de

