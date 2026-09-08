def canConstructArray(nums1):
    """
    Determine whether we can build nums2 (same length as nums1) where
    every element is EITHER:
        nums2[i] = nums1[i]
    OR
        nums2[i] = nums1[i] - nums1[j]   (for some j != i)
    such that all elements of nums2 end up with the SAME parity
    (all odd, or all even).

    Key Insight (parity rules for subtraction):
        even - even = even
        odd  - odd  = even
        even - odd  = odd
        odd  - even = odd

    Case A: If every number in nums1 is already even,
            just copy nums1 directly -> nums2 is all even. Done.

    Case B: If there is at least one odd number in nums1,
            pick that odd number (index k) as a "helper".
            - Keep every odd nums1[i] as itself (odd stays odd).
            - For every even nums1[i], compute nums1[i] - nums1[k]
              (even - odd = odd), which turns it odd too.
            This makes nums2 entirely odd.

    Since Case A or Case B always applies, the answer is ALWAYS True.
    This function also builds an example nums2 to demonstrate it.
    """

    n = len(nums1)

    # ---- Case A: all elements are even ----
    if all(x % 2 == 0 for x in nums1):
        nums2 = nums1[:]  # just copy everything
        print("All even case ->", nums2)
        return True

    # ---- Case B: at least one odd number exists ----
    # find index of an odd number to use as the "helper"
    k = next(i for i, x in enumerate(nums1) if x % 2 != 0)

    nums2 = [0] * n
    for i in range(n):
        if nums1[i] % 2 != 0:
            # already odd -> keep as is
            nums2[i] = nums1[i]
        else:
            # even -> subtract the odd helper to make it odd
            nums2[i] = nums1[i] - nums1[k]

    print("Mixed case (built using helper index {}) ->".format(k), nums2)
    return True


# ---------------- Test Examples ----------------
print(canConstructArray([2, 3]))   # Example 1 -> True
print(canConstructArray([4, 6]))   # Example 2 -> True
print(canConstructArray([1, 5, 9]))  # all odd -> True
print(canConstructArray([2, 4, 8]))  # all even -> True
print(canConstructArray([2, 3, 8, 5]))  # mixed -> True