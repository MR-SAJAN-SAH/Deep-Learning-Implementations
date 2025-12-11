def inspect_pdb(path):
    record_types = {}
    example_lines = {}

    with open(path, "r") as f:
        for line in f:
            if not line.strip():
                continue

            record = line[:6].strip()

            # Count occurrences of each record type
            record_types[record] = record_types.get(record, 0) + 1

            # Store one example line for each record type
            if record not in example_lines:
                example_lines[record] = line.rstrip()

    print("\n=== Record Types Found ===")
    for r, count in sorted(record_types.items()):
        print(f"{r}: {count}")

    print("\n=== Example Lines ===")
    for r, ex in example_lines.items():
        print(f"{r}: {ex}")


# Example usage:
inspect_pdb("4yki_GLY_ligand.pdb")
