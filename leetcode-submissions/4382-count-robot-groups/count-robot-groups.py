class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(speed)
        if n == 0:
            return 0

        # Step 1: Group adjacent robots that merge at t = 0 (distance <= distance)
        # Each group takes the speed of its rightmost robot.
        initial_groups_speed = []
        i = 0
        while i < n:
            j = i
            # Expand the component as long as adjacent robots are within distance
            while j + 1 < n and (position[j + 1] - position[j]) <= distance:
                j += 1
            # The rightmost robot in this t=0 component sets the group's speed
            initial_groups_speed.append(speed[j])
            i = j + 1

        # Step 2: Traverse the t=0 groups right-to-left to simulate movement over time
        grp = 1
        curr_speed = initial_groups_speed[-1]

        for k in range(len(initial_groups_speed) - 2, -1, -1):
            if initial_groups_speed[k] > curr_speed:
                # Left group is faster, so it catches up to the right group
                continue
            else:
                # Left group cannot catch up; forms a new independent group
                grp += 1
                curr_speed = initial_groups_speed[k]

        return grp