
resource "google_sql_database_instance" "main" {
  name             = "main-instance"
  database_version = "POSTGRES_15"
  region           = "europe-central2"
  settings {
    tier = "db-f1-micro"
}
}

resource "google_sql_database" "database" {
  name     = "my-database"
  instance = google_sql_database_instance.main.name
}

resource "google_sql_user" "users" {
  name     = "me"
  instance = google_sql_database_instance.main.name
  password = "changeme"
}

output "public_ip" {
    value = google_sql_database.database.master_public_ip
}
