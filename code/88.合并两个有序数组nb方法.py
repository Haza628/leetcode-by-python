def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """

    i = 0
    j = 0
    for k in range(m + n):
        if i == m:
            nums1[m+n-k-1] = nums2[n-j-1]
            j = j + 1
        elif j == n:
            nums1[m+n-k-1] = nums1[m-i-1]
            i = i + 1
        elif nums1[m-i-1] >= nums2[n-j-1]:
            nums1[m+n-k-1] = nums1[m-i-1]
            i = i + 1
        elif nums1[m-i-1] < nums2[n-j-1]:
            nums1[m+n-k-1] = nums2[n-j-1]
            j = j + 1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2, 3, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
