# Brute Force Approach
def lengthOfLongestSubstring(s):
    def check(start, end):
        chars = [0] * 120
        # print(start, end)
        for i in range(start, end + 1):
            c = s[i]
            chars[ord(c)] += 1
            if chars[ord(c)] > 1:
                return False
        return True

    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res


def lengthOfLongestSubstringSliding(str):
    n = len(str)
    res = 0

    for i in range(n):

        visited = [0] * 256

        for j in range(i, n):

            if (visited[ord(str[j])] == True):
                break

            else:
                res = max(res, j - i + 1)
                visited[ord(str[j])] = True

        visited[ord(str[i])] = False

    return res


def longestUniqueSubsttr(string):
    seen = {}
    maximum_length = 0
    start = 0

    for end in range(len(string)):
        if string[end] in seen:
            start = max(start, seen[string[end]] + 1)

        seen[string[end]] = end
        maximum_length = max(maximum_length, end - start + 1)
    return maximum_length


def longestUniqueSubSet(string):
    chart_set = set()
    l = 0
    max_len = 0
    for r in range(len(string)):
        while string[r] in chart_set:
            chart_set.remove(string[l])
            l += 1
        chart_set.add(string[r])
        max_len = max(max_len, r - l + 1)
    return max_len


if __name__ == "__main__":
    s = 'abcabcbb'
    print(longestUniqueSubsttr(s))
