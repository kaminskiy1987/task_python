from datetime import datetime
from time import time

def show_all():
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write('{} Time {}\n'.format('Showed all items', time_calc))

def search(search_object):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write('Search: {} Time {}\n'.format(search_object, time_calc))

def add(added_object):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write('Added: {} Time {}\n'.format(added_object, time_calc))

def change(changed_object):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write('Changed: {} Time {}\n'.format(changed_object, time_calc))

def del_item(deleted_object):
    time_calc = datetime.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write('Deleted: {} Time {}\n'.format(deleted_object, time_calc))
