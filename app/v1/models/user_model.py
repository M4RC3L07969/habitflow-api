from datetime import date

class User:
    id: str
    name: str
    email: str
    password_hash: str
    created_at: date

    def __init__(self, id, name, email, password_hash, created_at):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at