#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        if not isinstance(self.page_count, int):
            print("page_count must be an integer")
            return
        print("Flipping the page...wow, you read fast!")

    pass
    
        