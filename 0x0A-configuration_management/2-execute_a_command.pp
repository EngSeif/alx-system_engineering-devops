# Install Python 3.8 (if not already installed via system package manager)
package { 'python3.8':
  ensure   => installed,  # Ensure Python 3.8 is installed
  provider => 'pip3',     # Use pip3 provider
}

# Install Flask version 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3.8'],  # Require Python 3.8 to be installed first
}

# Install Werkzeug version 2.1.1
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['flask'],  # Require Flask to be installed first
}
