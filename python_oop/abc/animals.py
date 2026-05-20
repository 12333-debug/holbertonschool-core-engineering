#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals."""

    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class that implements sound."""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class that implements sound."""
    def sound(self):
        return "Meow"
