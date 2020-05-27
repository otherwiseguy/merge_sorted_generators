#!/usr/bin/python3
EMPTY = object()


def merge_unique(*sorted_gen):
    """Iterate over sorted generators, yielding the next unique value"""

    buckets = {gen: EMPTY for gen in sorted_gen}
    while buckets:
        removes = []
        for bucket, val in buckets.items():
            if val is EMPTY:
                buckets[bucket] = next(bucket, EMPTY)
                if buckets[bucket] is EMPTY:
                    removes.append(bucket)
        for remove in removes:
            del buckets[remove]
        min_keys = [key for key in buckets
                    if all(buckets[val] >= buckets[key]
                           for val in buckets)]
        for key in min_keys:
            val = buckets[key]
            buckets[key] = EMPTY
        if val is EMPTY:
            return
        yield val


a = iter(range(0, 5))
b = iter(range(4, 7))
c = iter(range(3, 8))
print(list(merge_unique(a, b, c)))
print(list(merge_unique(iter([]))))
