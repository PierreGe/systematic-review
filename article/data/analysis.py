import pandas as pd
import sys
import math
from fractions import gcd
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




