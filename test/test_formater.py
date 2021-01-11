from service.formater import plain_text_upper_case, plain_text, get_formatted
from pytest import fixture
import pytest


class Test_Formater:
    # content of test_module.py
    @pytest.fixture
    def name(self):
        return 'Jose'

    @pytest.fixture
    def msg(self):
        return 'message'

    def test_plain_uppercase(self):
        r = plain_text_upper_case("wwww", "EEeMSG")
        name = r.split(" ")[0]  # Splitting the string to check if both variables
        msg = r.split(" ")[1]  # has been converted properly to upper case
        assert (name.isupper() and msg.isupper), f' Failing to convert to upper case the variable name with the value {name} or the variable msg with the value {msg}'

    def test_plain_text(self, name, msg):  # Passing the variables name and msg as a fixture of pytest,
        r = plain_text(msg, name)  # so we need to call them with the same name as the function is defined
        assert (r == 'Jose message'), f' Failing to display plain text with the values {name} or the variable msg with the value {msg}'

    def test_get_formatted(self, name, msg):
        r = get_formatted(msg, name, "plain_uppercase")
        assert (r == 'JOSE MESSAGE'), f' Failing to convert to upper case the variable name with the value {name} or the variable msg with the value {msg}'

    # To be executed by a command line:
    # Linux:                            # Windows
    # cd directory_of_project           # dir directory_of_project
    # python3 -m pytest test/
    # It should display something like:
    #
# (base) user@pc:~/Projects/printerService$ python3 -m pytest -v test/
# ====================================================================== test session starts ======================================================
# platform linux -- Python 3.8.3, pytest-6.2.1, py-1.9.0, pluggy-0.13.1
# rootdir: /home/Projects/printerService
# collected 7 items
#
# test/test_formater.py::Test_Formater::test_plain_uppercase PASSED                                                                          [ 14%]
# test/test_formater.py::Test_Formater::test_plain_text PASSED                                                                               [ 28%]
# test/test_formater.py::Test_Formater::test_get_formatted PASSED                                                                            [ 42%]
# test/test_views.py::Test_Flask_Views::test_output PASSED                                                                                   [ 57%]
# test/test_views.py::Test_Flask_Views::test_outputs PASSED                                                                                  [ 71%]
# test/test_views.py::Test_Flask_Views::test_form PASSED                                                                                     [ 85%]
# test/test_views.py::Test_Flask_Views::test_mult PASSED                                                                                     [100%]
#======================================================================= 7 passed in 0.09s ========================================================