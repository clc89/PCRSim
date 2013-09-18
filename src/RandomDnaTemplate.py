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
            
        secondStrand = self.reverseComplement(firstStrand)

        dna[0]=firstStrand
        dna[1]=secondStrand
        
        return dna
    
    # select a random primer
    # based off of the length and the dna template given.
    def randPrimer(self, dna, length):
        start = randrange(length)
        primer = [0,0]
        primer[0] = dna[0][start:start+length]
        primer[1] = self.reverseComplement(primer[0])
        
        return primer
    
    
    
    def reverseComplement(self, dna):
        secondStrand=dna.replace('A','t')
        secondStrand=secondStrand.replace('T','a')
        secondStrand=secondStrand.replace('C','g')
        secondStrand=secondStrand.replace('G','c')
        secondStrand=secondStrand.upper()
        secondStrand = secondStrand[::-1] 
               
        return secondStrand


