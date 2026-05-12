def list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for src, nexts in adj_list.items():
        for dest in nexts:
            matrix[src][dest] = 1
    for row in matrix:
         print(row)          
    return matrix


adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}


adj_matrix = list_to_matrix(adj_list)