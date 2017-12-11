"""An attempt to get REST data by http and put selected fields in a file."""

import requests

# You need the Reqests running on your computer
# See http://docs.python-requests.org/en/master/user/install/#install"
# Maybe we should just package the whole thing

FIELDS_TO_EXTRACT = ('name', 'phone', 'email', 'website')
# should be moved to a config file and assumes we know these fields are present

def api_reader(target_url):
    "Gets data from a REST AP and returns a list of json records"

    my_request = requests.get(target_url, stream=True)
    # don't remember if the stream bit is important btw

    item_list = my_request.json()
    return item_list

def extract_fields(json_records, json_fields):
    "Extract specified fields from records and send back as a list of tab separated values"
    extracted_fields_list = [] # data to send back

    while json_records:
        json_record = json_records.pop()
        extracted_fields = '' # temporary string to hold fields
        for i in range(0, len(json_fields)):
            extracted_fields += json_record[json_fields[i]]
            if i < len(json_fields)-1: # if this is not the last field
                extracted_fields += '\t' # add a tab separator
        extracted_fields_list.append(extracted_fields)

    field_headings = ''
    for i in range(0, len(json_fields)):
        field_headings += json_fields[i]
        if i < len(json_fields)-1: # if this is not the last field
            field_headings += '\t' # add a tab separator
    extracted_fields_list.append(field_headings)

    return extracted_fields_list

def write_list(list_to_write):
    "Bung the list passed in a text file"
    fileything = open("regency.tsv", 'w')
    while list_to_write:
        fileything.write(list_to_write.pop()+'\n')
    fileything.close()
    return

def main():
    "Run the program"
    print("starting Regency Reports...")
    records = api_reader('https://jsonplaceholder.typicode.com/users')
    extracted = extract_fields(records, FIELDS_TO_EXTRACT)
    write_list(extracted)

if __name__ == "__main__":
    main()
