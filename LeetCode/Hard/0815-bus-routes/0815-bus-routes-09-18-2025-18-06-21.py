from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        stop_to_buses = defaultdict(list)
        for bus_index, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_index)
      
        if source not in stop_to_buses or target not in stop_to_buses:
            return -1
      
        queue = deque([(source, 0)])
        visited_buses = set()
        visited_stops = {source}
      
        while queue:
            current_stop, buses_taken = queue.popleft()
          
            if current_stop == target:
                return buses_taken
          
            for bus_index in stop_to_buses[current_stop]:
                if bus_index in visited_buses:
                    continue
                visited_buses.add(bus_index)

                for next_stop in routes[bus_index]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, buses_taken + 1))
        return -1