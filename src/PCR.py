from RandomDnaTemplate import RandomDna

segmentSize = 200
cycles = 1
dropOffRate = 0
primerSize = 20
dnaTemplateSize=2000

dna = RandomDna().randDna(dnaTemplateSize)
primer = RandomDna().randPrimer(dna, primerSize, segmentSize)
generatedDna = [dna]



p1 = dna[0].index(primer[0])-1
print " "*p1, "5'", primer[0],"3'"
print "5'",dna[0], "3'"

print "3'", dna[1], "5'"
p2 = dna[1].index(primer[1])-1
print " "*p2, "3'", primer[1],"5'"
segment = [dna[0][p1:p2+len(primer)],reverse(dna[1][p1:p2+len(primer)]]

for x in xrange(cycles):
  break
#for x in xrange(cycles):
  #for y in xrange(len(generatedDna)):
    #newCopy = pcrCycle(dna,segment)
    #generatedDna += newCopy
