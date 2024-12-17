resource "openstack_compute_instance_v2" "my_instance" {
  name        = var.instance_name
  image_name  = var.image
  flavor_name = var.flavor
  key_pair    = var.key_name

  network {
    name = var.network_name
  }

  security_groups = [var.security_group]
}

# Создание тома размером 20 ГБ
resource "openstack_blockstorage_volume_v3" "my_volume" {
  name        = "${var.instance_name}_volume"
  size        = 20 # размер в ГБ
}

# Присоединение тома к виртуальной машине
resource "openstack_compute_volume_attach_v2" "my_volume_attach" {
  instance_id = openstack_compute_instance_v2.my_instance.id
  volume_id   = openstack_blockstorage_volume_v3.my_volume.id
}