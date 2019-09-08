from ClassyCases import Classy as ClassyCases
from ClassyTuple import Classy as ClassyTuple

def testClassiness(me):

    assert me.items == [], "should have an items list"

    assert hasattr(me, "getClassiness") , "should have function"
    assert callable(me.getClassiness) , "should have function getClassiness"
    assert callable(me.addItem) , "should have function addItem"

    assert me.getClassiness() == 0, "Should be 0"
    me.addItem('tophat')
    assert me.getClassiness() == 2, "'tophat' should add 2"
    me.addItem('monocle')
    assert me.getClassiness() == 7, "'monocle' should add 5"
    me.addItem('bowtie')
    assert me.getClassiness() == 11, "'bowtie' should add 4"
    me.addItem('undefined item')
    assert me.getClassiness() == 11,  "undefined item should add 0"

    assert me.items == ["tophat","monocle", "bowtie", "undefined item"], \
        "should have added all the items"




if __name__ == '__main__':
  

    testClassiness(ClassyCases())
    testClassiness(ClassyTuple())
    print("Yay, everything has passed! 😃")