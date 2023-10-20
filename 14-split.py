part_size = 1000  # size of each part in megabytes
part_number = 1  # initial part number

with open('digital-nlog-all-2023-10-10.log', 'r') as file:
    while True:
        # Read part_size megabytes of data from the file
        data = file.read(part_size * 1024 * 1024)
        
        # Break the loop if there is no more data to read
        if not data:
            break
        
        # Write the data to a new part file
        part_filename = f'part{part_number}.txt'
        with open(part_filename, 'w') as part_file:
            part_file.write(data)
        
        part_number += 1
