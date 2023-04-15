#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, subprocess
try:
    import pyfstab
except ImportError as e:
    print(f'Importing pyfstab failed! reason: {e}\nTrying to install it via pip...')
    subprocess.run(['/usr/bin/env', 'python3', '-m', 'pip', 'install', 'pyfstab']) # Install pyfstab using pip
    try:
        import pyfstab
    except ImportError as e2:
        print(f'Failed again to import pyfstab! Reason: {e2}\nExiting...')
        sys.exit(-1)

