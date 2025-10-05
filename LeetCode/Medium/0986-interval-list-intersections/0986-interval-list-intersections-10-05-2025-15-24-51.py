class Solution:
    def intervalIntersection(self, intervals_a, intervals_b):
        mergedIntervals = []
        idx1 = 0
        idx2 = 0

        #print(intervals_a, intervals_b)

        while idx1 < len(intervals_a) and idx2 < len(intervals_b):
            left_obj = intervals_a[idx1]
            right_obj = intervals_b[idx2]
            #print(f"comparing {left_obj} and {right_obj}")
            if (
                (right_obj[0] <= left_obj[1])
                and (right_obj[0] >= left_obj[0])
            ) or (
                (left_obj[0] <= right_obj[1])
                and (left_obj[0] >= right_obj[0])
            ):
                low = max(right_obj[0], left_obj[0])
                high = min(right_obj[1], left_obj[1])
                mergedIntervals.append([low, high])
            print(
                f"right_obj[0] is {right_obj[0]}, left_obj[0] is {left_obj[0]} and {right_obj[0] <= left_obj[0]}"
            )

            if right_obj[1] <= left_obj[1]:
                if idx2 < len(intervals_b):
                    idx2 += 1
                else:
                    idx1 += 1
            else:
                if idx1 < len(intervals_a):
                    idx1 += 1
                else:
                    idx2 += 1

        return mergedIntervals