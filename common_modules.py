try:
    import os, sys, math, datetime, re, json, random, time, itertools, subprocess, logging
    import csv, numpy, pandas, matplotlib

    try:
        if "web" in use_category:
            import requests, beautifulsoup4
            print('Importing web modules')
            
        if "ai" in use_category:
            import sklearn, tensorflow
            print('Importing AI modules')

        print('Special modules loaded')
        
    except Exception as e:
        print(f'Error loading special modules: {e}')
        
except Exception as e:
    print(f'Error loading common modules: {e}')
