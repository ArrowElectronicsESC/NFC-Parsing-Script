# NFC Cockpit Parsing script

import csv

if __name__ == "__main_":

    with open('log_nfc.txt') as f:
        log = f.readlines()
        
        
    output = []
    for line in log:
      if "INFO" in line:
        time_data = line[12:20]
        hour, min, sec = time_data.split(':')
        output.append([hour, min, sec])
        
    fields = ['Hour', 'Minute', 'Second']
    with open('parsed_nfc.csv', 'w') as f:
        write = csv.writer(f)      
        write.writerow(fields)
        write.writerows(output)
