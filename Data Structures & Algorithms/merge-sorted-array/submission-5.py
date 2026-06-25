class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # len(nums1) = m+n

        i,j,k = 0,0,0
        temp_a = nums1[:-n]
        if n == 0:
            temp_a = nums1

        while(i< m and j < n):
            print("temp_2",temp_a[i])
            print("nums2",nums2[j])
            print("---")
            if temp_a[i]<= nums2[j]:
                nums1[k] = temp_a[i]
                print(nums1[k])
                k=k+1
                i=i+1
            elif nums2[j] < temp_a[i]:
                nums1[k] = nums2[j]
                print("here",nums1[k])
                k=k+1
                j=j+1

            
        print(nums1)
        while(j<n):
            nums1[k] = nums2[j]
            j=j+1
            k=k+1
        print(i)
        print(k)
        print(temp_a)
        while (i < m):
            nums1[k] = temp_a[i]
            i=i+1
            k=k+1
        print(nums1)
