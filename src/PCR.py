from RandomDnaTemplate import RandomDna

segmentSize = 200
cycles = 5
dropOffRate = 50
primerSize = 20
dnaTemplateSize=2000
segment=[0,0]
dna = RandomDna().randDna(dnaTemplateSize)
primer = RandomDna().randPrimer(dna, primerSize, segmentSize)
generatedDna = [dna]
avgLength=0
avgGC=0

p1 = dna[0].index(primer[0])-1
print " "*p1, "5'", primer[0],"3'"
print "5'",dna[0], "3'"

print "3'", dna[1], "5'"
p2 = dna[1].index(primer[1])-1
print " "*p2, "3'", primer[1],"5'"
segment[0] = dna[0][p1:p2+len(primer)]
segment[1] = dna[1][p1:p2+len(primer)]
#print segment
for x in xrange(cycles):
  break
for x in xrange(cycles):
  listLength=len(generatedDna)
  for y in xrange(listLength):
    toProcess=generatedDna[y]
    newCopy = RandomDna().pcrCycle(toProcess[0],toProcess[1],segment[0],segment[1])
    generatedDna += newCopy
    generatedDna.remove(toProcess)
print "total DNA fragments:"
print len(generatedDna)
print "average length:"
for x in xrange(len(generatedDna)):
  thisStrand=generatedDna[x]
  avgLength+=len(thisStrand[0])
  avgLength+=len(thisStrand[1])
  #print avgLength
  avgGC+=RandomDna.GCcontent(thisStrand[0])
  avgGC+=RandomDna.GCcontent(thisStrand[1])
avgLength=avgLength/len(generatedDna)
avgGC=avgGC/len(generatedDna)
print avgLength
print "GC content:"
print avgGC