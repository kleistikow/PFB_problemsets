#!/usr/bin/env python3

import os, sys



## method: sequence_to_kmer_list(sequence, kmer_length)
##
##  Extracts all kmers of a specified length from a sequence
##
##  ie.  sequence: GATCGATCGATCGA
##   and given kmer_length = 4
##   would yield
##                 GATC
##                  ATCG
##                   TCGA
##                    .... and so forth
##                       
##  input parameters:
##
##  seuqence : nucleotide sequence (type: string)
##
##  returns kmer_list : list of kmer sequences.
##                    ie.  ["GATC", "ATCG", ...]
read = 'ACTGCATCCTGGAAAGAATCAATGGTGGCCGGAAAGTGTTTTTCAAATACAAGAGTGACAATGTGCCCTGTTGTTT'   
def sequence_to_kmer_list(sequence, kmer_length):
    kmers_dict = {}
    num_kmers = len(sequence) - kmer_length + 1
    kmers_list = []    
    for i in range(num_kmers):
        kmer = read[i:i+kmer_length]
        kmers_list.append(kmer)
        if kmer not in kmers_dict:
           kmers_list.append(kmer)
           kmers_dict[kmer] = 0
        kmers_dict[kmer] += 1
        list(kmers_dict.keys())

    return kmers_list
   

def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} sequence kmer_length\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    sequence = sys.argv[1]
    kmer_length = int(sys.argv[2])

    kmers  = sequence_to_kmer_list(sequence, kmer_length)

    print(kmers)

    sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()
    
