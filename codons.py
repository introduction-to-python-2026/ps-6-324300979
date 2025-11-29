def create_codon_dict(path):
    path = "data/codons.txt"
    file = open(path)
    rows = file.readlines()
    file.close()
    codon2aa = {}
    for row in rows:
      cells = row.strip().split('\t')
      key = cells[0]
      value = cells[2]
      codon2aa[key] = value
    return codon2aa

