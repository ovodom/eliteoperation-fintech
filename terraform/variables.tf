variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "allowed_ssh_cidr" {
  description = "IP address range allowed to connect through SSH"
  type        = string
  default     = "127.0.0.1/32"
}
