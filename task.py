#!/usr/bin/env python3

class Task:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title')
        self.tags = kwargs.get('tags')
        self.note = kwargs.get('note')