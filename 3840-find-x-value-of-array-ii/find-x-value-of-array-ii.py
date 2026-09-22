class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        for i, v in enumerate(nums):
            p = size + i
            r = v % k
            prod[p] = r
            cnt[p][r] = 1

        for p in range(size - 1, 0, -1):
            l, r = p << 1, p << 1 | 1
            prod[p] = prod[l] * prod[r] % k
            c = cnt[l][:]
            for x in range(k):
                c[(prod[l] * x) % k] += cnt[r][x]
            cnt[p] = c

        def merge(p1, c1, p2, c2):
            c = c1[:]
            for x in range(k):
                c[(p1 * x) % k] += c2[x]
            return p1 * p2 % k, c

        def query(left, right):
            lp, lc = 1, [0] * k
            rp, rc = 1, [0] * k

            left += size
            right += size

            while left < right:
                if left & 1:
                    lp, lc = merge(lp, lc, prod[left], cnt[left])
                    left += 1
                if right & 1:
                    right -= 1
                    rp, rc = merge(prod[right], cnt[right], rp, rc)
                left >>= 1
                right >>= 1

            return merge(lp, lc, rp, rc)

        ans = []

        for index, value, start, x in queries:
            p = size + index
            r = value % k
            prod[p] = r
            cnt[p] = [0] * k
            cnt[p][r] = 1

            p >>= 1
            while p:
                l, r = p << 1, p << 1 | 1
                prod[p] = prod[l] * prod[r] % k
                c = cnt[l][:]
                for j in range(k):
                    c[(prod[l] * j) % k] += cnt[r][j]
                cnt[p] = c
                p >>= 1

            ans.append(query(start, n)[1][x])

        return ans