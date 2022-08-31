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
import shutil, json

filename = 'people.json'
orgFile = os.path.join(os.path.join(currentDir, 'resource'), filename)
fileToProcess = os.path.join(currentDir, 'tmp.json')
shutil.copyfile(orgFile, fileToProcess)

with open(fileToProcess, 'r') as jsonRead:
    data = json.load(jsonRead)

for row in data:
    temp = row['registered']
    row['registered'] = ''.join(temp.split(' '))

with open(fileToProcess, 'w') as jsonWrite:
    json.dump(data, jsonWrite)

try:
    with open(fileToProcess, 'rb') as people_file:
        data = JSONParser().parse(people_file)
        serializer = serializers.PeopleImportSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            print(f"Successfully loaded {filename}")
        else:
            # print(f"File format is invalid: {filename}")
            print(serializer.errors)
except OSError:
    raise OSError(f"Cannot open file {filename}")

if os.path.isfile(fileToProcess):
    os.remove(fileToProcess)