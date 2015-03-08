# -*- coding: UTF-8 -*-
class NotEnoughArgsError(Exception):
    """docstring for NotEnoughArgs"""
    def __init__(self, functName):
        self.functName = functName

    def __str__(self):
        return repr(self.functName)


class BadRequestError(Exception):
    """docstring for NotEnoughArgs"""
    pass


class VersionNotSupportedError(Exception):
    """docstring for NotEnoughArgs"""
    pass


class NotImplementedError(Exception):
    """docstring for NotEnoughArgs"""
    pass