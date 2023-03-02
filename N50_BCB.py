from Bio import SeqIO
data = SeqIO.parse("contigs.fa", "fasta")

cont_list = []
for seq_record in data:
    #print(seq_record.id)
    #print(repr(seq_record.seq))
    cont_list.append(len(seq_record))
    cont_list.sort()

print(cont_list)
largest_cont = (max(cont_list))

# count number of contigs
cont_count = len(cont_list)

# calculate total length of all contigs as sequence length
total_length = 0
for i in cont_list:
    total_length = total_length + i

# calculate N50
half_length = (total_length/2)
n_50 = 0
n_50_list = []
for i in cont_list:
    if n_50 + i < half_length:
        n_50 = n_50 + i
        n_50_list.append(i)
    elif n_50 >= half_length:
        break

print("number of contigs = " + (str(cont_count)) + '\n')
print("The total length of the sequence = " + str(total_length) + '\n')
print("The largest contig = " + str(largest_cont) + '\n')
print("N50 = " + str(max(n_50_list)))

# write results to an output file:
with open('report_n50.txt', 'w') as output:
    output.write("number of contigs = " + (str(cont_count)) + '\n')
    output.write("The total length of the sequence = " + str(total_length) + '\n')
    output.write("The largest contig = " + str(largest_cont) + '\n')
    output.write("N50 = " + str(max(n_50_list)))

