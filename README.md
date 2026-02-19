# Complete Advance FAST API

### Curl Syntax:

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [1,2,3]}'
```


- -X POST : Specifies the HTTP method
- -H: Adds headers
- -d: Sends request body data  


<br>It enables live reloading and better error visibility during development.
```bash
uvicorn main:app --reload --debug
```

- --reload: Automatically restarts the server when you change the code (development only)
- --debug: Enables verbose output and stack traces in logs (not for production)


## Types of Caching

1. Client-side-caching : Done in browsers or frontend using mechanisms like HTTP headers (Cache-Control)

2. Server-side-caching: Caching happens on the server using tools like **Redis**, **Memcached** or **in-memory dictionary** 

3. CDN caching: Content Delivery Networks cache static resources close to users for fast load times.

- CDN is a network of geographically distributed servers that work together to deliver digital content (websites, videos, images, scripts, etc..) to users more efficiently and reliably.

- Instead of every user fetching content from a single central server (which can be slow or overloaded) serves content from a server that is geographically closer to the user. 

- this reduces latency, speeds up loading times, and improves scalability and availability.


### Key Consideration with Caching

- **Cache Invalidation:** When data changes, how do you ensure the cache is updated? This is crucial challenge in caching systems.

- **Eviction Policies:** Caches have limited memory, so older or less-used data must be removed using strategies like:

    - LRU (Least Recently Used)
    - LFU (Least Frequently Used)
    - FIFO (First In First Out)

- **Consistency:** Make sure cached data doesn't become stale or inconsistent with the source.


### Commonly Used Tools:

- **Redis:** An in-memory key-value store, widely used for caching due to its speed and flexibility

- **Memcached:** Lightweight and fast in-memory caching system

- **CDNs:** Used to cache and serve static content globally (e.b., Cloudflare, Akamai)

- **Local Memory Cache:** Python dictionaries or FastAPI **Iru_cache** decorators for lightweight scenarios.


## Redis supports a wide variety of data structures:


| TYPE | DESCRIPTION    | USE CASE |
|---|---|---|
| String | Basic key-value pair | Caching tokens |
| List | Ordered collection  | Queues |
| Set | Unordered collection with no duplicates | Tags |
| Sorted Set | Sorted list with scores   | Leaderboards |
| Hash | Key-value pairs within a key | User session info |
| Stream | Append-only log with ID  | Event logging |
| Pub/Sub | Publish/Subscribe messaging system | Chat app |
| Bitmaps | Bit-level operations | User tracking |
| HyperLogLog | Approximate unique counts  | Counting unique visitors |


### Common use-cases of Redis:

- **Caching** (e.g., ML Predictions, DB queries, External API Call)
- **Session Management** (e.g., storing user sessions in web applications)
- **Rate Limiting** (e.g., API throttling)
- **Real-time Analytics** 
- **Leaderboards and Ranking systems** (sorted sets)
- **Pub/Sub Messaging**


### Redis Setup

1. Install Redis Server (One-time setup)
```bash
docker run -d -p 6379:6379 redis
```
2. Install Redis Python Client:
- There're generally two options:
    - redis-py: pip install redis
    - aioredis: pip install redis[async]  (reommended)


### Test Redis Setup Using Python:

| Code | PURPOSE |
| ---- | ------- |
| redis.Redis(...) | Connects Python code to Resis |
| .ping() | Tests the connection
| .set(key, value) | Stores a value in Redis |
| .get(key) | Retrieves a value | 
| .decode() | Converts bytes to a readable string | 


### 