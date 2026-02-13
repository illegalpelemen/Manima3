def list_of_traject():
    list_of_trajectories = [[[0,0],[1,0]] ]
    for a in range(1,5):
        last_trajectory = list_of_trajectories[-1].copy()
        new_point = last_trajectory[-1].copy()
        new_point[0] += 1

        last_trajectory.append(new_point)
        list_of_trajectories.append(last_trajectory)
    return list_of_trajectories