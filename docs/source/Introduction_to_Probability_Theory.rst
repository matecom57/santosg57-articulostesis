Introduction_to_Probability_Theory
==================================

https://manualdelatex.com/tutoriales/tipo-de-letra

1. Probability Spaces

1.1 Examples of random phenomena

1.2 Probability spaces

* to develop the formal mathematical structure, called a probabilty space
* random phenomena

envision -

* on the possible outcomes of the experiment
* we choose a set :math:`\Omega` whose points :math:`w` are associated with these outcomes.
* we next take a nonempty collection :math:`\mathscr{A}` of subsets of :math:`\Omega`  that is to represent the collection of "**events**" to which we wish to assign probabilities.
* By definition, now, an event means a set :math:`A` in :math:`\mathscr{A}`.
* The statement the event :math:`A` occurs means that the outcome of our experiment is represented by some point :math:`w \in A`
* if :math:`A` and :math:`B` are two events, the :math:`A \cup B` occurs if the outcome of our experiment is either represented by a point in A or a point in B.
* Now :math:`A \cap B` occurs if the outcome of our experiment is represented by some point that is in both A and B.
* Finally, to say that the event A does not occur is to say that the outcome of our experiment is not represented by a point in A, so that it must be represented by some point in :math:`A^c`.

**Definition 2** A probability measure P on a :math:`\sigma`-field of subsets :math:`\mathscr{A}` of a set :math:`\Omega` is a real-valued function having domain :math:`\mathscr{A}` satisfying the following properties:

(i) :math:`P(\Omega) = 1`

(ii) :math:`P(A) \geq 0` for all `A \in \mathscr{A}`.

(iii) If :math:`A_n` n=1, 2, 3, ..., are mutually disjoint sets in :math:`\mathscr{A}`, then

.. math::

   P(\bigcup_{n=1}^{\infty} A_n) = \sum_{n=1}^{\infty} P(A_n)

A probability space, denoted by :math:`(\Omega, \mathscr{A}, P)`, is a set :math:`\Omega`, a :math:`\sigma`-field of subsets :math:`\mathscr{A}`, and a probability measure P defined on :math:`\mathscr{A}`.


