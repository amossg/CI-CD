resource "google_sql_database_instance" "main" {
  name             = "main-instance"
  database_version = "POSTGRES_15"
  region           = "europe-central2"
  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled    = true
      authorized_networks {
        name    = "all-ip-addresses"
        value   = "0.0.0.0/0"
      }
    }
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

output "db_public_ip" {
    value = google_sql_database_instance.main.public_ip_address
}
