import pika
import os
import json

env_vars = os.getenv('VCAP_SERVICES')
service = json.loads(env_vars)['p-rabbitmq'][0]
amqp_url = service['credentials']['protocols']['amqp']['uri']
print(amqp_url)
connection = pika.BlockingConnection(pika.URLParameters(amqp_url))
# connection = pika.BlockingConnection(pika.URLParameters('amqp://7164d4ab-87d2-48fd-984e-eb0b7c20949e:2ps1a5qtoeljhvlj58haini24p@10.0.16.71:5672/5bb68766-99ac-43c8-948c-79a286b7a19b'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
