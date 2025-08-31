from src.util import *
from pathlib import Path
from src.yarascanner import *


def main():
    # Percorso assoluto del file monitor.ini
    ini_path = Path("/home/andrea/yarafilescanner/conf/monitor.ini")
    yara_path = Path("/home/andrea/yarafilescanner/conf/yara.ini")

    # Carica la configurazione
    config = load_config(ini_path)
    monitor_dir = config['FilePaths']['input']

    print(f"Input dir: {monitor_dir}")

    yara_config = load_config(yara_path)
    filerule_dir = yara_config['FileRules']['rules']

    print(f"Input dir: {filerule_dir}")

    filelist = get_file_list(monitor_dir)

    scanned_result = scan_file_format(monitor_dir, filelist)

    print(scanned_result)


if __name__ == "__main__":
    main()