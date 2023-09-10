import requests
import json
import logging

def get_numbers(urls, timeout=5):
  """Gets the numbers from the specified URLs."""
  # This function takes a list of URLs as input and returns a list of numbers,makes a request to each URL and parses the response as JSON.
  # The numbers in the JSON response are then added to the list of numbers.
  # The timeout parameter specifies the maximum amount of time to wait for each request.

  numbers = []
  for url in urls:
    response = requests.get(url, timeout=timeout)
    if response.status_code == 200:
      data = json.loads(response.content)
      numbers.extend(data["numbers"])

  return numbers

def main():
  urls = ["http://20.244.56.144/numbers/primes", "http://20.244.56.144/numbers/fibo"]
  # This defines a list of URLs.
  logging.basicConfig(level=logging.INFO)
  numbers = get_numbers(urls, timeout=5)
  # This calls the `get_numbers()` function and stores the results in the `numbers` variable.
  logging.info("The numbers are: %s", numbers)
  # This prints the results to the terminal.

if _name_ == "_main_":
  main()
