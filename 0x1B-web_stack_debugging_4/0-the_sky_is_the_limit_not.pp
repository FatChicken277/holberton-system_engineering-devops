# This script fix the file limit.
file_line { 'fix_file_limit':
  path  => '/etc/default/nginx',
  line  => 'ULIMIT="-n 1000"',
  match => '^ULIMIT=',
}

exec { 'restart':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => File_line['fix_file_limit'],
}
