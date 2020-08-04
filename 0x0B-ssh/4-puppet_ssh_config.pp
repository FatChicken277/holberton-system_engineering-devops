file_line { 'Turn off passwd auth':
  path     => '/etc/ssh/ssh_config',
  line     => '    PasswordAuthentication no',
  match    => '^ *PasswordAuthentication ',
  multiple => true,
  replace  => true
}
