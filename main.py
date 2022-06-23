# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

import pytest


def main_run():
    pytest.main(['-s','-v', '-W', 'ignore:Module already imported:pytest.PytestWarning',
                 '--alluredir', './report/report', "--clean-alluredir"])
    # pytest.main(['-s','-W', '--alluredir', './report/report', '--clean-alluredir','ignore:Module already imported:pytest.PytestWarning'])
    os.system('allure generate ./report/report -o ./allure-report --clean')

if __name__ == '__main__':
    main_run()
