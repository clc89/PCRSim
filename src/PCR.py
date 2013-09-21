from RandomDnaTemplate import RandomDna

#settings. We instantiate the inputs here. Most are self explanatory
segmentSize = 200
cycles = 15
dropOffRate = 50
primerSize = 20
dnaTemplateSize=2000

#the amplified segment is declared and instantiated here
segment=[0,0]

#the various outputs
avgLength=0
avgGC=0
lengthDistribution=[0]*(dnaTemplateSize+1) #maximum length+1

#the DNA is randomly generated, and the primer uses the DNA as a base to ensure compatibility
dna = RandomDna().randDna(dnaTemplateSize)
primer = RandomDna().randPrimer(dna, primerSize, segmentSize)
#all generated DNA is stored in a list until processed
generatedDna = [dna]

p1 = dna[0].index(primer[0])-1
print " "*p1, "5'", primer[0],"3'"
print "5'",dna[0], "3'"

print "3'", dna[1], "5'"
p2 = dna[1].index(primer[1])-1
print " "*p2, "3'", primer[1],"5'"

#for segment generation, we make sure each one is of the maximum length
segment[0] = dna[0][p1:p2+len(primer)+dropOffRate] 
segment[1] = dna[1][p1-dropOffRate:p2+len(primer)]

#The PCR cycle
for x in xrange(cycles):
  listLength=len(generatedDna)
  for y in xrange(listLength):
    toProcess=generatedDna[y]
    toProcess[0]=RandomDna().processivity(toProcess[0],dropOffRate,0,segmentSize)
    toProcess[1]=RandomDna().processivity(toProcess[1],dropOffRate,1,segmentSize)
    newCopy = RandomDna().pcrCycle(toProcess[0],toProcess[1],segment[0],segment[1])
    generatedDna += newCopy
    generatedDna.remove(toProcess)




#data processing
print "total DNA fragments:"
print len(generatedDna)
#This loop processes each strand of generated Dna for relevant information
for x in xrange(len(generatedDna)):
  thisStrand=generatedDna[x]
  
  avgLength+=len(thisStrand[0])
  avgLength+=len(thisStrand[1])
  
  avgGC+=RandomDna().GCcontent(thisStrand[0])
  avgGC+=RandomDna().GCcontent(thisStrand[1])
 
  lengthDistribution[len(thisStrand[0])]+=1
  lengthDistribution[len(thisStrand[1])]+=1
  
avgLength=avgLength/len(generatedDna)
avgGC=avgGC/(2*len(generatedDna))

#outputs
print "average length:"
print avgLength
print "Average GC content:"
print avgGC
print "length distribution:"
print lengthDistribution