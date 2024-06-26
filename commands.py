#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 22:56:03 2024

@author: barrettpoole14
"""

from datetime import datetime
import sys
import database

db = database.DatabaseManager("bookmarks.db")

class CreateBookmarksTableCommand:
    def execute(self):
        db.create_table("bookmarks", 
        {"id": "INTEGER PRIMARY KEY AUTOINCREMENT",
         "title": "TEXT NOT NULL",
         "url": "TEXT NOT NULL",
         "notes": "TEXT",
         "date_added": "TEXT NOT NULL"
         })
        
class AddBookmarkCommand:
    def execute(self, data):
        data['date_added'] = datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return 'Bookmark Added!'
    
class ListBookmarksCommand:
    def __init__(self, order_by='date_added'):
        self.order_by = order_by
        
    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()
    
class DeleteBookmarkCommand:
    def execute(self, data):
        db.delete('bookmarks', {'id': data})
        return 'Bookmark deleted!'
    
class QuitCommand:
    def execute(self):
        sys.exit()
