from random import randrange

class RandomDna(object):
    
    #returns both dna strands
    def randDna(self, length):
        n=length
        base=['A','T','C','G']
        dna=[0,0]
        firstStrand=''
        for x in xrange(n):
            firstStrand=firstStrand+base[randrange(4)]
        #print firstStrand
        secondStrand=firstStrand.replace('A','U')
        secondStrand=secondStrand.replace('T','A')
        secondStrand=secondStrand.replace('C','g')
        secondStrand=secondStrand.replace('G','C')
        secondStrand=secondStrand.upper()
        #print secondStrand
        dna[0]=firstStrand
        dna[1]=secondStrand[::-1]
        
        return dna
    
    def randPrimer(self, dna, length):
        return "testPrimer"


