def remove_duplicates(nums):
    """Remove duplicates in-place from sorted list `nums`.
    Returns the number of unique elements `k` and modifies `nums`
    so that the first `k` entries are the unique values.
    For clearer display this example fills the remaining slots with '_'.
    """
    if not nums:
        return 0
    write = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[write - 1]:
            nums[write] = nums[i]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = '_'
    return write


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = remove_duplicates(nums)
    print(k , nums)
    print(f"{k}, nums = [{', '.join(str(x) for x in nums)}]")
