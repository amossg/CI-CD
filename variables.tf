variable "project_id" {
  description = "The project ID of your project"
   default     = "celtic-beacon-387519"
}
variable "cluster_name" {
  description = "The name for the GKE cluster"
  default     = "gke-terraform"
}
variable "env_name" {
  description = "The environment for the GKE cluster"
  default     = "learn"
}
variable "region" {
  description = "The region to host the cluster in"
  default     = "europe-central2"
}
variable "zones" {
  description = "Cluster zone"
  default     = "europe-central2-b"
}
variable "network" {
  description = "The VPC network created to host the cluster in"
  default     = "gke-network"
}
variable "subnetwork" {
  description = "The subnetwork created to host the cluster in"
  default     = "gke-subnet"
}
variable "ip_range_pods_name" {
  description = "The secondary ip range to use for pods"
  default     = "ip-range-pods"
}
variable "ip_range_services_name" {
  description = "The secondary ip range to use for services"
  default     = "ip-range-services"
}
variable "service-account-id" {
  description = "The ID of service account of GCP"
  default     = "serviceaccount-id"
}
variable "cpus" {
  description = "Number of cpus"
  default     = "2"
}

variable "minnode" {
  description = "Minimum number of node pool"
  default     = 1
}
variable "maxnode" {
  description = "Maximum number of node pool"
  default     = 1
}

variable "disksize" {
  description = "Disk Size in GB"
  default     = 20
}

variable "address" {
  description = "First IP address of the IP range to allocate to CLoud SQL instances and other Private Service Access services. If not set, GCP will pick a valid one for you."
  type        = string
  default     = ""
}

variable "description" {
  description = "An optional description of the Global Address resource."
  type        = string
  default     = ""
}

variable "prefix_length" {
  description = "Prefix length of the IP range reserved for Cloud SQL instances and other Private Service Access services. Defaults to /16."
  type        = number
  default     = 16
}

variable "ip_version" {
  description = "IP Version for the allocation. Can be IPV4 or IPV6."
  type        = string
  default     = ""
}

variable "labels" {
  description = "The key/value labels for the IP range allocated to the peered network."
  type        = map(string)
  default     = {}
}

