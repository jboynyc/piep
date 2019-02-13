import subprocess, tempfile
from IPython.core.magic import register_cell_magic


def _call_piep(sexp):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tf:
        tf.write('#lang piep\n\n{}'.format(sexp))
    return subprocess.check_output(['racket', tf.name]).decode()

@register_cell_magic
def piep(line, cell):
    return _call_piep(cell.strip())
