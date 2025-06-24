Some novel concepts of intuitionistic fuzzy directed graphs with application in selecting a suitable place for opening restaurant
====================================================

In this manuscript, we ﬁrst initiate several types of eﬀective arcs of intuitionistic fuzzy directed graphs, followed by discussions on diﬀerent 
types of dominations in intuitionistic fuzzy directed graphs and their application in decision-making. The notion of dominations in fuzzy graphs, fuzzy 
directed graphs, intuitionistic fuzzy graphs and picture fuzzy graphs have been extensively discussed in the literature. Thus, the work presented in 
our study is two-fold: on one side, it extends the notion of domination in fuzzy directed graphs, while on the other side, it ﬁlls the gap existing in 
the literature. Initially, we introduce several types of eﬀective arcs like semi- 𝜆 eﬀective arc, semi- 𝜈 eﬀective arcs in intuitionistic fuzzy 
directed graphs. Subsequently, we initiate the notions of dominations and domination numbers for several types of intuitionistic fuzzy directed graphs 
based on these eﬀective arcs. We present numerous signiﬁcant characterizations of dominations in intuitionistic fuzzy directed graphs by utilizing 
minimal dominating sets. Furthermore, we investigate the minimal dominating sets and domination numbers of intuitionistic fuzzy-dipaths and dicycles, 
and provide various fascinating results. Finally, by utilizing the concepts presented in this study, we provide the algorithm for the solution of the 
problem related to decision-making regarding the opening of restaurants in various areas of the diﬀerent cities.

1. Introduction

The notion of fuzzy sets (FSs) was ﬁrstly initiated by Zadeh [1] in 1965. FSs found more ﬂexible compared to the classical sets. Due to its nature, 
numerous applications of FSs have been explored in various ﬁelds such as computer science, management sciences, artiﬁcial intelligence, 
decision-making etc. It has been observed that fuzzy logic manipulates complex types of information more eﬃciently than the classical logic. As the 
FSs are ﬂexible, many extensions of FSs have been initiated. In this regard, ﬁrst generalization of FSs termed IVFSs (depicted in Table 1) was 
explored by Zadeh [2]. In IVFSs, the membership degree was considered as a subinterval of [0, 1], rather than a particular number from [0, 1], as in 
case of FSs. However, the idea of non-membership value was not addressed in either FSs or IVFSs. Atanassov [3] added the concept of non-membership 
value and coined the new term

“intuitionistic fuzzy sets (IFs)”. In FSs, the membership degree of an element was considered within the interval [0, 1], with the nonmembership degree 
was deﬁned as one minus the degree of membership. In contrast, in IFSs both degrees were regarded in diﬀerent ways having the restriction that sum of 
these degrees should not exceed 1.

From past few decades, graph theory become a useful tool to model the real-life problems related to many ﬁelds of sciences. Diﬀerent types of graphs 
and the concepts related to them have been applied to various research areas such as organizing and structuring of diﬀerent patterns, networking, 
decision-making etc. Alternatively, to address real-life issues with uncertainties, the fuzzy logic developed into more useful and signiﬁcant 
approach. Recently, diﬀerent kind of issues with uncertainties have been modeled through fuzzy graphs (FGs). The idea of fuzzy graphs was initiated by 
Rosenfeld [4]. FGs are proven more eﬀective and ﬂexible as compared to the classical graphs. Many applications of FGs in diﬀerent ﬁelds of sciences 
have been investigated because of its ﬂexible nature. Bhattacharya [5] introduced several new terms in the theory of FGs. In [6], many advanced 
operations were introduced. Complement of FGs was initiated in [7]. The concepts of average connectivity in FGs were discussed by Poulik et al. [8]. 
Many researchers have introduced various concepts of classical graphs in the ﬁeld of FGs. Overall, FGs played a key role in numerous ﬁelds such as 
social sciences, modeling road networks etc. Ubaid ur Rehman [9] introduced some aggregation operators under complex fuzzy environment and applied 
towards multi-attribute decision-making. Jana et al. [10] initiated the notion of dombi operators under pythagorean fuzzy information and provided 
applications in multi-attribute decision making. Mahapatra et al. [11] initiated the applications of edge coloring of FGs. The concepts of FDGs (see 
Table 1) was presented by the Mordeson and Nair in [12]. FDGs were further investigated in [13]. The notion of bipolar-FDGs with application in 
decision-making was explored in [14]. The generalized form of FGs called IFGs(see Table 1) was presented in [15]. Similarly, the concepts of complex 
IFGs with application in networking was presented in [16]. Rashmanlou et al. [17] introduced the notion of IFGs with categorical properties. The notion 
of domination in IFGs by strong arcs and eﬀective arcs was discussed by [18]. Akram et al. [19] initiated the concepts of competition graphs under 
complex intuitionistic fuzzy environment. Numerous new concepts related to IFGs like IF-hypergraphs, strong-IFGs, IF-cycles and IF-tree were initiated 
in [20–22]. Ali et al. [23] introduced some complex intuitionistic fuzzy power interaction aggregation operators and applied in decisionmaking 
techniques. Similarly, the concepts of intuitionistic fuzzy directed graph (IFDGs) with application in decision support system was initiated in [24]. 
An interval-valued IFDG matrix approach in analyzing roadblocks was investigated in [25]. Nithyanandham et al. [26] introduced energy based bipolar 
IFDG and provided its applications in decision-making.

The term domination has a signiﬁcant importance in a classical graphs. Many researchers introduced various forms of dominations in graphs like double 
Roman domination [27], paired domination [28], broadcast domination [29], triple Roman domination [30], outer-convex domination [31] etc. Subsequently, 
many terms related to dominations of classical graphs have been shifted to FGs. In this context, by utilizing eﬀective arcs the term domination in FGs 
was studied by Somasundaram et al. [32]. Shanmugam et al. [33] initiated the concept of bridge domination in FGs. The concepts of covering and paired 
domination in IFGs was initiated by Sahoo et al. [34]. Domination in FDGs was discussed in [35]. Recently, in [36] the terms broadcasts and dominating 
broadcasts in FGs were introduced, with applications in transportation model. Parvathi et al. [37] initiated the concepts of dominations in IFGs. In 
the theory of IFGs, the term double domination was introduced by Nagoorgani et al. [38]. The idea of double domination and regular domination in 
intuitionistic fuzzy hypergraph was introduced by Sri et al. [39]. The term inverse domination in IFGs was discussed by Stephan et al. [40]. The 
concept of total perfect and total eﬃcient domination in intuitionistic fuzzy graphs were discussed by Hameed et al. [41]. The term domination in 
intuitionistic fuzzy incidence graph was introduced by Sadati et al. [42]. The concept of strong pair domination number in intuitionistic fuzzy 
inﬂuence graphs with application for the selection of hospital having the optimal medical facilities was initiated by Rehman et al. [43]. Recently, we 
(the authors with Guan, Shaﬁ and A. Khan) initiated the notion of domination in IFDGs which is based on strong arcs [44].

In this study, we provide several new concepts of dominations in IFDGs by utilizing the concepts of diﬀerent types of eﬀective arcs. We provide a 
direct extension of domination in DFGs on one side and ﬁll the existing gap in the literature on the other. We begin our study by introducing the 
concepts of various types of eﬀective arcs including semi- 𝜆 eﬀective arc, semi- 𝜈 eﬀective arcs etc in IFDGs. Then, we initiate the concepts of 
domination and domination number of several types of IFDGs based on these eﬀective arcs. Sequentially,

we initiate the notion of dominating set (DS), MIS (see Table 1) and MDS. By utilizing minimal dominating sets, we discuss numerous signiﬁcant 
characterizations related to domination in IFDG. Furthermore, we investigate the minimal dominating sets (MDSs) and domination numbers (DN) of 
IF-dipaths and dicycles, yielding various fascinating results. Finally, by using the concepts of domination in IFDGs, we provide the solution to the 
problem of opening restaurants in several areas of the city.

Motivations and Novelty.

In IFDGs, the degree of membership and non-membership of the directed edges are considered that is why it has an extensive domain in comparison with 
the FDGs. Furthermore, the terms domination in FGs [32], IFGs [37] and PFGs [45] have been established which motivated us to ﬁll the gap in the 
literature by introducing the concepts of dominations in IFDGs and presents its application towards decision. The summary of the novelty of our work is 
given below.

1. Firstly, we introduced various types of useful eﬀective arcs like semi- 𝜆 eﬀective arc, semi- 𝜈 eﬀective arcs etc in IFDGs. We characterize 
these terms by providing suitable examples.

2. We investigate the notions of dominating set (SCDS), minimal dominating set (MDS) and domination number of some IFDGs.

3. We introduce the concepts of IF-dipath and IF-dicycle in IFDG and also discuss their properties related to dominations.

4. Lastly, we provide its application towards decision-making.

This manuscript has six sections. In section 2, we provide few necessary terminologies regarding FSs, FGs and their extensions. In section 3, we 
initiate several types of eﬀective arcs of IFDGs and discuss dominations in IFDGs based on these terms. In section 4, we give the solution of the 
problem in decision-making which ensures the eﬀectiveness of domination in IFDGs. Section 5 includes the comparative study. Finally, section 6 
comprises of concluding remarks and future perspectives of our work.

2. Preliminaries Deﬁnition 2.1. [1] A pair (𝜆, 𝑍) is known as fuzzy set, where 𝑍 is a nonempty set and 𝜆 ∶ 𝑍 function.

Deﬁnition 2.2. [46] We can describe an intuitionistic fuzzy set (IFS) 𝑆 on set 𝑍 as follows.

⟶ [0,

1] represents the membership

𝑆 = {(𝑠,𝜆 𝑆 (𝑠),𝜈 𝑆 (𝑠) ∶ 𝑠 ∈ 𝑍)}

where 𝜆 𝑆 (𝑠) ∈ [0, 1] is the membership degree of 𝑠 ∈ 𝑆 , 𝜈 𝑆 (𝑠) ∈ [0, 1] represents the non-membership degree of 𝑠 ∈ 𝑆 satisfying

0 ≤ 𝜆 𝑆 (𝑠) + 𝜈 𝑆 (𝑠) ≤ 1, for all 𝑠 ∈ 𝑍 .

Deﬁnition 2.3. [4] A pair

𝐺 ̆ = (𝑋,

𝑌 ) is a fuzzy graph (FG), where 𝑋 = { 𝜓 𝑋 } and 𝑌 = { 𝜓 𝑌 } with

𝜓𝑋 

∶ 𝑈 → [0, 1] and

𝜓𝑌 

∶ 𝑈 × 𝑈 →

[0, 1], with 𝜓 𝑌 (𝑤, 𝑥) ≤ 𝜓 𝑋 (𝑤) ∧ 𝜓 𝑋 (𝑥).

Deﬁnition 2.4. [15] A pair 𝐺 ∗ = (𝑆, 𝑇 ), where 𝑆 = {𝜆 𝑆 , 𝜈 𝑆 }, 𝑇 = {𝜆 𝑇 , 𝜈 𝑇 }, is an IFG on 𝑈 , where (𝑖) 𝜆 𝑆 ∶ 𝑈 → [0, 1], 
and 𝜈 𝑆 ∶ 𝑈 → [0, 1] are the degree of membership and non-membership of all element 𝑤 ∈ 𝑈 , respectively, such that 0 ≤ 𝜆 𝑆 (𝑤) + 𝜈 𝑆 
(𝑤) ≤ 1, for all 𝑤 ∈ 𝑈 , and

(𝑖𝑖) 𝜆 𝑇 ∶ 𝑊 ⊆ 𝑈 ×𝑈 → [0, 1] and 𝜈 𝑇 ∶ 𝑊 ⊆ 𝑈 ×𝑈 → [0, 1] satisfying 𝜆 𝑇 (𝑤, 𝑥) ≤ 𝑚𝑖𝑛{𝜆 𝑆 (𝑤), 𝜆 𝑆 (𝑥)} and 𝜈 𝑇 (𝑤, 
𝑥) ≥ 𝑚𝑎𝑥{𝜈 𝑆 (𝑤), 𝜈 𝑆 (𝑥)}

with 0 ≤ 𝜆 𝑇 (𝑤, 𝑥) + 𝜈 𝑇 (𝑤, 𝑥) arc set of 𝐺 ∗ .

≤

1, for all (𝑤, 𝑥) ∈ 𝑈 × 𝑈 . Here, 𝑆 is the intuitionistic fuzzy node set, and 𝑇 is the intuitionistic fuzzy

Deﬁnition 2.5. [32] Let

𝐺 ̆ = (𝑋,

𝑌 ), where 𝑋 = { 𝜓 𝑋 } and 𝑌 = { 𝜓 𝑌 } is a FG of a crisp graph 𝐺 . For 𝑤, 𝑥 ∈ 𝑋 , we say 𝑤 dominates

𝑥 in 𝐺 ̆ , if 𝜓 ( 𝑤𝑥) = 𝜓 𝑋 (𝑤) ∧ 𝜓 𝑋 (𝑥).

Deﬁnition 2.6. [32] A subset 𝑋 1 of 𝑋 is the DS in 𝐺 ̆ is a MDS, if 𝑋 1 doesn’t contain any proper DS of

𝐺 ̆ , 𝐺 ̆ .

if for each 𝑤 ∈ 𝑋 1 there is 𝑥 ∈ 𝑈 − 𝑋 1 with 𝑤 dominates 𝑥 . A DS 𝑋 1 of a FG The DN(from Table 1) of 𝐺 ̆ is the minimum (fuzzy) 
cardinality of a DS in 𝐺 ̆ .

𝐺 ̂𝐷 

Deﬁnition 2.7. [35] Let = (𝑈, 𝐵) be a simple directed graph, where 𝑈 is a nonempty ﬁnite set and 𝐵 = {(𝑤, 𝑥) ∶ 𝑤, 𝑥 ∈ 𝑈, 𝑤 ≠ 𝑥} . A 
pair 𝐺 ̃ 𝐷 = ( 𝜓 𝑋 , 𝜓 𝑌 ) is fuzzy digraph (FDG), where 𝜓 𝑋 ∶ 𝑈 ⟶ [0, 1] and 𝜓 𝑌 ∶ 𝐵 ⟶ [0, 1] with 𝜓 𝑌 ((𝑤, 𝑥)) ≤ 𝜓 𝑋 (𝑤) ∧ 𝜓 
𝑋 (𝑥), for

all 𝑤, 𝑥 ∈ 𝑈 .

Deﬁnition 2.8. [35] Let 𝐺 ̂ 𝐷 = (𝑈, 𝐵) be an hidden digraph, where 𝑈 is the set of vertices and 𝐵 represents the set of directed edges. Then 𝐺 ̃ 
𝐷 = ( 𝜓 𝑈 , 𝜓 𝐵 ) is the fuzzy directed graph of 𝐺 ̂ 𝐷 , where 𝜓 𝑈 = { 𝜓 𝑈 (𝑤) ∶ 𝑤 ∈ 𝑈} is the set of vertices (nodes), and 𝜓 𝐵 = { 𝜓 
𝐵 ((𝑤, 𝑥)) ∶ 𝑤, 𝑥 ∈ 𝑈} represents the fuzzy directed edges from 𝜓 𝑈 (𝑤) to 𝜓 𝑈 (𝑥) in a fuzzy digraph 𝐺 ̃ 𝐷 .

Deﬁnition 2.9. [35] Let 𝐺 ̂ 𝐷 = (𝑈, 𝐵) be an hidden digraph of a FDG arc of 𝐺 ̃ 𝐷 , if 𝜓 𝐵 (𝑤, 𝑥) ≤ 𝜓 𝑈 (𝑤) ∧ 𝜓 𝑈 (𝑥), for all 𝑤, 𝑥 
∈ 𝑈 .

Deﬁnition 2.10. [24] A pair = (𝐴, 𝐵) is an intuitionistic fuzzy digraph (IFDG) of a digraph is an IFS on 𝑉 and 𝐵 = (𝜆 𝐵 , 𝜈 𝐵 ) represents an 
intuitionistic fuzzy relation on 𝑉 such that 𝜆 𝐵 ( 𝑦 𝑧)

𝑚𝑎𝑥{𝜈 𝐴 ( 𝑦 ), 𝜈 𝐴 (𝑧)}, and 0 ≤ 𝜆 𝐵 ( 𝑦 𝑧) + 𝜈 𝐵 ( 𝑦 𝑧) ≤ 1, for all 𝑦 , 𝑧 ∈ 𝑉 .

3. Domination in IFDGs through eﬀective arcs

= (𝑉 , 𝐸), where 𝐴 = (𝜆 𝐴 , 𝜈 𝐴 ) ≤ 𝑚𝑖𝑛{𝜆 𝐴 ( 𝑦 ), 𝜆 𝐴 (𝑧)}; 𝜈 𝐵 ( 𝑦 𝑧) ≥

Firstly, we introduce some types of eﬀective edges in IFDG such as semi- 𝜆 eﬀective arcs, semi- 𝜈 eﬀective arcs etc. Afterwards, we initiate the 
notion of domination in IFDG by utilizing these arcs. In this context, we discuss several useful characteristics of IFDG related to dominations. We 
also provide some fascinating results related to DS and MDS of IFDGs. Lastly, we present the terms IFdipath and IF-dicycle of IFDG and explore their 
MDSs, DNs etc. We also present some interesting results related to IF-dipath and IF-dicycle of IFDG.

Throughout our discussions, 𝐺 ̇ 𝐷 = (𝐴, 𝐵) will represent an IFDG of an hidden diagraph 𝐺 ̂ 𝐷 = (𝑉 , 𝐸), where 𝐴 = (𝜆 𝐴 , 𝜈 𝐴 ) and 𝐵 = (𝜆 
𝐵 , 𝜈 𝐵 ). We begin our discussion with the deﬁnition of an eﬀective arc in an IFDG as follows.

𝐺 ̇𝐷 

Deﬁnition 3.1. An arc ( 𝑦 , 𝑧) in an IFDG is an eﬀective arc, if 𝜆 𝐵 ( 𝑦 , 𝑧) = 𝑚𝑖𝑛{𝜆 𝐴 ( 𝑦 ), 𝜆 𝐴 (𝑧)} and 𝜈 𝐵 ( 𝑦 , 𝑧) = 
𝑚𝑎𝑥{𝜈 𝐴 ( 𝑦 ), 𝜈 𝐴 (𝑧)} such that 0 ≤ 𝜆 𝐵 ( 𝑦 , 𝑧) + 𝜈 𝐵 ( 𝑦 , 𝑧) ≤ 1, for all ( 𝑦 , 𝑧) ∈ 𝐵 .

Now we present the deﬁnitions of the corresponding eﬀective arcs that are semi 𝜆 -eﬀective arc and semi 𝜈 -eﬀective arc in an IFDG.

Deﬁnition 3.2. An arc ( 𝑦 , 𝑧) is known as semi 𝜆 -eﬀective arc of the IFDG 𝑚𝑎𝑥{𝜈 𝐴 ( 𝑦 ), 𝜈 𝐴 (𝑧)} with 0 ≤ 𝜆 𝐵 ( 𝑦 , 𝑧) + 𝜈 𝐵 ( 
𝑦 , 𝑧) ≤ 1, for all ( 𝑦 , 𝑧) ∈ 𝐵 .

𝐺 ̇𝐷 

, if 𝜆 𝐵 ( 𝑦 , 𝑧) = 𝑚𝑖𝑛{𝜆 𝐴 ( 𝑦 ), 𝜆 𝐴 (𝑧)} and 𝜈 𝐵 ( 𝑦 , 𝑧)

≠

𝐺 ̇𝐷 

Deﬁnition 3.3. An arc ( 𝑦 , 𝑧) is known as semi 𝜈 -eﬀective arc of IFDG 𝜆 𝐴 (𝑧)} and 𝜈 𝐵 ( 𝑦 , 𝑧) = 𝑚𝑎𝑥{𝜈 𝐴 ( 𝑦 ), 𝜈 𝐴 (𝑧)} such 
that 0 ≤ 𝜆 𝐵 ( 𝑦 , 𝑧) + 𝜈 𝐵 ( 𝑦 , 𝑧)

, if 𝜆 𝐵 ( 𝑦 , 𝑧) ≠ 𝑚𝑖𝑛{𝜆 𝐴 ( 𝑦 ), ≤ 1 for all ( 𝑦 , 𝑧) ∈ 𝐵 .

In Example 3.4, we identify the eﬀective arcs in an IFDG given in Fig. 1.

Example 3.4. Refer to IFDG shown in Fig. 1, we have the followings.

(𝑖) Consider the arc (𝑢, 𝑣) , here 𝜆 𝐵 (𝑢, 𝑣) = 𝑚𝑖𝑛{𝜆 𝐴 (𝑢), 𝜆 𝐴 (𝑣)} = 𝑚𝑖𝑛{0.4, 0.3} = 0.3 ≠ 0.2 and 𝜈 𝐵 (𝑢, 𝑣) = 𝑚𝑎𝑥{𝜈 𝐴 
(𝑢), 𝜈 𝐴 (𝑣)} = 𝑚𝑎𝑥{0.5, 0.4} = 0.5. Therefore an arc (𝑢, 𝑣) is non-eﬀective arc but arc (𝑢, 𝑣) is semi 𝜈 -eﬀective arc.

(𝑖𝑖) Let the arc (𝑣, 𝑤) , here 𝜆 𝐵 (𝑣, 𝑤) = 𝑚𝑖𝑛{𝜆 𝐴 (𝑣), 𝜆 𝐴 (𝑤)} = 𝑚𝑖𝑛{0.3, 0.5} = 0.3 and 𝜈 𝐵 (𝑣, 𝑤) = 𝑚𝑎𝑥{𝜈 𝐴 (𝑣), 𝜈 
𝐴 (𝑤)} = 𝑚𝑎𝑥{0.4, 0.4} =

0.4 ≠ 0.3. Thus the arc (𝑣, 𝑤) is non-eﬀective arc but arc (𝑣, 𝑤) is semi 𝜆 -eﬀective arc.

(𝑖𝑖𝑖) Let the arc (𝑤, 𝑢) , here 𝜆 𝐵 (𝑤, 𝑢) = 𝑚𝑖𝑛{𝜆 𝐴 (𝑤), 𝜆 𝐴 (𝑢)} = 𝑚𝑖𝑛{0.5, 0.4} = 0.4 and 𝜈 𝐵 (𝑤, 𝑢) = 𝑚𝑎𝑥{𝜈 𝐴 (𝑤), 
𝜈 𝐴 (𝑢)} = 𝑚𝑎𝑥{0.4, 0.5} =

0.5. Hence arc (𝑤, 𝑢) is an eﬀective arc.

In Deﬁnition 3.5, we present the notions of eﬀective neighborhood (ENbhd) and closed neighborhood (CNbhd) including their diﬀerent types with 
cardinalities.

Deﬁnition 3.5. Let

𝐺 ̇𝐷 

𝐺 ̂𝐷 

= (𝐴, 𝐵) be an IFDG deﬁned on an hidden digraph = (𝑉 , 𝐸). Then (𝑖) 𝑁 𝐸 ( 𝑦 ) = {𝑧 ∈ 𝑉 ∶ 𝑎𝑟𝑐( 𝑦 , 𝑧) is an eﬀective arc} is an ENbhd 
of 𝑦 ∈ 𝑉 while 𝑁 𝐸 [ 𝑦 ] = 𝑁 𝐸 ( 𝑦 ) ∪ { 𝑦 } is its CNbhd.

(𝑖𝑖) 𝑁 𝜆𝐸 ( 𝑦 ) = {𝑧 ∈ 𝑉 : 𝑎𝑟𝑐( 𝑦 , 𝑧) is a semi 𝜆 - eﬀective arc} is a semi 𝜆 - eﬀective neighborhood of 𝑦 ∈ 𝑉 and 𝑁 𝜆𝐸 [ 𝑦 ] 
= 𝑁 𝜆𝐸 ( 𝑦 ) ∪ { 𝑦 } is the closed neighborhood of 𝑦 .

(𝑖𝑖𝑖) 𝑁 𝜈𝐸 ( 𝑦 ) = {𝑧 ∈ 𝑉 ∶ 𝑎𝑟𝑐( 𝑦 , 𝑧) is semi 𝜈 - eﬀective arc} is a semi 𝜈 - eﬀective neighborhood of 𝑦 ∈ 𝑉 and closed 
neighborhood of 𝑦

is 𝑁 𝜈𝐸 [ 𝑦 ] = 𝑁 𝜈𝐸 ( 𝑦 ) ∪ { 𝑦 }.

(𝑖𝑣) 𝛿 𝐸 ( 𝐺 ̇𝐷  (𝑣) Δ 𝐸 ( 𝐺 ̇𝐷 

) = min{𝑁 𝐸 ( 𝑦 ) ∶ 𝑦 ∈ 𝑉 ( 𝐺 ̇ 𝐷 )} is the minimum cardinality of eﬀective neighborhood. ) = max {𝑁 𝐸 ( 𝑦 ) ∶ 𝑦 ∈ 𝑉 ( 𝐺 ̇ 𝐷 )} is the 
maximum cardinality of eﬀective neighborhood.

Deﬁnition 3.6. Let 𝑦 , 𝑧 be any two vertices of an IFDG . If a directed edge ( 𝑦 , 𝑧) is an eﬀective edge, then 𝑦 dominates 𝑧 . Example 3.7. 
The directed edge (𝑤, 𝑢) is an eﬀective edge of an IFDG shown in Fig. 1 while the edges (𝑢, 𝑣) and (𝑣, 𝑤) are not the eﬀective arcs. Thus the 
vertex 𝑤 dominates 𝑢 as there is an eﬀective edge between these two vertices. However, a vertex 𝑢 does not dominate 𝑣 , and a vertex 𝑣 does not 
dominate 𝑤 as there are no eﬀective edges between them.

Deﬁnition 3.8. Let 𝐺 ̇ 𝐷 = (𝐴, 𝐵) be an IFDG deﬁned on an hidden digraph 𝐺 ̂ 𝐷 = (𝑉 , 𝐸). A 𝐶 ⊂ 𝑉 is said to be a DS in an IFDG, if for each 
𝑧 ∈ 𝑉 − 𝐶 ∃ 𝑦 ∈ 𝐶 such that 𝑦 dominates 𝑧 .

Deﬁnition 3.9. If a dominating set 𝐶 doesn’t contain any other DS in an IFDG, then we call it a MDS. The minimum fuzzy cardinality among all DSs of 
an IFDG is said to be the eﬀective arc domination number (DN), represented by 𝜔 𝐸 ( 𝐺 ̇ 𝐷 ), and the corresponding DS is known as te minimum 
eﬀective edge DS. The total members in the minimum eﬀective edge DS is given by 𝑛[𝜔 𝐸 ( 𝐺 ̇ 𝐷 )].

Example 3.10. One can easily deduce that {(0.8, 0.1), (0.7, 0.2)}, {(0.5, 0.4), (0.7, 0.2)} and {(0.5,0.4), (0.8, 0.1), (0.8, 0.1)} are the MDSs of an 
IFDG 𝐺 ̇ 𝐷 shown in Fig. 2.

Remark 3.11. Let 𝐺 ̇ 𝐷 = (𝐴, 𝐵) be an IFDG. If 𝜆 𝐵 ( 𝑦 𝑧) < 𝑚𝑖𝑛(𝜆 𝐴 ( 𝑦 ), 𝜆 𝐴 (𝑧)), and 𝜈 𝐵 ( 𝑦 𝑧) > 𝑚𝑎𝑥(𝜈 𝐴 ( 𝑦 ), 𝜈 𝐴 
(𝑧)), then (𝜆 𝐴 , 𝜈 𝐴 ) is the only DS of 𝐺 ̇ 𝐷 . Example 3.12. By doing simple calculations, one can easily verify that {(0.3, 0.4), (0.4, 0.3), 
(0.5, 0.2), (0.6, 0.3)} is the only DS of an IFDG 𝐺 ̇ 𝐷 shown in Fig. 3.

Deﬁnition 3.13. Let 𝐺 ̇ 𝐷 be an IFDG and 𝑦 , 𝑧 be two vertices of 𝐺 ̇ 𝐷 . Then (𝑖) If the arc ( 𝑦 , 𝑧) is a semi 𝜆 - eﬀective arc, then we 
say that 𝑦 (semi 𝜆 - eﬀective) dominates 𝑧 .

(𝑖𝑖) If an arc ( 𝑦 , 𝑧) is a semi 𝜈 - eﬀective arc, then 𝑦 (semi 𝜈 - eﬀective) dominates 𝑧 .

Example 3.14. From Fig. 1, it can be easily seen that the arc (𝑢, 𝑣) is semi- 𝜈 eﬀective arc, hence 𝑢 (semi 𝜈 - eﬀective) dominate 𝑣 . 
Similarly, the arc (𝑣, 𝑤) is semi- 𝜆 eﬀective arc, hence 𝑣 (semi 𝜆 - eﬀective) dominate 𝑤 .


