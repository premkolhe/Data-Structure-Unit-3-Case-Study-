# Stack and Queue implementation using singly linked lists


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    """Stack follows LIFO: Last In, First Out."""

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {value} onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Nothing to pop.")
            return None

        value = self.top.data
        self.top = self.top.next
        print(f"Popped {value} from the stack.")
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None

        print(f"Top of stack: {self.top.data}")
        return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        current = self.top
        print("Stack (top to bottom):", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class LinkedListQueue:
    """Queue follows FIFO: First In, First Out."""

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(f"Enqueued {value} into the queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
            return None

        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"Dequeued {value} from the queue.")
        return value

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None

        print(f"Front of queue: {self.front.data}")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        current = self.front
        print("Queue (front to rear):", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def main():
    print("STACK OPERATIONS")
    stack = LinkedListStack()
    stack.push("Book A")
    stack.push("Book B")
    stack.push("Book C")
    stack.display()
    stack.peek()
    stack.pop()
    stack.display()

    print("\nQUEUE OPERATIONS")
    queue = LinkedListQueue()
    queue.enqueue("Customer 1")
    queue.enqueue("Customer 2")
    queue.enqueue("Customer 3")
    queue.display()
    queue.peek()
    queue.dequeue()
    queue.display()


if __name__ == "__main__":
    main()