class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_max = 0
        for altitude in gain:
            current_max += altitude
            if current_max > max_altitude:
                max_altitude = current_max
        return max_altitude