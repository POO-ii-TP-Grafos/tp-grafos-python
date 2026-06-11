import json

import matplotlib.pyplot as plt
import networkx as nx


def resolver_sistema_transporte(
    nodos_principales,
    nodos_secundarios,
    aristas_hoverboard,
    aristas_tranvia,
    k1,
    k2,
    pares_od,
):
    # Crea el grafo
    G = nx.Graph()

    # Nodos con atributos para diferenciarlos
    for n in nodos_principales:  # Estaciones
        G.add_node(n, tipo="principal", color="orange")
    for n in nodos_secundarios:  # Orígenes y destinos de los pasajeros
        G.add_node(n, tipo="secundario", color="skyblue")

    # Aristas de hoverboard
    for u, v, km in aristas_hoverboard:
        costo = k1 * km
        G.add_edge(u, v, weight=costo, tipo="hoverboard", info=f"{km}km")

    # Aristas de tranvía
    for u, v, tramos in aristas_tranvia:
        costo = k2 * tramos
        G.add_edge(u, v, weight=costo, tipo="tranvia", info=f"{tramos} tr")

    # Punto 1: Rutas menor costo
    print("--- RUTAS DE MENOR COSTO PARA PASAJEROS ---")
    for orig, dest in pares_od:
        try:
            camino = nx.shortest_path(G, source=orig, target=dest, weight="weight")
            costo_total = nx.shortest_path_length(
                G, source=orig, target=dest, weight="weight"
            )
            print(
                f"Ruta desde {orig} hasta {dest}: {' -> '.join(camino)} | Costo Total: ${costo_total:.2f}"
            )
        except nx.NetworkXNoPath:
            print(f"No existe ruta entre {orig} y {dest}")

    # Punto 2: Ruta camioneta de mantenimiento (TSP) ---
    print("\n--- RUTA DE CAMIONETA DE MANTENIMIENTO ---")
    # Extraemos el subgrafo de las estaciones
    subgrafo_estaciones = G.subgraph(nodos_principales)

    # NetworkX tiene un algoritmo para aproximar el TSP
    try:
        ruta_mantenimiento = nx.approximation.traveling_salesperson_problem(
            subgrafo_estaciones, weight="weight", cycle=True
        )
        print(f"Ruta de la camioneta (Ciclo): {' -> '.join(ruta_mantenimiento)}")
    except Exception:
        print(
            "Asegurate de que todas las estaciones estén conectadas entre sí para el TSP."
        )

    # Dibujar el grafo
    pos = nx.spring_layout(G, seed=42)
    colores = [G.nodes[n]["color"] for n in G.nodes]

    plt.figure(figsize=(10, 7))
    nx.draw_networkx_nodes(G, pos, node_color=colores, node_size=700)
    nx.draw_networkx_labels(G, pos, font_weight="bold")

    # Dibujar aristas según el tipo
    aristas_hb = [(u, v) for u, v, d in G.edges(data=True) if d["tipo"] == "hoverboard"]
    aristas_tr = [(u, v) for u, v, d in G.edges(data=True) if d["tipo"] == "tranvia"]

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=aristas_hb,
        width=2,
        edge_color="gray",
        style="dashed",
        label="Hoverboard",
    )
    nx.draw_networkx_edges(
        G, pos, edgelist=aristas_tr, width=4, edge_color="red", label="Tranvía"
    )

    # Etiquetas de peso
    labels = nx.get_edge_attributes(G, "weight")
    labels_redondeadas = {k: f"${v:.1f}" for k, v in labels.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels_redondeadas)

    plt.legend(["Estaciones (Nodos Principales)", "Casas/Destinos (Nodos Secundarios)"])
    plt.title("Red de Transporte Multimodal")
    plt.axis("off")
    plt.show()


def run():
    with open(
        "./src/input.json",
        "r",
        encoding="utf-8",
    ) as file:
        input = json.load(file)

    primary_nodes = input["nodes"]["primary"]
    secondary_nodes = input["nodes"]["secondary"]

    edges_hoverboard_raw = input["edges"]["hoverboard"]

    edges_hoverboard = []

    for edge in edges_hoverboard_raw:
        origin = edge["origin"]
        destiny = edge["destiny"]
        distance = edge["distance"]
        edges_hoverboard.append((origin, destiny, distance))

    edges_tram_raw = input["edges"]["tram"]

    edges_tram = []

    for edge in edges_tram_raw:
        origin = edge["origin"]
        destiny = edge["destiny"]
        distance = edge["distance"]
        edges_tram.append((origin, destiny, distance))

    cost_per_kilometer = input["cost_per_kilometer"]
    k1 = cost_per_kilometer["hoverboard"]
    k2 = cost_per_kilometer["tram"]

    pairs = []

    pairs_raw = input["pairs"]

    for pair in pairs_raw:
        origin = pair["origin"]
        destiny = pair["destiny"]
        pairs.append((origin, destiny))

    resolver_sistema_transporte(
        primary_nodes, secondary_nodes, edges_hoverboard, edges_tram, k1, k2, pairs
    )


run()
