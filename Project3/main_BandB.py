
# Branch and bound algorithm for the water supply problem
def water_supply_branch_and_bound(distances, values, max_distance):
    # Create a list of (weight, value) tuples
    items = list(zip(distances, values))
    # Number of items
    n = len(items)
    # Maximum value found so far (initializing it to zero)
    max_value = 0
    # List to track selected items
    selected_items = []

    # backtrack function to calculate the upper bound value
    def calculate_bound(node, curr_distance, curr_value):
        # initialize bound_value to current value
        bound_value = curr_value
        # initialize remaining max_distance to max_distance (since curr_distance is zero at start)
        remaining_max_distance = max_distance - curr_distance

        # Consider the remaining wells and their fractional values
        for i in range(node, n):
            # if the current distance is less than the remaining max_distance, include the well
            if items[i][0] <= remaining_max_distance:
                # update the bound_value
                bound_value += items[i][1]
                # update the remaining max_distance
                remaining_max_distance -= items[i][0]
            # if the current distance is greater than the remaining max_distance, include a fraction of the well
            else:
                fraction = remaining_max_distance / items[i][0]
                bound_value += items[i][1] * fraction
                break

        return bound_value

    # Helper function for branch and bound
    def branch_and_bound(node, curr_distance, curr_value, selected):
        # declare max_value as nonlocal
        nonlocal max_value, selected_items

        # If the current distance exceeds max_distance, return
        if curr_distance > max_distance:
            return None

        # If all items are processed, update max_value
        if node == n:
            max_value = max(max_value, curr_value)
            selected_items = selected[:]
            return None

        # Calculate the upper bound value
        bound_value = calculate_bound(node, curr_distance, curr_value)

        # If the upper bound value is less than the max_value, return
        if bound_value < max_value:
            return None

        # Explore the left subtree by excluding the current well
        branch_and_bound(node + 1, curr_distance, curr_value, selected)

        # Explore the right subtree by including the current well
        selected.append(node)
        branch_and_bound(node + 1, curr_distance + items[node][0], curr_value + items[node][1], selected)
        selected.pop()

    # Start branch and bound from the root node
    branch_and_bound(0, 0, 0, [])

    return max_value, selected_items


# Example usage
distances = [200, 150, 75, 250, 300, 85, 100, 400, 125, 50]
values = [30, 25, 45, 65, 40, 213213, 500, 70, 55, 200000]
max_distance = 200

max_value, selected_items = water_supply_branch_and_bound(distances, values, max_distance)
print("Maximum value:", max_value)
print("Selected items:", selected_items)
