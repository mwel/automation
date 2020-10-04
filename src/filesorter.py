from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class moveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_sort):
            src = folder_to_sort + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)


folder_to_sort = "/Users/mwellenhofer/Downloads"
folder_destination = "/Users/mwellenhofer/Downloads/Downloads_Archive"

# creating event handler
event_handler = moveHandler()

# creating observer object
observer = Observer()
observer.schedule(event_handler, folder_to_sort, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10),
except KeyboardInterrupt:
    observer.stop()
observer.join()