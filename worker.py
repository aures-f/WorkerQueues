import pika, time

# Conectar ao RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar a fila (durável)
channel.queue_declare(queue='task_queue', durable=True)

print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')

# Garantir distribuição justa (1 mensagem por vez)
channel.basic_qos(prefetch_count=1)

# Callback de processamento
def callback(ch, method, properties, body):
    print(f" [x] Recebido {body.decode()}")
    # Simular trabalho: cada '.' = 1 segundo
    time.sleep(body.decode().count('.'))
    print(" [x] Concluído")
    # Enviar confirmação manual
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Consumir mensagens
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
