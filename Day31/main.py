import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass
    
    # Get the current timestamp
    timestamp = os.path.getmtime(filename)
    
    # Convert the timestamp into a readable format, then into a string
    date = datetime.datetime.fromtimestamp(timestamp)
    date_str = date.strftime("%Y-%m-%d")
    
    # Return just the date portion 
    return date_str

print(file_date("newfile.txt"))
