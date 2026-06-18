print("Day 5 - Python variables and basic types")
print()

gene_name = "TP53"
read_count = 1520
expression_level = 8.73
is_significant = True

print("Basic variables")
print(gene_name)
print(read_count)
print(expression_level)
print(is_significant)
print()

print("Types")
print(type(gene_name))
print(type(read_count))
print(type(expression_level))
print(type(is_significant))
print()

genes = ["TP53", "BRCA1", "EGFR"]

sample = {
    "sample_id": "S01",
    "condition": "treated",
    "cell_line": "HEK293",
    "read_count": 35000,
    "mapping_rate": 0.87,
    "passed_qc": True,
}

print("List example")
print(genes)
print()

print("Dictionary example")
print(sample)
print(sample["sample_id"])
print(sample["condition"])
print(sample["read_count"])
print()

print("Variable names are case-sensitive")
gene = "TP53"
print(gene)
# print(Gene) would raise NameError because Gene was not defined.

