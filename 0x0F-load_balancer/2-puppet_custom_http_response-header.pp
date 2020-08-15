# install nginx

exec { 'update':
  command => 'sudo apt-get update',
  path    => ['/usr/bin', '/bin'],
}

package { 'nginx':
  ensure   => 'installed',
  name     => 'nginx',
  provider => 'apt',
  require  => Exec['update'],
}

# custom header

file_line { 'custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => "\tadd_header X-Served-By \$hostname;",
  after   => 'listen 80 default_server;',
  require => Package['nginx'],
}

# start server.

exec { 'restart':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => File_line['custom_header'],
}
