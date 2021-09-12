def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
print(lengthOfLastWord('Hi, Welcome to Leetcode')==8)