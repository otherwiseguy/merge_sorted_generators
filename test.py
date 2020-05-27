#!/usr/bin/python3
EMPTY = object()


def merge_union(*sorted_gen):
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


def merge_intersection(*sorted_gens):
    try:
        cut_off = next(sorted_gens[0])
        matches = 1
    except StopIteration:
        return  # The can't all match if one is empty
    while True:
        for gen in sorted_gens:
            while True:
                try:
                    val = next(gen)
                except StopIteration:
                    return
                if val >= cut_off:
                    break
            if  val != cut_off:
                cut_off = val
                matches = 1
            else:
                matches += 1
            if matches == len(sorted_gens):
                yield val


a = iter(range(0, 6))
b = iter(range(4, 7))
c = iter(range(3, 6))
print(list(merge_intersection(a, b, c)))
#print(list(merge_unique(a, b, c)))
#print(list(merge_unique(iter([]))))
#print(list(merge_unique(iter([1, 2]))))
