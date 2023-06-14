db_login = "postgres"
db_password = "042581"
db_port = 5432
db_host = "localhost"
db_name = "book_sales"
db_protocol = "postgresql"

DSN = f"{db_protocol}://{db_login}:{db_password}@{db_host}:{db_port}/{db_name}"