class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        T = [{} for i in xrange(len(points))]
        ans = 0
        for i in xrange(len(points)):
            for j in xrange(i+1, len(points)):
                dis = pow(pow(points[i][0]-points[j][0],2)+pow(points[i][1]-points[j][1],2),0.5)
                if T[i].has_key(dis):
                    T[i][dis] += 1
                    if T[i][dis] > 1:
                        ans += (T[i][dis] - 1) * 2
                else:
                    T[i][dis] = 1
                if T[j].has_key(dis):
                    T[j][dis] += 1
                    if T[j][dis] > 1:
                        ans += (T[j][dis] - 1) * 2
                else:
                    T[j][dis] = 1
        return ans

