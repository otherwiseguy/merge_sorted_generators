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


def circular(*items):
    if not items:
        return
    while True:
        for x in items:
            yield x


def merge_intersection(*sorted_gens):
    len_sorted_gens = len(sorted_gens)
    sorted_gens = circular(*sorted_gens)
    first = next(sorted_gens)
    try:
        val = cut_off = next(first)
        matches = 1
    except (StopIteration, IndexError):
        return  # The can't all match if one is empty
    for gen in sorted_gens:
        while True:
            if matches == len_sorted_gens:
                yield val
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
