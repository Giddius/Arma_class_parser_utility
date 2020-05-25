

# Author: Giddi    https://github.com/Giddius
# main.py (c) 2020
# Desc: Todo:
# Created:  2020-05-25T01:44:23.730Z
# Modified: !date!


import armaclass


# filteres the Output of the armaclass.parse as it is a horrible nested dict.
# has some problems with a complete config dump as there seem to be some symbols that python or armaclass can't handle
def do_it_really(config_file, csv_1, search_attribute):
    with open(config_file,'r', encoding="utf8") as f:
        content = f.read()
    Output_parse = armaclass.parse(content)

    go_through_it(Output_parse, csv_1, search_attribute)

def go_through_it(in_put, csv_1, search_attribute, former='Top'):
    for key, value in in_put.items():
        if key == search_attribute:
            with open(csv_1, 'a') as file_csv:
                file_csv.write('"{}","{}"\n'.format(former, value))
        check_it_out(value, csv_1, search_attribute, key)


def check_it_out(in_put, csv_1, search_attribute, in_former):
    if isinstance(in_put, dict):
        go_through_it(in_put, csv_1, search_attribute, former=in_former)



def run_through_config(in_put: dict, attribute_to_search_for: str):

    # the values of this dict are the paths to the config to be parsed
    # the keys are the name(path possible to) of the output file

    files_to_do = in_put


    for KEY, VALUE in files_to_do.items():
        with open(KEY,'w') as CSV_file:
            CSV_file.write('List:\n')
        do_it_really(VALUE, KEY, attribute_to_search_for)
