#!/usr/bin/env python3
def uppercase(c):
    if ord('a') <= ord(c) <= ord('z'):
        return chr(ord(c) - 32)
    return c
