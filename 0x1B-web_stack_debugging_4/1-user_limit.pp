# Change the OS configuration so that it is possible to login
# with the holberton user and open a file without any error message.
user { 'holberton':
  ensure => present,
}

file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton hard nofile 65536\n",
}
