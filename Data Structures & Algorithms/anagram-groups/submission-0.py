class Solution:
    def getFre(self, s: str):
        alpha = [0]*26
        for i in s:
            alpha[ord(i) - ord('a')]+=1
        return alpha
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = dict()
        ans = []
        for i in strs:
            alpha = tuple(self.getFre(i))
            if alpha in mp:
                mp[alpha].append(i)
            else:
                mp[alpha] = [i]
        for val in mp.values():
            ans.append(val)

        return ans

            


        