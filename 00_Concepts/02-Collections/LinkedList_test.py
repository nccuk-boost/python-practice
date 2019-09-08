import pytest

from LinkedList import List, Element

class TestLinkedList():
    def test_listSetup(self):
        assert callable(List.get_position), "should have function get_position"
        assert callable(List.append), "should have function append"
        assert callable(List.insert), "should have function insert"
        assert callable(List.delete), "should have function delete"

    def test_getPosition(self):
        me = List(values=(1,2,3,4))
        assert me.get_position(1).value == 2, \
            "should return element with value 2 at position 1"   


    def test_listAppend(self):
        me = List()
        me.append(Element(6))
        assert me.get_position(0).value == 6, \
            "should have inserted Element with value 0 at position 0"
        me.append(Element(60))
        assert me.get_position(1).value == 60, \
            "should have inserted Element with value 0 at position 0"
        me.append(Element(16))
        assert me.get_position(2).value == 16, \
            "should have inserted Element with value 0 at position 0"

    def test_listInsert(self):
        me = List(values=(1,2,3,4))
        me.insert(Element(10), 2)
        assert me.get_position(2).value == 10, \
            "should have inserted element with value 10 at position 2"
        assert me.get_position(1).value == 2, \
            "should still have element with value 2 at position 1"
        assert me.get_position(3).value == 3, \
            "should still have element with value 3 at position 3"
        me.insert(Element(42),5)
        assert me.get_position(5).value == 42, \
            "should have inserted element at the end"
        with pytest.raises(ValueError, \
            match="Insert value higher than list length"):  me.insert(Element(99),99)
        with pytest.raises(ValueError, \
            match="Insert value must at least be zero"):  me.insert(Element(-1),-1)

        me.insert(Element(0),0)
        assert me.get_position(0).value == 0, \
            "should have inserted element at the beginning"
        me = List()
        me.insert(Element(-1), 0)
        assert me.get_position(0).value == -1, \
            "should have inserted initial element at the beginning"

    def test_delete(self):
        me = List(values=(1,2,3,4))
        me.delete(2)
        assert me.get_position(1).value == 3, \
            "should show next element on position of deleted element"
        me.delete(1)
        assert me.get_position(0).value == 3, \
            "should delete first element"
        me.delete(4)
        assert me.get_position(0).value == 3, \
            "should delete last element"

        with pytest.raises(ValueError, \
            match="Element 9 not in List"):  me.delete(9)

        me.delete(3)
        with pytest.raises(ValueError, \
            match="No elements in List"):  me.delete(0)

        assert me.get_element(2) == (None, -1), \
            "should not find element with value 2 anymore"


    



# if __name__ == '__main__':
#     testListSetup()
#     testGetPosition()
#     testListAppend()
#     testListInsert()
#     testDelete()
#     print("Yay, everything has passed! 😃")