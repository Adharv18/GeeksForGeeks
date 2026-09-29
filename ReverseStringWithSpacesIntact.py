class Solution:
    def reverses(self, s):
        # code here
        i=0
        j=len(s)-1
        s = list(s)
        while i<=j:
            if s[i]!= " " and s[j]!=" ":
                s[i] , s[j]=s[j],s[i]
                i+=1
                j-=1
            else:
                if s[i] ==" ":
                    i+=1
                else:
                    j-=1
        return "".join(s)
