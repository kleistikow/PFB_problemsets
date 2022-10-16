#! usr/bin/env python3

class dnaseq(object):  
    def __init__(self, name, dnaseq, organism):
        self.name = name
        self.dnaseq = dnaseq
        self.organism = organism
    def length(self):
        return len(self.dnaseq)
    def nt_composition(self, fraction=False):
        nt_comp = {'A':0, 'T':0, 'G':0, 'C':0, 'N':0}
        for nt in self.dnaseq.upper():
            try:
                nt_comp[nt] += 1
            except KeyError:
                raise ValueError("Invalid nucleotide character '{}'".format(nt))

        if fraction:
            dnaseq_length = self.length()
            for nt in nt_comp:
                nt_comp[nt] = float(nt_comp[nt]) / dnaseq_length
                
        return nt_comp
    
    def gc_content(self):
        gc_chars = set('GCgc')
        gc_count = 0
        for nt in self.sequence:
            if nt in gc_chars:
                gc_count += 1

        return float(gc_count) / self.length()

    def __str__(self):
        return '>{}{}\n{}\n'.format(
            self.name,
            '' if self.organism is None else ' [{}]'.format(self.organism),
            _wrap(self.sequence, width=50)
        )
if __name__ == '__main__':
    record = dnaseq()
    record.name = 'KRL.srf.3310'
    record.dnaseq = 'AGACAAACCGGTGCCAACGTGCGCGGACGCCGCCGCCGCCACCGCCGCCACCGC'
    record.organism = 'Bacillus subtilis'

print('ID: {}\nORG: {}\nLEN: {}\nGC%: {}\nSEQ: {}\n{}'.format(        
	record.name,
        record.organism,
       	record.length(),
	record.gc_content() * 100, 
	record.dnaseq,
	str(record) 

    ))
print()
