Experimental results of a control time delay system using optimal control - art04 - 2011
=================================================

The optimal control for a temperature system with time delay is considered. Experimental results of the
control system are presented in this contribution. The integral term in the controller is approximated by
a quadrature method. Experimental results obtained demonstrate the effectiveness of the approximation
method. By a simple analysis in time domain, we demonstrate the robustness of the optimal controller.
We compare the optimal control’s performance with an industrial PID controller. This controller was
robustly tuned. The experiments indicate the correct optimization of the plant when the optimal control was
employed, despite limitations in the sensor, actuators, non-modeled dynamics, and uncertain parameters
of the process.

KEY WORDS: time delay systems; optimal control; experimental results; robust stability; industrial PID controller

1. INTRODUCTION
---------------

It is widely known that a number of time-delay systems are described by the following model:

.. math::

   \frac{Y(s)}{U(s)} = G(s) = \frac{K e^{−h}}{T s+1}

 (1)

Even though it might seem trivial to control stable systems described by the model of Equation (1),
for which a PID controller may suffice, it is not so, as it is shown next. It is not straightforward
to tune a PID controller for a first order and stable system with delays, because the presence
of time delays in the input lead to either poor performance or unstable behavior [1–3]. In fact,
specialized software exists for tuning PID controllers when an approximated model in the form
given by Equation (1) is considered. This is the case of the Expert Tune Software, which has PID
Loop Optimization for advanced tuning. Furthermore, numerous scientific reports have also been
presented, indicating the complexity of using PID controllers for this class of plants. For example,
costs are calculated when a PID controller is poorly tuned [4]. In [5] an approximated model of
Equation (1) for a refining process is considered and some problems associated when PID badly
tuned are reported. The same model and similar difficulties are reported in [6]. In contrast, we aim
to develop an optimal control strategy, which we claim is more efficient than PID controllers. To
validate our claims we also present a comparison study between an industrial PID (robustly tuned)
and the optimal control law implemented by us.

The optimal control approach of time delay systems has been proposed as an alternative to PID
controllers, namely the Maximum Principle [7], the suboptimal control (where time delays are
considered as disturbances [8]), or the use of operators in infinite dimensional spaces [9–12]. Also,
Dynamic Programming [13–16] and the use of complete type Lyapunov Krasovskii functionals
[17] have been explored in order to obtain suboptimal control [18]. The considered systems in
those reports present delays in the state, in the input or both. If a system displays delays in the
state and the optimal control uses state feedback, then the control presents distributed delays
in the states [13]. As it is proved in [19], when the system depicts delays in the control, the
controller has distributed delays in the control signal. The implementation of control laws involving
distributed delays has been studied by many authors. For example in [20, 21] the integral term of the
controller is approximated by a sum of point-wise delays by using a numerical quadrature method.
In [22] an optimal control for systems with delayed state is based on a numerical integration to
solve the set of equations on a grid. The approximated solution is found step by step on each
subinterval. This solution defines the matrices of the controller. Implementation problems have
been reported regarding unstable delayed systems. In [23] a quadrature method is used in order
to implement the integral term; however, when a more accurate approximation of the integral
term is used, the closed loop system becomes unstable. In [24], an analysis of the causes of
such behavior is presented: the characteristic equation in closed loop is a neutral type and the
poles of large magnitude are unstable. The approximation problem is treated in the frequency
domain considering a rectangular pulse in the integral and taking the approximation directly in the
z-domain [25].

Despite the fact that stable systems are not thought to show the implementation problems of
control laws of unstable systems [26], experimental validation, though important, is still missing.
Moreover, this experimental validation shows that even in the presence of nonlinear disturbances
and uncertain parameters, the optimal control law presents good performance.
Hence we present our own results for a temperature control system (stable in open-loop), which
is regulated by an optimal control law of infinite horizon. The optimal control involves a distributed
time delay in the controller and it is time invariant. We demonstrate that the exact control law is
robustly stable under nonlinear disturbances. Our experimental results validate the affectivity of
the quadrature approximation method.

Our results probe that implemented the optimal control law displays a similar performance, in
terms of the Integral Square Error (ISE), than an industrial PID used for comparison purposes.
Nevertheless, we must outline that the best performance of the PID was achieved when it was
robustly tuned. Our experiments indicate that the optimal controller is more energy efficient, since
it does not stay in the saturation region as much as the PID does.

The paper is organized as follows: In Section 2, considering nonlinear disturbances in the
nominal model, robust stability conditions are obtained. Experimental results are presented in
Section 3. Section 4 presents comparative results with an industrial PID controller and a different
numerical integration method. Concluding remarks are given in Section 5.

Notation: Along the paper yt denotes a piece of the trajectory of the considered system, i.e.
:math:`y_t = y(t + \theta), \theta ∈[−h,`0].

2. ROBUST STABILITY IN CLOSED LOOP
----------------------------------

Consider the nominal system given previously by Equation (1). One can obtain the difference
differential equation as

.. math::

   \begin{matrix}
   y ̇(t) = −ay(t)+bu(t −h)  \\
   y(0) = y_0, u(\theta)= \mu(\theta), \theta ∈[−h,0]
   \end{matrix}

(2)


where a=1/T , b= K/T , and :math:`\mu(\theta)` is an arbitrary piecewise continuous function. We need to find
a control law u such that the performance index

.. math::

   J = \int_0^∞(y^2^Q + u^2R)dt 

(3)

is minimum. Here :math:`Q \geq 0` and R>0. In order to obtain the controller u, we use the approach given
in [19], modified for the infinite horizon problem. Choosing v(t)=u(t −h), the performance index
can be rewritten as

.. math::

   J = \int^h^_0 y^2Q dt + \int^{\infty}_h (x^2Q+v^2R) dt

and the system (2) is

.. math::

   y'̇(t)=−ay(t)+bv(t), t ∈[h,∞)

with performance index

.. math::

   J = \int^{\infty}_h (x^2Q+v^2R)dt

The control law v(t) can be found by classical methods of delayed-free optimal control:

.. math::

   v(t)=−F y(t)

where :math:`F =−^{R−}b1`bP, and P satisfies an algebraic Riccati equation [27]. As only y(t −h) is available
as feedback to the controller, then

.. math::

   u(t −h)=−^{Fe}ah y(t −h \int_{t-h}^t e^{-a(s-t)} bu(s-h) ds

In Equation (4), the term u(s−h) can be obtained by Equation (2), and the controller u(t −h) can
be rewritten as

.. math::

   u(t −h)=−^{Fe}ah y(t −h)\int F^t_{t−} e^{−a(s−} [\dot{y}̇(s)+ay(s)]ds

The first integral term is solved when integrating by parts

.. math::

   −F\int^t_{t−} e^{−a(s−} \dot{y}̇(s)ds =−F y(t)+Feah y(t −h)−aF  t
t−h
e−a(s−t)
y(s)ds

yielding

u(t −h)=−F y(t)−2aF  0
−h
e−as y(t +s)ds (5)

Replacing the control law (5) in the nominal system (2):
y ̇(t)=a0y(t)+
 0
−h
d(s)y(t +s) ds

where

a0 =(−a−bF), d(s)=−2abFe−as

When nonlinear disturbances are considered in the model, we obtain the following:

 ̇
y ̄(t)=a0 y ̄(t)+
 0
−h
d(s)y ̄(t +s) ds+ f (y ̄) (6)

where disturbance f (y ̄) satisfies

| f (y ̄)||  ̄y|, >0 (7)

Remark 1

The system described by Equation (6) is not optimally controlled, but we need to find delay-
dependent sufficient conditions, which guarantee the robust stability in closed loop. Because the

model of Equation (1) is only an approximation, it makes sense to suppose the existence of
non-modeled dynamics.
Sufficient conditions that assure robust stability under nonlinear disturbances satisfying (7) must
be found. Consider the following Lyapunov Krasovskii functional

V (y ̄t)=0 y ̄
2(t)+0
 t
t−h
y ̄
2(s)(s−t +h)ds, 0>0, 0>0

This functional is unbounded radially because

0  ̄y(t)2V (y ̄t)(0+0h2)  ̄y(t)2
h

Now, we calculate the time derivative of V (y ̄t) along the trajectories of the system described by
Equation (6):
dV(y ̄t)
dt




(6)
= (20a0+0h)y ̄

2(t)+20 y ̄(t)
 0
−h
d(s)y ̄(t +s)ds+20 y ̄(t) f (y ̄)−0
 0
−h
y ̄2(t +s) ds

After some direct majorizations, and using (7):
dV (y ̄t)
dt




(6)
 −
 0
−h
[y ̄(t) y ̄(t +s)]
⎡
⎣
20
(a+bF −)
h −0 20abFe−as
20abFe−as 0
⎤
⎦
 y ̄(t)
y ̄(t +s)
ds

If matrix

M(s)=
⎡
⎣
20
(a+bF −)
h −0 20abFe−as
20abFe−as 0
⎤
⎦>0

then we conclude that the derivative along the trajectories of system (6) is stable. Matrix M(s) is
positive definite if

0<20
(a+bF −)
h −0 for all t0

and
0<[2Fb00+2a00−h2

0−200−4F2a2b2h2

0e−2as] for s ∈[−h,0]

Observe that −F2a2b2h2

0e−2as−F2a2b2h2

0, because s ∈[−h,0]. Consequently,

0 < [2Fb00+2a00−h2

0−200−4F2a2b2h2
0e−2as]

< 2Fb00+2a00−h2

0−200−4F2a2b2h2
0

The following lemma is established:
Lemma 2
Consider the disturbed system (6) and (7). System of Equation (6) is robustly stable under nonlinear
disturbances if positive constants 0 and 0 exist such that the following inequalities are satisfied:

0 < 20
(a+bF −)
h −0
0 < 2Fb00+2a00−h2

0−200−4F2a2b2
h2
0

(8)

3. EXPERIMENTAL RESULTS

In this section we present experimental results for a temperature control system. The system is a
box that has three fans actuated by three DC motors (3–12 V DC), a source of heat (an electrical
grid of 120 V AC, but we introduced 17.5 V AC), a temperature sensor (integrated circuit LM35),
and a tunnel as output in the box. We take as input the three fans whereas the feeding source of
heat remains constant. Figure 1 shows the instrumentation diagram of the system:
The approximated linear model of the plant is obtained by the open loop Ziegler–Nichols
method [28]:

Y (s)
U(s)
=G(s)= 0.1e−14s
226s+1 (9)
Equation (9) clearly complies with model of Equation (1), where Y (s) is the mapped temperature
and U(s) is the voltage applied to the fans. This approximation was obtained by analyzing the step
response of the system (Figure 2).
The external temperature was 25◦C. In the time domain we have that

y ̇(t)=−0.0044248y(t)+0.00044248u(t−14) (10)

here the units are in volts (100 mV represent 1◦C) and the time is expressed in seconds. Using the
equivalent controller given by (5) the optimal control is
u(t −14)=−Fe−0.0044248 y(t)−0.0088496F
 0
−14
e−0.0044248s y(t +s) ds

where F =70. This value was obtained by the solution of the Riccati equation and Q =1260 and
R=0.02. The closed loop is

y ̇(t)=a0(t)y(t)+
 0
−h
d(t +s)y(t +s)ds

where

a0 = −0.0073468
d(s) = −0.0002741e−0.0044248s

By employing the conditions given by Lemma (2), we obtain the following inequalities

0 < g1 =20

(0.035398−)
14 −0
0 < g2 =0.07079 700−142

0−1.051 9×10−6
2
0−200
Choosing 0 =1000, 0 =0.1, =0.001, the former inequalities are satisfied.

0<g1=4.814, 0<g2=5.6878

Hence, the mathematical analysis demonstrates that the system is robustly stable under nonlinear
disturbances. Our aim is to implement and validate the control law in real conditions.
3.1. Implementation of the control law
We need to control the temperature in the box considering the fans as actuators. By employing the
optimal controller (4), we have rewritten the control law as:
u(t −h)=−Feah y(t −h)−F
 0
−h
e−asbu(t +s−h)ds

If we approximate this control law by a quadrature method (composed Simpson’s rule), we obtain
the following controller:
u(t −h)  −Feah y(t −h)−F

g
3
(eah bu(t −2h)+bu(t −h))

+
2g
3
q
−1
k=1
(e−ax2k bu(t +s2k −h))+
4g
3
q
k=1
(e−ax2k−1 bu(t +s2k−1−h))
−adj
where g=h/2q, q is the number of partitions, sk = yk =−h+(h/2q)k. We performed a change
of variable in order to reach a Set Point (SP) different than zero, as we want to cool the box.
This change of variable is y ̄(t −h)= y(t −h)−SP. We add a constant term (adj=SP/(T )(b)) in
the control law that defines the approximated value in the actuators to hold the temperature when
the error is zero.
As the process has a large constant time (226 s), and a delay of 14 s, we consider that the digital
implementation is almost continuous with a sample period of 1 s. The control is implemented

on a personal computer with an Intel Pentium 4 processor, 2 GHz, 1 GB RAM, and a National
Instruments data acquisition card PCI-6071 E. The software is Lab View of National Instruments,
V. 7.1. The initial temperature in the camera was 50◦C, and the reference was set at 45◦C. The
external temperature at the initial moment was 25◦C. A sample compression block in Lab View
was used in order to filter the noise of the sensor. Figure 3 illustrates the obtained results of the
process variable (PV).
Figure 4 shows the control signal.
Remark 3
When temperature reaches or is around the SP, some problems appear in order to maintain the
temperature in the SP, because the value adj depends on values that are not precise but approximated
(T,b). The particular choosing of the parameters Q and R penalizes the convergence (Q) and the
control law (R) can take a large value, but another choosing of Q and R could give different
results.
Now, consider the case when temperature is risen. We elevated the applied voltage in the
grid to 20 V. This situation represents a disturbance in the plant. In this experiment the external
temperature was 25◦C, the initial temperature in the box was 50◦C, and the SP was fixed at 45◦C.
The disturbance was introduced in the second 1500. The following illustration shows the obtained
results (Figure 5).
The control signal is depicted in Figure 6.

We observe that the system remains stable, but the performance becomes poor. An alternative
is to elevate de controller gain, so we choose F =100 and introduce a disturbance in the second
700. Figure 7 shows the obtained results.
The control signal is shown in Figure 8.

Remark 4
In Figure 7, we observe that if the gain ought to be elevated, the system’s response displays a
better performance and the disturbances are not affected too much, but in Figure 8 the control
signal remains saturated for longer.
3.2. Response to trajectory tracking
In this section we present a more demanding task for the optimal controller. It has to adjust or
adapt as different SPs where set on line. This is known as trajectory tracking. In order to compare
the response in open and closed loop, we made an experiment applying the voltage corresponding
to the temperature of the SP (adj=SP/(T )(b)). Clearly, if the initial conditions are different than
the SP, the plant in open loop does not track the reference. Figure 9 shows the obtained results in
both open and closed loop, applying optimal the control law.
Figure 10 shows the control signal and the voltage applied in open loop.
A good performance of the plant can be observed and the control signal stays saturated briefly.
In the next section we present a comparison with a PID controller. For this experiment a composed
Simpson’s rule was employed, with different step numbers. Figure 11 shows the responses using
different step numbers.
Figure 12 shows the optimal control law signal using three different values for the step.
Observe that the behavior of the plant in closed loop is similar. However, with q =100 the plant
displays smoother trajectory and the control ‘reacts’ faster when a change in the reference occurs.

4. COMPARISON WITH AN INDUSTRIAL PID CONTROLLER

In order to compare the performance of the proposed optimal controller, we carried a series of
experiments with an industrial PID controller (Honeywell DC1040). This controller reads signals

coming from a thermocouple, element that gives finer readings that the low-cost sensor we employed
for our optimal controller. The Honeywell DC1040 has the industrial standard output signal of

4–20 mA; it also possesses dead-band time compensation, which is a type of time-delay compen-
sation and the controller autotunes. This type of controller is widely used in the industry due

to facilities of programming and accuracy. Experiments were conducted with the industrial PID
controller using the same plant where the optimal control law was tested. The results are shown
in the following subsections.
4.1. Robust PID
The performance of the PID controller is improved by using different tuning techniques. We
selected the D-partitions method in order to obtain a robust PID controller. We calculated the
following stability zones for the PID controller when the approximated model (9) is considered:
Kp ∈[−10,259.9]. By choosing Kp =30 (BP=3.3), the stability region for Ki is [0,2.36], Ki =
Kp/Ti . The value of Ki =0.7 (Ti =42.85 s); with which we calculated the stability region for Kd ,
Kd ∈[0,769.5], Kd = KpTd . We choose Kd =150 (Td =5 s). Observe that the interval for Ki and
Kd depends on the selected values of Kp and Ki respectively, see [3]. The response of the plant
is illustrated in Figure 13.
Figure 14 shows the control signals of the optimal control and PID controller.

Figure 15 shows the robust stability zone for the PID controller.
In Table I we summarize the responses using the integral square errors of the previous control
strategies.
Our results prove that the optimal control law implemented displays a similar performance, in
terms of the Integral Square Error (ISE), than the industrial PID. Nevertheless, we must outline
that the best performance of the PID was achieved when it was robustly tuned. Our experiments
indicate that the optimal controller is more energy efficient, since it does not stay in the saturation
region as much as the PID does.
4.2. Composed trapezoidal rule
In this section the integral term in the optimal control law is approximated by the composed
trapezoidal rule with different step numbers. The controller could be calculated as:

u(t−h)  −Feah y ̄(t−h)−F

g
3
(eah bu(t−2h)+bu(t−h))+g
q
−1
k=1
(e−axk bu(t+sk−h))

−adj (11)

where g=h/q, q is the number of partitions, sk =xk =−h+(h/q)k. A change of variable in order
to reach a SP different than zero is done. In fact, as we want to cool the box this change of variable
is y ̄(t −h)= y(t −h)−SP. The constant term (adj=SP/(T )(b)) is added in the control law which
defines the approximated value in the actuators to hold the temperature when the error is zero.
Figure 16 shows the responses of the plant in closed loop with the control law (11) with three
values for the integration step q.
Figure 17 shows the control signal applied to the actuators.
The following table shows comparative results using the performance index given by (3) for the
control law implemented with the Composed Simpson and trapezoidal rules.
We observe a decrement in the numerical value of the index when the number of partitions are
increasing (Table II).

5. CONCLUSIONS

We obtained satisfactory experimental results in the implementation of the optimal control for
a type of system with time delay in the input. By Lyapunov Krasovskii analysis, we provided
sufficient conditions to satisfying robust stability for nonlinear disturbances. These experiments
give evidence about feasibility of the approximated controller involving distributed time delays.
With this report we fill a gap in the scientific literature for this class of systems by actually
controlling a real plant and providing significant experimental results. The comparison with and
industrial PID controller demonstrates both, the more efficient response of the optimal control, and
the complexity inherent to control this type of systems. Future work includes experimenting with
numerical optimization in order to tune the PID controller, and implementing nonlinear optimal
controllers for time delay systems.

REFERENCES

1. Silva JG, Datta A, Bhattacharyya SP. PID Controllers for Time Delay Systems. Birkhauser: Basel, 2004.
2. Huang YJ, Wang YJ. Robust PID controller design for non-minimum phase time delay systems. ISA Transaction
2001; 40(1):31–39.
3. Munoz LE, Santos O, L  ̃ opez V, Paz MA. Robust control PID for time delays systems.  ́ Novel Algorithms and
Techniques in Telecommunications, Automation and Industrial Electronics. Springer: Berlin, 2008; 129–133.
4. Buckbee G. Poor controller tuning drives up valve costs. Control Magazine 2002; 15:47–51.
5. Huang MD, Hsieh WD. Control loop tuning in Hsiaokang Refinery. Taiwan Sugar 2002; 49(4):19–22.
6. Lyons S. Optimizing steam supply in a chemical plant. Available from: http://www.expertune.com/articles/
Lyons2000/casestudy.html#author, report to Expert Tune Inc., 2000.
7. Kharatishvili GL. The maximum principle in the theory of optimal processes with delay (in Russian). Doklady
Akademii Nauk SSSR 1961; 136:39–42.
8. Malek-Zavarei M, Jamshidi M. Time Delay Systems, Analysis, Optimization and Applications. North Holland
Systems and Control Series, vol. 9. North-Holland: Amsterdam, 1987.
9. Delfour MC, McCalla C, Mitter SK. Stability and infinite-time quadratic cost problem for linear hereditary
differential systems. SIAM Journal on Control and Optimization 1975; 13(1):48–88.
10. Gibson JS. Linear quadratic optimal control of hereditary differential systems: infinite dimensional Riccati
equations and numerical approximations. SIAM Journal on Control and Optimization 1983; 21(1):95–139.
11. Kwong RH. A stability theory for the linear quadratic Gaussian problem for systems with delays in the state,
control, and observations. SIAM Journal on Control and Optimization 1980; 18:49–75.
12. Vinter RB, Kwong RH. The infinite time quadratic control problem for linear systems with state and control
delay. SIAM Journal on Control and Optimization 1981; 19(1):139–153.
13. Krasovskii NN. On analytic design of optimal controllers for systems with time delay. Prikladnaya Matematika
i Mekhanika 1962; 26(1):39–51. (On the analytic construction of an optimal control in a system with time lags.
Journal of Applied Mathematics and Mechanics 1962; 6(1):50–67).
14. Ross DW, Flugge-Lotz I. An optimal control problem for systems with differential difference equation dynamics.
SIAM Journal on Control and Optimization 1969; 7:609–623.
15. Kuhsner HJ, Barnea DI. On the control of a linear functional differential equation with quadratic cost. SIAM
Journal on Control and Optimization 1970; 8(2):257–272.
16. Uchida K, Shimemura E, Kubo T, Abe N. The linear quadratic optimal control approach to feedback control
design for systems with delay. Automatica 1988; 24(6):773–780.
17. Kharitonov VL, Zhabko AP. Lyapunov Krasovskii approach to the robust stability analysis of time delay systems.
Automatica 2003; 39(1):15–20.
18. Santos O, Mondie S, Kharitonov VL. Linear quadratic suboptimal control for time delays systems.  ́ International
Journal of Control 2009; 82(1):147–154.
19. Alekal Y, Brunovsky P, Chyung DH, Lee EB. The quadratic problem for systems with time delays. IEEE
Transactions on Automatic Control 1971; 16(6):673–687.
20. Manitus AZ, Olbrot AW. Finite spectrum assignment problem for systems with delays. IEEE Transactions on
Automatic Control 1979; 24(4):541–553.
21. Fiagbedzi YA, Pearson AE. Feedback stabilization of linear autonomous time lag systems. IEEE Transactions
on Automatic Control 1986; 31(9):847–855.
22. Eller DH, Aggarwal JK, Banks HT. Optimal control of linear time delay systems. IEEE Transactions on Automatic
Control 1969; 14(6):678–687.
23. Van Assche V, Dambrine M, Lafay JF. Some problems arising in the implementation of distributed delay control
laws. Proceedings of the 38th Conference on Decision and Control, Phoenix, AZ, U.S.A., 1999; 4668–4672.
24. Santos O, Mondie S. Control laws involving distributed time delays: robustness of the implementation.  ́ Proceedings
2000 American Control Conference, vol. 4, Chicago, IL, U.S.A., 2000; 2479–2480.
25. Zhong Q. On distributed delay in linear control laws, part I, discrete delay implementations. IEEE Transactions
on Automatic Control 2004; 49(11):2074–2080.
26. Mondie S, Michels W. Finite spectrum assignment of unstable time-delay systems with a safe implementation.  ́
IEEE Transactions on Automatic Control 2003; 48(12):2207–2212.
27. Kalman RE. Contributions to the theory of optimal control. Bolet ́ın de la Sociedad Matematica Mexicana  ́ 1960;
5:102–119.
28. Ziegler JG, Nichols NB. Optimum settings for automatic controllers. ASME Transaction 1942; 64:759–768.







