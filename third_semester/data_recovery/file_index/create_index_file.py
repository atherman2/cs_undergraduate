def main():
    file = open('trabalhos.dat','rb')
    index_file = open('index_file.dat','xb')
    while is_there_record(file):
        write_record(index_file,read_record(file))
