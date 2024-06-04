import math
from Node import Node

def trace_entropy(logs: tuple[dict[Node], dict]) -> float:
    trie, trie_infos = logs
    total = 0
    for node in trie_infos["end_nodes"]:
        total += node.get_end_visits()
    acc = 0.0
    for node in trie_infos["end_nodes"]:
        p = node.get_end_visits() / total
        acc -= p * math.log2(p)
    return acc