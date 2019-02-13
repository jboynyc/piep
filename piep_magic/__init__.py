'''Use structured notation for SQL statements in your notebooks.'''

from .piep_magic import piep

def load_ipython_extension(ipython):
    ipython.register_magic_function(piep, 'cell')
