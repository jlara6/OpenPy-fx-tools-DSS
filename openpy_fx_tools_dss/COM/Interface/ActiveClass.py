# -*- coding: utf-8 -*-
# @Time    : 07/01/2023
# @Author  : Ing. Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : ActiveClass.py
# @Software: PyCharm

from .Base import Base

class ActiveClass(Base):
    """
    This interface can be used to gain access to the features of the active class without having to use a specific interface.
    This interface is embedded within the ActiveCircuit interface, requiring the definition of this interface before getting access the to ActiveClass interface.
    """
    def __init__(self, DSSObject):
        self.Base = Base(DSSObject)
        self.DSSObject = DSSObject
        self.DSSText = self.DSSObject.Text
        self.DSSCircuit = self.DSSObject.ActiveCircuit
        self.DSSActiveClass = self.DSSCircuit.ActiveClass;

    def AllNames(self, ClassName: str = None):
        """
        (read only) - This property returns the names for all the objects defined within the active class.
        The names are returned as an array of string.

        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        return self.Base._tuple_to_list(self.DSSActiveClass.AllNames)

    def First(self, ClassName: str = None):
        """
        (read only) - Sets first element in the active class to be the active DSS object.
        If object is a CktElement, ActiveCktELment also points to this element. Returns 0 if none.

        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        return self.DSSActiveClass.First

    def Next(self, ClassName: str = None):
        """
        (read only) - Sets next element in active class to be the active DSS object.
        If object is a CktElement, ActiveCktElement also points to this element.  Returns 0 if no more.

        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        return self.DSSActiveClass.Next

    def Name_read(self, ClassName: str = None):
        """
        (read/write) - This property is a read/write property that returns the name of the active object within the active class.
        if assigned, it sets the object specified in the given string as the active object.

        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        return self.DSSActiveClass.Name

    def Name_write(self, ClassName: str = None, data: str = None):
        """
        (read/write) - This property is a read/write property that returns the name of the active object within the active class.
        if assigned, it sets the object specified in the given string as the active object.

        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        self.DSSActiveClass.Name = data

    def NumElements(self, ClassName: str = None):
        """
        (read/write) - This property is a read/write property that returns the name of the active object within the active class.
        if assigned, it sets the object specified in the given string as the active object.

        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        return self.DSSActiveClass.NumElements
    def ActiveClassName(self):
        """
        (read/write) - This property is a read/write property that returns the name of the active object within the active class.
        if assigned, it sets the object specified in the given string as the active object.

        :return:
        """
        return self.DSSActiveClass.ActiveClassName

    def Count(self, ClassName: str = None):
        """
        (read only) - Returns the number of elements in the active class. Same as NumElements property.


        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        return self.DSSActiveClass.Count

    def ActiveClassParent(self, ClassName: str = None):
        """
        (read only) - Returns the name of the parent class for the active class.
        For example, the Load class is a child of power conversion elements (PCE), on the other hand,
        the Line class is a child of power delivery elements (PDE).

        :param ClassName:
        :return:
        """
        self.DSSCircuit.SetActiveClass(ClassName)
        return self.DSSActiveClass.ActiveClassParent


