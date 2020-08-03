# This script create a manifest that kills a process named killmenow.

exec { 'killmenowkiller':
  command   => 'pkill killmenow',
  path      => '/usr/bin'
}
