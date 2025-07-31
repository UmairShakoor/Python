from keystop import msg  # Handles Ctrl+C gracefully

import operator
from typing import List
from colorama import Fore, Style, init

init(autoreset=True)  # Auto reset colors after each print


def num() -> float:
    while True:
        n: str = input(Fore.CYAN + '\n➤ Enter Number: ').strip()

        try:
            return float(n)
        except Exception:
            print(Fore.RED + '✗ Invalid Number. Please try again.')


def func() -> str:
    funcs: List[str] = ['+', '-', '*', '/', '**', '//', 'avg', 'average']

    while True:
        f: str = input(Fore.YELLOW + '\n➤ Math Function (+, -, *, /, **, //, avg): ').strip()
        if f.lower() not in funcs:
            print(Fore.RED + '✗ Invalid Function. Allowed:', ', '.join(funcs))
            continue
        return f


def clean(n: float) -> str:
    return str(int(n)) if n.is_integer() else str(round(n, 4))


n1 = num()
f = func()
n2 = num()

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '**': operator.pow
}

if (n1 == 0 or n2 == 0) and (f in ['/', '//']):
    print(Fore.RED + f'\n{clean(n1)} {f} {clean(n2)} = Undefined (Cannot divide by 0)\n')
    exit()

elif f.lower() in ['average', 'avg']:
    result: str = clean((n1 + n2) / 2)
    print(Fore.GREEN + f'\n✓ Average of {clean(n1)} and {clean(n2)} = {result}\n')

else:
    result: str = clean(ops[f](n1, n2))
    print(Fore.GREEN + f'\n✓ {clean(n1)} {f} {clean(n2)} = {result}\n')
