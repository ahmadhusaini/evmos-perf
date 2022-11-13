docker network create back-tier

docker compose -f ./docker-compose-monit.yml up -d

docker compose -f ./docker-compose-evmos.yml up

# sleep 30


# docker compose -f ./docker-compose-evmos.yml down


# result=`~/.go/bin/styx 'tendermint_consensus_total_txs{chain_id="evmos_9000-1", instance="evmos-devnet:26660", job="evmos-tendermint"}'`


# echo "$result" | tr ";" "," >> test-gen.csv

# docker compose -f ./docker-compose-monit.yml down -d