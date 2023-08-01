module "gke_auth" {
  source       = "terraform-google-modules/kubernetes-engine/google//modules/auth"
  depends_on   = [module.gke]
  project_id   = var.project_id
  location     = module.gke.location
  cluster_name = module.gke.name
}

resource "local_file" "kubeconfig" {
  content  = module.gke_auth.kubeconfig_raw
  filename = "kubeconfig-${var.env_name}"
}
resource "google_compute_network" "private-network" {
  name         = "gke-network"
  auto_create_subnetworks = false
 
}
resource "google_compute_subnetwork" "my-subnetwork" {
  name   = "first-sub"
  region = "europe-central2"
  network = google_compute_network.private-network.self_link
  ip_cidr_range = "10.10.0.0/16"
  secondary_ip_range =[
{
        range_name    = "ip-range-pods-name"
        ip_cidr_range = "10.20.0.0/16"
},
{
        range_name    = "ip-range-services-name"
        ip_cidr_range = "10.30.0.0/16"
}
]
}

module "gke" {
  source            = "terraform-google-modules/kubernetes-engine/google//modules/private-cluster"
  project_id        = var.project_id
  name              = "${var.cluster_name}"
  regional          = false
  region            = var.region
  zones             = ["europe-central2-b"]
  network           = google_compute_network.private-network.name
  subnetwork        = google_compute_subnetwork.my-subnetwork.name
  ip_range_pods     = "ip-range-pods-name"
  ip_range_services = "ip-range-services-name"
  node_pools = [
    {
      name           = "node-pool"
      machine_type   = "n2-standard-2"
      node_locations = "europe-central2-b"
      min_count      = var.minnode
      max_count      = var.maxnode
      local_ssd_count = 0
      disk_size_gb   = var.disksize
      preemptible    = false
      auto_repair    = false
      auto_upgrade   = true
    },
  ]
}

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

resource "google_sql_user" "user" {
  name     = "me"
  instance = google_sql_database_instance.main.name
  password = "changeme"
}

output "db_public_ip" {
    value = google_sql_database_instance.main.public_ip_address
}

output "database_name" {
  description = "db name"
  value       = google_sql_database.database.name
}

output "db_user" {
  description = "db username"
  value = google_sql_user.user.name
}

output "db_password" {
  description = "db password"
  value = nonsensitive(google_sql_user.user.password)
}
