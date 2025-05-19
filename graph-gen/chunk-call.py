from main import Scene, Node, Edge, Cluster, Remove
from pathlib import Path

(
    Scene(
        Cluster("Master", Node("Chunk Reference 1")),
        Cluster("Worker", Node("Process"), Node("Chunk 1")),
        Edge("Chunk Reference 1", "Chunk 1", style="dashed"),
    )
    .scene(
        Remove("Master"),
        Cluster("Master", Node("Chunk Reference 1"), Node("ccall(f, CR1)")),
        Edge("Chunk Reference 1", "ccall(f, CR1)"),
    )
    .scene(
        Remove("Master"),
        Cluster(
            "Master",
            Node("Chunk Reference 1"),
            Node("Chunk Reference 2"),
            Node("ccall(f, CR1)"),
        ),
        Edge("ccall(f, CR1)", "Chunk Reference 2", label="returns"),
        Edge("ccall(f, CR1)", "Process", label="requests"),
    )
    .scene(
        Remove("Master"),
        Cluster(
            "Master",
            Node("Chunk Reference 1"),
            Node("Chunk Reference 2"),
        ),
        Remove(Edge("Chunk Reference 1", "ccall(f, CR1)")),
        Remove(Edge("ccall(f, CR1)", "Chunk Reference 2", label="returns")),
        Remove(Edge("ccall(f, CR1)", "Process", label="requests")),
        Edge("Chunk 1", "Process", label="f(C1)"),
    )
    .scene(
        Remove("Worker"),
        Edge("Process", "Chunk 2", label="returns"),
        Cluster("Worker", Node("Process"), Node("Chunk 1"), Node("Chunk 2")),
        Edge("Chunk Reference 2", "Chunk 2", style="dashed"),
    )
    .scene(
        Remove(Edge("Process", "Chunk 2", label="returns")),
        Remove(Edge("Chunk 1", "Process", label="f(C1)")),
    )
    .render(Path("../assets/graphs/chunk-call.dot"))
)
