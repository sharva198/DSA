class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List (Appends elements)
    def create_list(self, elements):
        for item in elements:
            new_node = Node(item)
            if not self.head:
                self.head = new_node
            else:
                curr = self.head
                while curr.next:
                    curr = curr.next
                curr.next = new_node
        print("Linked List created successfully.")

    # 2. Traverse and print the node values
    def traverse(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(res) + " -> None")

    # 3. Insert node at a specific position (1-indexed)
    def insert_at_position(self, pos, data):
        new_node = Node(data)
        if pos == 1: 
            new_node.next = self.head
            self.head = new_node
            print(f"Inserted {data} at position 1.")
            return

        curr = self.head
        for _ in range(pos - 2):
            if curr is None:
                print("Position out of bounds.")
                return
            curr = curr.next

        if curr is None:
            print("Position out of bounds.")
            return

        new_node.next = curr.next
        curr.next = new_node
        print(f"Inserted {data} at position {pos}.")

    # 4. Find Middle node and print its value
    def find_middle( self):
        if not self.head:
            print("List is empty.")
            return
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"Middle node value: {slow.data}")

    # 5. Delete node by value
    def delete_node(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            print(f"Deleted node with value {key}.")
            return

        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if not curr:
            print(f"Value {key} not found in the list.")
            return

        prev.next = curr.next
        print(f"Deleted node with value {key}.")

    # 6. Reverse list
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        print("Linked List reversed.")

    # 7. Calculate the sum of every two consecutive node values
    def sum_consecutive_nodes(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        sums = []
        while curr and curr.next:
            s = curr.data + curr.next.data
            sums.append(s)
            curr = curr.next.next
        
        # If there's a leftover single node at the end
        if curr:
            sums.append(curr.data)
            
        print("Sum of every two consecutive nodes:", sums)

# --- Driver Code / Demonstration ---
if __name__ == "__main__":
    ll = SinglyLinkedList()

    print("--- 1. Create Linked List ---")
    ll.create_list([10, 20, 30, 40, 50])

    print("\n--- 2. Traverse and Print ---")
    ll.traverse()

    print("\n--- 3. Insert at Specific Position (Pos 3, Val 25) ---")
    ll.insert_at_position(3, 25)
    ll.traverse()

    print("\n--- 4. Find Middle Node ---")
    ll.find_middle()

    print("\n--- 5. Delete Node (Val 20) ---")
    ll.delete_node(20)
    ll.traverse()

    print("\n--- 6. Reverse List ---")
    ll.reverse()
    ll.traverse()

    print("\n--- 7. Sum of Every Two Consecutive Nodes ---")
    ll.sum_consecutive_nodes()