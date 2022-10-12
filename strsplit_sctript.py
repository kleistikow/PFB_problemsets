#!/usr/bin/env python3
#10/12/22

taxa = 'naledi, sapiens , erectus , neanderthals'
print (taxa)
print (taxa[1])
type(taxa)

species = taxa.split(',')
print(species[1])
print(type(species))

species_sorted = sorted(species)
print(species_sorted)

species_len = sorted(species, key=len)
print (species_len)


