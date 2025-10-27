def main():
    # creation
    empty = set()
    fruits = {"apple", "banana", "orange", "apple"}  # duplicates ignored
    print("fruits (initial):", fruits)

    # from other iterables (removes duplicates)
    nums = set([1, 2, 3, 2, 4, 1])
    print("nums (from list, deduped):", nums)

    # add / update
    fruits.add("kiwi")
    fruits.update(["mango", "banana"])  # adding multiple; 'banana' already present
    print("fruits (after add/update):", fruits)

    # remove vs discard
    fruits.discard("pear")  # no error if missing
    try:
        fruits.remove("pear")  # KeyError if missing
    except KeyError:
        print("remove('pear') raised KeyError (was missing)")

    # pop (removes and returns an arbitrary element)
    arbitrary = fruits.pop()
    print("popped element:", arbitrary)
    print("fruits (after pop):", fruits)

    # set algebra
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    print("A:", A, "B:", B)
    print("union:", A | B)                # {1,2,3,4,5,6}
    print("intersection:", A & B)         # {3,4}
    print("difference A - B:", A - B)     # {1,2}
    print("symmetric_difference:", A ^ B) # {1,2,5,6}

    # methods equivalently
    print("A.union(B):", A.union(B))
    print("A.intersection(B):", A.intersection(B))

    # subset / superset
    C = {1, 2}
    print("C <= A (C is subset of A):", C <= A)
    print("A >= C (A is superset of C):", A >= C)

    # frozenset (immutable set, hashable)
    fs = frozenset([1, 2, 3])
    print("frozenset:", fs)

    # set comprehension
    squares = {x * x for x in range(1, 6)}
    print("squares:", squares)

    # convert to sorted list to show deterministic order for presentation
    mixed = {"z", "a", "m"}
    print("mixed (unordered set):", mixed)
    print("mixed sorted:", sorted(mixed))

    # removing duplicates from a list using set
    dup_list = [1, 2, 2, 3, 3, 3]
    unique_list = list(set(dup_list))
    print("unique_list (from dup_list):", unique_list)


if __name__ == "__main__":
    main()