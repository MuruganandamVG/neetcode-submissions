class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr=[]
        m=len(nums1)
        n=len(nums2)
        left=0
        right=0
        while left<m and right<n:
            if nums1[left]<=nums2[right]:
                arr.append(nums1[left])
                left+=1
            else:
                arr.append(nums2[right])
                right+=1
        while left<m:
            arr.append(nums1[left])
            left+=1
        while right<n:
            arr.append(nums2[right])
            right+=1
        print(arr)
        count=len(arr)
        mid=(count-1)//2
        if (count)%2==0:
            print(arr[mid])
            val=(arr[mid]+arr[mid+1])/2
            return val
        else:
            return arr[mid]



        