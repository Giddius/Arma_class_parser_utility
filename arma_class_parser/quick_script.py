from gidtools.gidfiles import ext_splitter, linereadit, pathmaker, readit, writeit
import os
import subprocess

# _maindir = pathmaker(sys.argv[1])

_header = """
---
title: Arma_Class_parser
...
"""


_maindir = pathmaker(r"D:\Dropbox\hobby\Modding\Programs\Github\My_Repos\Arma_class_parser_utility\arma_class_parser_src")

for file in os.listdir(pathmaker(_maindir, 'test')):
    os.remove(pathmaker(_maindir, 'test', file))


# os.chdir(_maindir)
# for files in os.listdir(_maindir):
#     if '.md' in files:
#         a = readit(files)
#         writeit(files, _header + '\n\n' + a.replace('\t', '  ').replace('\s\s', ' ').replace('\s', ' '))
#         print(files)
#         _name = ext_splitter(files)
#         print(_name)
#         subprocess.run(f"pandoc -s {_name}.md -o conv_{_name}.html --from markdown", check=False, shell=True)
#         print('!-------------------------------------------!!!! ' + _name + ' DONE!!!!-----------------------------------------!')


_line_list = []
for lines in linereadit(pathmaker(_maindir, 'cfg_keypaths.md')):
    if lines != '\n' and lines != '---':
        _line_list.append(lines)


_the_dict = {}
for line in _line_list:
    if '-->' in line:
        _sline = line.split(' --> ')
        _name = _sline.pop(0)

        if _name in _the_dict:
            if _sline[0] in _the_dict[_name]:
                _the_dict[_name][_sline[0]].append(' &rarr; '.join(_sline))
            else:
                _the_dict[_name][_sline[0]] = []
                _the_dict[_name][_sline[0]].append(' &rarr; '.join(_sline))
        else:
            _the_dict[_name] = {}
            _the_dict[_name][_sline[0]] = []
            _the_dict[_name][_sline[0]].append(' &rarr; '.join(_sline))

_new_dir = pathmaker(_maindir, 'test')
for key, value in _the_dict.items():
    if 'cfg' in key.casefold() and value != {}:
        _string = '# ' + key + '\n\n---\n\n'
        for bkey, bvalue in value.items():
            _string += '## ' + bkey + '\n\n> \n>' + '\n> \n>'.join(bvalue) + '\n\n\n---\n\n\n\n'
        writeit(pathmaker(_new_dir, f'{key}_keypaths.md'), _string)


os.chdir(_new_dir)
for files in os.listdir(_new_dir):
    if '.md' in files:
        a = readit(files)
        writeit(files, _header + '\n\n' + a)
        print(files)
        _name = ext_splitter(files)
        print(_name)
        subprocess.run(f"pandoc -s {_name}.md -o conv_{_name}.html --from markdown", check=False, shell=True)
        # subprocess.run(f"pandoc -s {_name}.md -o conv_{_name}.pdf --from markdown --template eisvogel --listings", check=False, shell=True)
        print('!-------------------------------------------!!!! ' + _name + ' DONE!!!!-----------------------------------------!')
