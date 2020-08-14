#intall libraries

package { 'puppet-module-puppetlabs-stdlib':
  ensure   => 'latest',
  name     => 'puppet-module-puppetlabs-stdlib',
  provider => 'apt',
}

# install nginx

package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt',
}

# custom header

file_line { 'custom_header':
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By \$hostname;",
  after  => '^server {$',
  notify => Service['nginx'],
}

# restart server.

service { "nginx":
    ensure => running,
}
