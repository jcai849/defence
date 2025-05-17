from dataclasses import dataclass
from typing import override
import graphviz
from pathlib import Path
import math


@dataclass
class Remove:
    target: "Edge | str"


@dataclass
class Node:
    name: str

    def render(self, g: graphviz.graphs.Digraph) -> None:
        g.node(name=self.name)


@dataclass
class Edge:
    start: str
    end: str

    def render(self, g: graphviz.graphs.Digraph) -> None:
        g.edge(tail_name=self.start, head_name=self.end)


@dataclass
class Cluster:
    name: str
    elements: "tuple[Node | Edge | Cluster, ...]"

    def __init__(self, name: str, *elements: "Node | Edge | Cluster"):
        self.name = name
        self.elements = elements

    def render(self, g: graphviz.graphs.Digraph):
        with g.subgraph(name=f"cluster_{self.name}") as c:
            for e in self.elements:
                e.render(c)

    def remove_edge(self, target: Edge) -> "Cluster":
        args: list[Node | Edge | Cluster] = []
        for e in self.elements:
            match e:
                case Cluster():
                    args.append(e.remove_edge(target))
                case _ if target != e:
                    args.append(e)
                case _:
                    pass
        return Cluster(self.name, *args)

    def remove(self, target: str) -> "Cluster":
        args: "list[Node | Edge | Cluster]" = []
        for e in self.elements:
            match e:
                case Node(name=name) if name != target:
                    args += [e]
                case Cluster(name=name) if name != target:
                    args += [e.remove(target)]
                case Edge():
                    args += [e]
                case _:
                    pass
        return Cluster(self.name, *args)


@dataclass
class Scene:
    scene_list: list[tuple[Node | Edge | Cluster | Remove, ...]]

    def __init__(self, *elements: Node | Edge | Cluster | Remove):
        self.scene_list = [elements]

    @classmethod
    def from_scene_list(cls, scene_list):
        s = Scene()
        s.scene_list = scene_list
        return s

    def scene(self, *elements: Node | Edge | Cluster | Remove) -> "Scene":
        self.scene_list += [elements]
        return self

    @override
    def __str__(self) -> str:
        g = graphviz.Digraph()
        for e in self.elements:
            e.render(g)
        return g.source

    def render(self, filepath: Path):
        digits = math.floor(math.log10(len(self.scene_list)))
        filepath.parent.mkdir(parents=True, exist_ok=True)
        for i in range(len(self.scene_list)):
            s = Scene.from_scene_list(self.scene_list[: i + 1])
            file = filepath.with_stem(f"{filepath.stem}_{i + 1:0{digits}d}")
            _ = file.write_text(str(s))

    @property
    def elements(self) -> list[Node | Edge | Cluster]:
        element_list: list[Node | Edge | Cluster] = []
        for scene in self.scene_list:
            additions: list[Node | Edge | Cluster] = []
            removals: list[Node | Edge | Cluster] = []

            for scene_element in scene:
                match scene_element:
                    case Remove(target=Edge()):
                        for element in element_list:
                            match element:
                                case Edge():
                                    removals.append(scene_element.target)  # pyright: ignore
                                case Cluster():
                                    removals.append(element)
                                    additions.append(
                                        element.remove_edge(scene_element.target)  # pyright: ignore
                                    )
                                case _:
                                    pass
                    case Remove(target=target):
                        for element in element_list:
                            match element:
                                case Cluster(name=name) | Node(name=name) if (
                                    name == target
                                ):
                                    removals.append(element)
                                case Cluster(name=name) if name != target:
                                    removals.append(element)
                                    additions.append(element.remove(target))  # pyright: ignore
                                case _:
                                    pass
                    case _:
                        if (
                            scene_element not in element_list
                            and scene_element not in additions
                        ):
                            additions.append(scene_element)

            for item in removals:
                if item in element_list:
                    element_list.remove(item)
            element_list += additions

        return element_list


def main(): ...


if __name__ == "__main__":
    main()
