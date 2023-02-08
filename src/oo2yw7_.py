"""Convert odt/ods to yw7. 

Version @release
Requires Python 3.6+
Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/oo2yw7
Published under the MIT License (https://opensource.org/licenses/mit-license.php)
"""
import sys
import platform
from pywriter.converter.yw7_importer import Yw7Importer
from pywriter.ui.ui_mb import UiMb


def main(sourcePath):
    """Convert an odt/ods document to yw7.
    
    - If yw7 project file exists, update it from odt/ods.
    - Otherwise, create a new yw7 project.
    
    Positional arguments:
        sourcePath -- document to convert. 
    """
    converter = Yw7Importer()
    converter.ui = UiMb(f'{_("Export to yw7")} (Python version {platform.python_version()})')
    kwargs = {'suffix': None}
    converter.run(sourcePath, **kwargs)


if __name__ == '__main__':
    try:
        sourcePath = sys.argv[1]
    except:
        sourcePath = ''
    main(sourcePath)
