class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse_iterative(self):
        nlist = LinkedList()
        nlist_tail = nlist.head
        self_list_tail = None
        while self_list_tail != self.head:
            cur = self.head
            while cur.next != self_list_tail:
                cur = cur.next
            if cur.next == None:
                nlist.head = Node(cur.data)
                nlist_tail = nlist.head
                self_list_tail = cur
            else:
                nlist_tail.next = Node(cur.data)
                nlist_tail = nlist_tail.next
                nlist_tail.next = None
                self_list_tail = cur
        return nlist

    def reverse_recursive(self):
        nlist = LinkedList()
        if self.head == None:
            return nlist
        elif self.head.next == None:
            nlist.head = Node(self.head.data)
            return nlist
        else:
            current = self.head
            self.head = self.head.next
            nlist = self.reverse_recursive()
            cur = nlist.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(current.data)
            self.head = current
            return nlist

    def reverse_self(self, item, tail=None):
        next = item.next
        item.next = tail
        if next is None:
            self.head = item
            return self
        else:
            return self.reverse_self(next, item)

    def sort_insertion(self):
        nlist = LinkedList()

        if self.head:
            new_node = Node(self.head.data)
            new_node.next = None
            nlist.head = new_node
        else:
            return nlist

        s_cur = self.head
        while s_cur.next:
            s_cur = s_cur.next
            n_cur = nlist.head
            while n_cur.next and (s_cur.data > n_cur.data):
                n_prev = n_cur
                n_cur = n_cur.next
            if s_cur.data <= nlist.head.data:
                new_node = Node(s_cur.data)
                new_node.next = nlist.head
                nlist.head = new_node
            elif s_cur.data <= n_cur.data:
                new_node = Node(s_cur.data)
                new_node.next = n_cur
                n_prev.next = new_node
            elif n_cur.next == None:
                new_node = Node(s_cur.data)
                new_node.next = None
                n_cur.next = new_node
            else:
                print("Something went wrong")

        return nlist

    def merge(self, list):
        merged_list = LinkedList()
        pointer_s = self.head
        pointer_l = list.head
        while pointer_s and pointer_l:
            if pointer_s.data < pointer_l.data:
                merged_list.insert_at_end(pointer_s.data)
                pointer_s = pointer_s.next
            else:
                merged_list.insert_at_end(pointer_l.data)
                pointer_l = pointer_l.next

        while pointer_s:
            merged_list.insert_at_end(pointer_s.data)
            pointer_s = pointer_s.next
        while pointer_l:
            merged_list.insert_at_end(pointer_l.data)
            pointer_l = pointer_l.next

        return merged_list


if __name__ == "__main__":
    # Створюємо зв'язний список
    llist_1 = LinkedList()
    llist_1.insert_at_beginning(5)
    llist_1.insert_at_beginning(10)
    llist_1.insert_at_beginning(15)
    llist_1.insert_at_end(25)
    llist_1.insert_at_end(20)

    print("Зв'язний список: 'llist_1':")
    llist_1.print_list()

    reversed_rec_list = LinkedList()
    reversed_rec_list = llist_1.reverse_recursive()
    print("Зв'язний список 'llist_1' реверсовано рекурсивно 'reversed_rec_list':")
    reversed_rec_list.print_list()

    reversed_iter_list = LinkedList()
    reversed_iter_list = llist_1.reverse_iterative()
    print("Зв'язний список 'llist_1' реверсовано ітеративно 'reversed_iter_list':")
    reversed_iter_list.print_list()

    print("Оригінальний зв'язний список 'llist_1':")
    llist_1.print_list()

    print("Оригінальний зв'язний список 'llist_1' - самореверсований:")
    llist_1.reverse_self(llist_1.head)
    llist_1.print_list()

    # сортуємо перший зв'зний список
    print("Відсортований зв'язний список 'llist_1':")
    list_1_sorted = llist_1.sort_insertion()
    list_1_sorted.print_list()

    # Створюємо другий зв'язний список
    llist_2 = LinkedList()
    print("Зв'язний список 'llist_2':")
    llist_2.insert_at_beginning(7)
    llist_2.insert_at_beginning(9)
    llist_2.insert_at_beginning(12)
    llist_2.insert_at_end(22)
    llist_2.insert_at_end(18)
    llist_2.insert_at_end(16)
    llist_2.insert_at_end(29)
    llist_2.print_list()

    # сортуємо другий зв'язний списки
    print("Відсортований зв'язний список:")
    list_2_sorted = llist_2.sort_insertion()
    list_2_sorted.print_list()

    # об'єднуємо обидва списки
    print("Об'єднаний зв'язний список:")
    merge_list = list_1_sorted.merge(list_2_sorted)
    merge_list.print_list()
