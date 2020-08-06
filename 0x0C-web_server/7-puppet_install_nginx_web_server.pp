#install nginx

package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt'
}

# start server.

exec { 'start':
  command => 'service nginx start',
  path    => '/usr/bin'
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
  line  => "\tlocation \/redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}",
  after => '^server {',
}

# config 404

file { '404.html':
  path    => '/var/www/html/404.html',
  mode    => '0664',
  content => "Ceci n'est pas une page"
}

file_line { '404':
  path  => '/etc/nginx/sites-available/default',
  line  => "\n\terror_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /var/www/html/;\n\t\tinternal;\n\t",
  after => '^server {',
}

# restart server.

exec { 'restart':
  command => 'service nginx restart',
  path    => '/usr/bin'
}
