class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        answer = []
        while i<len(word1) and j<len(word2):
            answer.append(word1[i])
            answer.append(word2[i])
            i+=1
            j+=1
        answer.extend(word1[i:])
        answer.extend(word2[j:])
        return "".join(answer)