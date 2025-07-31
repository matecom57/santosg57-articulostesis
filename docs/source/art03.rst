Numerical Methods for Solving Optimal Control Problems -art03 - 2015
================================================================

Chapter 1: Introduction
------------------------

Numerical mathematics is study of quantitative approximations to the solutions of
mathematical problems including consideration of and bounds to the errors involved. Optimal
control theory is no exception to this rule. The purpose here is to implement three different
numerical algorithms in MATLAB to approximate the solution to an optimal control problem.
Once the methods are developed, the concept of convergence for each method will be discussed
as well as any flaws or problems with each specific method. After this, the three methods will be
used to find the solution to three different test problems in order to see how the methods work
and compare their results to each other. Each of three problems is chosen for specific reasons
which will be explained in detail later on. Finally, a ‘winner’ will be chosen, if possible, from
the results of each method applied to the three test problems, in order to see which method is
best.

Chapter 2: General Set up
--------------------------

This thesis is dedicated to comparing different numerical processes for solving an optimal
control problem. Though only a few specific problems will be studied, some general theory and
processes must be established first before any specific details can be discussed. This chapter will
be broken into three separate sections. The first section will be dedicated to discussing general
optimization; the second will cover optimal control theory; and the third will discuss the specific
details needed for the family of problems in question.

Section 1: Optimization
-----------------------

The first idea that needs to be set up and defined is what an optimization problem is and
its relevance. In mathematics, optimization is the process in which the best feasible solution for
a problem is found. This usually entails finding either a maximum or minimum, which are called
extrema, of the possible solutions. This can be done in various ways, though the most common
involves using some version of the derivative of the function.
In optimization, when discussing extrema, a point needs to be made to determine if the
extrema in question is over the whole domain of the function or just over a certain interval or
region. If 𝑓 has a maximum (or minimum) over the entire domain, 𝐷, of the function, this is
called the absolute maximum (or minimum). This means is that, for some 𝑐 in the domain of 𝑓,
𝑓(𝑐) ≥ 𝑓(𝑥) ∀𝑥 ∈ 𝐷 (or 𝑓(𝑐) ≤ 𝑓(𝑥) ∀𝑥 ∈ 𝐷). These extrema values are referred to as global
extrema. However, these are not the only type of extreme; there are local extrema are when

there exist a maximum (or minimum) on a small interval, 𝐼, such that 𝐼 ⊂ 𝐷. This means that for
some 𝑑 ∈ 𝐼, 𝑓(𝑑) ≥ 𝑓(𝑥) ∀𝑥 ∈ 𝐼 (or 𝑓(𝑑) ≤ 𝑓(𝑥) ∀𝑥 ∈ 𝐼).
When it comes to whether or not there even exists an extrema value, a reference can be
made back to the Extreme Value Theorem [5], which states: If 𝑓: 𝑈 → ℝ, where 𝑈 ⊂ ℝ𝑛 , is
continuous over a closed interval, [𝑎, 𝑏], then 𝑓 attains an absolute maximum value, 𝑓(𝑐), and a
absolute minimum value, 𝑓(𝑑), for some numbers 𝑐, 𝑑 ∈ [𝑎, 𝑏]. For more on this, see [6] and [7].

Section 2: Optimal Control Theory
---------------------------------

From a general perspective, an optimal control problem is an optimization problem. The
difference between the two is that, in optimal control theory, the optimizer is a function, not just
a single value. This function that optimizes is called the optimal control. The technical
definition of an optimal control problem is the process of determining control and state
trajectories for a dynamic system over a period of time to minimize a performance index. The state
variable (or function) is the set of variables (functions) used to describe the mathematical state of
the system. The control or control function is an operation that controls the recording,
processing, or transmission of data. These two functions drive how the system works and how
the desired control is found. With these definitions, a basic optimal control problem can be
defined. This basic problem will be referred to as our standard problem (SP).

Standard Problem
(SP)
𝑡1
max 𝐽(𝑢) where 𝐽(𝑢) = ∫ 𝑓(𝑡, 𝑥(𝑡), 𝑢(𝑡)) 𝑑𝑡
𝑢
𝑡0
𝑥 ′ (𝑡) = 𝑔(𝑡, 𝑥(𝑡), 𝑢(𝑡))
𝑥(𝑡0 ) = 𝑥0 , 𝑥(𝑡1 ) is free
(2.01)
(2.02)
(2.03)
The optimal control, 𝑢∗ , is the function that optimizes the objective function, 𝐽(𝑢), as
seen in (2.01). This control is not bounded. The other arguments in equation (2.01) are 𝑡, which
is the time variable, and 𝑥(𝑡), which is the state equation. The relationship between 𝑢 and 𝑥 is
defined by equations (2.02) and (2.03) and is denoted by the relationship in the map 𝑢(𝑡) → 𝑥 =
𝑥(𝑢). Though this relationship does indeed exist, 𝑥 is really just a function of the independent
time variable, but in writing 𝑥(𝑢), the dependence that 𝑥 has on 𝑢 is shown. Equation (2.02) is
the constraint equation on the state, and the initial and terminal conditions are given by (2.03).
By setting 𝑥(𝑡1 ) to be free, this simply means that the state can grow over time unconditionally.
To solve our basic optimal control problem, a set of what is called necessary conditions
must be satisfied. In mathematics, a necessary condition is a condition that must be satisfied for
a statement to be true, but that does not in and of itself make it true. In regards to (SP), there are
such conditions that must be satisfied in order to solve the problem. In the 1950’s, a Russian
mathematician by the name of Lev Pontryagin and his co-workers in Moscow derived such
conditions. Pontryagin introduced the adjoint function to affix to the differential equation to
the objective functional. These functions serve a similar purpose as the Lagrange multipliers in

multivariable calculus. The derivation of these results can be found in [1]. The next few
paragraphs will summarize these results.
The necessary conditions needed to solve the basic problem are derived from what is
referred to as the Hamiltonian, 𝐻, which is given by equation (2.04).
𝐻(𝑡, 𝑥, 𝑢, 𝜆) = 𝑓(𝑡, 𝑥, 𝑢) + 𝜆𝑔(𝑡, 𝑥, 𝑢)
(2.04)
Here 𝜆 denotes the adjoint and is dependent on 𝑡, 𝑥, and 𝑢. Using this, Pontryagin determined
that the following conditions are satisfied by the optimal control, denoted as 𝑢∗ , when the
Hamiltonian is nonlinear in 𝑢.
𝜕𝐻
= 0 at 𝑢∗ ⟹ 𝑓𝑢 + 𝜆𝑔𝑢 = 0
𝜕𝑢
𝜆′ = −
𝜕𝐻
⟹ 𝜆′ = ℎ(𝑡, 𝑥, 𝜆, 𝑢) − (𝑓𝑥 + 𝜆𝑔𝑥 )
𝜕𝑥
𝜆(𝑡1 ) = 0
{
𝑥 ′ = 𝑔(𝑡, 𝑥, 𝑢)
𝑥(𝑡0 ) = 𝑥0
Optimality Condition(2.05)
Adjoint Equation(2.06)
Transversality Condition(2.07)
Dynamics of the State Equation (2.08)
With these conditions, there is now a process on how to solve the standard problem
defined by SP. This process can be found in Table 1.

Table 1: Analytical Process
(1) Form the Hamiltonian (2.04) for the problem.
(2) Write the adjoint differential equation, transversality boundary condition, and
the optimality condition in terms of three unknowns, 𝑢∗ , 𝑥 ∗ , and 𝜆.
(3) Use the optimality equation 𝐻𝑢 = 0 to solve for 𝑢∗ in terms of 𝑥 ∗ and 𝜆.
(4) Solve the two differential equations for 𝑥 ∗ and 𝜆 with two boundary
conditions.
(5) After finding the optimal state and adjoint, solve for the optimal control using
the formula derived by step (3).
If it is possible to solve for the optimal control in terms of 𝑥 ∗ and 𝜆, then the formula for
𝑢∗ is called the characterization of the optimal control. The state equation and adjoint equations
together with the characterization and boundary conditions are called the optimality system.
Now that the process on how to solve SP has been defined, it should be noted that it is not
enough to simply solve the necessary conditions in order to solve the optimal control problem.
Justification for the found solutions to be the actual solution for (SP) requires examining some
existence and uniqueness conditions. A true existence results guarantees an optimal control,
with finite objective functional. Such results usually require restrictions on either 𝑓 or 𝑔 or even
possibly both. For the analysis of the methods, an assumption of existence will be made, but for
reference on existence and uniqueness, refer back to [1].
Existence is only half of what is desired. Uniqueness of the optimal control is also
needed. Suppose an optimal control exists, 𝑢∗ , such that 𝐽(𝑢) ≤ 𝐽(𝑢∗ ) for all controls 𝑢. Now,

𝑢∗ is unique if and only if 𝐽(𝑢∗ ) = 𝐽(𝑢). This implies that 𝑢∗ = 𝑢 at all but finitely many points.
In this case, the associated states will be identical. The state 𝑥 ∗ , is the unique optimal state.
In most cases, if the solution to the state system is unique, then the corresponding optimal
control is also unique. This, however, can only be said for small time intervals.
Now, in general, uniqueness of the optimal control does not always imply that there is a
unique optimality system. To prove the uniqueness of the optimal control directly, the objective
functional 𝐽(𝑡, 𝑥(𝑢)) must have strict concavity established. However, this process is, in most
cases, difficult to prove. Thus, other ways to prove uniqueness must be found, such as proving
𝑓,𝑔 and the right hand side of the adjoint equation are Lipschitz in their state and adjoint
arguments. This only proves uniqueness for small time periods. Sometimes, one must bound the
optimality system to get this property easily.

Section 3: Numerical Processes
------------------------------

Though most problems have a theoretical answer, it is, in practice, very difficult to find
explicitly. Hence the necessity of numerical processes. Like mentioned in Section 2.2, the
main analytical technique is provided by Pontryagin’s Maximum Principle which gives
necessary conditions that the control and the state need to satisfy. These conditions can be
solved explicitly sometimes; however, for most problems, the conditions are too complicated to
be solved explicitly. This is especially true for problems that also involve additional constraints
on the state or the control. Because of these, numerical approaches are used to construct
approximations to these difficult equations.


One of these numerical processes is needed for all the methods. What is needed is a
method to solve ordinary differential equations and systems of differential equations. For this,
the Runge-Kutta algorithm will be used to solve such problems. Though there are many
different adaptations of Runge-Kutta, only the method in its classical, fourth order will be used.
The fourth order classical Runge-Kutta (RK4) method approximates the solution to the problem
𝑦 ′ = 𝑓(𝑡, 𝑥).
Classical, fourth order Runge-Kutta Algorithm
𝑘1 = 𝑓(𝑡𝑛 , 𝑥𝑛 )
ℎ
ℎ
𝑘2 = 𝑓 (𝑡𝑛 + , 𝑥𝑛 + 𝑘1 )
2
2
ℎ
ℎ
𝑘3 = 𝑓 (𝑡𝑛 + , 𝑥𝑛 + 𝑘2 )
2
2
𝑘4 = 𝑓(𝑡𝑛 + ℎ , 𝑥𝑛 + ℎ𝑘3 )
ℎ
𝑥𝑛+1 = 𝑥𝑛 + (𝑘1 + 2𝑘2 + 2𝑘3 + 𝑘4 )
6
RK4

Here, 𝑥𝑛+1 is the RK4 approximation of 𝑥(𝑡𝑛 + ℎ); here ℎ is the step size. 𝑥𝑛+1 is
calculated using the current value of 𝑥𝑛 plus the weighted average of four values, 𝑘𝑖 . Each of the
𝑘𝑖 values are determined for each 𝑛 step, then are overwritten for the next step; 𝑘1 is the
increment based on the slope of the beginning of the interval; 𝑘2 and 𝑘3 are both based on the
midpoint of the interval, and lastly, 𝑘4 is based on the slope at the end of the interval. The
Runge-Kutta Method has an error that is 𝒪(ℎ4 ), where ℎ is the step size and also it is
conditionally stable. The proof and further explanation of these ideas can be found in various
texts, one being [2].

Chapter 3:
Test Problems
Section 1:
Problem 1
Now that the general set up is done, the discussion can be focused on the desired family
of problems. This family can be found in [2] and will be referred back to as the Problem 1 (P1).
Problem 1
(P1)
1
max ∫ 𝐴𝑥(𝑡) − 𝐵𝑢(𝑡)2 𝑑𝑡
𝑢
(3.01)
0
1
𝑥 ′ (𝑡) = − 𝑥(𝑡)2 + 𝐶𝑢(𝑡)
2
subject to {
𝑥(0) = 𝑥0 > −2
𝐴 ≥ 0, 𝐵 > 0
(3.02)
The restriction on 𝐵 is so that this is indeed a maximization problem. Before any method
can be developed, there are a few key ideas that will be needed through all methods. The first
thing that is needed is the Hamiltonian, as defined by (2.04).
1
𝐻 = 𝐴𝑥 − 𝐵𝑢2 − 𝜆𝑥 2 + 𝐶𝜆𝑢
2
(3.03)
Using this, the optimality condition, as defined in (2.05), for this specific problem is
0=
𝜕𝐻
𝐶𝜆
= −2𝐵𝑢 + 𝐶𝜆 ⟹ 𝑢∗ =
𝜕𝑢
2𝐵
(3.04)
This clearly gives us an explicit formulation for the optimal control, which is only directly
depends on the adjoint, though the state affects it through the state’s relationship to the adjoint.
The final piece of setup is the two differential equations that will be used to solve for our optimal
control. One solves for the state and the second in turn solves the adjoint.

1
𝑥 ′ (𝑡) = 𝑥 2 + 𝐶𝑢
2
𝑥(0) = 𝑥0(3.05)
𝜆′ (𝑡) = −𝐴 + 𝑥𝜆
𝜆(1) = 0(3.06)
{
Note that the ODE in (3.06) was derived from (2.06) and (2.07). The solution is now completely
described by these two ODE’s and the equation for 𝑢∗ in (3.04).
This problem is used to initially test the three methods due to its changeable parameters
and initial state value. Also because of this fact, it produced many more results to discuss later in
Chapter 7.
Section 2:
Problem 2
The second problem that will be used to test the process can be found in [3]. This
problem will be referred to later to as Problem 2 (P2).
Problem 2
(P2)
1
1
min ∫ 𝑥(𝑡)2 + 𝑢(𝑡)2 𝑑𝑡
𝑢 2 0
subject to {
𝑥 ′ (𝑡) = −𝑥(𝑡) + 𝑢(𝑡)
𝑥(0) = 1
(3.07)
(3.08)
Once again, to construct the adjoint ODE, the Hamiltonian must be constructed.
Remember that from the Hamiltonian, not only is the adjoint ODE derived, but how to use it to
find the approximated optimal control as well. The Hamiltonian for (P2) is derived to be:

𝐻=
1 2 1 2
𝑥 + 𝑢 − 𝜆𝑥 + 𝜆𝑢
2
2
(3.09)
Using the Hamiltonian in (3.09), as defined by equation (2.06) and (2.07), the state and
adjoint ODE’s are given by equation (3.10) and (3.11).
{
𝑥 ′ (𝑡) = −𝑥 + 𝑢
𝑥(0) = 1(3.10)
𝜆′ (𝑡) = 𝑥 − 𝜆
{
𝜆(1) = 0(3.11)
Once again, we use the optimality condition defined in (2.05) to find the formula for the
optimal control, 𝑢∗ .
0=
𝜕𝐻
= 𝑢 + 𝜆 ⟹ 𝑢∗ = −𝜆
𝜕𝑢
(3.11)
Thus defining everything to find the solution to (P2). This problem is important because
from [3], the real solution is given. With the actual solution to (P2), the accuracy of the three
methods can be tested. The real solution for the state and adjoint are given in equations (3.12)
and (3.13).
𝑥(𝑡) =
√2 cosh (√2(𝑡 − 1)) − sinh (√2(𝑡 − 1))
√2 cosh(√2) + sinh(√2)
𝜆(𝑡) = −
sinh (√2(𝑡 − 1))
√2 cosh(√2) + sinh(√2)

Section 3:
Problem 3
The last problem can be found in [1]. This problem will be referred back to as Problem 3
(P3).
Problem 3
(P3)
1
min ∫ 𝑥(𝑡) + 𝑢(𝑡)𝑑𝑡
𝑢
0
subject to {
𝑥 ′ (𝑡) = 1 − 𝑢(𝑡)2
𝑥(0) = 1
(3.14)
(3.15)
It needs to be stated that Problem 3 is a minimization problem, so when the methods are
applied later, the negative of the objective function will be used since the algorithms are
designed to find the maximum. Other than that, the construction of all the necessary pieces to
solve for the solution are found the same way. First is the Hamiltonian, then the optimality
condition, then finally the state and adjoint ODE’s.
0=
𝐻 = 𝑥 + 𝑢 + 𝜆 − 𝜆𝑢2(3.16)
𝜕𝐻
1
= 1 − 2𝜆𝑢 ⇒ 𝑢∗ =
𝜕𝑢
2𝜆(3.17)
{
𝑥 ′ (𝑡) = 1 − 𝑢2
𝑥(0) = 1(3.18)
𝜆′ (𝑡) = −1
𝜆(1) = 0(3.19)

One thing to note about this problem is the relationship of the control to the adjoint. The
optimal control is inversely related to the adjoint, which causes the control to have issues as time
approaches 1. Thus this problem does not have a solution. This problem was used to see how the
three methods handle this fact: to see what the methods do when there is not supposed to be an
optimal control.

Chapter 4: Forward Backward Sweep
---------------------------------

Section 1: Analytical Process
-----------------------------

The first method that will be discussed is the Forward Backward Sweep (FBS). This
iterative method is named based on how the algorithm solves the problem’s state and adjoint
ODE’s. Given an approximation of the control function, FBS first solves the state ‘forward’ in
time (from 𝑡0 to 𝑡1 ) then solves the adjoint ‘backward’ (from 𝑡1 to 𝑡0 ). Once it has found the
state and adjoint functions, the control is updated based on (2.05) and then the state, control, and
adjoint are tested for convergence against a user provided tolerance and depending on that, the
algorithm eithers starts the process over using the updated control or the algorithm terminates
with the final approximations for the state, adjoint, and control functions considered as the
solution to the optimal control problem. The code developed is based heavily on the code listed
in [1], which was based on work from [8], but it has been generalized so that it can be used to
solve other problems, not just the problem (P1), for which it was built for.
Before starting, an initial value is needed for the control vector. In every case, this initial
value is a 𝑁 + 1 vector of zeros. With this, the FBS can begin and it does so with the state ODE.
To solve the state ODE, a simple RK4 method is applied, but to solve the adjoint ODE, the RK4
method has to be adapted to account for solving backwards in time. This however is the only
difference between the two RK4 algorithms. The first algorithm below is a translation of the
RK4 to work for 3 inputs, and the second is from the RK4 outfitted for 4 inputs and to solve
backwards. In both algorithms, the 𝑖 represents the 𝑖 𝑡ℎ element of the vector.

Runge-Kutta 4 (with 3 input update) Algorithm
URK4
𝐾1 = 𝑓(𝑡𝑖 , 𝑥𝑖 , 𝑢𝑖 )
ℎ
ℎ
1
𝐾2 = 𝑓 (𝑡𝑖 + , 𝑥𝑖 + 𝐾1 , (𝑢𝑖 + 𝑢𝑖+1 ))
2
2
2
ℎ
ℎ
1
𝐾3 = 𝑓 (𝑡𝑖 + , 𝑥𝑖 + 𝐾2 , (𝑢𝑖 + 𝑢𝑖+1 ))
2
2
2
𝐾4 = 𝑓(𝑡𝑖 + ℎ, 𝑥𝑖 + ℎ𝐾3 , 𝑢𝑖+1 )
ℎ
𝑥𝑖+1 = 𝑥𝑖 + (𝐾1 + 2𝐾2 + 2𝐾3 + 𝐾4 )
6
Backward Runge-Kutta 4
BRK4
𝑗 = 𝑁+2−𝑖
𝐾1 = 𝑓(𝑡𝑗 , 𝜆𝑗 , 𝑥𝑗 , 𝑢𝑗 )
ℎ
ℎ
1
1
𝐾2 = 𝑓 (𝑡𝑗 − , 𝜆𝑗 − 𝐾1 , (𝑥𝑗 + 𝑥𝑗−1 ), (𝑢𝑗 + 𝑢𝑗−1 ))
2
2
2
2
ℎ
ℎ
1
1
𝐾3 = 𝑓 (𝑡𝑗 − , 𝜆𝑗 − 𝐾2 , (𝑥𝑗 + 𝑥𝑗−1 ), (𝑢𝑗 + 𝑢𝑗−1 ))
2
2
2
2
𝐾4 = 𝑓(𝑡𝑗 − ℎ, 𝜆𝑗 − ℎ𝐾3 , 𝑥𝑗−1 , 𝑢𝑗−1 )
ℎ
𝜆𝑗−1 = 𝜆𝑗 − (𝐾1 + 2𝐾2 + 2𝐾3 + 𝐾4 )
6
Looking at the algorithms, it can be seen that the major difference in URK4 and BRK4 is
that the index counts down towards one instead of counting forward and all the time steps are
negative.
Now the algorithm has a state and a control for the current step, but before the program
can test for convergence, the actual control needs to be calculated. This means the actual control

for the current step is some mixture of the current control, 𝑢𝑛𝑒𝑤 , and the control from the past
step, 𝑢𝑜𝑙𝑑 . This can be done in many ways. One can simply take all of 𝑢𝑛𝑒𝑤 and disregard 𝑢𝑜𝑙𝑑
all together. Another is taking the average of the 𝑢𝑛𝑒𝑤 and 𝑢𝑜𝑙𝑑 and the last is an adaptive
scheme. This adaptive scheme is seen in equation (4.01). In (4.01) the variable 𝑐 𝑘 is a constant
such that 0 < 𝑐 < 1 and 𝑘 is the iteration number, not an exponent.
𝑢 = 𝑢𝑛𝑒𝑤 ∗ (1 − 𝑐 𝑘 ) + 𝑢𝑜𝑙𝑑 ∗ 𝑐 𝑘
(4.01)
Generally when this method is used, the larger 𝑘 gets, the less and less of the current
control is used in the mixture. Generally by doing this, the algorithm will converge faster,
however in the three test problems, the difference in convergence was not substantial, thus the
algorithm is set to take an average of the old control and the current control, though the code can
easily be adapted to use the equation set up in (4.01)
Once these two processes are done and 𝑢 has been calculated, the code calculates the
error terms in order to check for convergence. In the FBS, at the end of each iteration, it tests the
change between the newly calculated state, control and adjoint vector against the old state,
control, and adjoint to see if the difference in each is small enough to stop the algorithm. In the
FBS function, this is done when the test variable becomes positive. The test variable is the
minimum of all of the relative errors of the state, adjoint, and control. The relative error, for the
state vector, 𝑥, is given below. Note the 𝑘 represents the iteration step, not the 𝑘 𝑡ℎ element of 𝑥.
‖𝑥 (𝑘) − 𝑥 (𝑘+1) ‖1
‖𝑥 (𝑘) ‖1
16
≤𝛿
(4.02)

The relative error, as seen in equation (4.02) is then solved so that there is no division
because it is possible that ‖𝑥 (𝑘) ‖1 ≈ 0. When this is done, the result is equation (4.03)
𝛿‖𝑥 (𝑘) ‖1 − ‖𝑥 (𝑘) − 𝑥 (𝑘+1) ‖1 ≥ 0
(4.03)
When this is true for all three vectors being tested, the algorithm stops and the current
control is the optimal control approximation.
As an example of the outputs, the FBS was applied to the (P1), and the results are
displayed in Figure 1. In Figure 1, there are three graphs; the State, Control, and the Adjoint.

Section 2:
Convergence
Now that the process has been presented, a study of the convergence of the FBS is
necessary. One result is from the paper [3]. The theorem states that if a Lipschitz condition is
assumed for the integrand of (SP) and the equations for the state (2.02) and adjoint (2.03)
ODE’s, and that there exists a constant 𝑐0 (defined in the paper), then the FBS will converge if
the 𝑐0 is small enough. Another set of restrictions are that either the FBS works only if the
Lipschitz constants for the state, adjoint, and control is small enough or the time interval is small.
Because of these restrictions, this method does not work in most cases.

Chapter 5:
Shooter Method
Section 1:
Analytical Process
The Shooter Method (SM) is another way to solve an optimal control problem, like (SP).
This method still solves the ODE’s like the FBS with two exceptions: this method takes an
initial value for the adjoint equation and solves it forward, and then using a root finding method
for convergence, finds the initial time value that makes the adjoint equal to zero at time 𝑡1 .
Though the process of picking a new starting value for this process can be different, the
overall algorithm works the same. A different take on this can be found in [1]. The algorithm
first takes an initial interval. This interval is the range that contains an initial value for the
adjoint (at 𝑡0 ) will produce the desired end result of zero (𝜆(𝑡1 ) = 0). The algorithm tests the
end points of the interval as well as the test value determined by the root finding method. If the
test value does not produce a 𝜆(𝑡1 ) that is within tolerance of zero, it will use this information as
well as the 𝜆(𝑡1 ) data about the endpoint to produce a new test value. The three ways that the
algorithm does that is either by doing a bisection, secant, or regula falsi root finding scheme.
The Runge-Kutta algorithm here is actually slightly different than the one used in the
FBS. This Runge-Kutta takes the vector formed by the state and adjoint ODE’S and runs the
Runge-Kutta process once with both terms at the same time, thus it is solving the differential in
equation (5.01).
𝑔(𝑡, 𝜙1 , 𝑢)
Δ(𝑡, 𝜙, 𝑢) = [𝑥′] = [
]
ℎ(𝑡, 𝜙1 , 𝜙2 , 𝑢)
𝜆′
{
𝑥0
𝑥(0)
[
] = [𝜆 ]

Here, one thing to note is what 𝜙 represents. It is a vector of the state and adjoint
𝑥
variable i.e. 𝜙 = [ ].
𝜆
Referring back to RK4, between each 𝑘𝑖 values, the algorithm computes the value for the
control with the current state and adjoint values, then used that to find the value of the next 𝐾𝑖
value. This can be seen by observing the algorithm in SRK4.
Runge-Kutta for Shooter Method
SRK4
𝑥𝑖
𝑋 = [𝜆 ]
𝑈 = 𝑢(𝑡𝑖 , 𝑋1 , 𝑋2 )
𝑖
𝐾1 = Δ(𝑡, 𝑋, 𝑈)
𝑥𝑖
ℎ
𝑋 = [𝜆 ] + 𝐾1
𝑖
2
ℎ
𝑈 = 𝑢 (𝑡𝑖 + , 𝑋1 , 𝑋2 )
2
ℎ
𝐾2 = Δ (𝑡 + , 𝑋, 𝑈)
2
ℎ
𝑈 = 𝑢 (𝑡𝑖 + , 𝑋1 , 𝑋2 )
2
𝑥𝑖
ℎ
𝑋 = [𝜆 ] + 𝐾2
𝑖
2
ℎ
𝐾3 = Δ (𝑡 + , 𝑋, 𝑈)
2
𝑥𝑖
𝑋 = [𝜆 ] + ℎ𝐾3
𝑖
𝑈 = 𝑢(𝑡𝑖 + ℎ, 𝑋1 , 𝑋2 )
𝐾4 = Δ(𝑡 + ℎ, 𝑋, 𝑈)
𝑥𝑖
ℎ
𝑋̅ = [𝜆 ] + (𝐾1 + 2𝐾2 + 2𝐾3 + 𝐾4 )
𝑖
6
𝑥𝑖+1 = 𝑋̅1
𝜆𝑖+1 = 𝑋̅2

By inspection, for each 𝐾𝑖 value needed for the process, the algorithm computes the
changes in the state and adjoint vector, then updates the control, and then computes the current
𝐾𝑖 value. When this process is finished, it computes the next term for the state and adjoint, and
then runs the algorithm again until it has computed each element of the corresponding vector.
Once the Shooter Method has successfully calculated the state and adjoint values—
including the values using the left and right endpoints of the interval of initial adjoint values—a
zero-finding method of the users choice will determine if the initial guess produces a value close
enough to zero, or if an updated initial guess for the adjoint needs to be found. As mentioned
before, there are three different root finding methods used for this algorithm: Bisection, Secant,
and Regula-Falsi. For all three algorithms, let Λ(𝜆0 ) denote the process that sets the initial value
for the adjoint as 𝜆0 , i.e. λ(𝑡0 ) = 𝜆0 , computes the adjoint and then sets Λ(𝜆0 ) as the value of
the adjoint at 𝑡1 , i.e. Λ(𝜆0 ) = 𝜆(𝑡1 ). In the Bisection and Regula-Falsi methods, an initial
interval is needed. This interval, [𝑎0 , 𝑏0 ], needs to exist such that ideal 𝜆0 ∈ [𝑎0 , 𝑏0 ] and Λ(𝑎0 ) ∙
Λ(𝑏0 ) < 0. The Secant Method is a strict update of the value that moves closer to Λ = 0.
In the Bisection method, 𝑥𝑘 is the value being tested to see if Λ(𝑥𝑘 )is close to zero. The
Bisection method takes 𝑥𝑘 and the interval [𝑎𝑘 , 𝑏𝑘 ], determines which half the solution lies in,
and then uses the midpoint of the half-interval as the next test value and updates the interval
endpoints. This process can be found in ZF1. The Bisection method terminates when
|Λ(𝑥𝑘+1 )| < 𝛿 ̅ ≪ 1.

Bisection
ZF1
If Λ(𝑎𝑘 ) ∙ Λ(𝑥𝑘 ) < 0
𝑎𝑘+1 = 𝑎𝑘
𝑏𝑘+1 = 𝑥𝑘
1
𝑥𝑘+1 = 2 (𝑎𝑘+1 + 𝑏𝑘+1 )
Else
𝑎𝑘+1 = 𝑥𝑘
𝑏𝑘+1 = 𝑏𝑘
1
𝑥𝑘+1 = (𝑎𝑘+1 + 𝑏𝑘+1 )
2
The next breakdown is for the Secant Method. It differs from Bisection and Regula Falsi
because it is an update of the value, not of the interval. The way it does that is by taking the
previous two values, 𝑥𝑘 and 𝑥𝑘+1 , and constructs the secant line between these two values. The
point in which the secant line is zero is the next value in the sequence, 𝑥𝑘+2. The formula for
this is found in ZF2. This method terminates when |Λ(𝑥𝑘+2 )| < 𝛿 ̅ ≪ 1.
Secant
ZF2
𝑥𝑘+2 = 𝑥𝑘+1 − Λ(𝑥𝑘+1 )
𝑥𝑘+1 − 𝑥𝑘
Λ(𝑥𝑘+1 ) − Λ(𝑥𝑘 )
The last method is the Regula Falsi method. This method is a blend of the last two. It
updates the interval like Bisection, but instead uses the Secant Method value instead of the
midpoint. The method can be found in ZF3. The Regula Falsi method terminates, like the last
two methods, when |Λ(𝑥𝑘+1 )| < 𝛿 ̅ ≪ 1.

Regula-Falsi
ZF3
If Λ(𝑎𝑘 ) ∙ Λ(𝑥𝑘 ) < 0
𝑎𝑘+1 = 𝑎𝑘
𝑏𝑘+1 = 𝑥𝑘
𝑥𝑘+1 = 𝑏𝑘+1 −
Else
𝑎𝑘+1 = 𝑥𝑘
𝑏𝑘+1 = 𝑏𝑘
𝑥𝑘+1 = 𝑏𝑘+1 −
Λ(𝑏𝑘+1 )(𝑏𝑘+1 −𝑎𝑘+1 )
Λ(𝑏𝑘+1 )−Λ(𝑎𝑘+1 )
Λ(𝑏𝑘+1 )(𝑏𝑘+1 −𝑎𝑘+1 )
Λ(𝑏𝑘+1 )−Λ(𝑎𝑘+1 )
In regards to the Shooter Method, once the root finding method has found a value, it tests
it to see if it is small enough. If it is, then the algorithm terminates and the current
approximations for the state, adjoint, and control are the solution. If not, it loops back through
the algorithm with updated initial conditions and starts the process over again.
Section 2:
Convergence
The convergence of the Shooter Method depends on three things. The first two are the
two numerical processes that make up the method: Runge-Kutta and a root finding method. The
last dependence is initial data set. This section will discuss how each method affects the
convergence. When it comes to converging, it is known from the theory discussed in Chapter 2
that Runge-Kutta will find an approximate solution for small enough h. To make sure ℎ is small
enough, the number of mesh points, 𝑁, needs to be large. Thus the root finding method
convergence is what needs to be shown. From [4], the proofs of convergence for all three

methods are given. All three methods convergence is based on the Intermediate Value Theorem,
which states that if a function, 𝑝(𝑥), is continuous over a closed interval, [𝑎, 𝑏], and if 𝑝(𝑎) ∙
𝑝(𝑏) < 0, then there exists a value 𝜉 ∈ [𝑎, 𝑏] such that 𝑝(𝜉) = 0. Thus, the convergence of the
Shooter Method will depend on the correct initial interval for the adjoint. If the Shooter Method
does indeed have the correction initial interval, then the Shooter can approximate the state,
adjoint, and control. The Shooter Method terminates when the 𝑙1 –norm of the change in the
control from the last control is below a tolerance, 𝛿.
To find the initial interval, two methods were implemented. Mathematically, these
intervals have to have certain properties. The first thing the interval needs to satisfy is the
Intermediate Value Theorem so that it satisfies the zero method. What is meant by this is that
there needs to be an interval that contains a value that, if set to 𝜆(𝑡0 ), using Runge-Kutta, will
produce an adjoint vector such that 𝜆(𝑡1 ) = 0. To find this interval, two different MATLAB
functions are used to find this interval two different ways.
The first, which is the lambda0_finder, is used when no previous information about
the interval is found. The MATLAB functions starts at −100 and counts up until it finds a value
that causes Runge-Kutta to produce an adjoint vector whose last value that can be computed
successfully. When it finds one, the function then keeps counting up until it finds another value
that has the opposite sign. Once it finds this value, it uses a bisection-like process to narrow the
interval. This small interval is the initial interval that will be used for the Shooter Method.
The second MATLAB function, which is called lambda0_finder_adjusted. This
function is used when there is previous information given about the interval, for example the
adjoint produced by FBS. This function takes this approximation to the initial value and moves
left and right until it finds the desired interval. This interval is then used as the initial interval for

the Shooter Method. These two functions were created to help find the interval needed to run the
Shooter Method. These methods are used mostly for the initial interval for (P1). For the other
two problems, information from FBS is found, then the interval is built around it.
Since the Shooter Method has three different options for finding zeros, a comparison
needs to be made among the three of them. The difference can be seen in Table 2. The figure
has a few different parameter sets for (P1) as well as (P2) and (P3). For each of the root finding
methods used in the Shooter Method, the work to find the initial interval is not accounted for.

As can be seen by Table 2, generally, the bisection method takes more iterations to
converge at the answer while the Secant and Regula Falsi take the same number of iterations.
Next the accuracy of the Shooter with the three root finding methods needs to be seen. By using
the Shooter Method with the three root finding methods and applying them to (P2), the accuracy
of the root finding methods can be seen in Table 3.

With the results from Tables 2 and 3, it can be concluded that Regula Falsi is the better
root finding method, thus for the comparisons in Chapter 7, it will be used as the root finding
method when the Shooter Method is compared to the other methods.

Chapter 6:
Direct Optimization Process
Section 1:
Analytical Process
For this process, no adjoint equation is necessary. Instead, the 𝐽(𝑢) functional will be
converted into an integral approximation then use an optimization process to solve for the
maximizing or minimizing control 𝑢 by use of the MATLAB Optimization Toolbox (MOT).
The first step is to convert our integral functional, 𝐽, from (2.09) into a function that the
MOT can work with. Though are many ways of doing just that, the Trapezoid Rule of
integration approximation will be the only one we use. The algorithm is not dependent upon this
fact and can be adapted easily to incorporate other integration approximations. The Trapezoid
Rule is defined in equation (6.01).
Trapezoid Rule
(6.01)
𝑛−1
𝑏
ℎ
∫ 𝑓(𝑥) 𝑑𝑥 ≈ [𝑓(𝑎) + 𝑓(𝑏) + 2 ∑ 𝑓(𝑥𝑖 )]
2
𝑎
𝑖=1
where 𝑥𝑖 = 𝑎 + 𝑖ℎ
Note that in (6.01), 𝑓 does not have to be a function of a single variable. Here 𝑥 can represent a
single value or a collection of variables. A thing to note, that equation (6.01) is continuous as
long as 𝑓 is continuous. This will play a part when the convergence of the Direct Optimization is
discussed in the next section.
Now that the Trapezoid Rule has been defined, the process for solving for the optimal
control, 𝑢∗ , by optimization algorithm can be explained. The algorithm starts by first converting

𝐽 into an appropriate function. In doing this, the algorithm creates a function of the vector 𝑢 so
that the MOT finds the minimum. This function proceeds by first computing the state vector
using Runge-Kutta given the current 𝑢, then it uses the Trapezoid Rule with the state and control
in the objective functional to create the final value. The last step is to negate the function. This
is because the MOT can only find minimum, and from theory, the maximum of a function is the
minimum of the negative of the function.
The next step is to actually use the MOT. The MOT provides functions for finding
parameters that minimize objectives while satisfying constraints. The toolbox includes solvers
for linear programming, mixed-integer linear programming, quadratic programming, nonlinear
optimization, and nonlinear least squares. They can be used to find the optimal solutions to
continuous and discrete problems, perform tradeoff analyses, and incorporate optimization
methods into algorithms and applications.
The first thing that needs to be set up before optimizing is the options for the MOT.
These options determines the type of numerical optimization that will be done. Experimenting
with these options would make one of the test problem produce a better result while causing the
opposite effect for the other two test problems. Thus when the algorithm was run to test the
three problems, all of these are left to default, with the exception of Algorithm, which is set to
‘quasi-Newton’. This refers to how it computes the Hessian in the optimization process.
The MOT has many different minimizing methods. The one that was used here is the
function fminunc. This particular function ends depending certain parameters and reports the
result using a certain output, called exitflag. This variable indicates why the algorithm
terminates. One can find ways to interpret the exitflag from the function from MATLAB.
In the case for the three test problems, this variable is equal to 1. What this means is that the

condition met for the algorithm to terminate and call the value it has the ‘solution’ is when the
magnitude of the gradient is small enough.
Section 2:
Convergence
This method is going to converge because of the Extreme Value Theorem. As mentioned
with the Trapezoid Rule, it can be seen that equation (6.01) is continuous as long as the 𝑓
function in the objective function 𝐽 is continuous on the interval [𝑡0 , 𝑡1 ]. When it comes to
iteration rates, MOT keeps track of the number of iterations it takes to find a minimum. Each
time it finds a value and tests it to be a potential minimum, the MOT counts that as an iteration
step. In order to compare it to the other two methods, our implementation of the algorithm keeps
track of the number of function evaluations.

Chapter 7:
Processes Applied to Problems



