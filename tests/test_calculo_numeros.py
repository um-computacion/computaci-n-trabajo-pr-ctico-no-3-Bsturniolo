import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch
class TestCalculoNumeros(unittest.TestCase):
    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='100'
    )   
if __name__ == '__main__':
    unittest.main()