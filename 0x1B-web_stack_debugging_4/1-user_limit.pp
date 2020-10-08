# This script removes the user limits
exec { 'fix_user_limit':
  command => 'sed -i /holberton/d /etc/security/limits.conf',
  path    => '/bin',
}
