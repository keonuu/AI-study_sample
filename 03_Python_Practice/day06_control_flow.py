print("Day 6 - Python conditionals, loops, and functions")
print()


def check_qc(rate):
    if rate >= 0.9:
        return "excellent"
    elif rate >= 0.8:
        return "pass"
    else:
        return "fail"


print("Single sample QC")
sample_id = "S01"
mapping_rate = 0.92
result = check_qc(mapping_rate)
print(sample_id, result)
print()

print("Loop over mapping rates")
mapping_rates = [0.92, 0.79, 0.81]

for rate in mapping_rates:
    result = check_qc(rate)
    print(rate, result)

print()

print("Loop over sample dictionaries")
samples = [
    {"sample_id": "S01", "mapping_rate": 0.92},
    {"sample_id": "S02", "mapping_rate": 0.76},
    {"sample_id": "S03", "mapping_rate": 0.84},
]

for sample in samples:
    result = check_qc(sample["mapping_rate"])
    print(sample["sample_id"], result)

print()

print("Condition order example")


def check_qc_wrong_order(rate):
    if rate >= 0.8:
        return "pass"
    elif rate >= 0.9:
        return "excellent"
    else:
        return "fail"


print("Correct order:", check_qc(0.92))
print("Wrong order:", check_qc_wrong_order(0.92))
