#!/usr/bin/env python3

class SwimMixin:
    """Mixin that adds swimming behavior."""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior."""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon that can swim, fly, and roar."""
    def roar(self):
        print("The dragon roars!")
