class Solution:
    def countBits(self, n: int) -> List[int]:

      result = []

      result.append(0)
      if n == 0:
        return result
      result.append(1)

      for i in range(2, n+1):
        if i % 2 == 0:
          result.append(result[i // 2])
        else:
          result.append(result[i // 2] + 1)

      return result
        