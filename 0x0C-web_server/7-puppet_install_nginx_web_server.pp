#install nginx

package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt'
}

# create index

file { 'index':
  path    => '/var/www/html/index.html',
  mode    => '0664',
  content => 'Holberton School'
}

# config redirection

file_line { 'redirect_me':
  path  => '/etc/nginx/sites-available/default',
  line  => "\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}",
  after => '^server {',
}

# start server.

service { 'nginx':
  ensure => running,
  enable => true
}
