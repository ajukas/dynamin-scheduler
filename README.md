# Dynamic Scheduler

This is a poc to test if is possible to run a dynamic scheduled job, reciving the timer as a parameter

### Prerequisites
* python3
* pip3

### Installation
```bash
pip3 install -r requirements.txt
```

### Usage
The `HOSTNAME` and `PORT` are on `.env` file

```bash
pip3 src/api.py
```

### Examples of requests to create a scheduled job
```bash
curl --request POST \
  --url http://localhost:8080/create \
  --header 'Content-Type: application/json' \
  --data '{
	"seconds": 9
}'
```