#!/usr/bin/env python

#This script uses the file genome_result.txt generated by Qualimap and calculates the autosomal coverage.

import sys

def parse_qualimap_coverage(genome_results_file):
    autosomal_cov_length = 0
    autosomal_cov_bases = 0
    coverage_section = False
    with open(genome_results_file, 'r') as f:
        for line in f:
            if line.startswith('>>>>>>> Coverage per contig'):
                coverage_section = True
                continue
            if coverage_section:
                line = line.strip()
                if line:
                    sections = line.split()
                    part1 = sections[0][:3]
                    part2 = sections[0][3:]
                    if part1 == 'chr' and part2.isdigit() and int(part2) <= 22:
                        autosomal_cov_length += float(sections[1])
                        autosomal_cov_bases += float(sections[2])
        if autosomal_cov_length and autosomal_cov_bases:
            return autosomal_cov_bases / autosomal_cov_length
        else:
            return 0.0

if len(sys.argv) < 2:
        print('Usage: calculate_autosomal_coverage.py filename')
        sys.exit(1)

result = parse_qualimap_coverage(sys.argv[1])
print('Coverage = %f' % result)
sys.exit(0)
