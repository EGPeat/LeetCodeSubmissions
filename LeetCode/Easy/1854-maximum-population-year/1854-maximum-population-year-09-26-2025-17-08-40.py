class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        births = [x[0] for x in logs]
        deaths = [x[1] for x in logs]
        years = [0] * 100 #or 101 for null spot
        births.sort()
        deaths.sort()
        bi, di = 0, 0
        for i in range(100):
        #for i in range(1, 101): #null spot for range
            years[i] = years[i - 1]
            while bi < len(births) and births[bi] == (1950 + i):
                years[i] += 1
                bi += 1
            while di < len(deaths) and deaths[di] == (1950 + i):
                years[i] -= 1
                di += 1
        return 1950 + years.index(max(years))