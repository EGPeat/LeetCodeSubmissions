class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curr_gas = 0
        n = len(gas)
        for i, station in enumerate(gas):
            #print(f"########################\nstarting at station #{i}")
            price = cost[i % n]
            curr_gas = station
            e = i + 1
            
            while curr_gas > 0:
                station = gas[e%n]
                price = cost[(e-1)%n]
                temp_curr_gas = curr_gas - price
                if temp_curr_gas < 0:
                    #print("temp_curr_gas wasn't enough, womp womp")
                    break
                if e%n == i:
                    #print("Found it")
                    return i
                #print(f"e = {e%n}, curr_gas = {curr_gas}, station = {station}, price = {price}, curr_gas after = {curr_gas - price + station}")
                curr_gas = curr_gas - price + station
                e+= 1
                
        return -1