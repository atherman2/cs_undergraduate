import os

def main() -> None:
    file = open('trabalhos.dat','rb')
    index_file = open('index_file.dat','xb')
    f_current_byte_offset = 0
    record_header_size = 4
    file.seek(record_header_size,os.SEEK_SET)
    f_current_byte_offset += record_header_size
    f_next_byte_offset = f_current_byte_offset
    while is_there_record(file):
        f_current_byte_offset = f_next_byte_offset
        record, f_next_byte_offset = read_record(file, f_current_byte_offset)
        record_key = get_record_key(record)
        write_record(index_file, record_key, f_current_byte_offset)

def is_there_record(file) -> str:
    # return the next byte of a file as a string that can be used as a boolean value
    # the boolean value tells if there is one more record
    next_byte = file.read(1)
    next_byte_decoded = next_byte.decode()
    file.seek(-1,os.SEEK_CUR)
    return next_byte_decoded

def read_record(file, current_byte_offset):
    # receives the current_byte_offset and reads a record
    # returns the record read and the next_byte_offset
    next_byte_offset = current_byte_offset
    bin_record_size = file.read(2)
    next_byte_offset += 2
    record_size = int.from_bytes(bin_record_size)
    record = file.read(record_size)
    next_byte_offset += record_size
    return record, next_byte_offset

def get_record_key(record):
    fields = record.split('|')
    return fields[0]