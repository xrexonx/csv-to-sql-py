# Csv to mySql

Assume that you already have python installed on your machine. 
To check version
```
$ python -V
Python 3.7.3
$ pip3 -V
pip 19.1.1
```
Also need to have virtualenv
```
$ pip3 install virtualenv
```

### Create environment
```
$ virtualenv venv
```

### Activate environment
```
$  source venv/Scripts/activate
```

### Install packages
```
$ pip3 install -r requirements.txt
```

### Run export data to csv
```
$ py export.py
```

### Run migration
Assume that you already created your database and tables
```
$ py import.py
```

### To verify
    * Check length after migration
    * Create random query to source DB and destination DB then match both results

## TODO
Refactor into dynamic migration scripts and use class for the implementation

