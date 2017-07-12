class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = [str(i) for i in xrange(1,n+1)]
        i = 3
        j = 5
        while i <= n:
            ans[i-1] = 'Fizz'
            i += 3
        while j <= n:
            if ans[j-1] == 'Fizz':
                ans[j-1] = 'FizzBuzz'
            else:
                ans[j-1] = 'Buzz'
            j += 5
        return ans

