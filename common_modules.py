try:
    import os, sys, math, datetime, re, json, random, time, itertools, subprocess, logging
    import csv, numpy, pandas, matplotlib

    try:
        if "web" in use_category:
            import requests, beautifulsoup4
        if "ai" in use_category:
            import scikit-learn, tensorflow
        except:
            print('"use_category" list missing!"')
except:
    print('Error loading common modules"')