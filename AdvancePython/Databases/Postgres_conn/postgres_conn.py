# run with 'pipenv run python <filename>'

import psycopg2
from psycopg2 import sql
from config import DB_POSTGRES

db_config = DB_POSTGRES
target_db = "test"


def run_setup() -> None:
    conn = None
    target_conn = None

    try:
        conn = psycopg2.connect(**db_config)
        conn.autocommit = True

        with conn.cursor() as cursor:
            query = sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s")
            cursor.execute(query, (target_db,))
            exists = cursor.fetchone()

            if not exists:
                cursor.execute("CREATE DATABASE {}".format(sql.Identifier(target_db)))
                print(f"Database '{target_db}' created successfully!")
            else:
                print(f"Database '{target_db}' already exists.")

            target_config = db_config.copy()
            target_config["database"] = target_db

            conn = psycopg2.connect(**target_config)
            with conn.cursor() as cursor:
                table_name = "users"

                cursor.execute(
                    """
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_name = %s
                    );""",
                    (table_name,),
                )

                if cursor.fetchone()[0]:
                    cursor.execute(
                        sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
                    )

                    colnames = [desc[0] for desc in cursor.description]
                    print(f"\nTable: {table_name}")
                    print(" | ".join(colnames))
                    print("-" * 30)

                    rows = cursor.fetchall()
                    for row in rows:
                        print(" | ".join(map(str, row)))
                else:
                    print(f"Table '{table_name}' does not exist in '{target_db}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if "conn" in locals() and conn:
            conn.close()


if __name__ == "__main__":
    run_setup()
