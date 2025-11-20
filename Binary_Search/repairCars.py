class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        #first thing to be done: For a predefined fixed time, can all the cars be repaired?
        # try it in linear time on answer, then upgrade it to search for answer with binary search, log(cars) time
        min_time = 1

        #if i have a fixed time, can i repair the cars?
        def can_repair(cars, ranks, fixed_time):
            #for each mechanic calculate how many they can repair in fixed time and then subtract from cars, if it is <= 0 then True
            for rank in ranks:
                cars -= math.floor((fixed_time/rank)** (1/2))
                if cars <= 0: return True
            return False

        #not bin search:
        # while not can_repair(cars, ranks, min_time):
        #     min_time += 1

        #bin search
        max_time = max(ranks) * cars**2 #max time to repair all cars, the answer is between 1 and this number
        while min_time <= max_time:
            mid = (max_time + min_time) //2
            if can_repair(cars, ranks, mid):
                max_time = mid - 1
            else:
                min_time = mid + 1
        return min_time