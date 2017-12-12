"""A prototype - gets some REST data from the web and puts some of it in tab seaparated file."""

import requests # See http://docs.python-requests.org/en/master/user/install/#install"

# Config. Would be better in a separate file.
SOURCE_API = 'https://jsonplaceholder.typicode.com/users'
FIELDS_TO_EXTRACT = ('name', 'email', 'phone')
OUTPUT_FILE = './output/prototype/regency.tsv'

def api_reader(target_url):
    "Gets json data from an API and returns a list of json objects"
    my_request = requests.get(target_url, stream=True) # stream may not matter
    json_list = my_request.json()
    return json_list

def tabulate(json_records, json_fields):
    "Convert list of json records into a table containing the fields requested"
    table = []
    row = []
    # Add headings in the first row of the table using the field names requested
    for heading in json_fields:
        row.append(heading)
    table.append(row)
    # Iterate through each record and the required elements
    for record in json_records:
        row = []
        for j in range(0, len(json_fields)):
            row.append(record[json_fields[j]])
        table.append(row)
    return table

def save_tsvlist(list_to_write, file_name):
    "Writes a 2D list to a tab delimited file"
    with open(file_name, 'w') as thefile:
        thefile.writelines('\t'.join(i) + '\n' for i in list_to_write)
    thefile.close()
    return

def main():
    "Run the program"
    print("starting Regency Reports...")
    source_data = api_reader(SOURCE_API)
    tabulated_data = tabulate(source_data, FIELDS_TO_EXTRACT)
    save_tsvlist(tabulated_data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
