import os

def main():
    file = open('trabalhos.dat','rb')
    index_file = open('index_file.dat','xb')
    while is_there_record(file):
        write_record(index_file,read_record(file))

def is_there_record(file) -> str:
    next_byte_decoded = file.read(1).decode()
    file.seek(-1,os.SEEK_CUR)
    return next_byte_decoded