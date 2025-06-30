Chapter 1
Introduction

Abstract This chapter gives a short historical introduction to bioinformatics and
computational biology and compares both disciplines.

1.1 A Very Short History of Bioinformatics and Computational Biology

Sequencing of the first proteins by Frederick Sanger in 1953 (1958 Nobel Prize in
Chemistry for his work on the structure of proteins, especially that of insulin) and
the first protein crystal structure analysis by Max Perutz and John Kendrew (1962
Nobel Prize in Chemistry for determining the first atomic structures of proteins
using X-ray crystallography) in 1960 were among the first important datasets
that gave rise to computational biology and bioinformatics. John Kendrew took
advantage of the first European computer named ESDAC (electronic delay stor-
age automatic calculator, set up in 1949 in Cambridge/UK) to calculate the
structure of myoglobin from X-ray diffraction data. Thus, John Kendrew can be
considered as one of the founders of chemoinformatics. At the same time, John
William Mauchly and John Presper Eckert developed the first commercially avail-
able computer UNIVAC I (universal automatic computer) in 1951 (Fig. 1.1), and,
in 1956, IBM employee John Backus developed with Fortran the first compiler
programming language.

https://www.whatisbiotechnology.org/index.php/exhibitions/sanger/insulin


Fortran was the programming language used by Margaret Oakley Dayhoff from
the United States (Fig. 1.2). She was a pioneer in bioinformatics. One of her first
projects was to create a Fortran program to determine the full protein sequence
from sequence fragments in the early 1960s (Dayhoff, 1965). The same task,

Fig. 1.1: UNIVAC I. The first commercially available computer was composed of 5.200 elec-
tron, weighed 13 tons, and consumed 125 kW. At a frequency of 2.25 MHz, it could execute
1.905 calculations per second. The entire computer occupied 36 m2. The program was input
by punched cards

but to an incomparably greater extent and with DNA sequences, was solved
by the team led by Craig Venter when they established whole-genome shotgun
sequencing. With this method, complete genomes are assembled from "shredded"
genomic DNA. It was used when sequencing the first genome of a free-living
bacterium in 1995 (Fleischmann et al., 1995) and in the sequencing of the human
genome in 2001 by Celera Genomics (Venter et al., 2001).

In the 1970s, Margaret Dayhoff examined the frequency of amino acid exchanges
on the basis of a few hundred related protein sequences using statistical methods.
From this data she developed the so-called substitution matrices, which are of
great practical importance in sequence analysis and sequence queries in databases
to this day. In this context, the first algorithms to reconstruct the evolution of
protein sequences of organisms were developed (Fitch and Margoliash, 1967).
Prerequisite was access to powerful computers, such as the IBM 7090 that was
also used in the Mercury and Gemini space program. In 1977, Alan Maxam and
Walter Gilbert and, independently, Frederick Sanger published methods, which
laid the foundation for automated DNA sequencing.

Two years later, the company Oracle introduced the first commercial database
software, and, in 1979, Walter Goad developed the prototype of GenBank, the
first public nucleic acid and protein sequence database. To find sequences in this
database that are similar to a query sequence, a sequence alignment algorithm
originally developed by Needleman and Wunsch (1970) and modified by Smith
and Waterman (1981) was employed. This development led to BLAST (basic

Fig. 1.2: Margaret Dayhoff (1925-1983). A pioneering bioinformatician. Photo: Ruth E. Dayhoff, M.D.; US National Library of Medicine

local alignment software tool), a software known by every molecular biologist
today (Altschul et al., 1990, 1997).

Molecular Design Ltd. (chemical databases, founded in 1978), Health Design
Inc. (toxicological predictions, founded in 1978), Tripos Associates Inc. (molecular modeling and drug design, founded in 1979), and IntelliGenetics (DNA and
protein sequence analysis, founded in 1980) were pioneers in market-based use
of computers in the field of chemistry and biochemistry. Astonishingly, the basis
for what today is celebrated as bioinformatics revolution has been laid out about
30 years ago.

In the early days of bioinformatics, access to a computer for bioscientists was
anything but a matter of course. In the early 1960s, computers were the size
of closets, cost at least $ 50.000, could only edit one program at a time and
could only be used by one single user at a time. Initially, only universities and
other large research facilities could afford a computer that had to be maintained
and operated by qualified personnel. Users supplied their programs in the form of
punched cards and received their results a few days later. In 1969, Ken Thompson
and Ritchie Dennies from the US company AT&T started to develop a multiuser
operating system, allowing program execution by multiple users in parallel: Unix.
They published their idea in 1974 (Ritchie and Thompson, 1974) and thus set
in motion the distribution of Unix. Today, access to computers is available to all
students. In addition, the development of the World Wide Web allows to exchange
large amounts of data easily and biological databases can be accessed through
user-friendly interfaces (front ends). Therefore, we saw a boom in computational
biology.

1.2 Contemporary Biology

For many scientists, the computer has become more important than the actual
experiment. This is true for both bench and field scientists. The development of
automated, computer-controlled instrumentation has led to the generation of lots
of tools which aid data retrieval, analysis, and visualization. Automation of data
collection affects all disciplines; it does not make any difference if the data source
is a photoelectric barrier at the entry of a beehive, a meteorological station, an
animal trap, or a DNA sequencing machine. Usually, data analysis is supported
by software programmed by specialist scientists. The focus of such software is to
solve problems, but not user-friendliness. Like MUSCLE, a powerful software for
sequence alignments (Edgar, 2004), these tools often use the command line of
the operating system, i.e., either the DOS window in Microsoft Windows or the
Unix-like terminal (console, shell) in Apple’s macOS and Linux.

Currently, data processing with office software packages like Microsoft Excel is
common in sciences like biology. But there are limitations. Zeeberg et al. (2004)
showed that Excel could irreversibly change gene names to non-gene names: This
even affected one of the most important resources for molecular biology informa-
tion, GenBank. Due to default date format conversions and floating-point format
conversions in Excel, the gene name SEPT1 (encoding a protein of the septin
family) becomes 1-Sep and the gene identifier 2310009E13 gets converted to the
floating-point number 2.31E+13, respectively. These changes are irreversible; the
original gene names or identifiers cannot be recovered. Furthermore, the organization and format of data frequently needs to be adapted to certain analysis
software requirements, e.g., columns need to become rows or colons should be
commas. These few examples illustrate that, with commercial software, one is
usually bound to standard functionality. If scientists want to escape from these
limits, they should learn something about data processing, which in turn requires
knowledge about command line tools. In this book I introduce you to some of
the possibilities from an experimental biologist’s perspective.

1.3 Computational Biology or Bioinformatics?

The title of this book is Computational Biology; however, the title of many
similar books is Bioinformatics. This immediately raises the question: What is the
difference? Does bioinformatics sell better? Is bioinformatics what most people
do?

I spent quite a while to find out what is buried behind both terms. For the second
edition I even worked out a comparison of the frequency of both terms in Amazon
Books, Google Scholar, Google Books, and PubMed searches. The result was the
impression that there is no clear distinction. Today, in April 2024, Google found
215,000,000 hits for bioinformatics and 39,900,000 hits for computational biology.
Google Trends teaches me that the term bioinformatics has been queried seven
to eight times more frequently than computational biology over the past 10 years.
However, in a recent review, Christos Ouzounis shows that Google Trends hits
for the query term bioinformatics has diminished by almost sixfold over the past
7 years (Ouzounis, 2012). He extrapolates that the term will be irrelevant in 651
weeks, i.e., in 2024—well, now. Apart from this humorous conclusion, the review
uses both terms interchangeably.

Nowadays, I can ask ChatGPT, which I did. The answer was that bioinformatics
and computational biology are closely related fields, but they have distinct focuses
and methodologies:

* Bioinformatics primarily deals with the development and application of computational techniques for the analysis and interpretation of biological data.
This includes the management, storage, retrieval, and analysis of large-scale
biological datasets, such as DNA sequences, protein structures, and gene expression profiles. Bioinformatics approaches often involve the development of
algorithms, databases, and software tools to extract meaningful insights from
biological data. It encompasses a wide range of topics, including sequence
alignment, genome assembly, phylogenetics, and functional genomics.

* Computational biology, on the other hand, is a broader field that encompasses the use of computational methods to study biological systems and
processes. It integrates concepts and techniques from mathematics, statistics,
computer science, and biology to model and simulate biological phenomena.
Computational biologists develop mathematical models and computational
simulations to understand complex biological systems, predict their behavior,
and test hypotheses. This field covers diverse areas, such as systems biology,
structural biology, evolutionary biology, and mathematical modeling of biological processes.

In summary, bioinformatics focuses on the development and application of computational tools and techniques for biological data analysis, while computational
biology involves the use of computational methods to study biological systems
and processes at various levels of complexity.

During my professional career in industries, I was head of projects which aimed
at different things like gene discovery, data integration, and visualization and
statistical analyzes. I was employed as a bioinformatics manager. But was it
bioinformatics what I was doing? Or was it computational biology? Or something
else? There are many opinions on what bioinformatics or computational biology
are. To me, computational biology is the complement to experimental
biology. The aim of both disciplines is to learn more about biology, i.e., an
ecosystem, a synthetic cell, the stoichiometrics of a genome, and the regulation
of a gene. Bioinformatics on the other hand provides algorithms and tools for
the treatment of biological data. Here, the focus lays more at the side of the
algorithm or the statistical method applied. Anyway, both terms are frequently
used in synonym and the buzz word clearly is bioinformatics—I am glad that you
still found this book ;-)

1.4 Computers in Biology

The first use of a computer for sequence analysis was in the 1960s by Margaret Dayhoff (Dayhoff, 1965; Dayhoff and Ledley, 1962). Since then, the field
of computational biology has developed immensely, as has the power of computers. Recent years have seen an exponential growth in biological data, which is
usually no longer published in a conventional sense, but deposited in databases.
Every year, the journal Nucleic Acid Research devotes an issue to present new
databases. All these data need to be processed, analyzed, and incorporated into
one’s own research focus. The buzz word is bioinformatics, used by almost everybody who once "blasted" (i.e. queried) a sequence against GenBank or calculated
a distance tree. Still, we have to discriminate between bioinformatics as a tool
and bioinformatics as a research field. What most biologists—and I—mean by
bioinformatics is that they perform computational biology, in contrary to experimental biology. Whatever you call it, biologists have to treat increasingly large
amounts of data and often depend on command-line based software tools in order
to perform front-line research.

Let me give you one vivid example: No, a GUI has not been implemented yet. Are
you a biologist? Replies like this are not uncommon when bioinformatics software
developers are asked whether there is a graphical user interface (GUI) for their
software. I encountered this answer at the ISMB 2004 conference (Intelligent
Systems for Molecular Biology) in Glasgow. Robert Edgar demonstrated his new
sequence alignment software MUSCLE (Edgar, 2004), which was awarded the
best paper price. As in many other cases, this software was originally developed
for Linux and had no nice graphical user interface—it only run in the command
line. Today, ports to Windows and macOS exist, and a web interface has been
set up. Yet, the Linux, Windows, and macOS versions still have no GUI, and the
web interface is functionally limited; most program options are only available via
the command line. Why do programmers commonly omit the GUI? One reason
is that the bioinformaticians are interested in solving an algorithmic problem.
In order to convince everybody that he or she can do better than others, the
programmer has to implement his or her algorithm, i.e., write a program. He or
she definitely does not want to spend a lot of time on implementing a GUI. This
is commonly done by others. And then it depends on the competence, focus, and
will of the GUI programmer if he or she makes all the features of the background
command line program accessible via the graphical interface. Now, without the
skills to work in the command line, you might quickly be put off the peak of
research tools.

Automation of high-throughput data retrieval from increasingly sophisticated devices puts masses of raw data on hard disks. As mentioned above, commercial
applications often show practical limitations in processing these data. In order
not to be trapped by the given functionality of a software application, modern
biologists have to learn new skills. The setup of data processing channels is often
determined by the file formats that the installed software can handle. These are
often proprietary formats that bind the user to that particular software. Working
in the fields functional genomics and synthetic biology, I frequently observe the
need for file format conversions. The task is often easy, like changing decimal
delimiters, permuting columns, or fusing columns from different files, but the
number of processed files is huge. There is a clear advantage for those scientists
who are capable of automating such transformations. It all boils down to this:
Modern biologists require high-throughput data processing and analysis
skills and this book shall assist you to gain them.

1.5 Digital Lab Benches and Designing Organisms

Ironically, while language extensions like BioPython and BioPerl are good tools
for experienced programmers who need to make software for biologists, they are
usually too complicated to be useful to biologists themselves. Consequently, there
was a trend to develop programming languages designed for bio data analysis.
However, they have not become established: Neither BioBike, a programmable
knowledge environment for biologists (Elhai et al., 2009; Massar et al., 2005), nor
the Darwin Workbench (Gonnet et al., 2000) or Microsoft’s VisualGEC, specifically designed for the envisioned workflow in synthetic biology (Pedersen and
Phillips, 2009), initiated a new trend.

Instead, common data science platforms such as Python, R, or Julia are easier
accessible thanks to more intuitive interfaces and support from AI. Julia1 is
a relatively new programming language that combines high performance with
ease of use, making it well suited for scientific computing tasks in biology. It
is increasingly being adopted for tasks such as genomic analysis, mathematical
modeling, and machine learning.

1.6 The Future: AI-Aided Science

In the past decade, computational biology has seen significant advancements
that have revolutionized the field. Besides high-throughput, single-molecule, and
single-cell sequencing technologies, machine learning and artificial intelligence
algorithms for analyzing complex biological data made a jump forward (Danaeifar
and Najafi, 2024; Paggi et al., 2024; Roy et al., 2024). These algorithms can
identify patterns and relationships in large datasets that would be impossible for
humans to discern, leading to new insights into biological processes and disease
mechanisms. For example, machine learning algorithms have been used to predict
protein structures, identify genetic variants associated with disease, and classify
cancer subtypes based on gene expression profiles.

Furthermore, advances in computational modeling and simulation have allowed
researchers to simulate complex biological systems and predict their behavior under different conditions. This has led to the development of virtual drug screening
platforms, personalized medicine approaches, and predictive models for understanding the dynamics of biological networks (Salas-Nuñez et al., 2024). These
computational models have the potential to revolutionize drug discovery and
development, as well as personalized medicine, by enabling researchers to test
hypotheses and make predictions before conducting costly and time-consuming
experiments.

Overall, since the publication of the second edition of this book, computational
biology has seen tremendous advancements, and I am sure that we will see even
more groundbreaking discoveries and innovations in the years to come—maybe
with your help.

1.7 Get Involved

The advances and discoveries described above place new demands on the edu-
cation of biologists. Ten years ago, it was inconceivable to me that I would ever

use CRISPR/Cas and nanopore-based DNA sequencing with high school teachers
and students. Of course, it is not part of the general high school curriculum (yet)
but part of extra activities for those interested (see my project website2). But I
think it is important to show high school students that there is an exciting bridge
between computer science and biology.
About 40 years ago, a number of molecular biological methods such as PCR

(polymerase chain reaction) were included in university curricula, and depart-
ments dealing with molecular biological aspects in different biological disciplines

were erected. Around 20 years ago, the same happened for bioinformatics and
today we see a similar development in the emerging field of bio data sciences
and genomics. Often these departments are anchored outside of biology, e.g., in
mathematics, computer science, or physics. Consequently, computational biology
is taught to the specialist instead of all students. Like scientific data presentation
or writing skills, knowledge of computational biology is assumed to be common
knowledge. It remains to the initiative or the fortune of the student to acquire
this knowledge as part of his training. But what skills have to be learned? What

is needed by a biologist in order to process and analyze large sets of experimen-
tal data? In my opinion the basic skills are how to make best use of the Linux

operating system and how to write little programs for data processing, analysis,
and visualization.
This book covers all these topics and shall provide you with a solid introduction
to get involved.


