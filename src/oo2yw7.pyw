from oo2yw7_lib import run
import sys

try:
    sourcePath = sys.argv[1]
except:
    sourcePath = ''
run(sourcePath)
