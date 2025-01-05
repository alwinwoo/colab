try:
    import os, sys, re, json, itertools, subprocess
    import time, datetime
    import math, random
    import logging
    import csv, numpy, pandas, matplotlib

    os.system('pip install pytz')
    import pytz
    
    try:
        if "web" in use_category:
            import requests, beautifulsoup4
            print('Importing web modules')
                
        if "ai" in use_category:
            import sklearn, tensorflow
            print('Importing AI modules')
    
        print('Special modules loaded')
            
    except Exception as e:
        try:
            if "web" in use_category:
                os.system('pip install beautifulsoup4')
            if "ai" in use_category:
                os.system('pip install scikit-learn tensorflow')
        except Exception as e:
            print(f'Error loading special modules: {e}')
            
except Exception as e:
    print(f'Error loading common modules: {e}')
