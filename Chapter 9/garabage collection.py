#                                       What is Garbage Collection?

# Garbage Collection (GC) is the process of automatically freeing memory occupied by objects that are no longer in use.

#                                        How does Python manage memory?

# Python uses **two mechanisms**:

# 1. **Reference Counting (Primary)**

#    * Every object keeps a count of how many variables reference it.
#    * When the reference count becomes **0**, the object's memory is freed immediately.

# E:g
# a = [1, 2, 3]
# b = a      # Reference count increases

# del a      # Count decreases
# del b      # Count becomes 0 → memory is freed

# 2. **Garbage Collector (Secondary)**

#    * Handles **circular references** that reference counting cannot clean up.

# Example:
# class A:
#     pass

# x = A()
# y = A()

# x.ref = y
# y.ref = x

# Even after:

# del x
# del y

# the objects still reference each other. Their reference counts never become 0, so **reference counting alone cannot free them**.

# The **garbage collector (`gc`)** periodically detects these unreachable cycles and removes them i:e frees the unreachable objects.


#                                        Why do we have the `gc` module?

# The garbage collector already runs automatically.

# The `gc` module is provided to:

#  Force a garbage collection (`gc.collect()`)
#  Enable or disable the collector
#  Inspect unreachable objects
#  Debug memory leaks
