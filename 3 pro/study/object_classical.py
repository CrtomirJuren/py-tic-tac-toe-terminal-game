class Obj(object):
    """property demo"""
    def __init__(self, new_attribute = None):
        self._attribute = new_attribute
    
    #
    @property            # first decorate the getter method
    def attribute(self): # This getter method name is *the* name
        return self._attribute
    #
    
    @attribute.setter    # the property decorates with `.setter` now
    def attribute(self, value):   # name, e.g. "attribute", is the same
        self._attribute = value   # the "value" name isn't special

    #
    @attribute.deleter     # decorate with `.deleter`
    def attribute(self):   # again, the method name is the same
        del self._attribute

if __name__ == '__main__':
    obj = Obj()
    
    obj.attribute = 1  
    print(obj.attribute)
    
    # del obj.attribute
    # print(obj.attribute)