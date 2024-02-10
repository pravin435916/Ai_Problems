# 8 Queen problem using DFS
from collections import deque

def print_puzzle(state):
    for row in state:
        print(row)
    print()

def is_goal_state(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_next_states(state):
    i, j = find_empty_tile(state)
    next_states = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for move in moves:
        new_i, new_j = i + move[0], j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row.copy() for row in state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            next_states.append(new_state)
    return next_states

def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        current_state, path = queue.popleft()
        if is_goal_state(current_state):
            return path
        visited.add(tuple(map(tuple, current_state)))
        for next_state in generate_next_states(current_state):
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [next_state]))
    return None

if _name_ == "_main_":
    initial_state =[[1, 2, 3], [4, 8, 5], [7, 6, 0]]
    print("Initial State:")
    print_puzzle(initial_state)
    solution_path = bfs(initial_state)
    if solution_path:
        print("Solution:")
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}:")
            print_puzzle(state)
    else:
        print("No solution found.")
