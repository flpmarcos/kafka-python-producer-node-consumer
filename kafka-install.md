# Seguindo tutorial de exemplo kafka para ter o primeiro contato
# https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f

# PRE REQUISITES
Docker
Docker compose
Git

# INSTALANDO KAFKA
git clone https://github.com/confluentinc/cp-docker-images

cd cp-docker-images/examples/kafka-single-node

# Executar arquivo compose
docker-compose up -d

# Teste (Devera conter dois container de acordo com a configuracao no docker compose)
docker-compose ps

# Olhando logs para verificar o funcionamento
# zookeeper
docker-compose logs zookeeper | grep -i binding
# kafka
docker-compose logs kafka | grep -i started

# Teste criando um Topic
docker-compose exec kafka  \
kafka-topics --create --topic meu-topico-legal --partitions 1 --replication-factor 1 --if-not-exists --zookeeper localhost:32181

# Confirmando Topic foi Criado
docker-compose exec kafka  \
  kafka-topics --describe --topic meu-topico-legal --zookeeper localhost:32181

# Criando mensagem por linha de comando
docker-compose exec kafka  \
  bash -c "seq 100 | kafka-console-producer --request-required-acks 1 --broker-list localhost:29092 --topic meu-topico-legal && echo 'Produced 100 messages.'"

# Consumindo mensagens por linha de comando
docker-compose exec kafka  \
  kafka-console-consumer --bootstrap-server localhost:29092 --topic meu-topico-legal --from-beginning --max-messages 100


# Produzindo informações por código
python producer/producer.py

# Consumindo informçaões por código

# Media das informações
consumer/consumer_avg.js
# Soma das informações
consumer/consumer_sum.js


