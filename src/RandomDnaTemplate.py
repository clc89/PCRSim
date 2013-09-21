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
    # based off of the length and the dna template.
    def randPrimer(self, dna, pLength, sLength):
        primer = [0,0]
        start = randrange(len(dna[0])-sLength)      
        segment = dna[0][start: start+sLength]
        #print "starting index of segment: ",start
        #print "segment:",segment
        #print "        ",self.reverseComplement(segment)
        #print "expected size:",sLength, " actual size:", len(segment)
        fPrimer = segment[0: pLength]
        rPrimer = segment[len(segment)-pLength: len(segment)]
        primer[0] = fPrimer
        primer[1] = self.reverseComplement(rPrimer)
        return primer
    
    def pcrCycle(self, dna0, dna1, segment0, segment1):
        firstCopy = [dna0,segment1]
        secondCopy = [segment0,dna1]
        copies = [firstCopy,secondCopy]
        return copies
    
    def reverseComplement(self, dna):
        secondStrand=dna.replace('A','t')
        secondStrand=secondStrand.replace('T','a')
        secondStrand=secondStrand.replace('C','g')
        secondStrand=secondStrand.replace('G','c')
        secondStrand=secondStrand.upper()
        #secondStrand = secondStrand[::-1] 
               
        return secondStrand
        
    def GCcontent(self,dna):
        G = dna.count('G')
        C = dna.count('C')
        GC = ((float(G + C)/len(dna)*100))
        return GC
        
    #Takes a strand, dropOffRate, and relative location (top or bottom strand)
    def processivity(self, strand, DoR, loc, minLength):
        x=randrange(DoR)
        if (loc==0):
          if len(strand[: len(strand)-x])>minLength:
            return strand[: len(strand)-x]
          else:
            return strand[: minLength]
        else:
          if len(strand[x:])>minLength:
            return strand[x: ]
          else: 
            return strand[(len(strand)-minLength):]

