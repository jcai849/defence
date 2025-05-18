from main import Scene, Node, Edge, Cluster, Remove
from pathlib import Path

(
    Scene(
        Cluster(
            "Distributed Object 1",
            Node("ChunkRef 1"),
            Node("ChunkRef 2"),
            Node("ChunkRef 3"),
            Node("ChunkRef 4"),
        ),
        Cluster("Worker 1", Node("Chunk 1"), Node("Chunk 4")),
        Cluster("Worker 2", Node("Chunk 3")),
        Cluster("Worker 3", Node("Chunk 2")),
        Edge("ChunkRef 1", "Chunk 1", style="dashed"),
        Edge("ChunkRef 2", "Chunk 2", style="dashed"),
        Edge("ChunkRef 3", "Chunk 3", style="dashed"),
        Edge("ChunkRef 4", "Chunk 4", style="dashed"),
    )
    .scene(
        Node("ccall"),
        Edge("ChunkRef 1", "ccall"),
        Edge("Chunk 1", "ccall", label="biglm"),
    )
    .scene(
        Remove(Edge("ChunkRef 1", "ccall")),
        Remove(Edge("Chunk 1", "ccall", label="biglm")),
        Node("ChunkRef 5"),
        Remove("Worker 1"),
        Cluster("Worker 1", Node("Chunk 1"), Node("Chunk 4"), Node("Chunk 5")),
        Edge("ccall", "Chunk 5"),
        Edge("ccall", "ChunkRef 5"),
        Edge("ChunkRef 5", "Chunk 5", style="dashed"),
    )
    .scene(
        Remove(Edge("ccall", "Chunk 5")),
        Remove(Edge("ccall", "ChunkRef 5")),
        Edge("ChunkRef 2", "ccall"),
        Edge("Chunk 2", "ccall", label="update"),
        Edge("ChunkRef 5", "ccall"),
        Edge("Chunk 5", "ccall", label="update"),
    )
    .scene(
        Remove(Edge("ChunkRef 2", "ccall")),
        Remove(Edge("Chunk 2", "ccall", label="update")),
        Remove(Edge("ChunkRef 5", "ccall")),
        Remove(Edge("Chunk 5", "ccall", label="update")),
        Remove("Worker 3"),
        Cluster("Worker 3", Node("Chunk 2"), Node("Chunk 6")),
        Node("ChunkRef 6"),
        Edge("ccall", "Chunk 6"),
        Edge("ccall", "ChunkRef 6"),
        Edge("ChunkRef 6", "Chunk 6", style="dashed"),
    )
    .scene(
        Remove(Edge("ccall", "Chunk 6")),
        Remove(Edge("ccall", "ChunkRef 6")),
        Edge("ChunkRef 3", "ccall"),
        Edge("Chunk 3", "ccall", label="update"),
        Edge("ChunkRef 6", "ccall"),
        Edge("Chunk 6", "ccall", label="update"),
    )
    .scene(
        Remove(Edge("ChunkRef 3", "ccall")),
        Remove(Edge("Chunk 3", "ccall", label="update")),
        Remove(Edge("ChunkRef 6", "ccall")),
        Remove(Edge("Chunk 6", "ccall", label="update")),
        Remove("Worker 2"),
        Cluster("Worker 2", Node("Chunk 3"), Node("Chunk 7")),
        Node("ChunkRef 7"),
        Edge("ccall", "Chunk 7"),
        Edge("ccall", "ChunkRef 7"),
        Edge("ChunkRef 7", "Chunk 7", style="dashed"),
    )
    .scene(
        Remove(Edge("ccall", "Chunk 7")),
        Remove(Edge("ccall", "ChunkRef 7")),
        Edge("ChunkRef 4", "ccall"),
        Edge("Chunk 4", "ccall", label="update"),
        Edge("ChunkRef 7", "ccall"),
        Edge("Chunk 7", "ccall", label="update"),
    )
    .scene(
        Remove(Edge("ChunkRef 4", "ccall")),
        Remove(Edge("Chunk 4", "ccall", label="update")),
        Remove(Edge("ChunkRef 7", "ccall")),
        Remove(Edge("Chunk 7", "ccall", label="update")),
        Remove("Worker 1"),
        Cluster(
            "Worker 1",
            Node("Chunk 1"),
            Node("Chunk 4"),
            Node("Chunk 5"),
            Node("Chunk 8"),
        ),
        Node("ChunkRef 8"),
        Edge("ccall", "Chunk 8"),
        Edge("ccall", "ChunkRef 8"),
        Edge("ChunkRef 8", "Chunk 8", style="dashed"),
    )
    .scene(
        Remove(Edge("ccall", "Chunk 8")),
        Remove(Edge("ccall", "ChunkRef 8")),
        Remove("ccall"),
        Remove("ChunkRef 5"),
        Remove("ChunkRef 6"),
        Remove("ChunkRef 7"),
        Remove("ChunkRef 8"),
        Remove("Chunk 5"),
        Remove("Chunk 6"),
        Remove("Chunk 7"),
        Remove(Edge("ChunkRef 5", "Chunk 5", style="dashed")),
        Remove(Edge("ChunkRef 6", "Chunk 6", style="dashed")),
        Remove(Edge("ChunkRef 7", "Chunk 7", style="dashed")),
        Cluster("Distributed Object 2", Node("ChunkRef 8")),
    )
    .render(Path("../assets/graphs/dlm.dot"))
)
