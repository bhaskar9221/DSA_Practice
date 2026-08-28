class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        mid = ''
        for i in range(26):
            if cnt[i] & 1:
                if n % 2 == 0:
                    return ''
                if mid:
                    return ''
                mid = chr(i + 97)
            cnt[i] //= 2

        m = n // 2
        t = target[:m]
        cur = cnt[:]
        ans = None
        prefix = []

        for i, ch in enumerate(t):
            x = ord(ch) - 97

            for j in range(x + 1, 26):
                if cur[j]:
                    left = ''.join(prefix) + chr(j + 97)
                    rem = cur[:]
                    rem[j] -= 1
                    tail = ''.join(chr(k + 97) * rem[k] for k in range(26))
                    h = left + tail
                    p = h + mid + h[::-1]
                    if p > target:
                        ans = p
                    break

            if cur[x] == 0:
                break

            cur[x] -= 1
            prefix.append(ch)
        else:
            h = ''.join(prefix)
            p = h + mid + h[::-1]
            if p > target:
                return p

        return ans or ''