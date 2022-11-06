docker network create back-tier

docker compose -f ./docker-compose-monit.yml up -d

docker compose -f ./docker-compose-evmos.yml up