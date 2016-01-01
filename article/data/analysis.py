import pandas as pd
import sys
import math
from fractions import gcd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import itertools as it

filename = "tm.csv"

data = pd.read_csv(filename, quotechar='"', skipinitialspace=True)

data_classification = data[data["Rejet"].isnull()]
data_reject = data[data["Rejet"].notnull()]


print "======================================================"
print "Accepted for classification:\t" + str(len(data_classification))
print "Rejected before classification:\t" + str(len(data_reject))
print "======================================================"
data = data_classification
print "== Yearly distribution ==============================="
for y in xrange(2000,2016):
    print str(y) + ":\t\t" + str(len(data[data["Date publication"] == y]))
print ""
print "== Detection strategy ================================"
print "Ai:\t\t"        + str(len(data[data["Ds-ai"].notnull()]))
print "Logic:\t\t"     + str(len(data[data["Ds-logic"].notnull()]))
print "Graph:\t\t"     + str(len(data[data["Ds-graph"].notnull()]))
print "Metric:\t\t"    + str(len(data[data["Ds-metric"].notnull()]))
print "Automata:\t"  + str(len(data[data["Ds-automaton"].notnull()]))
print "Profiling:\t" + str(len(data[data["Ds-prof"].notnull()]))
print "Matching:\t"  + str(len(data[data["Ds-matching"].notnull()]))
print "Others:\t\t"    + str(len(data[data["Ds-other"].notnull()]))
print ""
print "== Language Dependance ==============================="
print "Dependant:\t"    + str(len(data[data["Lg-dependant"].notnull()]))
print "Independant:\t"  + str(len(data[data["Lg-independant"].notnull()]))
print ""
print "== Analysis Type ====================================="
print "Static:\t\t"   + str(len(data[data["At-static"].notnull()]))
print "Dynamic:\t"  + str(len(data[data["At-dynamic"].notnull()]))
print "Hybrid:\t\t"   + str(len(data[data["At-hybrid"].notnull()]))
print ""
print "== Detection Level ==================================="
print "Exec:\t\t"   + str(len(data[data["Dl-exec"].notnull()]))
print "Source:\t\t" + str(len(data[data["Dl-source"].notnull()]))
print "Model:\t\t"  + str(len(data[data["Dl-model"].notnull()]))
print ""
print "== Detection generality =============================="
print "Generic:\t"  + str(len(data[data["Dp-generic"].notnull()]))
print "Specific:\t"  + str(len(data[data["Dg-specific"].notnull()]))
print ""
print "== Detected pattern types ============================"
print "Creationnal:\t"  + str(len(data[data["Pt-creationnal"].notnull()]))
print "Behavioural:\t"  + str(len(data[data["Pt-behaviour"].notnull()]))
print "Structural:\t"   + str(len(data[data["Pt-structural"].notnull()]))
print "Other:\t\t"        + str(len(data[data["Pt-other"].notnull()]))
print ""
print "== Validation method ================================="
print "Benchmark:\t"   + str(len(data[data["Vm-benchmark"].notnull()]))
print "Case study:\t"  + str(len(data[data["Vm-casestudy"].notnull()]))
print "Experiment:\t"  + str(len(data[data["Vm-experiment"].notnull()]))
print "Survey:\t\t"      + str(len(data[data["Vm-survey"].notnull()]))
print "Other:\t\t"       + str(len(data[data["Vm-other"].notnull()]))
print "None:\t\t"        + str(len(data[data["Vm-none"].notnull()]))
print ""
print "== Analysis type / deteted pattern types"
print "\t\tStatic\tDynamic\tHybrid"
cs = len(data[data["Pt-creationnal"].notnull() & data["At-static"].notnull()])
cd = len(data[data["Pt-creationnal"].notnull() & data["At-dynamic"].notnull()])
ch = len(data[data["Pt-creationnal"].notnull() & data["At-hybrid"].notnull()])
bs = len(data[data["Pt-behaviour"].notnull() & data["At-static"].notnull()])
bd = len(data[data["Pt-behaviour"].notnull() & data["At-dynamic"].notnull()])
bh = len(data[data["Pt-behaviour"].notnull() & data["At-hybrid"].notnull()])
ss = len(data[data["Pt-structural"].notnull() & data["At-static"].notnull()])
sd = len(data[data["Pt-structural"].notnull() & data["At-dynamic"].notnull()])
sh = len(data[data["Pt-structural"].notnull() & data["At-hybrid"].notnull()])
os = len(data[data["Pt-other"].notnull() & data["At-static"].notnull()])
od = len(data[data["Pt-other"].notnull() & data["At-dynamic"].notnull()])
oh = len(data[data["Pt-other"].notnull() & data["At-hybrid"].notnull()])
print "Creationnal:\t" + str(cs) + "\t" + str(cd) + "\t" + str(ch)
print "Behavioural:\t" + str(bs) + "\t" + str(bd) + "\t" + str(bh)
print "Structural:\t"  + str(ss) + "\t" + str(sd) + "\t" + str(sh)
print "Other:\t\t"     + str(os) + "\t" +  str(od) + "\t" + str(oh)

#====================================================================
# Year hist
#====================================================================

plt.hist(data["Date publication"], facecolor="grey")
plt.title("Distribution of articles over the years")
plt.savefig("../img/year_distribution.png")

#====================================================================
# Pattern distribution
#====================================================================

fig = plt.figure(figsize=(8,2.5))
gs1 = GridSpec(1, 4)
p1 = fig.add_subplot(gs1[0])
p2 = fig.add_subplot(gs1[1])
p3 = fig.add_subplot(gs1[2])
p4 = fig.add_subplot(gs1[3])

p1.pie([ss, sd, sh], autopct='%1.1f%%', pctdistance=1.4, colors=["lightgrey", "grey", "darkgrey"])
p1.set_title("Structural")
p1.axis("equal")

p2.pie([bs, bd, bh], autopct='%1.1f%%', pctdistance=1.4,  colors=["lightgrey", "grey", "darkgrey"])
p2.set_title("Behavioural")
p2.axis("equal")

p3.pie([cs, cd, ch], autopct='%1.1f%%', pctdistance=1.4,  colors=["lightgrey", "grey", "darkgrey"])
p3.set_title("Creationnal")
p3.axis("equal")

gs1.tight_layout(fig)


p, _ , _=p4.pie([cs, cd, ch], autopct='%1.1f%%', colors=["lightgrey", "grey", "darkgrey"])

p4.axis("equal")
p4.set_visible(False)
lgd = fig.legend(p, ["Static", "Dynamic", "Hybrid"], loc="right")
fig.savefig("../img/analysis_v_pattern.png")
#plt.savefig("../img/creationnal.png", bbox_extra_artists=(lgd,), bbox_inches='tight')
