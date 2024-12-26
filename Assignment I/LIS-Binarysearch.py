import bisect

def length_of_lis_binary_search(arr):
    lis = []

    for num in arr:
        pos = bisect.bisect_left(lis, num)  # Find position to replace or extend
        if pos == len(lis):
            lis.append(num)  # Extend the subsequence
        else:
            lis[pos] = num  # Replace the existing value

    return len(lis)  # Length of the LIS
