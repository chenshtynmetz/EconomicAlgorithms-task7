import networkx as nx
import pulp as p


# this function finds an egalitarian room division out of all the divisions without envy
def egalitarianRent(values: list[list[float]], rent: float):
    """"
     >>> [egalitarianRent([[3, 4, 5], [5, 2, 3], [7, 1, 3]], 3000)]
     [['person 2 get room 0 in price: 1003.0', 'person 1 get room 1 in price: 998.0', 'person 0 get room 2 in price: 999.0']]
     >>> [egalitarianRent([[12, 6, 13, 1], [5, 7, 11, 2], [8, 1, 11, 12], [12, 12, 3, 2]], 7000)]
     [['person 0 get room 0 in price: 1752.5', 'person 3 get room 1 in price: 1749.5', 'person 1 get room 2 in price: 1753.5', 'person 2 get room 3 in price: 1744.5']]
     >>> [egalitarianRent([[50, 1, 1, 1], [35, 3, 4, 2], [28, 1, 5, 1], [32, 2, 3, 2]], 5000)]
     [['person 0 get room 0 in price: 1285.75', 'person 1 get room 1 in price: 1236.75', 'person 2 get room 2 in price: 1240.75', 'person 3 get room 3 in price: 1236.75']]
    """
    # find divisions without envy by find a division that maximizes the values
    # we do this by build graph and find max matching with networkx
    g = nx.Graph()
    for i in range(0, len(values)):
        for j in range(0, len(values[0])):
            g.add_edge('person ' + str(i), 'room ' + str(j), weight=values[i][j])
    alloc = nx.max_weight_matching(g)
    # insert the matching into sorted dictionary
    dic_match = {}
    for i in range(0, len(alloc)):
        curr = alloc.pop()
        if "room" in curr[0]:
            flag = 0
        else:
            flag = 1
        str_split = curr[flag].split(" ")
        str_split2 = curr[(flag + 1) % 2].split(" ")
        dic_match[int(str_split[1])] = int(str_split2[1])
    # find an egalitarian division by linear programming
    Lp_prob = p.LpProblem('Problem', p.LpMaximize)
    list_var = []  # list of all the 'p' variables that present the price for any room
    for i in range(0, len(dic_match)):
        list_var.append(p.LpVariable("p" + str(i)))  # create all the 'p' variables
    z = p.LpVariable("z")  # this variable care for the minimum
    # Constraints
    for j in range(0, len(dic_match)):
        Lp_prob += z <= (values[dic_match[j]][j] - list_var[j])  # z need to be the minimum
    # make sure that this without envy
    for j in range(0, len(dic_match)):
        for i in range(0, len(dic_match)):
            Lp_prob += (values[dic_match[j]][j] - list_var[j]) >= (values[dic_match[j]][i] - list_var[i])
    # the sum of all the 'p' variables need to be equal to the rent
    sum_p = 0
    for i in range(0, len(list_var)):
        sum_p += list_var[i]
    Lp_prob += sum_p == rent
    status = Lp_prob.solve()  # Solver
    # enter the answer to new dictionary
    ans_dic = {}
    for i in range(0, len(dic_match)):
        ans_dic[i] = "person " + str(dic_match[i]) + " get room " + str(i) + " in price: " + str(list_var[i].value())
    return list(ans_dic.values())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
