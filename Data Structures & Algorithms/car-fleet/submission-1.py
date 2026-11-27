class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create pairs of position and speed, sort them in reverse order of position 
        #so that we can process the cars from the closest to the target to the farthest
        cars = sorted(zip(position, speed), reverse=True) # O(n log n) for sorting
        stack = []
        for pos, spd in cars:
            #calculate the time it takes for the car to reach the target
            time = (target - pos) / spd # decimal division to get float time
            stack.append(time)
            # if at least two cars are in the stack and the last car's time 
            # is less than or equal to the second last car's time, remove the last car from the stack
            # since it will catch up to the second last car and form a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)