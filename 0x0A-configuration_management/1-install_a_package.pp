# Puppet manifest to install Flask version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.0.2',  # Replace with the version compatible with Flask 2.1.0
  provider => 'pip3',
}
