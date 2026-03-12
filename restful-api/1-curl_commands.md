# Consuming Data from an API using curl

## Checking curl installation

Command:

curl --version

Example Output:

curl 7.68.0 (x86_64-pc-linux-gnu)
Protocols: http https ftp ftps
Features: IPv6 SSL libz


---

# Fetching a webpage

Command:

curl http://example.com

Description:
This command retrieves the HTML content of the example.com webpage.


---

# Fetching data from an API

Command:

curl https://jsonplaceholder.typicode.com/posts

Description:
This retrieves a list of posts from the JSONPlaceholder public API.

Example Output (shortened):

[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati",
    "body": "quia et suscipit..."
  }
]


---

# Fetching only HTTP headers

Command:

curl -I https://jsonplaceholder.typicode.com/posts

Example Output:

HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Cache-Control: max-age=43200
Date: Mon, 01 Jan 2024 12:00:00 GMT

Description:
The `-I` flag retrieves only the response headers without the response body.


---

# Making a POST request

Command:

curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

Example Output:

{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}

Description:
The `-X POST` option specifies the HTTP method, and `-d` sends data to the API.
JSONPlaceholder simulates creating a new post and returns an object with id 101.