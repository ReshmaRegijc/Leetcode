def strStr(self, haystack: str, needle: str) -> int:
    if len(needle)==0:
        return 0
    x = haystack.find(needle)
    return x
