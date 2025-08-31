"""
import configparser
from pathlib import Path

def load_config(filepath):
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    config.read(filepath)
    return config

#path for monitor.ini
monitor_path=Path("C:/Users/andre/PycharmProjects/scry") #path for monitor.ini
yara_path=Path("C:/Users/andre/PycharmProjects/scry/conf/") #path for yara

#load configuration
config = load_config(monitor_path)
monitor_dir=config['FilePaths']['input']

#path for yara.ini
yara_config=load_config(yara_path)
filerule_dir = yara_config['FileRules']['rules']

#watchdogs
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"file created: { event.src_path }")
        return super().on_created(event)

    def on_modified(self, event):
        print(f"file modified: { event.src_path }")
        return super().on_modified(event)


#watchdogs class implementation and observable
observer = Observer()
handler = MyHandler()
p = "C:/"
observer.schedule(handler, path=p, recursive=True)
observer.start()

while True:
    cmd = input(">>> ")
    if cmd == "q": break

observer.stop()
observer.join()



from src.yarascanner import *

filelist=get_file_list(monitor_dir)

scanned_results=scan_file_format(monitor_dir, filelist)

print(scanned_results)

"""