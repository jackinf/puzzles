def numberOfConnections(gridOfNodes):
    # time complexity O(n^2)
    connections = 0
    if len(gridOfNodes) <= 1:
        return connections

    prev_nodes_sum = sum([x for x in gridOfNodes[0] if x == 1])
    for row in gridOfNodes[1:]:
        curr_nodes_sum = sum([x for x in row if x == 1])
        if curr_nodes_sum > 0:
            connections += prev_nodes_sum * curr_nodes_sum
            prev_nodes_sum = curr_nodes_sum
    return connections


if __name__ == "__main__":
    grid1 = [[1, 0, 1, 1], [0, 1, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0]]
    print(numberOfConnections(grid1))  # 8