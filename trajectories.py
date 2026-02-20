import random
def list_of_traject():
    list_of_trajectories = [[[0,0],[1,0]] ]
    for a in range(1,25):
        last_trajectory = list_of_trajectories[-1]
        new_trajectory = last_trajectory.copy()
        new_point = last_trajectory[-1].copy()
        new_point[random.randint(0,1)] += random.randint(1,3)

        new_trajectory.append(new_point)
        list_of_trajectories.append(new_trajectory)
    return list_of_trajectories