import itertools

# With recursion
subset = []


def subsets(nums, length, k):
    k = k - 1
    x = []
    if len(nums) == 0:  # base step
        return nums
    # print('k', k)
    if k > 0:  # first step to have all length 1 elements in array
        if len(subset) == 0:
            y = [[i] for i in nums]
            subset.extend(y)
            # print('subset', subset)
        curr_len = len(subset)  # get the difference from previous step
        # print('curr_len', curr_len)
        for i in range(len(nums)):
            for j in range(length):
                # print('j', j)
                x.append([nums[i]] + subset[-j - 1])
            # print('x', x)
        subset.extend(x)
        print("subset", subset)
       #print('len(subset)-curr_len,', len(subset) - curr_len, )
        subsets(nums, len(subset) - curr_len, k)  # recursive step
        return subset, len(subset) - curr_len


subsets([1, 2, 3], 2, 2)

# with itertools combinations

nums = set(map(int, input("Enter numbers ").split()))
k = int(input("Enter you k please "))
print(list(map(set, itertools.combinations(nums, k))))
