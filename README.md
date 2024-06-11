# flask-postgres-backend
source .venv/bin/activate  -setup virtual python environment

docker build --tag python-flask-docker .  
docker run -it  -p 3000:3000 python-flask-docker
docker-compose up -d 
docker-compose up -d --build  --build docker image
docker exec -it 38411c0418fc56a54206826a24648f22456a7d0b********** bash  --To ssh to container
docker-compose exec  psql-db psql --username=postgres --dbname=himanshu  --execute docker service
docker-compose logs -f   --view logs

