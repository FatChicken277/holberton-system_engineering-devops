# This script fix the file limit.
include stdlib

file_line { 'fix_file_limit':
  path  => '/etc/default/nginx',
  line  => 'ULIMIT="-n 1536"',
  match => '^ULIMIT=',
}

exec { 'restart':
  command => 'service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => File_line['fix_file_limit'],
}
