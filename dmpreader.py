import struct

def read_dump_file(file_path):
    """Read and parse a dump file."""
    try:
        with open(file_path, 'rb') as f:
            # Read the file header
            header = f.read(4)
            if header != b'DUMP':
                print("Invalid dump file format.")
                return

            # Read the number of records
            num_records, = struct.unpack('<I', f.read(4))
            print(f"Number of records: {num_records}")

            # Read and process each record
            for _ in range(num_records):
                record_type, record_length = struct.unpack('<BI', f.read(5))
                if record_type == 1:  # Assuming record type 1 contains ASCII data
                    data = f.read(record_length).decode('utf-8')
                    print(f"Record (ASCII): {data}")
                elif record_type == 2:  # Assuming record type 2 contains binary data
                    data = f.read(record_length)
                    print(f"Record (Binary): {data}")
                else:
                    print(f"Unknown record type: {record_type}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the dump file: ")
    read_dump_file(file_path)
