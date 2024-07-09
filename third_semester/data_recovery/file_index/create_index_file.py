import os

def main() -> None:
    file = open('trabalhos.dat','rb')
    index_file = open('index_file.dat','xb')
    record_header = 4
    file.seek(record_header,os.SEEK_SET)
    next_byte_offset = record_header
    while is_there_record(file):
        current_byte_offset = next_byte_offset
        record, next_byte_offset = read_record(file, current_byte_offset)
        record_key = record_key(record)
        write_record(index_file, record_key, current_byte_offset)

def is_there_record(file) -> str:
    # return the next byte of a file as a string that can be used as a boolean value
    # the boolean value tells if there is one more record
    next_byte_decoded = file.read(1).decode()
    file.seek(-1,os.SEEK_CUR)
    return next_byte_decoded