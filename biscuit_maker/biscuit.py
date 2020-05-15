from enum import Enum

class BiscuitStates(Enum):
    NONEXISTENT = "NONEXISTENT"
    DOLLOP = "DOLLOP"
    STAMPED = "STAMPED"
    BAKED_SEMI = "BAKED_SEMI"
    BAKED_FULLY = "BAKED_FULLY"
    BAKED_BURNED = "BAKED_BURNED"


class Biscuit(object):
    """Biscuit base class"""

    def __init__(self):
        """"""
        self._state = BiscuitStates.NONEXISTENT

    def process(self, new_state, **args):
        """Base interface for changing the state of biscuit."""
        self._state = new_state

    def get_state(self):
        """Base interface for reading current biscuit."""
        return self._state
