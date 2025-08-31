import yara
from os import listdir
from os.path import isfile, join

path_to_scan = '/home/andrea/yarafilescanner/yarafilescanner/batch/sample_files'
def scan_file_format(folder, filelist):

    #TODO modificare meccanismo con cui vengono serviti i path delle regole dentro questo file
    rules = yara.compile(filepath='/home/andrea/yararules/files/NonStandard_File_Forma.yar')
    return [{filename:rules.match(f"{folder}/{filename}")} for filename in filelist if len(rules.match(f"{folder}/{filename}")) != 0 ]


def get_file_list(folder_to_check):
    return [f for f in listdir(folder_to_check) if isfile(join(folder_to_check,f))]
