import os

home = os.environ['HOME']

if not os.path.exists('/usr/sbin/nginx'):
    os.system('apt update')
    os.system('apt install nginx -y')
os.chdir('/etc')
os.system('rm -rf nginx')
os.system('rm -rf '+home+'/catkin_ws/src/third_party/web_server/nginx')
os.system('cp -R '+home+'/catkin_ws/src/third_party/web_server/nginx_backup  '+home+'/catkin_ws/src/third_party/web_server/nginx')
os.system('sudo ln -s '+home+'/catkin_ws/src/third_party/web_server/nginx  /etc/nginx')

file = open(home+'/catkin_ws/src/third_party/web_server/nginx/nginx.conf','w+')
file.write(
"""user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	##
	# Logging Settings
	##

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Gzip Settings
	##

	gzip on;

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

	##
	# Virtual Host Configs
	##

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;

    server {
        listen 8081;
        index  index.html;
        root %(remote)s;
        location /api {
            proxy_pass http://localhost:3421;
        }
    }

}""" % {   'remote':home+'/catkin_ws/src/remote/dist',
           'events': r'{}'}
)
file.close()
os.system('nginx -s reload')