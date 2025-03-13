
from enum import EnumMeta
class EnumContainsMeta(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        else:
            return True