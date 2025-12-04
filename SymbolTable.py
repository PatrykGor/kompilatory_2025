#!/usr/bin/python


class Symbol:
    def __init__(self, name, obj_type):
        self.name = name
        self.type = obj_type

class SymbolTable(object):
    def __init__(self, parent=None, name="scope"):
        self.parent = parent          # parent scope
        self.name = name              # scope name (optional)
        self.symbols = {}             # dictionary: name → symbol

    def put(self, name, symbol):
        """Insert or overwrite a symbol in the current scope."""
        self.symbols[name] = symbol

    def get(self, name):
        """Lookup a symbol in this scope, then recursively in parents."""
        symbol = self.symbols.get(name)
        if symbol is not None:
            return symbol

        # If not found, try parent scope
        if self.parent is not None:
            return self.parent.get(name)

        return None  # not found anywhere

    def pushScope(self, name="scope"):
        """Create a new scope whose parent is the current one."""
        return SymbolTable(parent=self, name=name)

    def popScope(self):
        """Return the parent scope (caller must update self.symtab)."""
        return self.parent


