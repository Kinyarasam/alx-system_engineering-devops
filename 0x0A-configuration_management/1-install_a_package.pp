# install a package flask from pip -v 2.1.0

exec { 'install python packages':
  command => 'pip3 install -U Flask==2.1.0',
  path    => '/usr/bin'
}
