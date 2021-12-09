import bmemcached

host = 'm-bp199987c3c8bff4.memcache.rds.aliyuncs.com'
port = 11211
user = 'm-bp199987c3c8bff4'
password = 'rety3zvzv5eAiyw'
client = bmemcached.Client(host + ':' + str(port), user, password)
client.set('greeting', 'hello memcache!')
print(client.get('greeting'))
