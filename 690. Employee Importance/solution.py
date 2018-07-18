# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = dict()
        for employee in employees:
            d[employee.id] = employee.importance, employee.subordinates
        subs = d[id][1]
        res = d[id][0]
        while subs:
            new = list()
            for sub in subs:
                res += d[sub][0]
                new += d[sub][1]
            subs = new
        return res
        
if __name__ == '__main__':
    s = Solution()
    e1 = Employee(1, 2, [2])
    e2 = Employee(2, 3, [])
    print(s.getImportance([e1, e2], 2))
