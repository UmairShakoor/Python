import sys
import builtins

def _patched_input(prompt=''):
    try:
        return original_input(prompt)
    except KeyboardInterrupt:
        print('\n\nProgram Interrupted.\n\tGoodbye!, As you wish.\n')
        sys.exit()

# Patch only once
if not hasattr(builtins, 'original_input'):
    original_input = builtins.input
    builtins.input = _patched_input

# Dummy symbol to allow: from keystop import msg
msg = None
