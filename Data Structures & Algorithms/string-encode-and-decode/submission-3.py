class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+= str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            print(s[i:j])
            str_l = int(s[i:j])
            res.append(s[j+1:j+str_l+1])
            i = j+str_l+1
        return res


            



