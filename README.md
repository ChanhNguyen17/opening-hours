# Restaurant Opening Hours API

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Testing](#testing)
  - [Using pytest](#using-pytest)
  - [Manual Testing with Curl](#manual-testing-with-curl)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed.
- Docker and Docker Compose installed.

## Project Structure

The project is organized as follows:

- `src`
  - `app`
    - `exception_handlers.py`: Exception handling logic.
    - `routers.py`: FastAPI routers and views.
  - `cache`
    - `redis.py`: Redis cache logic.
  - `models`
    - `opening_hours.py`: Pydantic models for opening hours.
  - `routers`
    - `opening_hours.py`: FastAPI routers for opening hours.
  - `views`
    - `opening_hours`: Logic to render opening hours in human-readable format.
  - `settings`: Configuration settings for the project.
  - `utils`: Utility functions.
- `tests`
  - `test_app.py`: Tests for the FastAPI application.
  - `test_models.py`: Tests for data models.
  - `test_utils.py`: Tests for utility functions.
  - `test_views.py`: Tests for rendering opening hours.
  - `test_cache.py`: Tests for Redis cache.
- `app.py`: Main application entry point.
- `docker-compose.yaml`: Docker Compose configuration for running the application.


### Performance Improvement with Redis Cache:
This API utilizes Redis cache to improve performance by storing previously processed results. When you make requests for the same opening hours again, the API will retrieve the response from the cache, resulting in faster response times.

## Getting Started

To get this project up and running, follow these steps:

1. Clone the repository to your local machine:

    ```shell
    git clone https://github.com/yourusername/restaurant-opening-hours-api.git
    ```

2. Build and start the Docker containers using Docker Compose: This will create and start the FastAPI server and a Redis container.

    ```shell
    docker-compose up -d
    ```

3. The server should now be running at `http://0.0.0.0:8000`. You can access the API via this URL.

## Testing
You can test the API both programmatically using `pytest` and manually using `curl`.

### Using pytest
To run automated tests using pytest, execute the following command from the project root:

```shell
docker-compose exec fastapi pytest
```
This will execute all the tests and display the results.

### Manual Testing with Curl
You can test the API manually with curl. Here's an example of testing the API with a sample request:

```shell
# Send a POST request to the restaurant opening hours endpoint
curl -X POST -H "Content-Type: application/json" -d '{
"monday" : [{"type": "close", "value": 1000}, {"type":  "open", "value":  28800}, {"type": "close", "value": 36001}, {"type": "open", "value": 39600}, {"type": "close", "value": 45678}],
"tuesday" : [ { "type" : "open", "value" : 14400 }, { "type" : "close", "value" : 21600 } ],
"wednesday" : [],
"thursday" : [ { "type" : "open", "value" : 37800 }, { "type" : "close", "value" : 64800 } ],
"friday" : [ { "type" : "open", "value" : 36000 } ],
"saturday" : [ { "type" : "close", "value" : 3600 }, { "type" : "open", "value" : 36000 } ],
"sunday" : [ { "type" : "close", "value" : 3605 }, {"type" : "open", "value" : 43200 }, { "type" : "close", "value" : 75600 }, {"type" : "open", "value" : 86399 } ]
}' http://0.0.0.0:8000/restaurant-opening-hours
```

The expected response should be:
```json
{
  "Monday": "8 AM - 10:00:01 AM, 11 AM - 12:41:18 PM",
  "Tuesday": "4 AM - 6 AM",
  "Wednesday": "Closed",
  "Thursday": "10:30 AM - 6 PM",
  "Friday": "10 AM - 1 AM",
  "Saturday": "10 AM - 1:00:05 AM",
  "Sunday": "12 PM - 9 PM, 11:59:59 PM - 12:16:40 AM"
}
```

Bad Request:
```shell
curl -X POST -H "Content-Type: application/json" -d '{
    "monday": [{"type": "open", "value": 3600}, {"type": "close", "value": "invalid_time"}],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": [],
    "saturday": [],
    "sunday": []
}' http://0.0.0.0:8000/restaurant-opening-hours
```
The response to a bad request will return a 400 status code with details about the invalid request format.

```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": [
        "body",
        "monday",
        1,
        "value"
      ],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "invalid_time",
      "url": "https://errors.pydantic.dev/2.4/v/int_parsing"
    }
  ]
}
```

To stop the Docker containers using:
```shell
docker-compose down
```