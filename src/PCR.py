from RandomDnaTemplate import RandomDna

segmentSize = 100
cycles = 1
dropOffRate = 0
primerSize = 20
dnaTemplateSize=750

dna = RandomDna().randDna(dnaTemplateSize)
primer = RandomDna().randPrimer(dna, primerSize, segmentSize)
generatedDna = []

i = 1;
while i <= cycles:
    #print "cycle number: ", i
    i+=1


p1 = dna[0].index(primer[0])-1
print " "*p1, "5'", primer[0],"3'"
print "5'",dna[0], "3'"

print "3'", dna[1], "5'"
p2 = dna[1].index(primer[1])-1
print " "*p2, "3'", primer[1],"5'"


