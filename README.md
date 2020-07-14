# Todo List Project

This a python api project **without using any framework**. No flask or django are needed.

I used the [http.server](https://docs.python.org/3/library/http.server.html) library, one of python3 defaut libraries to build this.

## Requirement

### System

- Python 3.6
- Postgres

### Library:

- sqlalchemy
- psycopg2
- pyrsistent

## Run guild

1. Install requirement libraries
```bash
pip install -r requirements.txt 
```

2. Config database connection in [./src/cfg/defaults.py](./src/cfg/defaults.py)
```python3
DB_CONNECTION = "postgres://postgres:postgres@localhost/local"
```

3. Initial project
```bash
make init-db
```

4. Run project
```bash
make run
```

## Develop guild

1. Install requirement develop libraries
```bash
pip install -r requirements.dev.txt 
```

2. Test system
```bash
make run-test
```
