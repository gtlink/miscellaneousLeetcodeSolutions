##Transposing an array matrix
##You can use either zip or do a list comprehension
class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

        #return zip(*A)