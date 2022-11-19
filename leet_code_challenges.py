class Solution:

    def romanToInt(self, s: str) -> int:
        r_sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            if i + 1 < len(s):
                if r_sym[s[i]] < r_sym[s[i + 1]]:
                    num += (-r_sym[s[i]])
                else:
                    num += r_sym[s[i]]
        num += r_sym[s[-1]]
        return num

    def longestCommonPrefix(self, strs):
        main_str = strs[0]
        result = ''
        for l in range(len(main_str) + 1):
            if len(strs) == 1:
                return main_str
            all_match = False
            for word in strs:
                if len(word) >= l and main_str[:l] == word[:l]:
                    all_match = True
                else:
                    all_match = False
                    break
            if all_match:
                result = main_str[:l]
        return result


if __name__ == '__main__':
    s = Solution()
    print('*' * 50, "PROBLEM 1")
    pb1 = [["flower","flower","flower","flower"],
           ["ab","a"], ["a"],["aaa","aa","aaa"]]
    for lst in pb1:
        print(s.longestCommonPrefix(lst))
    print('*'*50, "PROBLEM 2")
    pb2 = ["III", "MCMXCIV", "LVIII"]
    for stnrg in pb2:
        print(s.romanToInt(stnrg))