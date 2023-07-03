class Transaction:
    def __init__(self):
        self.rollback_ops = []

    def log(self, command, *args):
        self.roll_back_ops.append(
            (command, args)
        )

    def rollback(self):
        for command, args in reversed(self.ops):
            command(*args)


class Database:
    def __init__(self):
        self.transactions = []
        self.store = {}

    def set(self, key, value, is_rollback=False):
        if self.transactions and not is_rollback:
            current_transaction = self.transactions[-1]
            if key in self.store:
                current_transaction.log(
                    self.set, key, self.store[key], True
                )
            else:
                current_transaction.log(self.delete, key, True)

        self.store[key] = value
    
    def get(self, key):
        if key in self.store:
            return self.store[key]
        else:
            throw

    def delete(self, key, is_rollback=False):
        if key in self.store:
            if self.transactions and not is_rollback:
                self.transactions[-1].log(
                    self.set, key, self.store[key], True
                )

            del self.store[key]

    def begin(self):
        self.transactions.append(Transaction())

    def rollback(self):
        self.transactions.pop().rollback()

    def commit(self):
        """Permanently stores and closes all open transactional blocks."""
        self.blocks = []

