from random import randrange

class RandomDna(object):
    
    # returns both dna strands.
    # the second strand is the reverse complement
    # of of the first strand.
    def randDna(self, length):
        n=length
        base=['A','T','C','G']
        dna=[0,0]
        firstStrand=''
        for x in xrange(n):
            firstStrand=firstStrand+base[randrange(4)]
        #print firstStrand
        secondStrand=firstStrand.replace('A','t')
        secondStrand=secondStrand.replace('T','a')
        secondStrand=secondStrand.replace('C','g')
        secondStrand=secondStrand.replace('G','c')
        secondStrand=secondStrand.upper()
        #print secondStrand
        dna[0]=firstStrand
        dna[1]=secondStrand[::-1]
        
        return dna
    
    #TODO - write code to select a random primer
    #       based off of the length and the dna template given.
    def randPrimer(self, dna, length):
        return "testPrimer"


