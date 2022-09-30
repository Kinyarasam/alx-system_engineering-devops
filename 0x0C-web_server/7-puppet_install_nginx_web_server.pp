# Configuring your server

# Setup New Ubuntu server with nginx
exec { 'update system':
  command => '/usr/bin/apt-get update',
}

# Update package dependancies and install nginx
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

# create index file
file {'/var/www/html/index.nginx-debian.html':
  content => 'Hello World!
'
}

# add redirection
exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

# nginx status
service {'nginx':
  ensure  => running,
  require => Package['nginx']
}

