import subprocess

import os

converter = '"C:/Program Files (x86)/Steam/steamapps/common/Arma 3 Tools/TexView2/Pal2PacE.exe"'

subprocess.run(converter + " P:/a3/characters_f/BLUFOR/Data/armor1_co.paa " + os.path.join(os.getcwd(), 'test.png'), check=False, shell=True)

# os.remove(os.path.join(os.getcwd(), 'test.png'))
