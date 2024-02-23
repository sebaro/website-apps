import redis

url_connection = redis.from_url("redis://default:3c47bc17a9d848babf5a2f90c33e4ac7@helped-macaw-35286.upstash.io:35286")
url_connection.ping()
