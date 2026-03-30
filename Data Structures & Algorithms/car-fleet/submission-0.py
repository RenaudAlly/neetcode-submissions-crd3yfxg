class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carFleets = 0
        
        # Sort the cars (getting the car ahead)
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse = True, key = lambda i : i[0])
        
        # Compare the current car against the car at the top of the stack 
        stack = []

        for car in cars:
            # For initializing the stack
            if not stack:
                stack.append(car)
                continue
            
            current_car_eta = (target - car[0]) / car[1] # time = distance / speed
            car_ahead_eta = (target - stack[-1][0]) / stack[-1][1] 

            # If current car's ETA is lesser than or equal to car ahead, move on 
            # Else, add it to the stack
            # Continue looking at cars behind
            if current_car_eta > car_ahead_eta:
                stack.append(car)

        return len(stack)