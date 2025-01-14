# Problema:
#Você é responsável por planejar a rota de um motorista que deseja viajar de uma cidade a outra, utilizando o menor caminho possível em termos de distância. O grafo das cidades e estradas é representado por um dicionário, onde as chaves são os nomes das cidades e os valores são as distâncias para as cidades vizinhas.

#Requisitos:
#Desenvolver uma função que calcule a menor distância entre duas cidades.
#Exibir o caminho detalhado da rota.

import heapq

def dijkstra(graph, start, goal):
    # Inicializa a fila de prioridade e as distâncias
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distances = {city: float('inf') for city in graph}
    distances[start] = 0
    previous_nodes = {city: None for city in graph}

    while priority_queue:
        current_distance, current_city = heapq.heappop(priority_queue)

        # Se chegarmos à cidade-alvo, paramos
        if current_city == goal:
            break

        # Verifica os vizinhos da cidade atual
        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight

            # Se encontrarmos um caminho mais curto
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_city
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstrói o caminho da cidade-alvo até a cidade de partida
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    path.reverse()
    return distances[goal], path

# Grafo representando cidades e distâncias (em km)
graph = {
    'A': {'B': 5, 'D': 9, 'E': 2},
    'B': {'A': 5, 'C': 2},
    'C': {'B': 2, 'D': 3},
    'D': {'A': 9, 'C': 3, 'F': 2},
    'E': {'A': 2, 'F': 3},
    'F': {'D': 2, 'E': 3}
}

# Definindo a cidade de partida e destino
start_city = 'A'
goal_city = 'F'

# Calculando o menor caminho
distance, path = dijkstra(graph, start_city, goal_city)

# Exibindo o resultado
print(f"A menor distância de {start_city} para {goal_city} é {distance} km.")
print(f"O caminho é: {' -> '.join(path)}")
