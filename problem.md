# Programación con Objetos II (2026)

## TP 2

En una ciudad, para proteger el medio ambiente, se diseñó un nuevo sistema de trasporte, mediante un combinación de hoverboard y tranvía . Se creó una red de tranvía une que puntos relevantes de la ciudad. Cada pasajero viaja en hoverboard desde su origen hasta la estación de tranvía más cercana, vieja en este hasta la estación más cercana a su destino y luego nuevamente en hoverboard hasta su destino. En esta red de transporte existen nodos principales, que corresponden a las estaciones de tranvía y nodos secundarios que corresponden a los puntos definidos como orígenes y destinos de los usuarios del servicio. Por otra parte, existen una camioneta de mantenimiento, que recorre periódicamente las estaciones de tranvía.

El costo que el usuario debe abonar por cada viaje realizado de calcula como

`K1 * kmHB + k2 * tramos`

Donde K1 y k2 son constantes

kmHB es la distancia en km a recorrer en hoverboar tramos es la cantidad de estaciones de tranvía recorridas Se pide modelizar este problema utilizando grafos.

Se desea saber

1. Dado un par origen-destino la ruta de menor costo.

2. La ruta de menor costo para que la camioneta pueda pasar por todas las estaciones.

Mostrar el grafo.

Resolver el problema. Se puede utilizar cualquier librería que maneje grafos, por ejemplo networkx.

Generar por lo menos 2 grafos distintos y para cada uno de ellos 3 pares origen-destino.

El método de ingreso de los datos, queda a criterio de cada grupo.
