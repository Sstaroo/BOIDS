class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge(a, b):
    # Inicializar la lista enlazada resultante
    result = None

    # Mientras ambas listas no estén vacías
    while a is not None and b is not None:
        if a.value > b.value:
            result = ListNode(b.value, result)
            b = b.next
            # next_node = a.next
            # a.next = result
            # result = a
            # a = next_node
        else:
            result = ListNode(a.value, result)
            a = a.next
            # next_node = b.next
            # b.next = result
            # result = b
            # b = next_node

    # Si queda algún nodo en la lista a
    while a is not None:
        result = ListNode(a.value, result)
        a = a.next
        # next_node = a.next
        # a.next = result
        # result = a
        # a = next_node

    # Si queda algún nodo en la lista b
    while b is not None:
        result = ListNode(b.value, result)
        b = b.next
        # next_node = b.next
        # b.next = result
        # result = b
        # b = next_node

    return result

# Función para imprimir la lista enlazada
def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Ejemplo de uso:
# Lista a: 1 -> 3 -> 5
a = ListNode(1)
a.next = ListNode(3)
a.next.next = ListNode(5)

# Lista b: 2 -> 4 -> 6
b = ListNode(2)
b.next = ListNode(4)
b.next.next = ListNode(6)

# Mezclar las listas a y b
result = merge(a, b)
print_list(result)  # Debería imprimir 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> None

