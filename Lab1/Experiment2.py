from collections import deque
from math import gcd

def water_jug(cap_a, cap_b, goal):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()
        if a == goal or b == goal:
            return path

        moves = [
            (cap_a, b),  # fill jug 1
            (a, cap_b),  # fill jug 2
            (0, b),      # empty jug 1
            (a, 0),      # empty jug 2
            (a - min(a, cap_b - b), b + min(a, cap_b - b)),  # pour jug 1 into jug 2
            (a + min(b, cap_a - a), b - min(b, cap_a - a)),  # pour jug 2 into jug 1
        ]
        for state in moves:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None

print(" ------Water Jug Problem ----")
cap_a = int(input("Enter capacity of Jug 1 (liters): "))
cap_b = int(input("Enter capacity of Jug 2 (liters): "))
goal = int(input("Enter the goal amount (liters): "))

if cap_a <= 0 or cap_b <= 0 or goal < 0:
    print("Please enter positive numbers ")
elif goal > max(cap_a, cap_b) or goal % gcd(cap_a, cap_b) != 0:
    print("This goal is not possible with these jug sizes.")
else:
    solution = water_jug(cap_a, cap_b, goal)
    print(f"\nJug 1 = {cap_a}L, Jug 2 = {cap_b}L, Goal = {goal}L")
    for step, (a, b) in enumerate(solution):
        print(f"Step {step}: Jug 1 = {a}, Jug 2 = {b}") 