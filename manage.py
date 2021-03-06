#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJMODELS_SETTINGS_MODULE", "project.settings")

    from djmodels.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
