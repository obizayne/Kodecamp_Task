# delivery_utils.py

import json
import uuid
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'packages.json')

class Package:
    def __init__(self, sender, recipient, status="Pending", package_id=None):
        self.id = package_id or str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'recipient': self.recipient,
            'status': self.status
        }

    @staticmethod
    def from_dict(data):
        return Package(
            sender=data['sender'],
            recipient=data['recipient'],
            status=data['status'],
            package_id=data['id']
        )

def save_packages(packages):
    with open(DATA_FILE, 'w') as file:
        json.dump([pkg.to_dict() for pkg in packages], file, indent=4)
    print(f"Packages saved to {DATA_FILE}")

def load_packages():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            return [Package.from_dict(pkg) for pkg in data]
    return []
