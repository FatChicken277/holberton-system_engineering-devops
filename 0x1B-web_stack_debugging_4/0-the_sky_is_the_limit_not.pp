# This script fix the file limit.
exec { 'fix-for-nginx':
  command => 'sed -i s/15/1536/ /etc/default/nginx && service nginx restart',
  path    => '/bin',
}
