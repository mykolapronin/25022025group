import psycopg2

PGHOST = 'ep-tiny-lake-a2a59kmr-pooler.eu-central-1.aws.neon.tech'
PGDATABASE = 'neondb'
PGUSER = 'neondb_owner'
PGPASSWORD = 'npg_jas48GpSCfut'
PORT = 5432

with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS brand (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL
            )
        """
        cursor.execute(query)

        query = """
            CREATE TABLE IF NOT EXISTS customer (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS car (
                id SERIAL PRIMARY KEY,
                model VARCHAR(50) NOT NULL,
                cost INTEGER,
                brand_id INTEGER REFERENCES brand(id),
                customer_id INTEGER REFERENCES customer(id)
            );
        """
        cursor.execute(query)

# CREATE
with psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT) as connection:
    with connection.cursor() as cursor:
        # query_insert =  'INSERT INTO brand (name) VALUES (%s)'
        # cursor.execute(query_insert, ('BMW',))
        # print(result1)

        # query_insert = 'INSERT INTO brand (name) VALUES (%s) RETURNING id, name'
        # cursor.execute(query_insert, ('AUDI2222',))
        # print(cursor.fetchone())

        # query_insert = 'INSERT INTO customer (name) VALUES (%s) RETURNING id, name'
        # owners = [
        #     ('Max',),
        #     ('Max',),
        #     ('Alex',),
        # ]
        # cursor.executemany(query_insert, owners)

        query_insert = 'INSERT INTO car (model, cost, brand_id, customer_id) VALUES (%s, %s, %s, %s)'
        cars = [
            ('Corolla', 25000, 1, 4),
            ('Yaris', 23000, 1, 7),
            ('F150', 50000, 2, 4),
        ]
        cursor.executemany(query_insert, cars)
