"""Read Fasta returns a list of dictionaries of fastas and dna_sequence
    author == @_drjimoh
    date 27:06:2020 
"""

def read_file(filename):
    file = open(filename, 'r+')
    lines = file.readlines()
    file.close()
    return lines

def read_fasta(filename):
    index_list = []
    lines = read_file(filename)
    for x in lines:
        dna_seq = ''
        if x[0] == '>':
            index_list.append(lines.index(x))
    dna_list = []
    for x in index_list:
        fasta_seq = {}
        fasta_seq['reference'] = lines[x].strip()
        dna_string = ''
        y = x+1
        try:
            while y < index_list[index_list.index(x)+1] and y < len(lines):
                dna_string += str(lines[y].strip())
                y += 1
            # print(dna_string)
            fasta_seq['DNA']  = dna_string
            dna_list.append(fasta_seq)
        except Exception as e:
            pass
    return dna_list

