docker build -t <image name>
docker run -d -p 3306:3306 --name mysql -e MYSQL_ROOT_PASSWORD=root <image name>