class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = list()
        valids = list()
        for index, op in enumerate(ops):
            if op not in ['C', 'D', '+']:
                valids.append(True)
                points.append(int(op))
            elif op == 'C':
                valids.append(False)
                for i in range(index - 1, -1, -1):
                    if valids[i]:  # find the first valid record
                        points.append(-points[i])
                        valids[i] = False
                        break
            elif op =='D':
                valids.append(True)
                for i in range(index - 1, -1, -1):
                    if valids[i]:
                        points.append(2 * points[i])
                        break
            elif op == '+':
                valids.append(True)
                found = 0
                j, k = -1, -1
                for i in range(index - 1, -1, -1):
                    if valids[i]:
                        if found == 0:
                            j = i
                            found += 1
                        elif found == 1:
                            k = i
                            break
                points.append(points[j] + points[k])
        return sum(points)
                    
        
if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
                        
                        
