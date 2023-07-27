terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
   #   version = "4.8.0"
    }
  }
}


provider "google" {
    project = "celtic-beacon-387519"
    region = "europe-central2"
    credentials = file("./key.json")
    zone = "europe-central2-b"

}


provider "google-beta" {
    project = "celtic-beacon-387519"
    region = "europe-central2"
    credentials = file("./key.json")
    zone = "europe-central2-b"
}
