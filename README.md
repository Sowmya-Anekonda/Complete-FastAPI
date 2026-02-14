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