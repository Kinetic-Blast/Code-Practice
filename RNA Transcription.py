RNA_Dict = {"G":"C","C":"G","T":"A","A":"U"}

DNA_with_errors = "ATCGTTAXGGGCTAATCGATCGATG"
DNA_without_errors = "ATCGTTAGGACTAATCGATCGATG"


def to_RNA(DNAStrand):
    return "".join([RNA_Dict.get(chr," * ") for chr in DNAStrand])


print(to_RNA(DNA_with_errors))
print(to_RNA(DNA_without_errors))