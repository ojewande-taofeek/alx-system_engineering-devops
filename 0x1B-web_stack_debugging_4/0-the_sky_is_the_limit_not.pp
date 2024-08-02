# esting how well our web server setup featuring Nginx is doing
# under pressure and it turns out it’s not doing well:
# we are getting a huge amount of failed requests.

exec { 'com':
  command  => 'sed -i s/15/4096/g /etc/default/nginx; sudo service nginx restart',
  provider => 'shell'
}
