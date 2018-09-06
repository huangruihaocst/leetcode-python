# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda i: (i.start, i.end))
        prev_end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < prev_end:
                return False
            prev_end = interval.end
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canAttendMeetings([Interval(7, 10), Interval(2, 4)]))
