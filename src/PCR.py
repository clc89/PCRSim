from RandomDnaTemplate import RandomDna

segmentSize = 200
cycles = 1
dropOffRate = 0
primerSize = 20
dnaTemplateSize=2000
segment=[0,0]
dna = RandomDna().randDna(dnaTemplateSize)
primer = RandomDna().randPrimer(dna, primerSize, segmentSize)
generatedDna = [dna]



p1 = dna[0].index(primer[0])-1
print " "*p1, "5'", primer[0],"3'"
print "5'",dna[0], "3'"

print "3'", dna[1], "5'"
p2 = dna[1].index(primer[1])-1
print " "*p2, "3'", primer[1],"5'"
segment[0] = dna[0][p1:p2+len(primer)]
segment[1] = dna[1][p1:p2+len(primer)]
print segment
for x in xrange(cycles):
  break
for x in xrange(cycles):
  #listLength=len(generatedDna)
  for y in xrange(2):
    toProcess=generatedDna(y)
    newCopy = RandomDna().pcrCycle(toProcess[0],toProcess[1],segment[0],segment[1])
    generatedDna += newCopy
print generatedDna