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
    # Datos de ejemplo
    nodos_principales = ["E1", "E2", "E3", "E4"]  # Estaciones
    nodos_secundarios = ["C1", "C2", "C3"]  # Casas/Destinos

    aristas_hoverboard = [
        ("C1", "E1", 2),
        ("C1", "E2", 3),
        ("C2", "E2", 1),
        ("C2", "E3", 4),
        ("C3", "E3", 2),
        ("C3", "E4", 5),
    ]

    aristas_tranvia = [
        ("E1", "E2", 1),
        ("E2", "E3", 1),
        ("E3", "E4", 1),
        ("E4", "E1", 1),
    ]

    k1 = 10  # Costo por km en hoverboard
    k2 = 20  # Costo por tramo en tranvía

    pares_od = [("C1", "C3"), ("C2", "C1"), ("C3", "C2")]

    resolver_sistema_transporte(
        nodos_principales,
        nodos_secundarios,
        aristas_hoverboard,
        aristas_tranvia,
        k1,
        k2,
        pares_od,
    )


run()
