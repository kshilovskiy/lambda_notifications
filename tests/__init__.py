from os.path import dirname, join, realpath
import sys

current_path = dirname(realpath(__file__))
functions_path = join(dirname(current_path), 'functions')

sys.path.append(functions_path)
sys.path.append(current_path)
sys.path.append(join(functions_path, 'basic'))
