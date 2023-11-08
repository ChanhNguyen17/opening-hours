# Restaurant Opening Hours API

## Table of Contents
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Testing](#testing)
  - [Using pytest](#using-pytest)
  - [Manual Testing with Curl](#manual-testing-with-curl)
- [Part 2](#part-2)

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

## Part 2
Tell us what you think about the data format. Is the current JSON structure the best way to represent  that kind of data or can you come up with a better version?

The current JSON structure is quite straightforward and easy to understand. It uses keys for each day of the week and an array of objects to represent the opening and closing times. However, there are a few areas where it could potentially be improved:

1. **Handling of opening and closing times**: The current structure uses separate objects for opening and closing times. This could potentially lead to errors if the data is not perfectly aligned. For instance, if an 'open' object is not followed by a 'close' object, it could lead to confusion. A possible improvement could be to pair opening and closing times together in the same object, like so:

  ```json
  "monday": [
    {
      "open": 36000,
      "close": 64800
    },
    {
      "open": 37800,
      "close": 64800
    }
  ]
  ```

2. **Handling of overnight hours**: The current structure does not handle overnight hours very intuitively. If a restaurant closes after midnight, the closing time is represented on the next day. This could be confusing and could make the data harder to process. A possible solution could be to allow the 'close' value to exceed the maximum UNIX timestamp for a day (86400), indicating that the closing time is on the next day.

3. **Use of UNIX timestamps**: While UNIX timestamps are a universal way to represent time, they might not be the most intuitive format for this use case. A more human-readable format like "HH:MM" could make the data easier to understand and process.

Here's how the data could look with these changes:

  ```json
  "monday": [
    {
      "open": "10:00",
      "close": "18:00"
    },
    {
      "open": "20:00",
      "close": "02:00"
    }
  ]
  ```

In this structure, it's clear that the restaurant opens at 10:00 AM, closes at 6:00 PM, reopens at 8:00 PM, and closes at 2:00 AM on the next day. This format is more intuitive and easier to understand at a glance.
