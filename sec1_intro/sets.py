# sets
# sets don't hold order and eliminates duplicates

science = {"Bob", "Ali", "Sarah"}
chemistry ={"Jenny", "Omar", "Sarah"}

# .difference() science but not chemistry
set_diff = science.difference(chemistry)
print(f"Set difference: {set_diff}")
# >>> output:  Ali and Bob in science, are not in chemistry

# .intersection() return element in both sets
set_intersection = science.intersection(chemistry)
print(f"set intersection: {set_intersection}")

# symmetric_difference() elements not in both sets

sym_diff = science.symmetric_difference(chemistry)
print(f"Symmetric difference: {sym_diff}" )


# union() unites the two sets elements into one

union_set = science.union(chemistry)
print(f"union of both science and chemistry: {union_set}")
