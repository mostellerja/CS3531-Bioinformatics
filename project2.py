import numpy as np
import matplotlib.pyplot as plt
import os
from os import listdir
from os.path import isfile, join

RNA_seq = 'GGCCGCGGCAGGUUCGAGUCCUGCCGCGAUCGCCAC'
RNA_sec_struct = '((((((((((((.......)))))))))...)))..'
S1 = []
S2 = []
S3 = []
def count_bps(rna_seq, rna_sec_struct):

    count_au = 0
    count_gc = 0
    count_gu = 0
    final_count = 0
    for i in range(len(rna_sec_struct)):
        if rna_sec_struct[i] == '(':
            S3.append(i)
        if rna_sec_struct[i] == ')':
            close_index = i
            open_index = S3.pop()



            if rna_seq[open_index] == 'A' and rna_seq[close_index] == 'U':
                count_au += 1
            if rna_seq[open_index] == 'U' and rna_seq[close_index] == 'A':
                count_au += 1
            if rna_seq[open_index] == 'G' and rna_seq[close_index] == 'C':
                count_gc += 1
            if rna_seq[open_index] == 'C' and rna_seq[close_index] == 'G':
                count_gc += 1
            if rna_seq[open_index] == 'G' and rna_seq[close_index] == 'U':
                count_gu += 1
            if rna_seq[open_index] == 'U' and rna_seq[close_index] == 'G':
                count_gu += 1
    print(count_au)
    print(count_gc)
    print(count_gu)
    return count_au, count_gc, count_gu
def get_RNAseq_and_secondary_struct_from_FASTA(full_name):
    RNA_seq = 'GGCCGCGGCAGGUUCGAGUCCUGCCGCGAUCGCCAC'
    RNA_sec_struct = '((((((((((((.......)))))))))...)))..'
    S2 = []
    S3 = []
    file1 = open(full_name, 'r')
    Lines = file1.readlines()


    for line in Lines:
        if not line.startswith('>'):
            print(line)

            for i in range(len(line)):
                # print(line[i])
                if line in 'ACGU':
                    if line[i] == 'A':
                        S1.append('A')
                    if line[i] == 'C':
                        S1.append('C')
                    if line[i] == 'G':
                        S1.append('G')
                    if line[i] == 'U':
                        S1.append('U')
                if line in '().':
                    if line[i] == '(':
                        S2.append('(')
                    if line[i] == ')':
                        S2.append(')')
                    if line[i] == '.':
                        S2.append('.')
    return RNA_seq, RNA_sec_struct



def directory_path():
    dir_path = 'real_sec_structures'
    for f in listdir(dir_path):
        full_name = join(dir_path, f)
        if isfile(full_name):
            print(full_name)
            get_RNAseq_and_secondary_struct_from_FASTA(full_name)

    count_bps(RNA_seq, RNA_sec_struct)
    get_RNAseq_and_secondary_struct_from_FASTA(dir_path)
    readDirectory(dir_path)


def readDirectory(dir_path):
    total_AU_count = 0
    total_CG_count = 0
    total_GU_count = 0
    for f in listdir(dir_path):
        au = get_RNAseq_and_secondary_struct_from_FASTA(dir_path)
        cg = get_RNAseq_and_secondary_struct_from_FASTA(dir_path)
        gu = get_RNAseq_and_secondary_struct_from_FASTA(dir_path)
        total_AU_count += au
        total_CG_count += cg
        total_GU_count += gu

        AU_percent = (total_AU_count) / (total_AU_count + total_CG_count + total_GU_count) * 100
        print("AU percent is: ", AU_percent)
        CG_percent = (total_CG_count) / (total_AU_count + total_CG_count + total_GU_count) * 100
        print("CG percent is: ", CG_percent)
        GU_percent = (total_GU_count) / (total_AU_count + total_CG_count + total_GU_count) * 100
        print("GU percent is: ", GU_percent)

        # creating the dataset
        data = {'A': AU_percent, 'C': CG_percent, 'G': GU_percent}
        courses = list(data.keys())
        values = list(data.values())

        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(courses, values, color='blue',
                width=0.4)

        plt.xlabel("Base Pairs")
        plt.ylabel("Percentage of Base Pairs Present")
        plt.title("Percentage of Base Pair in a Genome Sequence")
        plt.show()


def main():
    directory_path()


if __name__ == '__main__':
    main()

