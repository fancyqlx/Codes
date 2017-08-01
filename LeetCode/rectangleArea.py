class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        width = 0
        length = 0
        if C-A < G-E:
            width = self.difference(E,G,A,C)
        else:
            width = self.difference(A,C,E,G)
        if D-B < H-F:
            length = self.difference(F,H,B,D)
        else:
            length = self.difference(B,D,F,H)
        return (C-A)*(D-B)+(G-E)*(H-F)-width*length

    def difference(self,a,b,c,d):
        if a<=c:
            if d<=b:
                return d-c
            elif c<=b:
                return b-c
        elif a<=d:
            if d<=b:
                return d-a
        return 0


