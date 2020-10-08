# This script fix the file limit.
exec { 'fix_file_limit':
  command => 'sed -i /ULIMIT/d /etc/default/nginx',
  path    => '/bin',
}
