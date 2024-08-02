# Using strace, find out why Apache is returning a 500 error.
# Once you find the issue, fix it and then automate it using Puppet
# (instead of using Bash as you were previously doing).
exec {'exec':
    command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php;
    service apache2 restart',
    provider => shell
  }
