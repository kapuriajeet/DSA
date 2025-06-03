# First Solution
# TC - O(n logn + m logm)
# SC - O(1)
s = "racecar"
t = "carrace"
class SolutionOne:
    def validAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

class SolutionTwo:
    def validAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)

        return dict_s == dict_t

solOne = SolutionOne()
solTwo = SolutionTwo()
print(solOne.validAnagram(s, t))
print(solTwo.validAnagram(s, t))