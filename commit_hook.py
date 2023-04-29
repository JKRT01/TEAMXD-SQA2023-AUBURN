#!/usr/bin/sh
import os
import os.path
import sys
import re
from subprocess import run
import scanner

if __name__ == '__main__':
    cmd = run("git diff HEAD^ HEAD --name-only --diff-filter=ACMR",capture_output=True,shell=True)
    # check file change
    lines = cmd.stdout.splitlines()
    any_py_changed = False
    for line in lines:
        line = line.decode('utf-8')
        match = re.search(".py$", line)
        if match:
          any_py_changed = True
    # python file change detected, run scanner
    if any_py_changed:
        cwd = os.getcwd()
        content_as_ls   = scanner.runScanner( cwd )
        df_all          = pd.DataFrame( getCountFromAnalysis( content_as_ls ) )
        df_all.to_csv(path.join(cwd, "report.csv"), header= constants.CSV_HEADER , index=False, encoding= constants.CSV_ENCODING ) 