2023, VOL. 43, NO. 11, 547–565
[https://doi.org/10.1080/10985549.2023.2256640](https://doi.org/10.1080/10985549.2023.2256640)

RESEARCH ARTICLE

## A SNAI2/CTCF Interaction is Required for NOTCH1 Expression in Rhabdomyosarcoma

Prethish Sreenivas,[a] Long Wang,[a] Meng Wang,[b] Anil Challa,[a][,][c] Paulomi Modi,[a] Nicole Rae Hensch,[a] Berkley Gryder,[d]

Hsien-Chao Chou,[e] Xiang R. Zhao,[a] Benjamin Sunkel,[b] Rodrigo Moreno-Campos,[a] Javed Khan,[f] Benjamin Z. Stanton,[b]

Myron S. Ignatius[a]

aGreehey Children’s Cancer Research Institute, Department of Molecular Medicine, University of Texas Health Sciences Center, San Antonio, Texas, USA

bCenter for Childhood Cancer and Blood Diseases, Abigail Wexner Research Institute at Nationwide Children’s Hospital, The Ohio State University, Columbus, Ohio, USA

cDepartment of Biology, University of Alabama at Birmingham, Birmingham, USA

dDepartment of Genetics and Genome Sciences, Case Western Reserve University, Cleveland, Ohio, USA

eGenetics Branch, NIH, Bethesda, Maryland, USA

fPediatric Oncology Branch, NCI, NIH, Bethesda, Maryland, USA

ABSTRACT Rhabdomyosarcoma (RMS) is a pediatric malignancy of the muscle with
characteristics of cells blocked in differentiation. NOTCH1 is an oncogene that promotes
self-renewal and blocks differentiation in the fusion negative-RMS sub-type. However,
how NOTCH1 expression is transcriptionally maintained in tumors is unknown. Analyses
of SNAI2 and CTCF chromatin binding and HiC analyses revealed a conserved SNAI2/
CTCF overlapping peak downstream of the NOTCH1 locus marking a sub-topologically
associating domain (TAD) boundary. Deletion of the SNAI2-CTCF peak showed that it is
essential for NOTCH1 expression and viability of FN-RMS cells. Reintroducing constitutively activated NOTCH1-DE in cells with the SNAI2-CTCF peak deleted restored cellviability. Ablation of SNAI2 using CRISPR/Cas9 reagents resulted in the loss of majority of
RD and SMS-CTR FN-RMS cells. However, the few surviving clones that repopulate
cultures have recovered NOTCH1. Cells that re-establish NOTCH1 expression after SNAI2
ablation are unable to differentiate robustly as SNAI2 shRNA knockdown cells; yet, SNAI2ablated cells continued to be exquisitely sensitive to ionizing radiation. Thus, we have
uncovered a novel mechanism by which SNAI2 and CTCF maintenance of a sub-TAD
boundary promotes rather than represses NOTCH1 expression. Further, we demonstrate
that SNAI2 suppression of apoptosis post-radiation is independent of SNAI2/NOTCH1
effects on self-renewal and differentiation.

KEYWORDS Rhabdomyosarcoma, SNAI2, CTCF, NOTCH1, Notch, Chromatin, HiC, ChIP- # 2023 The Author(s). Published with

license by Taylor & Francis Group, LLC. This is

seq, CRISPR/Cas9, gene regulation


INTRODUCTION

habdomyosarcoma (RMS) is a pediatric malignancy of the muscle with features of
myogenic cells blocked in differentiation. Over the last two decades, molecular

# R

characterization studies, drug screens, and exome/whole genome sequencing studies
have identified many of the major oncogenic driver and tumor suppressor genes that
are overexpressed, amplified, mutated, and/or lost in RMS tumors.[1][–][3] These studies
confirm that the fusion positive (FP)-RMS sub-type is driven by either PAX3/PAX7 fused
to FOXO1, while RAS pathway mutations are frequently observed in fusion negative
(FN)-RMS.[1][–][3] Additionally, these studies have identified and characterized multiple
genes and pathways by which RMS tumors promote growth and block myogenic differentiation.[1][–][4] The most frequently mis-regulated pathways include the RAS/MEK,
N t h H d h Hi HDAC d W t i li th 4–6 Th t di l


Received 1 October 2022
Revised 29 August 2023
Accepted 30 August 2023


-----

show that transformed tumor cells co-opt lineage-specific transcription factors PAX7,
MYOD, and MYF5 to promote tumor growth, while at the same time repressing terminal myogenic differentiation.[7][,][8] Accordingly, we hypothesize that releasing the block
in myogenic differentiation will likely lead to loss of tumor growth, increased myogenic
differentiation, and result in better responses to therapy. Therefore, a more precise
understanding of how the myogenic differentiation program is disrupted in RMS
tumors has the potential to lead to better treatments for this disease.

Our previous work was among the first to establish that SNAI1 and SNAI2, best
known for their roles in epithelial to mesenchymal transition in neural crest cells and
tumors of epithelial origin, are also highly expressed in RMS and other sarcomas. In
RMS they block myogenic differentiation in the RAS-mutant FN-RMS sub-type.[9][,][10] With
an optimized SNAI2 ChIP-Seq strategy, we showed SNAI2 prevents myogenic differentiation by repressing a network of transcription factors and myogenic structural proteins that are necessary for terminal myogenic differentiation.[10] We found that
competition for the same E-Box DNA binding elements between SNAI2 and the myogenic transcription factor MYOD, enables SNAI2 to repress MYOD-driven myogenic differentiation while still allowing its pro-growth effects.[10] We therefore uncovered a
novel mechanism whereby muscle lineage transcription factor MYOD’s pro-growth
and pro-proliferation functions are enabled while its pro-differentiation functions are
inhibited.[10] We recently identified that SNAI2 protects RMS tumors from ionizing radiation (IR)-induced apoptosis through direct repression of pro-apoptotic BIM expression.[11] We found that while a majority of genes are repressed by SNAI2, a small yet
important subset of genes (e.g., NOTCH1) also require SNAI2 for their expression.[10] This
finding suggests that in some contexts SNAI2 can also activate gene expression.
However, how SNAI2, a well-known transcriptional repressor, can directly activate gene
expression remains unknown,[12][–][14] even though it has been reported that regulators
of epithelial to mesenchymal transition, for example, ZEB1 can activate gene
expression.[15]

The Notch signaling pathway, especially NOTCH1, is an important modulator of
stemness and differentiation in the muscle and in RMS. Despite an extensive understanding of Notch signaling, including the identification and characterization of activating or loss of function mutations in cancer, mechanisms for how NOTCH1
expression is maintained or regulated in normal and malignant cells remains an important unknown. In this study, we define a novel mechanism by which SNAI2 activates
rather than represses NOTCH1 expression. We show that SNAI2 and CTCF can physically
interact and also co-occupy the same chromatin region. A subset of SNAI2/CTCF sites
are associated with chromatin 3D topologically associating domain (TAD) boundaries.
We show that a SNAI2/CTCF co-binding site occupies a highly conserved sub-TAD
boundary that is essential for maintaining NOTCH1 expression. However, as previously
described[9], NOTCH1 is essential for viability and blocks myogenic differentiation and
promotes self-renewal in FN-RMS tumors. In contrast, FP-RMS Rh30 cells do not require
NOTCH1 expression for viability. We show that SNAI2 effects on self-renewal and preventing myogenic differentiation are mediated in part by maintaining NOTCH1 expression, yet it is independently required to protect RMS cells from the effects of ionizing
radiation through its repression of pro-apoptotic BIM expression. Our results reveal a
mechanism by which SNAI2 is required for stem cell regulator NOTCH1 expression via
regulation of chromatin 3D structure.

RESULTS

SNAI2 is required for NOTCH1 expression in FN-RMS cells. To evaluate the role of
SNAI2 in RMS biology, we previously generated stable knockdown of SNAI2 in RD and
SMS-CTR RMS cells using validated shRNAs (10). Analysis of shSNAI2 stable knockdown
cells revealed robust myogenic differentiation in vitro and in vivo, loss of cell proliferation, and decreased self-renewal capability in vitro. In the same study, we performed
ChIP f SNAI2 d MYOD d RNA i t l d SNAI2 k kd ll t


-----

define the gene regulatory network that SNAI2 modulates.[10] In the SNAI2-knockdown,
we observed induction of expression of myogenic differentiation factors MYOG, MEF2
family members MEF2A/C/D, CDKN1A, and a large cluster of myogenic terminal differentiation genes, which is consistent with SNAI2 being a transcriptional repressor.[10]

However, contrary to its characterized role as a transcriptional repressor, we also found
a smaller cluster of genes that are downregulated when SNAI2 is ablated with shRNA
(Fig. 1A). The downregulated genes included members of the Notch, Hippo, Shh, and
Wnt signaling pathways. We have previously characterized a NOTCH1/SNAI1/MEF2C
pathway in FN-RMS that expands self-renewal and prevents myogenic differentiation
in vitro and in vivo.[9] In that study, we showed that NOTCH1 expression is positively correlated with both SNAI1 and SNAI2 expression in RMS tumors. In our present study,
using representative and commonly used RMS RD, SMS-CTR and Rh30 cells,[16] we
explore the unexpected finding that SNAI2 is required to maintain Notch signaling and
in particular NOTCH1 expression, taking advantage of our considerable prior understanding of its role in FN-RMS.

Gene expression analyses for Notch signaling components in SNAI2 knockdown
cells compared to control shRNA cells revealed that Notch signaling receptors
(NOTCH1, 2, and 3), Notch pathway components (DTX1, 2, 4, PSNEN), and Notch signaling targets (HES1, DTX1, DTX2, CCND1) were downregulated upon loss of SNAI2
(Fig. 1A). GSEA analysis showed that the Notch pathway was downregulated in SNAI2
knockdown RD and SMS-CTR cells (Fig. 1B). Our qPCR analysis comparing control
shRNA to SNAI2 knockdown cells confirmed that NOTCH1 expression was lost in SNAI2

FIG 1 SNAI2 is required for NOTCH1 expression in FN-RMS cells. (A) Representation of pathways downregulated in shSNAI2 knockdown cells compared to
shScrambled (Scr) RD and SMS-CTR cells. Number of genes in each class is on the Y axis. The highlighted box indicates Log 2-fold change in expression of
Notch pathway genes comparing the RNA-seq data in shSNAI2 vs shScr cells. (B) GSEA analysis showing distribution of Notch pathway genes in shSNAI2
compared to shScr RD cells. Less than 0 enrichment score indicates downregulated gene sets in shSNAI2 sample. (C) Relative gene expression via real time
qPCR of cancer pathway genes in shSNAI2 knockdown compared to shScr RD and SMS-CTR cells grown in differentiation media. [�] < 0.05, [��] < 0.001,
��� < 0.0001 P-value by Student’s t test, error bars represent standard deviation of three technical replicates. (D) Protein expression of Intracellular
NOTCH1 (ICN1), Intracellular NOTCH2 (ICN2), and Intracellular NOTCH3 (ICN3) in shSNAI2 knockdown compared to shScr in RD and SMS-CTR cells, b-tubulin
was used as loading control.


-----

knockdown cells (Fig. 1C). Consistent with the RNA-seq data, we observed downregulation
of various growth/cancer signaling pathway genes in RD and SMS-CTR cells (Fig. 1C).[10] In
addition, Western blots for NOTCH1 in RD and SMS-CTR cells with shSNAI2 knockdown
also showed a reduction of intracellular domain of NOTCH1 (ICN1) and NOTCH3 (ICN3) but
not NOTCH2 (ICN2) proteins (Fig. 1D). Our analysis indicates that SNAI2 is required for
NOTCH1 and potentially NOTCH3 expression.

SNAI2 binds downstream of NOTCH1 locus at a CTCF binding site that defines a
sub-TAD boundary. Since SNAI2 is a known transcriptional repressor, we next sought
to understand the mechanistic basis for how it also maintains NOTCH1 expression. We
first analyzed SNAI2 ChIP-seq tracks at the NOTCH1 and NOTCH3 loci. We observed a
strong SNAI2 binding peak downstream of only the NOTCH1 gene, and this highly
enriched SNAI2-bound site overlapped with a CTCF peak (Fig. 2A, left). NOTCH1 is on
chromosome 9 (139,286,300–139,440,010) and transcribed 5[0]-3 from the anti-sense
strand. Importantly, assessing the ENCODE data base[17] for other factors bound to this
site in the listed cell lines showed enrichment of SMC3, a cohesion involved in loop formation, along with CTCF at this site. This site was also devoid of HDAC2 binding, suggesting that this was not a repressive element containing a SNAI2-HDAC complex
(Fig. 2B). This peak region was previously annotated as part of a potential CTCF chromatin insulator loop boundary in blood cancer cells,[18] and there are SNPs associated
with this peak that are present in individual patients with ovarian, prostrate and liver
cancers in COSMIC,[19] suggesting a functional role in regulating NOTCH1 expression
(Fig. 2B). In addition, the CTCF peak at the SNAI2/CTCF site downstream of NOTCH1
hereafter referred to as the N1TAD element – was conserved across cell lines of different lineages represented on the ENCODE database (Fig. 2C). We also compared our
SNAI2 ChIP-seq data with three published SNAI2-ChIP seq tracks and observed that the
SNAI2 peak downstream of the NOTCH1 site was well conserved (Fig. 2D). We found
that this region was devoid of detectable H3K27ac, H3K4Me3 and H3K4Me1 enrichment, indicating that it is not an enhancer element. We therefore hypothesized that
this overlapping SNAI2/CTCF peak could be part of a NOTCH1 gene regulatory TAD
(topologically associated domain). The SNAI2/CTCF peak occupied one end of the
boundary, while only CTCF was present on the other end of the sub-TAD or chromatin
loop (16). The sub-TAD structure we identified was conserved in cell line HiC data from
IMR90 and GM1287 cells (Fig. 2E and F).[20] To understand the chromatin architecture
associated with this element, we analyzed newly generated Hi-C data in fusion negative RD, SMS-CTR and fusion positive Rh30, Rh41 RMS cell lines and observed that this
peak was situated at a sub-TAD boundary within a larger TAD that encompasses the
NOTCH1 locus (Figs. 2A right and 3A).[21] The analysis of this site across published chromatin data sets from ENCODE indicated that this is a well-conserved element in all cell
types assessed and harbors a potential chromatin subdomain containing the NOTCH1
gene.

To understand the potential chromatin interactions of SNAI2, we assessed previously generated data for chromatin binding in the context of SNAI2 using ChromHMM.
This analysis showed that while the majority of SNAI2 binding sites lie within
enhancers and promoters, a significant number of SNAI2 binding sites overlapped with
CTCF binding sites.[10] We investigated this further by aligning SNAI2 (2569) and CTCF
ChIP-seq binding peaks (33,860), in SMS-CTR cells and observed that 30% of SNAI2
binding overlaps with CTCF (Fig. 3B). Further comparison of binding intensity at CTCF
and SNAI2 sites for these two factors showed that while both SNAI2 and CTCF are
mildly enriched at each other’s binding regions, interestingly, a subset of sites had
strong enrichment for both SNAI2 and CTCF, suggesting co-binding at such chromatin
bound peaks (Fig. 3C). We also assessed the enrichment of SNAI2 and CTCF peaks at
insulated boundaries (16) and both SNAI2 and CTCF were enriched at characterized
insulator boundaries (Fig. 3C).[18] Overall, our analysis of SNAI2 and CTCF ChIP-seq data
showed that SNAI2 is enriched at a subset of CTCF sites, and some of these sites are
i t d ith h ti b d i


-----

FIG 2 SNAI2 binds downstream of NOTCH1 at a chromatin domain insulator CTCF binding site that defines a sub-TAD boundary. (A) (Left) ChIP-seq tracks
of SNAI2 and CTCF at the NOTCH1 locus along with H3k27AC and relative SNAI2 enrichment in SMS-CTR cells under shScr and shSNAI2 conditions (D Delta
enrichment values). Lines represent previously defined CTCF-CTCF loop anchor points.[18] NOTCH1 is on chr 9,139,286,300–139,440,010 and transcribed 5[0]-3[0]

from the anti-sense strand (hg38). (Right) Hi-C chromatin interaction heatmap in SMS-CTR cells at the NOTCH1 locus, black line indicates TADs
(topologically associated domains) in the vicinity of SNAI2/CTCF binding peak. Intensity of chromatin interactions are indicated by red (high), yellow
(medium) and blue (low). Light green line indicates position of the SNAI2/CTCF peak from ChIP-seq data. (B) Tracks from the ENCODE database, showing
binding of chromatin binding factors CTCF, SMC3, HDAC2, H3K27Ac, H3K4Me3 and H3K4Me1 at the N1TAD site. Also indicated are mutations from
COSMIC. (C) CTCF enrichment at the N1TAD element across cell lines from various tissue types in ENCODE. (D). SNAI2 ChIP-seq data from four cell lines
from the literature comparing the NOTCH1 N1TAD peak to other validated SNAI2 peaks at target genes. (GEO accession numbers in Materials and
Methods). (E and F) Hi-C heat map of chromatin interactions in IMR90 (fibroblast) and GM12878 (lymphoblastoid) cells from previously published data.[20]

Both cell lines have sub-TAD structures at the NOTCH1 locus, green line indicates sub-TAD boundary downstream of NOTCH1.

SNAI2 regulates the NOTCH1 TAD boundary by direct protein-protein
interaction with CTCF. To understand the chromatin context of the N1TAD region at
the NOTCH1 locus and to further evaluate if the structural domains seen in Hi-C data
are mediated by CTCF, we performed HiChIP for CTCF in RD cells. Consistent with the
Hi-C data, HiChIP for CTCF showed a well-defined sub-TAD structure at the NOTCH1
locus, with its boundary at the CTCF-SNAI2 site (Fig. 3D and E). To confirm enrichment
observed by ChIP-seq for CTCF and SNAI2 at the N1TAD region, we validated our findi i ChIP PCR (Fi 3F) I dditi f d th t CTCF i h t


-----

FIG 3 A subset of SNAI2 and CTCF binding sites overlap and SNAI2 can form a protein-protein interaction with CTCF. (A) Hi-C chromatin interaction
heatmap in RD Rh30 and Rh4 cells at the NOTCH1 locus, green line indicates sub-TAD boundary downstream of NOTCH1, with SNAI2/CTCF binding peak.
Intensity of chromatin interactions are indicated by red (high), yellow (medium) and blue (low). (B) Overlap of SNAI2 and CTCF binding peaks in embryonic
stem cells (ES), keratinocytes and SMS-CTR (RMS) cells represented as the percentage of intersecting ChIP enrichment peak regions from the three datasets.
(C) Average Enrichment score assessed using HOMER analyses for enrichment for CTCF or SNAI2 binding at only SNAI2, CTCF or SNAI2-CTCF overlapping
peaks in SMS-CTR ChIP-seq data. Average enrichment score of CTCF and SNAI2 binding at insulator boundaries indicates CTCF binding sites with insulator
function.[18] (D and E) Hi-C and HiChIP for CTCF in RD cells showing the 3D structure of the sub-TAD region at the NOTCH1 locus. Also plotted is the SNAI2
binding peak at the N1TAD site. (F) Chromatin enrichment for CTCF at the SNAI2-CTCF N1TAD site in RD cell line, shScr and shSNAI2 cells assessed by
ChIP-qPCR ([�] < 0.05, [��] < 0.001, [���] < 0.0001 P-value by Student’s t test, error bars represent standard deviation of three technical replicates). (G) Coimmunoprecipitation assays in RD cells. Endogenous SNAI2 (SNAI2-IP) and CTCF pull downs (CTCF-IP) were probed for SNAI2 and CTCF respectively in IP
fractions along with IgG pulldown under similar conditions. 2% of total lysate was loaded as input.

reduced at the N1TAD element in SNAI2 shRNA knockdown cells, suggesting that
SNAI2 binding maintains or augments CTCF binding at the N1TAD element (Fig. 3F).
Our findings indicate that SNAI2 and CTCF binding can overlap; we therefore asked if
SNAI2 and CTCF also physically interact at the protein level using in vitro pulldown/
co-immunoprecipitation assays. Immunoprecipitation of SNAI2 in RD cells showed
enrichment of CTCF in the pulldown fraction, as well as SNAI2 enrichment in the CTCF
pulldown fraction but no enrichment using a control IgG antibody, confirming a protein-protein interaction between SNAI2 and CTCF (Fig. 3G). Protein-protein interaction
and co-occupancy of chromatin by SNAI2-CTCF suggests direct regulation of CTCF
function by SNAI2. At the N1TAD region, we observed a requirement of SNAI2 for optimal CTCF binding or cooperative binding. Together, our HiChIP data supports our Hi-C
findings and confirms that the 3D structures seen at the NOTCH1 locus was indeed
occupied by CTCF. Overall, our data indicates that SNAI2 binds downstream of the


-----

NOTCH1 gene and stabilizes a CTCF-CTCF loop (sub-TAD), and loss of SNAI2 by knockdown via shRNA leads to reduced CTCF binding.
Deletion of the SNAI2/CTCF (N1TAD)-binding site leads to loss of NOTCH1
expression and loss of cell proliferation in FN-RMS cells. To determine the functional requirement of the SNAI2/CTCF sub-TAD peak for NOTCH1 expression, we
designed guide RNAs to target the SNAI2/CTCF N1TAD (sub-TAD) site, and in this context defined if the SNAI2/CTCF TAD boundary is required to maintain NOTCH1 expression. CRISPR sgRNAs were designed for deleting a 365 bp region overlapping with the
SNAI2 and CTCF binding sites, and as a negative control, we also targeted a smaller
SNAI2 peak distal to the N1TAD peak (negative control) (Fig. 4A). DNA constructs with
5[0] and 3[0] sgRNAs to the control and N1TAD region were packaged into lentiviral vectors carrying dual selection antibiotic markers (puromycin and hygromycin) to ablate
the N1TAD site in RMS cells. Following CRISPR-mediated ablation of the SNAI2/CTCF
binding sites in RD, SMS-CTR and Rh30 cells, we assessed the effect on NOTCH1 expression, cell survival, proliferation and differentiation. Deletion of the N1TAD region was
confirmed by a heteroduplex assay and also by genomic PCR followed by DNA
sequencing (Fig. 4B and C). Loss of the N1TAD regulatory element at the NOTCH1 locus

FIG 4 CRISPR/Cas9 ablation of the N1TAD sub-TAD site leads to loss of NOTCH1 expression and results in loss of cell proliferation and survival in FN-RMS
cells. (A) ChIP-seq data for SNAI2 and H3K27ac binding at the NOTCH1 locus. Overlayed is the schematic of the CRISPR/Cas9 guide RNA targeting strategy
to ablate the N1TAD and negative control sites. (B) DNA heteroduplex assays of genomic PCR products from Ctl gRNA or N1TAD gRNA lentiviral infected
RD, SMS-CTR and Rh30 cells run on PAGE gels. The deleted fragment in N1TAD cells leads to loss of a 365 bp PCR product. (C) Chromatogram of Sanger
sequencing of N1TAD deleted (365bp) region in RD cells. (D) Relative gene expression of NOTCH1 mRNA in N1TAD deleted cells compared to Control RD
cells assessed by real time qPCR. ([�] < 0.05, [��] < 0.001, [���] < 0.0001 P value by Student’s t test, error bars represent standard deviation of three technical
replicates.) (E) Gene expression analysis of genes neighboring N1TAD region in N1TAD ablated cells compared to control cells. ([�] < 0.05, [��] < 0.001,
��� < 0.0001 P-value by Student’s t test, error bars represent standard deviation of three technical replicates.) (F) Western blot of Intracellular NOTCH1
(ICN1) in Ctl (control) gRNA and N1TAD-deleted cells. GAPDH was used as loading control. (G-H) NOTCH1 expression in Ctl and N1TAD-deleted cells in SMSCTR and Rh30 cells. (Error bars represent standard deviation of three technical replicates.) (I) Cell confluence over time in N1TAD and Ctl deleted RD and
SMS-CTR cells. (Error bars represent standard deviation in three technical replicates.) (J) Colony formation assays in Ctl, N1TAD-deleted and Negative
control (Neg Ctl) RD cells. (K) Cell confluence over time in N1TAD and Ctl deleted Rh30 cells (Error bars represent standard deviation in three technical
li ) (L) C l f i f C l d N1TAD d l d Rh30 ll


-----

resulted in significant loss of NOTCH1 mRNA expression (Fig. 4D). While there was drastic reduction of the NOTCH1 mRNA, two genes immediately downstream of N1TAD
element, C19orf163 and SEC16A, were unaffected or slightly increased in the
CRISPR/Cas9 knockout cells compared to controls (Fig. 4E), indicating that binding of
SNAI2/CTCF at the N1TAD element is required for NOTCH1 expression. The effect of
N1TAD deletion was specific to NOTCH1, as the expression levels of other genes in the
immediate vicinity but outside of the sub-TAD were unaffected or increased. To confirm if the effect of diminished NOTCH1 expression observed via qPCR was also
observed at the protein level, we performed Western blot analysis and observed similar
losses in ICN1 protein levels in N1TAD-deleted RD, SMS-CTR and Rh30 cells (Fig. 4F).
The effect of N1TAD deletion on NOTCH1 mRNA in SMS-CTR and Rh30 cells was similar
to RD cells (Fig. 4G and H). Growth curve analysis of N1TAD-deleted cells showed complete loss of cell confluence of N1TAD deleted cells compared to control RD and SMSCTR cells (Fig. 4I), and these cells did not survive 20 days post-selection. Therefore, all
assays were performed within this time window in transient CRISPR/Cas9 lentivirusinfected cells. Consistent with the growth assays, colony formation in N1TAD-deleted
cells was significantly reduced compared to control guide RNA expressing cells and
negative control CRISPR/Cas9 deleted cells (Fig. 4J). We also tested the effects of
N1TAD deletion in a NOTCH1-independent RMS cell line, Rh30. We predicted that since
Rh30 cells do not require NOTCH1 for viability, the N1TAD deletion should result in the
loss of NOTCH1 but have no effect on cell viability or growth. Indeed, our analysis in
Rh30 N1TAD-deleted cells showed that upon CRISPR deletion, while NOTCH1 levels are
reduced, these cells did not show any growth defects and formed similar number of
colonies as control cells (Fig. 4K and L). Lack of deleterious effects upon deletion of the
SNAI2-bound negative control confirmed that effects of our deletions of the N1TAD
site are specific and not due to off target effects or disruption of other genes. Thus, the
SNAI2/CTCF-bound N1TAD site is essential for NOTCH1 expression and viability in
FN-RMS.
Lethality resulting from loss of the SNAI2/CTCF co-occupied Sub-TAD
boundary regulating NOTCH1 expression can be rescued by exogenous NOTCH1.
To explore further the effects of N1TAD deletion in RMS cells, we performed sphere formation and differentiation assays in the CRISPR-targeted RD cells. Consistent with our
confluency and colony formation assays, we observed a significant loss in tumor
sphere formation in N1TAD-deleted cells, indicating that self-renewal capability of
these cells is highly compromised (Fig. 5A and B). Next, we assayed the differentiation
potential of N1TAD-deleted cells by culturing them in myogenic differentiation
medium (3 days) and staining for muscle differentiation markers MyHC and MEF2C.
The N1TAD-deleted cells displayed substantially higher level of myogenic differentiation compared to control cells (Fig. 5C and D). Our data indicate that N1TADmediated NOTCH1 loss potentiates myogenic differentiation along with restricting
sphere formation. This effect is consistent with the previously characterized role of
NOTCH1 as a self-renewal factor and an inhibitor of myogenic differentiation in the
muscle and FN-RMS.[9][,][22][–][24] To confirm if the effects seen in N1TAD-deleted cells are not
due to nonspecific changes in the chromatin at the locus, we deleted a region 10 kb
downstream of the NOTCH1 (5 kb from N1TAD) locus which contained a minor SNAI2
peak (devoid of CTCF peak) and was closer to two neighboring genes C19orf163 and
SEC16A. CRISPR sgRNA-mediated deletion of the negative control region (Neg Ctl) did
not affect NOTCH1 expression, growth, or sphere formation ability of RD cells (Fig. 5E
to H). Lack of deleterious effects upon deletion of the NOTCH1 negative control enhancer fragment provide supporting evidence that the effects of deletion of the N1TAD
region are specific and not due to off target effects or disruption of other genes.

To discern whether N1TAD knockout effects on cell viability are mediated by loss of
NOTCH1 expression, we designed an experiment with co-infection of a construct
encoding a constitutively active NOTCH1 cDNA along with Cas9 and gRNA’s for N1TAD
deletion in RD cells to determine if re-expressing NOTCH1 would restore viability
(Fi 5I) Th NOTCH1 tit ti l ti t t t i th i t ll l d i


-----

FIG 5 Lethality resulting from loss of SNAI2/CTCF bound sub-TAD boundary regulating NOTCH1 expression can be rescued by exogenous NOTCH1. (A and
B) Sphere formation assay images for Ctl and N1TAD RD deleted cells. Spheres per field is indicated in the image. Images taken with a 2� objective.
(C and D) Differentiation assay images for Ctl and N1TAD deleted cells. Myogenic differentiation scored by blue-DAPI, green-MyHC, red-MEF2C, scale
bar ¼ 100 mM. (E) Western blot for intracellular NOTCH1(ICN1) protein expression upon CRISPR/Cas9 deletion of a nearby control genomic region (Neg Ctl)
compared to control gRNA region. GAPDH was used as a loading control. (F) Cell confluence in N1TAD, Neg Ctl and Ctl deleted cells. (Error bars represent
standard deviation in three technical replicates.) (G-H) Sphere formation assays of Ctl and Neg Ctl deleted cells, imaged after 15 days in neuro-basal
medium, spheres per field is indicated in the image. Imaged at 2� objective. (I) Schematic showing strategy for rescue of Notch signaling using NOTCH1
DE in N1TAD deleted cells. (J) DNA heteroduplex assays of genomic PCR products from genomic PCRs of Ctl þ NOTCH1DE and N1TAD-deleted þ NOTCH1DE
RD cells. (K) Western blots of Intracellular NOTCH1 (ICN1) in Ctl þ NOTCH1DE and N1TAD deleted þ NOTCH1DE RD cells. b-tubulin was used as loading
control. (L) Cell confluency over time in Ctl þ NOTCH1DE and N1TAD-deleted þ NOTCH1DE RD cells. (Error bars represent standard deviation of three
technical replicates.) (M) Chromatogram of Sanger sequencing of N1TAD-deleted þ NOTCH1DE RD cells. (N) Cell confluence images of control, N1TADdeleted, Ctl þ DE & N1TAD deleted þDE RD cells at Day 4 and 10 (all images were obtained using a 10� objective).

of NOTCH1 protein and lacks the transmembrane domain, hence the cells have constitutively active NOTCH1 signaling (NOTCH1 DE).[25] The resulting cells were assayed for
ICN1 expression and growth kinetics. The NOTCH1DE þ N1TAD cells expressed
NOTCH1 protein similar to control cells and rescued viability of the N1TAD-deleted
cells (Fig. 5J to N). The growth kinetics of NOTCH1DE þ N1TAD cells was slightly slower
than Control þ NOTCH1DE cells, and morphologically they resembled control cells
th th N1TAD d l t d ll th h th N1TAD i d l t d


-----

FIG 6 Ablation of SNAI2 results in the recovery of RD and SMS-CTR cells with enhanced NOTCH1 expression. (A) Schematic off CRISPR/Cas9 guide RNA
targeting strategy to eliminate SNAI2. Chromatogram of Sanger sequencing from SNAI2 CRISPR/Cas9 KO cells is shown below, indicating the region of exon
deleted in SNAI2. (B) Western blot of control and SNAI2 KO cells indicating complete loss of SNAI2. b-tubulin was used as loading control. (C) Images of
SMS-CTR, RD and Rh30 cells post SNAI2 KO, indicating extensive cell death in SMS-CTR and RD lines, however Rh30 cells were less affected by SNAI2 KO
(all images were taken using a 10� objective). (D) NOTCH1 mRNA levels in SMS-CTR, RD and Rh30 cells comparing SNAI2 KO to control cells. ([�] < 0.05,
�� < 0.001, ��� < 0.0001 P value by Student’s t test, error bars represent standard deviation of three technical replicates.)

(Fig. 5L and N). Finally, we confirmed that N1TAD was deleted in the surviving cells
using DNA sequencing (Fig. 5M).

Given that the SNAI2/CTCF-bound N1TAD is essential to maintain NOTCH1 expression, we tested if ablation of SNAI2 in FN-RMS RD and SMS-CTR cells would also result
in the loss NOTCH1 (ICN1) expression and also a loss of cell viability. CRISPR/Cas9 deletion of SNAI2 using a two-guide RNA strategy (deletion of 149 amino acids in exon 2)
resulted in the loss of majority of RD and SMS-CTR cells. In contrast, FP-RMS Rh30 cells
did not perish upon SNAI2 ablation (Fig. 6A to C). We observed that while the majority
of RD and SMS-CTR cells with SNAI2 Knocked out (KO) die, a few clones survive and
repopulate cultures over time. We determined NOTCH1 expression in the clones that
survived, and as expected we find that these cells re-express ICN1 (Figs. 6D and 7A).
Together, our analysis with N1TAD and SNAI2 KO in the RD and SMS-CTR cells demonstrates that the SNAI2/CTCF N1TAD element is essential for NOTCH1 expression, and
that SNAI2 is required for NOTCH1 expression. However, in the SNAI2 KO, rare clones
can regulate NOTCH1 independently of SNAI2.
SNAI2 regulation of NOTCH1 expression and effects on self-renewal and
differentiation in FN-RMS can be uncoupled from SNAI2 requirements on
protecting cells from ionizing radiation. We have previously reported that SNAI2
protects RMS cells, xenografts, and PDXs from ionizing radiation. We showed that the
radioprotective effects of SNAI2 are mediated by repression of pro-apoptotic BIM
(BCL2L11) d b i d d t f 53[11] I FN RMS RD d SMS CTR ll ft l


-----

FIG 7 SNAI2 regulation of NOTCH1 expression and effects on self-renewal and differentiation in FN-RMS can be uncoupled from SNAI2 requirements on
protecting cells from ionizing radiation. (A) Western blot of SNAI2 and intracellular NOTCH1 (ICN1) in CRISPR/Cas9 SNAI2 ablated cells (SNAI2 knockout).
b-tubulin was used as loading control. (B) Confluency assay over time in Ctl and SNAI2 KO RD cells. (Error bars represent standard deviation of three
technical replicates.) (C-D) Differentiation of SNAI2 KO RD cells compared to control cells after 3 days in myogenic differentiation medium. Blue-DAPI,
green-MyHC and red-MEF2C staining, scale bar 100 mM. ([�] < 0.05, [��] < 0.001, [���] < 0.0001 P value by Student’s t test, error bars represent standard
deviation of three technical replicates.) (E) Quantification of differentiation in RD SNAI2 KO and Ctl cells after 3 days in myogenic differentiation medium.
(F) Sphere formation assays in RD and Rh30 Ctl and SNAI2 KO cells imaged with a 2� objective. (G) Quantification of RD and Rh30 tumor spheres in SNAI2
KO compared to Control cells. ([�] < 0.05, [��] < 0.001, [���] < 0.0001 P value by Student’s t test, error bars represent standard deviation of three technical
replicates.) (H and I) Survival fraction analysis in Ctrl and SNAI2 KO cells after treatment with different doses of ionizing radiation in RD and Rh30 cells.
([�] < 0.05, [��] < 0.001, [���] < 0.0001 P value by Student’s t test, error bars represent standard deviation of three biological replicates.) (J) Colony formation
assays from above of Ctrl and SNAI2 KO cells after exposure to different doses of ionizing radiation. (K) Western blot of BIM in RD and Rh30 cells. b-tubulin
was used as loading control. (L) Western blots of myogenic differentiation proteins in SNAI2 KO cells compared to control gRNA cells. b-tubulin was used
as loading control.

of SNAI2, the rare surviving clones re-express NOTCH1 and grow at similar growth rates
to control cells (Figs. 6C and D, 7B). This provided us with the opportunity to test if rescued cells also recover the ability for self-renewal and are blocked in differentiation
due to NOTCH1 re-expression, yet continue to be sensitive to ionizing radiation, which
is mediated through SNAI2 repression of BIM expression.
We performed differentiation assays in RD (FN-RMS) and Rh30 (FP-RMS) cells comparing control to SNAI2-ablated conditions. We found that while SNAI2 knockout RD
cells are more prone to myogenic differentiation, this effect (�8% differentiated
myosin-MyHC positivity) even though significant was not as prominent as shRNA
knockdown cells (�20%, differentiated myosin-MyHC positivity) (Fig. 7C to E) (4). In
contrast, Rh30 cells with SNAI2 shRNA knockdown do not undergo myogenic differentiation.[11] We next assessed the effect of SNAI2 knockout on sphere formation in RD
and Rh30 cells. In RD cells, rather unexpectedly, we found that even though SNAI2
knockout cells express higher levels of NOTCH1, they formed only half as many spheres
as control cells. Rh30 cells with SNAI2 ablated have no significant differences in sphere
forming ability compared to control cells (Fig. 7F and G).

Next, we performed colony formation survival assays in SNAI2 KO RD and Rh30 cells
t t d ith i i d f i i i di ti W b d th t b th RD d


-----

Rh30 SNAI2 KO cells were significantly lost after radiation compared with control cells.
Thus, both RD and Rh30 cells with SNAI2 loss are exquisitely sensitive to ionizing radiation (Fig. 7H to J).[11] Furthermore, this effect is independent of NOTCH1 expression.
Next, we assessed BIM expression in SNAI2 knockout RD and Rh30 cells and found that
SNAI2-ablated cells as expected expressed high BIM compared to controls (Fig. 7K and
L), indicating that they are primed for apoptosis.

Our data clearly indicates that SNAI2-mediated effects on differentiation and selfrenewal are distinct from its effects on protection from ionizing radiation-induced
apoptosis. Further, since our data suggest that SNAI2 affects self-renewal and differentiation are via different mechanisms, we tested the effect of SNAI2 on repression of
MYOG, MEF2A and MEF2C, all genes critical for myogenic differentiation in SNAI2
shRNA knockdown cells.[10] We found that despite SNAI2 KO cells expressing higher levels of ICN1, they also expressed high levels of MYOG, MEF2A, and MEF2C (Fig. 7L), suggesting that SNAI2 effects on blocking myogenic differentiation are retained despite
high NOTCH1 levels. However, the re-expression of NOTCH1 independently of SNAI2
likely is inhibiting terminal differentiation and self-renewal by other mechanisms.
Together, our experiments show that SNAI2-mediated effects on self-renewal and differentiation are reliant in part on its ability to maintain NOTCH1 expression, through
N1TAD. However, its effects on preventing apoptosis postradiation is independent of
its regulation of self-renewal and myogenic differentiation.

DISCUSSION

Here we demonstrate a novel mechanism by which SNAI2, a well-known transcriptional repressor, can also regulate gene expression via regulation of chromatin topological domain structure that is essential for NOTCH1 expression. This function of SNAI2
is distinct from its previously defined roles in RMS, where it inhibits myogenic differentiation via repressing gene expression by binding to E-Box elements associated with
enhancers in genes required for terminal myogenic differentiation.[10] Gene expression
relies on a complex interplay between promoters and enhancers, where selective
enhancer usage determines tissue specificity, and chromatin looping enables the
establishment of long-range enhancer promoter interactions. However, the role of
transcription factors in shaping the three-dimensional organization of the genome during cell differentiation remains poorly understood. Genome-wide studies have mostly
focused on general mechanisms involving CTCF [20][,][26][–][28] and YY1-dependent chromatin
organization.[29] Key outstanding questions in the field include how a general chromatin
insulator protein CTCF that has over 50,000 binding sites across the genome sets up
TAD boundaries only at specific loci, and how it modulates 3D chromatin structure in a
tissue-specific manner is not well understood. In this report, we focused on the role of
SNAI2 in regulating NOTCH1 expression for the following reasons: (1) NOTCH1 is an
important regulator of stem cell biology and myogenic differentiation in RMS and the
muscle, yet how NOTCH1 is regulated at the transcriptional level is not well understood, (2) The SNAI2/CTCF co-binding site represents a high affinity peak relative to
other called peaks, and it is devoid of HDAC2 or H3K27ac binding, suggesting a novel
mode of gene regulation by a transcriptional repressor SNAI2 (Fig. 2B).

The Notch pathway is essential for growth and differentiation in multiple cell types
and was characterized as a growth signal produced by the notochord in the developing embryo that drives neurogenesis and other essential processes during development.[30][,][31] The Notch signaling pathway is a critical regulator of muscle stem cells,
differentiation, and growth. The ablation of Notch genetically or by Notch inhibitors
leads to induction of differentiation and subsequent loss of regenerative capability in
muscle progenitors (5, 6). Notch signaling is required to maintain and expand muscle
stem cells via symmetric cell divisions.[23][,][24] In the aging muscle, there is loss of Notch
signaling in muscle stem cells, and re-expressing Notch ligand Jagged1 can restore the
ability to regenerate muscle.[22][,][32] High Notch signaling is often observed in RMS, and
hi h N t h i li d th b f t ti ll b h


-----

10-fold and prevents myogenic differentiation in FN-RMS tumors.[9][,][33][–][35] NOTCH1 is particularly important for regulating both the self-renewal properties and number of
muscle stem cells, and loss of NOTCH1 leads to reduced regenerative capacity in aging
muscle.[22][,][32] Accordingly, activating mutations in NOTCH1 or loss of FBXW7, which is
required for NOTCH1 turnover, are observed in a small subset of FN-RMS tumors.[1][–][3]

However, a majority of FN-tumors express high levels of NOTCH1 by unknown mechanisms. Our data indicates that in cells or tissues that express high levels of SNAI2,
SNAI2 stabilizes a CTCF-CTCF 3D chromatin loop/TAD boundary resulting in higher
NOTCH1 expression. Conversely, SNAI2 knockdown via shRNA or CRISPR/Cas9 deletion
of the SNAI2/CTCF binding site leads to destabilization of the chromatin domain, loss
of NOTCH1 expression, and loss of viability of FN-RMS RD and SMS-CTR cells. Thus,
SNAI2 expression acts as a molecular switch at the distal NOTCH1 TAD boundary that
can regulate differential NOTCH1 expression (Fig. 8A and B). Since SNAI2 expression is
inducible, for example, post-damage via radiation, an important feature of SNAI2 regulation of NOTCH1 expression may be the ability to modulate stem cell factor NOTCH1
expression in response to damage, resulting in increased stem cell numbers only when
needed (e.g., post-injury to muscle, or in the case of tumors post radiation therapy
induced damage). In FN-RMS tumors, continuous maintenance of high SNAI2 and high
NOTCH1 expression results in the tumor being locked in a proliferative state, along
with the ability for self-renewal. In support of this model, high SNAI2 expression is positively correlated with NOTCH1 expression in RMS tumors.[9] Thus, SNAI2 regulation of
NOTCH1 in FN-RMS cells is important to enhance self-renewal and growth and provides
another mechanism to prevent myogenic differentiation.

With respect to myogenic differentiation in FN-RMS RD and SMS-CTR cells, our
study finds that knockdown of SNAI2 results in the loss of NOTCH1-3 at the mRNA level
but only NOTCH1 (ICN1) and NOTCH3 (ICN3) at the protein level. Second, complete
ablation of SNAI2 results in the survival of rare clones with either rescued ICN1, ICN2
and/or ICN3. Since, all three NOTCH receptors are shown to have important roles in
rhabdomyosarcoma differentiation, our study is not designed to dissect the roles of
individual receptors.[9][,][33][,][34][,][36][,][37] However, we can infer the following based on our analyses. We have previously shown that knockdown of NOTCH1 results in increased
MYOG, MEF2C resulting in robust differentiation.[9] Whereas NOTCH1 overexpression
blocks myogenic differentiation and increases sphere formation. Knockdown of
NOTCH3 similarly increases myogenic differentiation resulting in increased MYOG and
differentiation.[37] Conversely, overexpression results in the opposite effect.[38] SNAI2
complete ablation results in increased expression of direct regulated genes MYOG,

FIG 8 A SNAI2/CTCF interaction is required for NOTCH1 expression in rhabdomyosarcoma. (A-B) Model depicting stabilization of CTCF-CTCF chromatin loop
by SNAI2. SNAI2 binding at the sub-TAD chromatin boundary maintains normal NOTCH1 expression (A). SNAI2 knockdown or deletion of SNAI2-CTCF
bi di i l d d bili i f h i l d l f NOTCH1 i (B)


-----

MEF2A and also indirectly regulated genes MEF2C and CDKN1A. Despite the increased
expression of NOTCH1 and/or NOTCH2 and/or NOTCH3 in RD and SMS-CTR cells with
SNAI2 ablation, SNAI2 regulated MYOG, MEF2A and differentiation is increased rather
than suppressed. However, since differentiation is not as robust as partial knockdown
of SNAI2, it is possible that enhanced expression of SNAI1 in SNAI2 ablated cells may
also partially block myogenic differentiation via an EBox mechanism.[39] In addition,
NOTCH1 and or 3 may also partially suppress differentiation via regulating NOTCH targets genes HES1 and HEY1 involved in differentiation through EBox independent
mechanisms.[33][,][36] Second, SNAI2 may have NOTCH independent effects on regulating
self-renewal, as sphere formation is still disrupted in SNAI2 knockout RD cells. Finally,
since the effects we have outlined may occur in different cell subpopulations i.e. selfrenewing versus differentiating cells, single cell analyses along with manipulations of
NOTCH1-3 expression in the context of SNAI2 knockout will be required to define
SNAI2 dependent and independent effects on myogenic differentiation and selfrenewal.

SNAI2 has traditionally been characterized as a transcriptional repressor, inhibiting
gene expression by recruiting HDACs and other repressive complexes to gene promoters/enhancers.[14][,][40] However, we observed that reduction in SNAI2 can also lead to
loss of gene expression, indicating that SNAI2 is also required to maintain gene expression. From our current study, we suggest SNAI2 function in protecting insulated chromatin neighborhoods is necessary to maintain and/or reinforce gene expression via
stabilization of loop domains or TAD boundaries in concert with CTCF. In support,
SNAI2 and CTCF can physically interact and additionally overlapping CTCF-SNAI2 binding sites were observed in at least a third of all SNAI2 chromatin bound sites in ES cells
(28%)[41] and keratinocytes (42%)[42] and in RMS cells (30%),[10][,][11] with many of these sites
conserved across the three cell lines (Fig. 3B). Furthermore, the effect of SNAI2/CTCF
on regulating NOTCH1 expression is different from its effect on repressing pro-apoptotic BIM[11] expression and on repressing myogenic differentiation through direct competition with myogenic E-boxes at transcription factors and structural gene enhancers
that are required for terminal myogenic differentiation.[10] Furthermore, our studies to
date suggest that SNAI2 effects on differentiation (MYOD-SNAI2 interaction) can be
uncoupled from its role in blocking apoptosis (SNAI2 repression of BIM) and its effect
on self-renewal (SNAI2-CTCF activation of NOTCH1). Thus, our understanding of gene
regulation at the level of chromatin suggests different activities of SNAI2, including
effects on differentiation, self-renewal, and apoptosis, are distinct modules of its overall
function. Currently, SNAI2 ChIP-seq data is available for myogenic cells,[10][,][11] ES cells,[41]

keratinocytes,[42] and lung fibroblasts.[43] While a subset of the SNAI2 binding sites does
overlap including, the SNAI2/CTCF site regulating NOTCH1 expression, however we
find that tissue specific binding is not well conserved, implying SNAI2 context dependent binding across tissues (Fig. 3B). As more data is generated for SNAI2 chromatin
occupancy, conserved and tissue specific chromatin regulatory functions of this factor
will become clearer. The SNAI2/CTCF interaction that maintains and modulates TAD
structures, and local gene expression suggests that transcription factors can regulate
gene expression via reinforcing a TAD domain/boundary. In our future experiments,
we plan to more broadly explore the role of SNAI2 in maintaining TAD boundaries and
the molecular mechanisms associated with transcription factor mediated TAD
assembly.

MATERIALS AND METHODS

Material availability. Further information and requests for resources and reagents should be
directed to corresponding author.
Cell lines. The human rhabdomyosarcoma cell lines RD (female), Rh30 (male), and SMS-CTR (male)[16]

were gifted by Dr Peter Houghton, GCCRI. RD, Rh30 and SMS-CTR cells were maintained in DMEM supplemented with 10% FBS at 37 [�]C with 5% CO2. Cell lines were authenticated by genotyping.
Differentiation of RMS cells was performed for 3 days in DMEM þ 2% horse serum.

Lentiviral and siRNA knockdown. CRISPR gRNA against SNAI2, NOTCH1 N1TAD (pLenticrispr
P V2) hRNA ( LKO 1) k d i f d (F GENE6 P ) HEK293T ll


-----

TABLE 1 List of reagents and resources.

REAGENT/RESOURCE SOURCE IDENTIFIER

Antibodies
Slug (C19G7) CST Cat# 9585, RRID:AB_2239535
NOTCH1 CST Cat# 3608, RRID:AB_2153354
NOTCH2 CST Cat# 4530, RRID:AB_10860068
NOTCH3 CST Cat# 5276, RRID:AB_10560515
CTCF CST Cat# 2899, RRID:AB_2086794
Myosin Heavy Chain DSHB Cat# MF 20, RRID:AB_2147781
MEF2C (D80C1) CST Cat# 5030, RRID:AB_10548759
MEF2A CST Cat# 9736, RRID:AB_10691852
MYOG DSHB Cat# F5D, RRID:AB_2146602
H3K27Ac Active motif Cat# 39133, RRID:AB_2561016
aTubulin (DM1A) Abcam Cat# ab7291, RRID:AB_2241126
b-Tubulin Abcam Cat# Ab6046, RRID:AB_2210370
GAPDH CST Cat# 2118, RRID:AB_561053
HRP (Horseradish peroxidase) anti-rabbit CST Cat# 7074, RRID:AB_2099233
HRP anti-mouse GE Healthcare Cat# NA931, RRID:AB_772210
Rabbit (DA1E) Isotype Control CST Cat# 3900, RRID:AB_1550038
Critical Commercial Assays
High-Capacity cDNA Reverse Transcription Kit Thermo Fisher 4368814
RNeasy mini kit Qiagen 74104
Experimental Models: Cell Lines
Oligonucleotides for qPCR
Primer Species/Assay Sequence
GAPDH_FWD Human qPCR GGTGGTCTCCTCTGACTTCAACA
GAPDH_REV Human qPCR GTTGCTGTAGCCAAATTCGTTGT
NOTCH1 3’UTR F Human qPCR CCCTGCCCGTTCTTGAAATG
NOTCH1 3’UTR R Human qPCR GGGTAGGATGCCTCCGTGTG
NOTCH1 EXON1 F Human qPCR GCGCAGCGAAGGAACGAG
NOTCH1 EXON1 R Human qPCR GACGGTCCCGCCCTCTCT
SEC16A_F Human qPCR CCTTACAGGAGACGGGCTAAT
SEC16A_R Human qPCR GTGGACTGCTTTTGGACGAAC
C9ORF163_F Human qPCR TTTGAACAGAGTTAGGGAGCACG
C9ORF163_R Human qPCR CCTGGCTCTTGGGTTCTTTGA
GLI1 FWD Human qPCR AGCGTGAGCCTGAATCTGTG
GLI1 REV Human qPCR CAGCATGTACTGGGCTTTGAA
SOX7 FWD Human qPCR AGCCGGAGCAGACCTTCTT
SOX7 REV Human qPCR GCCGGGGAGTAATAGGCAG
HDAC4 FWD Human qPCR GGCCCACCGGAATCTGAAC
HDAC4 REV Human qPCR GAACTCTGGTCAAGGGAACTG
PTCHD1_FWD Human qPCR AGCACCGTCTCTACTCGGAC
PTCHD1_REV Human qPCR GAACCTGGATCTTGGTGACAG
PDGFA FWD Human qPCR GCAAGACCAGGACGGTCATTT
PDGFA REV Human qPCR GGCACTTGACACTGCTCGT
HEY1 FWD Human qPCR CGAGGTGGAGAAGGAGAGTG
HEY1 REV Human qPCR CTGGGTACCAGCCTTCTCAG
RBPJ_FWD Human qPCR AAGGAGCCCCACGAGAAAAAT
RBPJ_REV Human qPCR ACCGAACTTGCATTGATTCCAG
TCF7L1 FWD Human qPCR TCGTCCCTGGTCAACGAGT
TCF7L1 REV Human qPCR ACTTCGGCGAAATAGTCCCG
GLI3 FWD Human qPCR GAAGTGCTCCACTCGAACAGA
GLI3 REV Human qPCR GTGGCTGCATAGTGATTGCG
JDP2 FWD Human qPCR TGGAGGAGCTGAAATACGCT
JDP2 REV Human qPCR CCTTTTCCTTCGCTCCTCTT
1 MEF2C F Human qPCR CCAAGGACTAATCTGATCGGG
2 MEF2C R Human qPCR TTTCCTGTTTCCTCCAAACAA
NOTCH1 F Human qPCR CACTGTGGGCGGGTCC
NOTCH1 R Human qPCR GTTGTATTGGTTCGGCACCAT
NOTCH3 F Human qPCR TGGCGACCTCACTTACGACT
NOTCH3 R Human qPCR CACTGGCAGTTATAGGTGTTGAC
RUNX1 F Human qPCR CCACTCCACTGCCTTTAACC
RUNX1 R Human qPCR CTGGGTGCACAGAAGGAGAG
SNAI2 F Human qPCR CAGACCCTGGTTGCTTCAA


(Continued)


-----

TABLE 1 (Continued).

REAGENT/RESOURCE SOURCE IDENTIFIER

SNAI2 R Human qPCR TGACCTGTCTGCAAATGCTC
SOX9a F Human qPCR GACGCTGGGCAAGCTCT
SOX9a R Human qPCR GTAATCCGGGTGGTCCTTCT
shRNA
siSlug3 shSNAI2.2 Addgene #10905
psPAX2 Addgene #12260
pMD2.G Addgene #12259
Crispr gRNA
gRNA gRNA location gRNA sequence
N1TAD g1 F NOTCH1 TAD ACAGGATAATAGCAGTGTCG
N1TAD g1 R NOTCH1 TAD CGGACCCGTTGTATCGTTCT
N1TADExt-Neg Ctl-F Neg Ctl CACCATAAGGCGTGGAAGACGGGC
N1TADExt-Neg Ctl-R Neg Ctl AAACGCCCGTCTTCCACGCCTTAT
Genomic PCR/Heteroduplex assay
NOTCH1-Gen-F1 AAGTGGCCCAACAACCCCCTTC
NOTCH1-Gen-R1 TCAGGAGTTCCACACCAGCCTGG
NOTCH1_NC_Gen_F2 CTCTTTCAGCCCTTCACAGC
NOTCH1_NC_Gen_R2 GGGGGAACGAACCGAGTAG
hU6 GAGGGCCTATTTCCCATGATT
ChIP primers
NOTCH1_TAD_Chip_F4 TTGAGCCCCAGCTTCCTCAT
NOTCH1_TAD_Chip_R4 GGCAAGCGTGCACCTGTTAC
NEG_CTL_NIH_FWD AGGGAGTTTTTATGAGCATTCCA
NEG_CTL_NIH_REV AGCAGGTAAAGGTCCATATTTCA
Deposited Data
SNAI2 ChIP-seq RD, SMS-CTR, JR1 GEO GSE137168
MYOD ChIP-seq RD, SMS-CTR, JR1 GEO GSE137168
H3K27ac ChIP-seq RD, SMS-CTR, JR1 GEO GSE137168
RNA-seq RD, SMS-CTR, JR1 GEO GSE137168
Software and Algorithms
MACS2 47 [https://github.com/taoliu/MACS](https://github.com/taoliu/MACS)
Samtools 48 [http://samtools.sourceforge.net/](http://samtools.sourceforge.net/)
Homer 49 [http://homer.ucsd.edu/homer/](http://homer.ucsd.edu/homer/)
Bedtools 50 [https://github.com/arq5x/bedtools2](https://github.com/arq5x/bedtools2)
EDEN 51
Tophat 52 [https://github.com/infphilo/tophat](https://github.com/infphilo/tophat)
BWA 53 [http://bio-bwa.sourceforge.net/](http://bio)
FastQC N/A [http://www.bioinformatics.babraham.ac.uk/projects/fastqc](http://www.bioinformatics.babraham.ac.uk/projects/fastqc)
STAR 54 [https://github.com/alexdobin/STAR](https://github.com/alexdobin/STAR)
Gene Set Enrichment Analysis (GSEA) 55 [http://software.broadinstitute.org/cancer/software/genepattern/](http://software.broadinstitute.org/cancer/software/genepattern/)
IGV 56 [https://software.broadinstitute.org/software/igv/](https://software.broadinstitute.org/software/igv/)
GraphPad Prism7 N/A [https://www.graphpad.com/](https://www.graphpad.com/)
R studio v3.5.1 N/A [https://www.rstudio.com/products/rstudio/](https://www.rstudio.com/products/rstudio/)

Rhabdomyosarcoma cells were infected with viral particles for 24 h at 37 [�]C with 4 mg/mL of Protamine
(EMD Millipore). Cell viability and growth was monitored by Incucyte in three biological replicates. List
of shRNA and gRNA sequence is listed in Table 1.
Gene expression. RNA isolation was performed using Qiagen RNA easy kit and cDNA was prepared
using a High Capacity cDNA synthesis Kit (ThermoFisher #4368814), followed by quantitative PCR in ABI
QuantStudio6 Real-time PCR system. List of PCR primers used in this study is listed in Table 1. Fold
change gene expression in treatment sample compared to control was calculated by [DD]ct method.
Statistical significance in three independent biological replicates was calculated by Student’s two-tailed
t test.
Western blotting. Total cell lysate was obtained by lysing in 1� RIPA buffer (Millipore) supplemented
with protease inhibitors (Roche) and MG213 (Calbiochem). Membranes (PVDF, BioRad) were developed
using ECL reagent (Immobilon, Millipore). Internal control and target antibodies were performed on different regions of the same blot and imaged (Li-Cor). Antibodies used in the study is listed in Table 1.
Immunofluorescence staining. Cells in maintained in three days with differentiation medium were
fixed in 4% (PFA)/PBS, permeabilized in 0.5% Triton X-100/PBS, and probed with rabbit a-MEF2C (CST,
5030) and a-myosin heavy chain (DSHB, MF20/MyHC) in 2% FBS/PBS. Secondary antibodies used were
Alexa-488 goat a-mouse and Alexa-563 goat a-rabbit (Invitrogen) and DAPI. Imaging was performed


-----

using the Olympus confocal microscope FV3000 with Olympus FV315S-SW image acquisition software.
Images were processed in ImageJ and Adobe Photoshop.
Colony formation assay. After 72 h of selection a total of 10 � 10[2] Ctl and N1TAD KO cells were
seeded in six-well plates with 2 mL of DMEM (10% FBS). Medium was refreshed every 2 days, and after
14 days, cells were fixed and stained with Crystal Violet in 50% methanol. Colonies containing > 50 cells
were counted. Triplicate assays were carried out in three independent experiments.
Sphere formation assay. RD or SMS-CTR cells were serially diluted in 100 mL Neuro Basal Medium
(NBM).[9] The diluted cells were gently added to 1 mL of pre-warmed NBM per well of a 24-well plate
(Corning Cat #3603). The cells were incubated for at least 15–20 days with 100 mL of fresh media added
every two days. The spheres were counted manually or using the Celigo Imaging Cytometer automated
cell counting apparatus (Nexcelom Bioscience LLC, Lawrence, MA).

RNA-seq, ChIP-seq & Hi-C. The RNA-seq and ChIP-seq data used in this article was generated previously in our lab and is described in Pomella et al., 2021[10] (GEO accession GSE137168). Previously published ChIP-seq data used were from the following GEO accessions GSE61475, GSE55421 & GSE131687.
Hi-C maps of IMR90 and GM12878 were from Rao et al., 2014[20] (visualized by Juicebox). Hi-C maps of
RD, SMS-CTR, Rh30 and RH4 is published data generated in collaboration with Dr Benjamin Stanton Lab
at NCH, Ohio.
HiChIP. SMS-CTR cells were fixed with DSG for 10 min at room temperature (23 [�]C), then 1% formaldehyde for 12 min at room temperature. Cells (�8 million) were then lysed gently to release nuclei, permeabilized in 0.5% SDS for 10 min at 62 [�]C, quenched with 10% Triton X-100, and digested with Dpnii
(400 U, overnight at 37 [�]C) which was then heat inactivated (20 min, 62 [�]C). Biotin incorporation was
done with biotin-14-dATP (Thermo, Cat #19524-016) and DNA Polymerase I, Large (Klenow) Fragment
(NEB, Cat #M0210) for 1 h at 37 [�]C. Then, we performed in situ ligation with T4 DNA ligase (2 h room temperature and 16 [�]C overnight). Nuclei were pelleted and sonicated (28 cycles with shearing “on” time
with 30 seconds “‘on” 30 s off, using the Active Motif Epi-shear probe sonicator, 30% power). Lysates
were immunoprecipitated with anti-CTCF (CST, Cat #2899), overnight incubation (rotating at 4 [�]C), then
bound to Dynabeads Protein A (Thermo, Cat #10002D) and incubated (2 h at 4 [�]C). Dynabeads were
then held magnetically, washed, eluted, and treated with Proteinase K (30 min at 55 [�]C); crosslinks were
reversed by heating to 67 [�]C for 2 h. DNA was purified using ChIP DNA Clean and Concentrator kit
(Zymo Cat #D5205). Biotin capture and washing was done with Dynabeads M-280 Streptavidin (Thermo,
Cat #11205D), followed by end repair, A-tailing, adapter ligation and library amplification all on-bead as
previously reported.[44] Libraries were paired-end sequenced to a shallow depth of 80–120 million reads
to generate contact maps with 30 million valid, long-range cis contacts. Analysis was performed using
HiC-Pro[45] and visualized in Juicebox.[46]

Quantification and statistical analysis. The significance of results was assessed by applicable statistical tests for each experiment described. Except where stated, all experiments were performed at least
in three biological replicates. Student’s two-tailed t test was used for testing significance of qRT-PCR,
sphere assays, and colony assay. P values were reported on the related figures or in the text.
Representative imaging data from three biological replicates was used to quantify immunofluorescence
staining data, and significance was assessed by Student’s two-tailed t test, with P-values reported on the
related figures or in the text. Statistical analysis of NGS data is described in Pomella et al., 2021.[10]

Software used for statistical tests include R, GraphPad Prism and Microsoft Excel.

ACKNOWLEDGEMENTS

M.S.I., P.S., and A.C. designed the experiments, P.S., L.W., M.P., N.R.H., B.S., X.Z., and
R.M. carried out the experiments, P.M., and N.R.H. performed the irradiation experiment
and analysis, B.G., H.C., B.Z.S., and J.K. analyzed the HiChIP data, M.W., B.S., and B.Z.S.
analyzed the R.M.S. HiC data, X.Z., and R.M. validated SNAI2 KO cells. P.S., M.S.I., N.R.H.,
and P.M., wrote the manuscript with help from J.K. and B.Z.S. This project has been
funded with federal funds from NIH grants (R00CA175184 to M.S. Ignatius) and CPRIT
Scholar grant (RR160062 to M.S. Ignatius). M.S. Ignatius is a recipient of the Max and
Minnie Tomerlin Voelcker Fund Young Investigator Award. N.R. Hensch has been supported by the Cancer Prevention and Research Institute of Texas (CPRIT) Research
Training Award (RP 170345) and the Greehey Graduate Fellowship in Children’s Health.

ORCID

Prethish Sreenivas http://orcid.org/0000-0002-1260-4464
Myron S. Ignatius http://orcid.org/0000-0001-6639-7707

DATA AVAILABILITY STATEMENT

The datasets used in this study are available at GEO (Gene Expression Omnibus) with
the accession number (GSE137168, [https://www.ncbi.nlm.nih.gov/geo/query/acc.](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE137168)
[cgi?acc=GSE137168). A source data file accompanies this manuscript. The remaining](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE137168)
d t il bl ithi th ti l il bl f th th t


-----

DISCLOSURE STATEMENT

No potential conflict of interest was reported by the authors.

REFERENCES

1. Chen X, Stewart E, Shelat AA, Qu C, Bahrami A, Hatley M, Wu G, Bradley C,
McEvoy J, Pappo A, et al. Targeting oxidative stress in embryonal rhabdo[myosarcoma. Cancer Cell. 2013;24:710–724. doi:10.1016/j.ccr.2013.11.](https://doi.org/10.1016/j.ccr.2013.11.002)
[002.](https://doi.org/10.1016/j.ccr.2013.11.002)
2. Seki M, Nishimura R, Yoshida K, Shimamura T, Shiraishi Y, Sato Y, Kato M,
Chiba K, Tanaka H, Hoshino N, et al. Integrated genetic and epigenetic
analysis defines novel molecular subgroups in rhabdomyosarcoma. Nat
[Commun. 2015;6:7557. doi:10.1038/ncomms8557.](https://doi.org/10.1038/ncomms8557)
3. Shern JF, Chen L, Chmielecki J, Wei JS, Patidar R, Rosenberg M, Ambrogio
L, Auclair D, Wang J, Song YK, et al. Comprehensive genomic analysis of
rhabdomyosarcoma reveals a landscape of alterations affecting a common genetic axis in fusion-positive and fusion-negative tumors. Cancer
[Discov. 2014;4:216–231. doi:10.1158/2159-8290.CD-13-0639.](https://doi.org/10.1158/2159-8290.CD-13-0639)
4. Yohe ME, Heske CM, Stewart E, Adamson PC, Ahmed N, Antonescu CR,
Chen E, Collins N, Ehrlich A, Galindo RL, et al. Insights into pediatric
rhabdomyosarcoma research: Challenges and goals. Pediatr Blood
[Cancer. 2019;66:e27869. doi:10.1002/pbc.27869.](https://doi.org/10.1002/pbc.27869)
5. Kashi VP, Hatley ME, Galindo RL. Probing for a deeper understanding of
rhabdomyosarcoma: insights from complementary model systems. Nat
[Rev Cancer. 2015;15:426–439. doi:10.1038/nrc3961.](https://doi.org/10.1038/nrc3961)
6. Skapek SX, Ferrari A, Gupta AA, Lupo PJ, Butler E, Shipley J, Barr FG,
[Hawkins DS. Rhabdomyosarcoma. Nat Rev Dis Primers. 2019;5:1. doi:10.](https://doi.org/10.1038/s41572-018-0051-2)
[1038/s41572-018-0051-2.](https://doi.org/10.1038/s41572-018-0051-2)
7. Langdon CG, Gadek KE, Garcia MR, Evans MK, Reed KB, Bush M, Hanna JA,
Drummond CJ, Maguire MC, Leavey PJ, et al. Synthetic essentiality
between PTEN and core dependency factor PAX7 dictates rhabdomyosar[coma identity. Nat Commun. 2021;12:5520. doi:10.1038/s41467-021-](https://doi.org/10.1038/s41467-021-25829-4)
[25829-4.](https://doi.org/10.1038/s41467-021-25829-4)
8. Tenente IM, Hayes MN, Ignatius MS, McCarthy K, Yohe M, Sindiri S, Gryder
B, Oliveira ML, Ramakrishnan A, Tang Q, et al. Myogenic regulatory transcription factors regulate growth in rhabdomyosarcoma. Elife. 2017;6:
[doi:10.7554/eLife.19214.](https://doi.org/10.7554/eLife.19214)
9. Ignatius MS, Hayes MN, Lobbardi R, Chen EY, McCarthy KM, Sreenivas P,
Motala Z, Durbin AD, Molodtsov A, Reeder S, et al. The
NOTCH1/SNAIL1/MEF2C pathway regulates growth and self-renewal in
[embryonal rhabdomyosarcoma. Cell Rep. 2017;19:2304–2318. doi:10.](https://doi.org/10.1016/j.celrep.2017.05.061)
[1016/j.celrep.2017.05.061.](https://doi.org/10.1016/j.celrep.2017.05.061)
10. Pomella S, Sreenivas P, Gryder BE, Wang L, Milewski D, Cassandri M, Baxi
K, Hensch NR, Carcarino E, Song Y, et al. Interaction between SNAI2 and
MYOD enhances oncogenesis and suppresses differentiation in fusion
[negative rhabdomyosarcoma. Nat Commun. 2021;12:192. doi:10.1038/](https://doi.org/10.1038/s41467-020-20386-8)
[s41467-020-20386-8.](https://doi.org/10.1038/s41467-020-20386-8)
11. Wang L, Hensch NR, Bondra K, Sreenivas P, Zhao XR, Chen J, Moreno
Campos R, Baxi K, Vaseva AV, Sunkel BD, et al. SNAI2-mediated repression
of BIM protects rhabdomyosarcoma from ionizing radiation. Cancer Res.
[2021;81:5451–5463. doi:10.1158/0008-5472.CAN-20-4191.](https://doi.org/10.1158/0008-5472.CAN-20-4191)
12. Chen Y, Gridley T. Compensatory regulation of the Snai1 and Snai2 genes
[during chondrogenesis. J Bone Miner Res. 2013;28:1412–1421. doi:10.](https://doi.org/10.1002/jbmr.1871)
[1002/jbmr.1871.](https://doi.org/10.1002/jbmr.1871)
13. Sakai D, Suzuki T, Osumi N, Wakamatsu Y. Cooperative action of Sox9,
Snail2 and PKA signaling in early neural crest development.
[Development. 2006;133:1323–1333. doi:10.1242/dev.02297.](https://doi.org/10.1242/dev.02297)
14. Zhou W, Gross KM, Kuperwasser C. Molecular regulation of Snai2 in devel[opment and disease. J Cell Sci. 2019;132: doi:10.1242/jcs.235127.](https://doi.org/10.1242/jcs.235127)
15. Lehmann W, Mossmann D, Kleemann J, Mock K, Meisinger C, Brummer T,
Herr R, Brabletz S, Stemmler MP, Brabletz T, et al. ZEB1 turns into a transcriptional activator by interacting with YAP1 in aggressive cancer types.
[Nat Commun. 2016;7:10498. doi:10.1038/ncomms10498.](https://doi.org/10.1038/ncomms10498)
16. Hinson ARP, Jones R, Crose LES, Belyea BC, Barr FG, Linardic CM. Human
rhabdomyosarcoma cell lines for rhabdomyosarcoma research: utility
[and pitfalls. Front Oncol. 2013;3:183. doi:10.3389/fonc.2013.00183.](https://doi.org/10.3389/fonc.2013.00183)
17. Consortium EP. An integrated encyclopedia of DNA elements in the
[human genome. Nature. 2012;489:57–74. doi:10.1038/nature11247.](https://doi.org/10.1038/nature11247)
18. Hnisz D, Weintraub AS, Day DS, Valton A-L, Bak RO, Li CH, Goldmann J,
Lajoie BR, Fan ZP, Sigova AA, et al. Activation of proto-oncogenes by disruption of chromosome neighborhoods. Science. 2016;351:1454–1458.
[doi:10 1126/science aad9024](https://doi.org/10.1126/science.aad9024)


19. Tate JG, Bamford S, Jubb HC, Sondka Z, Beare DM, Bindal N, Boutselakis H,
Cole CG, Creatore C, Dawson E, et al. COSMIC: the catalogue of somatic
[mutations in cancer. Nucleic Acids Res. 2019;47:D941–D947. doi:10.1093/](https://doi.org/10.1093/nar/gky1015)
[nar/gky1015.](https://doi.org/10.1093/nar/gky1015)
20. Rao SSP, Huntley MH, Durand NC, Stamenova EK, Bochkov ID, Robinson
JT, Sanborn AL, Machol I, Omer AD, Lander ES, et al. A 3D map of the
human genome at kilobase resolution reveals principles of chromatin
[looping. Cell. 2014;159:1665–1680. doi:10.1016/j.cell.2014.11.021.](https://doi.org/10.1016/j.cell.2014.11.021)
21. Wang M, Sreenivas P, Sunkel BD, Wang L, Ignatius M, Stanton BZ. The 3D
chromatin landscape of rhabdomyosarcoma. NAR Cancer. 2023;5:
[zcad028. doi:10.1093/narcan/zcad028.](https://doi.org/10.1093/narcan/zcad028)
22. Conboy IM, Conboy MJ, Smythe GM, Rando TA. Notch-mediated restoration of regenerative potential to aged muscle. Science. 2003;302:1575–
[1577. 302/5650/1575. doi:10.1126/science.1087573.](https://doi.org/10.1126/science.1087573)
23. Conboy IM, Rando TA. The regulation of Notch signaling controls satellite
cell activation and cell fate determination in postnatal myogenesis. Dev
[Cell. 2002;3:397–409. doi:10.1016/s1534-5807(02)00254-x.](https://doi.org/10.1016/s1534-5807(02)00254-x)
24. Kuang S, Kuroda K, Le Grand F, Rudnicki MA. Asymmetric self-renewal
and commitment of satellite stem cells in muscle. Cell. 2007;129:999–
[1010. doi:10.1016/j.cell.2007.03.044.](https://doi.org/10.1016/j.cell.2007.03.044)
25. Jarriault S, Brou C, Logeat F, Schroeter EH, Kopan R, Israel A. Signalling
downstream of activated mammalian Notch. Nature. 1995;377:355–358.
[doi:10.1038/377355a0.](https://doi.org/10.1038/377355a0)
26. Bonev B, Mendelson Cohen N, Szabo Q, Fritsch L, Papadopoulos GL,
Lubling Y, Xu X, Lv X, Hugnot J-P, Tanay A, et al. Multiscale 3D genome
rewiring during mouse neural development. Cell. 2017;171:557–572. doi:
[10.1016/j.cell.2017.09.043.](https://doi.org/10.1016/j.cell.2017.09.043)
27. Nora EP, Goloborodko A, Valton A-L, Gibcus JH, Uebersohn A, Abdennur
N, Dekker J, Mirny LA, Bruneau BG. Targeted degradation of CTCF decouples local insulation of chromosome domains from genomic compart[mentalization. Cell. 2017;169:930–944. doi:10.1016/j.cell.2017.05.004.](https://doi.org/10.1016/j.cell.2017.05.004)
28. Splinter E, Heath H, Kooren J, Palstra R-J, Klous P, Grosveld F, Galjart N, de
Laat W. CTCF mediates long-range chromatin looping and local histone
modification in the beta-globin locus. Genes Dev. 2006;20:2349–2354.
[doi:10.1101/gad.399506.](https://doi.org/10.1101/gad.399506)
29. Weintraub AS, Li CH, Zamudio AV, Sigova AA, Hannett NM, Day DS,
Abraham BJ, Cohen MA, Nabet B, Buckley DL, et al. YY1 is a structural
[regulator of enhancer-promoter loops. Cell. 2017;171:1573–1588. doi:10.](https://doi.org/10.1016/j.cell.2017.11.008)
[1016/j.cell.2017.11.008.](https://doi.org/10.1016/j.cell.2017.11.008)
30. Bray SJ. Notch signalling in context. Nat Rev Mol Cell Biol. 2016;17:722–
[735. doi:10.1038/nrm.2016.94.](https://doi.org/10.1038/nrm.2016.94)
31. Siebel C, Lendahl U. Notch signaling in development, tissue homeostasis,
[and disease. Physiol Rev. 2017;97:1235–1294. doi:10.1152/physrev.00005.](https://doi.org/10.1152/physrev.00005.2017)
[2017.](https://doi.org/10.1152/physrev.00005.2017)
32. Conboy IM, Conboy MJ, Wagers AJ, Girma ER, Weissman IL, Rando TA.
Rejuvenation of aged progenitor cells by exposure to a young systemic
[environment. Nature. 2005;433:760–764. doi:10.1038/nature03260.](https://doi.org/10.1038/nature03260)
33. Belyea BC, Naini S, Bentley RC, Linardic CM. Inhibition of the Notch-Hey1
axis blocks embryonal rhabdomyosarcoma tumorigenesis. Clin Cancer
[Res. 2011;17:7324–7336. doi:10.1158/1078-0432.CCR-11-1004.](https://doi.org/10.1158/1078-0432.CCR-11-1004)
34. Rota R, Ciarapica R, Miele L, Locatelli F. Notch signaling in pediatric soft
[tissue sarcomas. BMC Med. 2012;10:141. doi:10.1186/1741-7015-10-141.](https://doi.org/10.1186/1741-7015-10-141)
35. Slemmons KK, Crose LES, Riedel S, Sushnitha M, Belyea B, Linardic CM. A
novel notch-YAP circuit drives stemness and tumorigenesis in embryonal
[rhabdomyosarcoma. Mol Cancer Res. 2017;15:1777–1791. doi:10.1158/](https://doi.org/10.1158/1541-7786.MCR-17-0004)
[1541-7786.MCR-17-0004.](https://doi.org/10.1158/1541-7786.MCR-17-0004)
36. Kovach AR, Oristian KM, Kirsch DG, Bentley RC, Cheng C, Chen X, Chen PH, Chi J-TA, Linardic CM. Identification and targeting of a HES1-YAP1CDKN1C functional interaction in fusion-negative rhabdomyosarcoma.
[Mol Oncol. 2022;16:3587–3605. doi:10.1002/1878-0261.13304.](https://doi.org/10.1002/1878-0261.13304)
37. Raimondi L, Ciarapica R, De Salvo M, Verginelli F, Gueguen M, Martini C,
De Sio L, Cortese G, Locatelli M, Dang TP, et al. Inhibition of Notch3 signalling induces rhabdomyosarcoma cell differentiation promoting p38 phosphorylation and p21(Cip1) expression and hampers tumour cell growth
[in vitro and in vivo. Cell Death Differ. 2012;19:871–881. doi:10.1038/cdd.](https://doi.org/10.1038/cdd.2011.171)
[2011 171](https://doi.org/10.1038/cdd.2011.171)


-----

38. De Salvo M, Raimondi L, Vella S, Adesso L, Ciarapica R, Verginelli F,
Pannuti A, Citti A, Boldrini R, Milano GM, et al. Hyper-activation of Notch3
amplifies the proliferative potential of rhabdomyosarcoma cells. PloS
[One. 2014;9:e96238. doi:10.1371/journal.pone.0096238.](https://doi.org/10.1371/journal.pone.0096238)
39. Soleimani VD, Yin H, Jahani-Asl A, Ming H, Kockx CEM, van Ijcken WFJ,
Grosveld F, Rudnicki MA. Snail regulates MyoD binding-site occupancy to
direct enhancer switching and differentiation-specific transcription in
[myogenesis. Mol Cell. 2012;47:457–468. doi:10.1016/j.molcel.2012.05.046.](https://doi.org/10.1016/j.molcel.2012.05.046)
40. Nieto MA, Huang RY, Jackson RA, Thiery JP. Emt: 2016. Cell. 2016;166:21–
[45. doi:10.1016/j.cell.2016.06.028.](https://doi.org/10.1016/j.cell.2016.06.028)
41. Tsankov AM, Gu H, Akopian V, Ziller MJ, Donaghey J, Amit I, Gnirke A,
Meissner A. Transcription factor binding dynamics during human ES cell
[differentiation. Nature. 2015;518:344–349. doi:10.1038/nature14233.](https://doi.org/10.1038/nature14233)
42. Mistry DS, Chen Y, Wang Y, Zhang K, Sen GL. SNAI2 controls the undifferentiated state of human epidermal progenitor cells. Stem Cells. 2014;32:
[3209–3218. doi:10.1002/stem.1809.](https://doi.org/10.1002/stem.1809)
43. Kurppa KJ, Liu Y, To C, Zhang T, Fan M, Vajdi A, Knelson EH, Xie Y, Lim K,
Cejas P, et al. Treatment-induced tumor dormancy through YAP-mediated transcriptional reprogramming of the apoptotic pathway. Cancer
[Cell. 2020;37:104–122 e112. doi:10.1016/j.ccell.2019.12.006.](https://doi.org/10.1016/j.ccell.2019.12.006)
44. Gryder BE, Khan J, Stanton BZ. Measurement of differential chromatin
interactions with absolute quantification of architecture (AquA-HiChIP).
[Nat Protoc. 2020;15:1209–1236. doi:10.1038/s41596-019-0285-9.](https://doi.org/10.1038/s41596-019-0285-9)
45. Servant N, Varoquaux N, Lajoie BR, Viara E, Chen C-J, Vert J-P, Heard E,
Dekker J, Barillot E. HiC-Pro: an optimized and flexible pipeline for Hi-C data
[processing. Genome Biol. 2015;16:259. doi:10.1186/s13059-015-0831-x.](https://doi.org/10.1186/s13059-015-0831-x)
46. Durand NC, Robinson JT, Shamim MS, Machol I, Mesirov JP, Lander
ES, Aiden EL. Juicebox provides a visualization system for Hi-C con[tact maps with unlimited zoom. Cell Syst. 2016;3:99–101. doi:10.1016/](https://doi.org/10.1016/j.cels.2015.07.012)
[j.cels.2015.07.012.](https://doi.org/10.1016/j.cels.2015.07.012)
47. Zhang Y, Liu T, Meyer CA, Eeckhoute J, Johnson DS, Bernstein BE, Nusbaum
C, Myers RM, Brown M, Li W, et al. Model-based analysis of ChIP-Seq
[(MACS). Genome Biol. 2008;9:R137. doi:10.1186/gb-2008-9-9-r137.](https://doi.org/10.1186/gb-2008-9-9-r137)


48. Li H, Handsaker B, Wysoker A, Fennell T, Ruan J, Homer N, Marth G,
Abecasis G, Durbin R, 1000 Genome Project Data Processing Subgroup.
The sequence alignment/map format and SAMtools. Bioinformatics.
[2009;25:2078–2079. doi:10.1093/bioinformatics/btp352.](https://doi.org/10.1093/bioinformatics/btp352)
49. Heinz S, Benner C, Spann N, Bertolino E, Lin YC, Laslo P, Cheng JX, Murre
C, Singh H, Glass CK. Simple combinations of lineage-determining transcription factors prime cis-regulatory elements required for macrophage
[and B cell identities. Mol Cell. 2010;38:576–589. doi:10.1016/j.molcel.](https://doi.org/10.1016/j.molcel.2010.05.004)
[2010.05.004.](https://doi.org/10.1016/j.molcel.2010.05.004)
50. Quinlan AR, Hall IM. BEDTools: a flexible suite of utilities for comparing
[genomic features. Bioinformatics. 2010;26:841–842. doi:10.1093/bioinfor-](https://doi.org/10.1093/bioinformatics/btq033)
[matics/btq033.](https://doi.org/10.1093/bioinformatics/btq033)
51. Gryder BE, Yohe ME, Chou HC, Zhang X, Marques J, Wachtel M, Schaefer
B, Sen N, Song Y, Gualtieri A, et al. PAX3-FOXO1 establishes myogenic
super enhancers and confers BET bromodomain vulnerability. Cancer
[Discov. 2017;7:884–899. doi:10.1158/2159-8290.CD-16-1297.](https://doi.org/10.1158/2159-8290.CD-16-1297)
52. Trapnell C, Pachter L, Salzberg SL. TopHat: discovering splice junctions
[with RNA-Seq. Bioinformatics. 2009;25:1105–1111. doi:10.1093/bioinfor-](https://doi.org/10.1093/bioinformatics/btp120)
[matics/btp120.](https://doi.org/10.1093/bioinformatics/btp120)
53. Li H, Durbin R. Fast and accurate short read alignment with Burrows–
[Wheeler transform. Bioinformatics. 2009;25:1754–1760. doi:10.1093/bio-](https://doi.org/10.1093/bioinformatics/btp324)
[informatics/btp324.](https://doi.org/10.1093/bioinformatics/btp324)
54. Dobin A, Davis CA, Schlesinger F, Drenkow J, Zaleski C, Jha S, Batut P,
Chaisson M, Gingeras TR. STAR: ultrafast universal RNA-seq aligner.
[Bioinformatics. 2013;29:15–21. doi:10.1093/bioinformatics/bts635.](https://doi.org/10.1093/bioinformatics/bts635)
55. Subramanian A, Tamayo P, Mootha VK, Mukherjee S, Ebert BL, Gillette
MA, Paulovich A, Pomeroy SL, Golub TR, Lander ES, et al. Gene set enrichment analysis: a knowledge-based approach for interpreting genomewide expression profiles. Proc Natl Acad Sci USA. 2005;102:15545–15550.
[doi:10.1073/pnas.0506580102.](https://doi.org/10.1073/pnas.0506580102)
56. Robinson JT, Thorvaldsdottir H, Winckler W, Guttman M, Lander ES, Getz�
G, Mesirov JP. Integrative genomics viewer. Nat Biotechnol. 2011;29:24–
[26. doi:10.1038/nbt.1754.](https://doi.org/10.1038/nbt.1754)


-----

