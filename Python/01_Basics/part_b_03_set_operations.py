# ============================================================
# Part-B Program 3: Set Operations
# Description: Demonstrate common operations performed
#              on two Python sets.
# ============================================================

# Create two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print("Set 1:", set1)
print("Set 2:", set2)

# Union - Combines all unique elements
print("\nUnion:", set1.union(set2))

# Intersection - Finds common elements
print("Intersection:", set1.intersection(set2))

# Difference - Elements present in set1 but not set2
print("Difference (Set 1 - Set 2):", set1.difference(set2))

# Symmetric Difference - Elements present in either set,
# but not in both
print("Symmetric Difference:", set1.symmetric_difference(set2))

# ------------------------------------------------------------
# Expected Output:
#
# Set 1: {10, 20, 30, 40, 50}
# Set 2: {30, 40, 50, 60, 70}
#
# Union: {10, 20, 30, 40, 50, 60, 70}
# Intersection: {30, 40, 50}
# Difference (Set 1 - Set 2): {10, 20}
# Symmetric Difference: {10, 20, 60, 70}
# ------------------------------------------------------------
