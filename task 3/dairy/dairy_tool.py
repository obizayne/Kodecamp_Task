# diary_tools.py

import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'diary.json')

class DiaryEntry:
    def __init__(self, title, content, date=None):
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            'date': self.date,
            'title': self.title,
            'content': self.content
        }

    @staticmethod
    def from_dict(data):
        return DiaryEntry(
            title=data['title'],
            content=data['content'],
            date=data['date']
        )

def save_entries(entries):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump([entry.to_dict() for entry in entries], file, indent=4)
        print("Entries saved successfully.")
    except Exception as e:
        print(f"Error saving entries: {e}")

def load_entries():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                return [DiaryEntry.from_dict(entry) for entry in data]
    except Exception as e:
        print(f"Error loading entries: {e}")
    return []

def search_entries(entries, keyword):
    results = []
    for entry in entries:
        if keyword.lower() in entry.title.lower() or keyword in entry.date:
            results.append(entry)
    return results
