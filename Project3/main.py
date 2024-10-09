
# main function to run the algorithm
def water_supply(distances, values, max_distance):
    # Number of wells
    n = len(distances)  

    # backtrack function to calculate the maximum value
    def backtrack(idx, curr_distance, curr_value):
        # maximum value is reached either by reaching the max possible distance or by choosing all wells
        if idx == n or curr_distance == max_distance:
            return curr_value

        # Exclude the current item, i.e. don't build a well at the current location
        exclude_value = backtrack(idx + 1, curr_distance, curr_value)

        # Include the current well if it doesn't exceed the max distance
        if curr_distance + distances[idx] <= max_distance:
            # calculate the value if the current well is included
            include_value = backtrack(idx + 1, curr_distance + distances[idx], curr_value + values[idx])
        else:
            # Exceeds max_distance, assign a very low value
            include_value = float('-inf')

        # Return the maximum value between including and excluding the current well
        return max(exclude_value, include_value)

    # Start backtracking from the first node
    return backtrack(0, 0, 0)


# Example usage
distances = [200, 150, 75, 250, 300, 85, 100, 400, 125, 50]
values = [30, 25, 45, 65, 40, 35, 500, 70, 55, 200000]
max_distance = 200

max_value = water_supply(distances, values, max_distance)
print("Maximum value:", max_value)
