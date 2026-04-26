graph = {
0: [1, 3],
1: [2, 3],
2: [0],
3: [4, 2],
4: [0],
}

if len(graph) > 15:
    print("Слишком большой граф")



Sicles = []

def searching_easy_ways(current_dot, start_dot, visited_dots, K):
    if len(visited_dots) >= K:
        return

    for neighbor in graph[current_dot]:
        if neighbor == start_dot and len(visited_dots) > 1:
            sicle = visited_dots + [start_dot]
            print(sicle)
            Sicles.append(sicle)

        if neighbor not in visited_dots:
            searching_easy_ways(neighbor, start_dot, visited_dots+[neighbor], K)


K=3
searching_easy_ways(0,0,[0], K)



def delete_dublicats(sicle):
    sicle = sicle[:-1]
    min_figure_in_sicle = min(sicle)
    min_index = sicle.index(min_figure_in_sicle)
    new_sicle = sicle[min_index:] + sicle[:min_index]
    return new_sicle + [new_sicle[0]]


def Normalizing_Sicles(Sicles):
    clean_Sicles = []
    for s in Sicles:
        clean_Sicle = delete_dublicats(s)

        if clean_Sicle not in clean_Sicles:
            clean_Sicles.append(clean_Sicle)
    print(clean_Sicles)
    print(len(clean_Sicles))
    print(len(clean_Sicles) > 0)


Normalizing_Sicles(Sicles)






