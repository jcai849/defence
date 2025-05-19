from main import Scene, Node, Edge, Cluster, Remove
from pathlib import Path

(
    Scene(
        Cluster(
            "Master",
            Node("dlm(DO1)"),
            Cluster(
                "Distributed Object 1",
                Node("ChunkRef 1"),
                Node("ChunkRef 2"),
                Node("ChunkRef 3"),
            ),
        ),
        Cluster("Worker 1", Node("Chunk 1"), Node("Chunk 2")),
        Cluster("Worker 2", Node("Chunk 3")),
        Edge("ChunkRef 1", "Chunk 1", style="dashed"),
        Edge("ChunkRef 2", "Chunk 2", style="dashed"),
        Edge("ChunkRef 3", "Chunk 3", style="dashed"),
        Edge("Distributed Object 1", "dlm(DO1)"),
    )
    .scene(
        Node("ccall(biglm, CR1)"),
        Edge("dlm(DO1)", "ccall(biglm, CR1)"),
        Edge("ccall(biglm, CR1)", "ChunkRef 1"),
        Node("ChunkRef 4"),
        Edge("ccall(biglm, CR1)", "ChunkRef 4", label="returns"),
    )
    .render(Path("../assets/graphs/dlm.dot"))
)
