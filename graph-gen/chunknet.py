from main import Scene, Node, Edge, Cluster
from pathlib import Path

(
    Scene(
        Node("Client"),
        Node("Locator"),
        Cluster("Worker 1", Node("Data Store"), Node("Computation Store")),
        Node("Worker 2"),
    )
    .scene(Edge("Client", "Locator", label="GET /locations/"))
    .scene(Edge("Locator", "Client", label="Locations"))
    .scene(
        Edge("Client", "Worker 1", label="Arguments"),
        Edge("Client", "Worker 1", label="Computation"),
    )
    .render(Path("../assets/graphs/chunknet.dot"))
)
