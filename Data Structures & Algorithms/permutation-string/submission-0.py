class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        right = len(s1)
        s1freq = {}
        s2freq = {}

        # Initialize frequency for s1 and the first window of s2
        for i in range(len(s1)):
            s1freq[s1[i]] = s1freq.get(s1[i], 0) + 1
            s2freq[s2[i]] = s2freq.get(s2[i], 0) + 1

        # Check the first window
        if s1freq == s2freq:
            return True

        # Slide the window
        while right < len(s2):
            # Add the new rightmost character
            s2freq[s2[right]] = s2freq.get(s2[right], 0) + 1

            # Remove the leftmost character
            s2freq[s2[left]] -= 1
            if s2freq[s2[left]] == 0:
                del s2freq[s2[left]]

            # Move window forward
            left += 1
            right += 1

            # Check if current window matches
            if s1freq == s2freq:
                return True

        return False
