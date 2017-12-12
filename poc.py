"""An attempt to get REST data by http work on the data and put the result in a file."""

import requests # See http://docs.python-requests.org/en/master/user/install/#install"

# Config. Would be better in a separate file.
SOURCE_API = 'https://jsonplaceholder.typicode.com/users'
FIELDS_TO_EXTRACT = ('name', 'email', 'phone')
OUTPUT_FILE = './output/prototype/regency.txt'

def api_reader(target_url):
    "Gets json data from an API and returns a list of json objects"
    my_request = requests.get(target_url, stream=True) # stream may not matter
    json_list = my_request.json()
    return json_list

def extract_fields(json_records, json_fields):
    "Extract specified fields from records and send back as a list of tab separated values"
    number_of_records = len(json_records)
    number_of_fields = len(json_fields)
    results_list = []

    for i in range(0, number_of_records):
        json_record = json_records.pop()
        line = ''
        for j in range(0, number_of_fields):
            line += json_record[json_fields[j]]
            # add a tab separator unless this is the final field
            if j+1 != number_of_fields:
                line += '\t'
        results_list.insert(i, line)

    line = ''
    for j in range(0, number_of_fields):
        line += json_fields[j]
        # add a tab separator unless this is the final field
        if j+1 != number_of_fields:
            line += '\t'
    results_list.append(line)


    return results_list

def save_list(list_to_write):
    "Writes a list to a text file"
    output_file = open(OUTPUT_FILE, 'w')
    while list_to_write:
        output_file.write(list_to_write.pop()+'\n')
    output_file.close()
    return

def main():
    "Run the program"
    print("starting Regency Reports...")
    records = api_reader(SOURCE_API)
    extracted = extract_fields(records, FIELDS_TO_EXTRACT)
    save_list(extracted)

if __name__ == "__main__":
    main()
