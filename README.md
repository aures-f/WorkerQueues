# WorkerQueues

Este repositório faz parte de uma **atividade acadêmica** da disciplina de **Sistemas Distribuídos** (UFC).  
O objetivo é demonstrar o padrão **Worker Queues** (fila de trabalho) usando **RabbitMQ** e **Python**.

## Contexto

A atividade tem como finalidade praticar conceitos de **mensageria** e **processamento distribuído**, utilizando filas para desacoplar a produção e o consumo de mensagens.  
Com isso, múltiplos *workers* podem processar tarefas em paralelo, aumentando a escalabilidade do sistema.

## Estrutura do Projeto

- *newtask.py* → envia mensagens/tarefas para a fila.  
- *worker.py* → consome as mensagens e simula o processamento.  
- *rabbitmq/* → ambiente virtual Python usado no desenvolvimento.

## Requisitos

- Python 3.x  
- RabbitMQ (instalado e em execução)  
- Biblioteca [pika](https://pypi.org/project/pika/) para comunicação com RabbitMQ  

## Instalação e uso

1. Clone este repositório:
bash
git clone https://github.com/aures-f/WorkerQueues.git
cd WorkerQueues
2. Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate   # no Windows
source venv/bin/activate  # no Linux/macOS
3. Instale as dependências:
pip install pika
4. Certifique-se de que o RabbitMQ esteja rodando.
5. Em um terminal, inicie o worker:
python worker.py
6. Em outro terminal, envie tarefas:
python newtask.py "Primeira Tarefa"

## Exemplo de execução
Enviando uma tarefa:
python newtask.py "Segunda Tarefa"
Saída no worker:
 [x] Received 'Segunda Tarefa'
 [x] Done

## Aprendizados

Uso de RabbitMQ para comunicação assíncrona.

Conceito de filas de mensagens.

Escalabilidade com múltiplos workers.

Integração entre produtor e consumidor em sistemas distribuídos.



