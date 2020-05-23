import armaclass

# filteres the Output of the armaclass.parse as it is a horrible nested dict.
# has some problems with a complete config dump as there seem to be some symbols that python or armaclass can't handle
def do_it_really(config_file, csv_1):
    with open(config_file,'r') as f:
        content = f.read()
    Output_parse = armaclass.parse(content)
    for key, value in Output_parse.items():

        for a_key, a_value in value.items():

            if isinstance(a_value, dict):
                for b_key, b_value in a_value.items():
                    if b_key == 'displayName':
                        with open(csv_1, 'a') as file_csv:
                            file_csv.write('"{}","{}"\n'.format(a_key, b_value))


# the values of this dict are the paths to the config to be parsed
# the keys are the name(path possible to) of the output file
files_to_do = {'cfg_weapons_dispnames.csv': 'D:/Dropbox/hobby/Modding/Ressources/Templates/Config_dumb/CfgWeapons_dump.cpp',
               'cfg_vehicles_dispnames.csv': 'D:/Dropbox/hobby/Modding/Ressources/Templates/Config_dumb/CfgVehicles_dump.cpp'}


for KEY, VALUE in files_to_do.items():
    with open(KEY,'w') as CSV_file:
        CSV_file.write('List:\n')
    do_it_really(VALUE, KEY)