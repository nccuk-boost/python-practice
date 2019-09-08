class List():
    def __init__(self, head=None, values=()):
        self.head = head
        self.create_list(values)


    def create_list(self, values=()):

        if len(values)>0:
            current =  Element(values[0])
            self.head = current
    

            for val in range(1,len(values)):
                current.next = Element(values[val])
                current = current.next

    
    def get_position(self, position):
        current = self.head
        idx=0

        if self.head:
            while current and idx < position:
                current = current.next
                idx += 1

        return current

    def get_element(self, value):
        current = self.head
        idx=0

        if self.head:
            while current and current.value != value:
                current = current.next
                idx += 1
        if current == None:
            idx = -1
            
        return current, idx

   

            
    def append(self, element):

        current = self.head

        if current:
            while current.next:
                current = current.next
            current.next = element
        else:
            self.head = element 
        

            

    def insert(self, element, position):
        prev = self.head

        if self.head and position>0:
            prev = self.get_position(position-1)
            next = self.get_position(position)

            if prev:
                prev.next = element
                element.next = next
            else:
                raise ValueError("Insert value higher than list length")

        elif position == 0 and self.head:
             next = self.get_position(position)
             self.head = element
             element.next = next
        elif position < 0:
            raise ValueError("Insert value must at least be zero") 
        else:
            self.head = element

                
    
    def delete(self, value):

        elem, pos = self.get_element(value)

        if self.head == None:
            raise ValueError("No elements in List")
        elif elem == None:
            raise ValueError(f"Element {value} not in List")
        else:
            if pos == 0:
                self.head = self.head.next
            else:         
                prev = self.get_position(pos-1)
                next = self.get_position(pos+1)
                prev.next = next

        return elem
                

class Element():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    