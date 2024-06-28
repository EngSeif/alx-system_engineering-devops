# Install Flask version 2.1.0 using pip3

package { 'pip3':
  ensure   => installed,
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['pip3'],
}
