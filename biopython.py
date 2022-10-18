! usr/bin/env python3
#biopython problem set
import Bio
import re
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.SeqUtils import six_frame_translations

with open('Python_08.fasta') as fasta_file08: 
	identifiers = []
	lengths = []
	for seq_record in SeqIO.parse(fasta_file08, 'fasta'):
		identifiers.append(seq_record.id)
		lengths.append(len(seq_record.seq))
		print('ID->',seq_record.id)
		print('Sequence->',seq_record.seq)
		print('Length->',len(seq_record))
		print('GC cont->',GC(seq_record.seq))
		print('SixFrameTranslation->', six_frame_translations(seq_record.seq))
