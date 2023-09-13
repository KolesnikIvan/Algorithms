"""
self made python linked list
sources 
https://www.techiedelight.com/ru/linked-list-implementation-python/
https://habr.com/ru/companies/otus/articles/470828/
"""


import random
from typing import Any
import uuid

class Node:
    def __init__(self, data: Any, uid: uuid.uuid4(), next_uid=None) -> None:
        self.data = data
        self.uid = uid
        self.next_uid = next_uid

class LinkedList:
    def __init__(self, header: uuid.UUID = None) -> None:
        self.header = header    # указатель на начальный элемент связного списка
        self.linked_list: tuple[Node] = tuple() # кортеж узлов списка; контейнер нужен для хранения списка

    def __str__(self):
        result_string = str([(item.data, item.uid) for item in self.linked_list])
        return result_string
    
    def contain(self, uid) -> bool:
        """returns True, if LinkedList contains uid"""
        pointer: uuid.UUID = self.header
        while pointer is not None:
            for nd in self.linked_list:
                if nd.uid == uid:
                    return True
                elif nd.uid == pointer:
                    pointer = nd.next_uid
                    break
            else:
                raise Exception("Not found header in linked list")
        return False

    def append(self, new_value: Node) -> None:
        """Добавляет к связному списку элемент с заданным значением new_value"""
        new_uid = uuid.uuid4()
        new_node = Node(data=new_value, uid=new_uid)
        if len(self.linked_list) == 0:
            self.linked_list = new_node,
            self.header = new_uid
        else:
            last_node = self.get_item_by_idx(len(self.linked_list) - 1)
            self.linked_list = *self.linked_list, new_node
            last_node.next_uid = new_uid

    def get_item_by_idx(self, idx) -> Node:
        """Возвращает элемент связного списка по порядковому номеру"""
        pointer = self.header
        counter = 0
        while pointer is not None:
            for node in self.linked_list:
                if node.uid == pointer:
                    if counter == idx:
                        return node
                    else:
                        counter += 1
                        pointer = node.next_uid
                        break
            if counter == idx and pointer is None:
                return node
        raise IndexError("Index out of range. The LinkedList is shorter than given index.")
    
    def get_item_by_uid(self, uid):
        """Возвращает узел по идентификатору"""
        pointer = self.header
        for node in self.linked_list:
            if node.uid == pointer:
                # можно бы сразу проверять совпадение с искомым uid
                if node.uid == uid:
                    # но моделирется итерацию не по кортежу, а по указателям узлов на последующий узел
                    return node
                else:
                    pointer = node.next_uid
        raise Exception(f"No uid {uid} found")
            

    def __next__(self):
        pointer = self.header
        while pointer is not None:
            try:
                for node in self.linked_list:
                    if node.uid == pointer:
                        return node
            finally:
                pointer = node.next_uid
        raise StopIteration
    
    def insert(self, idx: int, new_value: Any) -> None:
        new_uid = uuid.uuid4()
        if idx == 0:
            previous_node = self.get_item_by_idx(0)
            new_node = Node(data=new_value, uid=new_uid, next_uid=self.header)
            self.header = new_uid
        else:
            previous_node = self.get_item_by_idx(idx - 1)
            new_node = Node(data=new_value, uid=new_uid, next_uid=previous_node.next_uid)
            previous_node.next_uid = new_uid
            self.linked_list = *self.linked_list, new_node
        
    def remove(self, idx: int) -> None:
        """Удаляет элемент связного списка с указнным порядковым номером"""
        node_to_delete = self.get_item_by_idx(idx)
        previous_node = self.get_item_by_idx(idx - 1)
        previous_node.next_uid = node_to_delete.next_uid
        for num, node in enumerate(self.linked_list):
            if node.uid == node_to_delete.uid:
                self.linked_list = *self.linked_list[:num], *self.linked_list[num+1:]
                break
                    

if __name__ == "__main__":
    llist = LinkedList()
    for _ in range(random.randint(15, 30)):
        llist.append(random.randint(3, 30))
    print(*str(llist).split(), sep="\n")

    pos = len(llist.linked_list) // 2
    llist.remove(pos)
    print(*str(llist).split(), sep="\n")

    new_value = 153
    pos = len(llist.linked_list) // 2
    llist.insert(pos, new_value=new_value)
    print(*str(llist).split(), sep="\n")
    print(llist.contain(random.choice(llist.linked_list)))

    for node in llist.linked_list:
        print(node.data, node.uid, node.next_uid)
