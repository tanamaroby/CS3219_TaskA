# How to run docker container

## Get the docker images

### Option 1

Get the docker image from docker hub using the command

    docker pull robytanama/cs3219_taska

### Option 2

Clone the repository using

    git clone https://github.com/tanamaroby/CS3219_TaskA.git

Then, build the image from the Dockerfile using the command

    docker build -t robytanama/cs3219_taska .

## Running the container without reverse proxy

Once the cs3219_taska image is up, just run the following command

    docker run -p 8888:5000 --name cs3219_taska robytanama/cs3219_taska

The html page (sentence generator) is now accessible on http://localhost:8888

## Running the container with reverse proxy

To do this, you need to clone the repo first to get all the files.

Pull the Nginx image first using the command

    docker pull nginx

Then, assuming that the cs3219_taska image has already been created, run docker compose using the command

    docker-compose up -d nginx

ensure that Nginx service is created first to test out the dependency

The html page is now accessible on http://localhost:80 (might be a bit slow, try to refresh if time out).

