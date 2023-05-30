"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""
import itertools
import logging
import random
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    node_mapping = {}
    root = None

    with open(path_to_log_file, "r") as file:
        for line in file:
            line = line.strip()

            log_level, log_message = line.split(":", 1)
            log_level = log_level.strip()
            log_message = log_message.strip()

            node_val = int(log_message[log_message.index("[") + 1 : log_message.index("]")])
            left_val = 0
            right_val = 0

            if "left is not empty" in log_message:
                left_val = int(log_message[log_message.index("[", log_message.index("left")) + 1 : log_message.index("]", log_message.index("left"))])
            if "right is not empty" in log_message:
                right_val = int(log_message[log_message.index("[", log_message.index("right")) + 1 : log_message.index("]", log_message.index("right"))])

            node = node_mapping.get(node_val)
            if not node:
                node = BinaryTreeNode(val=node_val)
                node_mapping[node_val] = node

            if left_val:
                left_node = node_mapping.get(left_val)
                if not left_node:
                    left_node = BinaryTreeNode(val=left_val)
                    node_mapping[left_val] = left_node
                node.left = left_node

            if right_val:
                right_node = node_mapping.get(right_val)
                if not right_node:
                    right_node = BinaryTreeNode(val=right_val)
                    node_mapping[right_val] = right_node
                node.right = right_node

            if not root:
                root = node

    return root


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
    )

    root = get_tree(7)
    walk(root)


