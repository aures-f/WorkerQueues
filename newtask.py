import sys
import pika

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a fila (durável)
channel.queue_declare(queue='task_queue', durable=True)

# Pega a mensagem da linha de comando ou usa padrão
message = ' '.join(sys.argv[1:]) or "Hello World!"

# Publicar mensagem persistente
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.DeliveryMode.Persistent  # mensagem persistente
    )
)

print(f" [x] Enviado {message}")
connection.close()
