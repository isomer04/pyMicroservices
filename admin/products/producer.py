# https://customer.cloudamqp.com/saml/metadata/aaea6cd8-407c-43fa-b3dc-008182a2ac1c

# d5c6cd93-4ce5-b956-5632f439007f

import pika, json

params =  pika.URLParameters('')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    # channel.basic_publish(exchange='', routing_key='admin', body='hello')
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties )
    
    

# # CloudAMQP API endpoint for creating instances
# api_url = "https://api.cloudamqp.com/api/instances"

# # Your CloudAMQP API key
# api_key = "YOUR_API_KEY"

# # Headers for authentication
# headers = {
#     "Authorization": f"Basic {api_key}:",
#     "Content-Type": "application/x-www-form-urlencoded",
# }
