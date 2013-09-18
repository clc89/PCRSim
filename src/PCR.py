from RandomDnaTemplate import RandomDna

dna = RandomDna().randDna(10)
primer = RandomDna().randPrimer(dna, 5)
cycles = 1
dropOffRate = 0
i = 1;
generatedDna = []
while i <= cycles:
    print "cycle number: ", i
    i+=1


print dna
print primer