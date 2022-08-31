import os
import sys


currentDir = os.path.abspath(os.getcwd())    
if currentDir not in sys.path:       
    sys.path.append(currentDir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pandora.settings')
import django
django.setup()

from api import serializers
from rest_framework.parsers import JSONParser

filename = 'companies.json'
filepath = os.path.join(os.path.join(currentDir, 'resource'), filename)

try:
    with open(filepath, 'rb') as companies_file:
        data = JSONParser().parse(companies_file)
        serializer = serializers.CompaniesSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            print(f"Successfully loaded {filename}")
        else:
            print(serializer.errors)
except OSError:
    raise OSError('Cannot open file %s' % filename)