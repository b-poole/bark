#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:13:11 2024

@author: barrettpoole14
"""
import commands

class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call
        
    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        print(message)
        
    def __str__(self):
        return self.name

def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
    print()

def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options

def get_option_choice(options):
    choice = input('Choose an option: ')
    while not option_choice_is_valid(choice, options):
        print('Invalid choice')
        choice = input('Choose an option: ')
    return options[choice.upper()]

if __name__ == '__main__':
    commands.CreateBookmarksTableCommand().execute()
    
    options = {
    'A': Option('Add a bookmark', commands.AddBookmarkCommand()),
    'B': Option("List bookmarks by date", commands.ListBookmarksCommand()),
    'C': Option("List bookmarks by title", commands.ListBookmarksCommand(order_by='title')),
    'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand()),
    'Q': Option('Quit', commands.QuitCommand())    
    }
    print_options(options)
    
    chosen_option = get_option_choice(options)
    chosen_option.choose()
    