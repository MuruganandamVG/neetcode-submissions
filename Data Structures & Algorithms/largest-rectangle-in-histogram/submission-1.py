class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        def findPse(heights):
            pse=[-1]*n
            st=[]
            for i in range(n):
                while st and heights[i]<=heights[st[-1]]:
                    st.pop()
                if len(st):
                    pse[i]=st[-1]
                st.append(i)
            return pse
        def findNse(heights):
            nse=[n]*n
            st=[]
            for i in range(n-1,-1,-1):
                while st and heights[i]<=heights[st[-1]]:
                    st.pop()
                if len(st):
                    nse[i]=st[-1]
                st.append(i)
            return nse
        pse=findPse(heights)
        nse=findNse(heights)
        maxArea=0
        for i in range(n):
            area=(nse[i]-pse[i]-1)*heights[i]
            maxArea=max(area,maxArea)
        return maxArea


        