from main import Scene, Node, Edge, Cluster, Remove
from pathlib import Path

(
    Scene(
        Node("Client"),
        Node("Locator"),
        Cluster(
            "Worker 1",
            Node("Processing"),
            Node("Data Store"),
            Node("Computation Store"),
        ),
        Node("Worker 2"),
        Edge("Worker 2", "Worker 2", label="Computing"),
    )
    .scene(Edge("Client", "Locator", label="GET /locations/"))
    .scene(
        Remove(Edge("Client", "Locator", label="GET /locations/")),
        Edge("Locator", "Client", label="Locations"),
    )
    .scene(
        Remove(Edge("Locator", "Client", label="Locations")),
        Edge("Client", "Processing", label="Computation"),
    )
    .scene(
        Remove(Edge("Client", "Processing", label="Computation")),
        Edge("Processing", "Computation Store", label="Register Computation"),
        Edge("Client", "Processing", label="GET /data"),
    )
    .scene(
        Remove(Edge("Processing", "Computation Store", label="Register Computation")),
        Edge("Processing", "Worker 2", label="GET /data/"),
    )
    .scene(
        Remove(Edge("Worker 2", "Worker 2", label="Computing")),
        Remove(Edge("Processing", "Worker 2", label="GET /data/")),
        Edge("Worker 2", "Worker 2", label="Complete Current Computation"),
    )
    .scene(
        Remove(Edge("Worker 2", "Worker 2", label="Complete Current Computation")),
        Edge("Worker 2", "Worker 2", label="Register Computation output"),
    )
    .scene(
        Remove(Edge("Worker 2", "Worker 2", label="Register Computation output")),
        Edge("Worker 2", "Processing", label="Requested Data"),
    )
    .scene(
        Remove(Edge("Worker 2", "Processing", label="Requested Data")),
        Edge("Processing", "Data Store", label="Register Data"),
    )
    .scene(
        Remove(Edge("Processing", "Data Store", label="Register Data")),
        Edge("Processing", "Computation Store", label="Run Computation"),
    )
    .scene(
        Remove(Edge("Processing", "Computation Store", label="Run Computation")),
        Edge("Processing", "Data Store", label="Register Computation Output"),
    )
    .scene(
        Remove(Edge("Processing", "Data Store", label="Register Computation Output")),
        Edge("Processing", "Client", label="Data"),
    )
    .render(Path("../assets/graphs/chunknet.dot"))
)
