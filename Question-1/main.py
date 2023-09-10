def get_numbers(urls):
  """Gets the numbers from the specified URLs."""
  # This function takes a list of URLs as input and returns a list of numbers.
  # The function makes a request to each URL and parses the response as JSON.
  # The numbers in the JSON response are then added to the list of numbers.

  numbers = []
  for url in urls:
    # This loop iterates over the list of URLs.
    response = requests.get(url)
    # This makes a request to the specified URL.
    if response.status_code == 200:
      # This checks if the response status code is 200, which means that the request was successful.
      data = json.loads(response.content)
      # This parses the response as JSON.
      numbers.extend(data["numbers"])
    # This adds the numbers in the JSON response to the list of numbers.
  return numbers

def main():
  """The main function."""
  # This is the main function.
  urls = ["http://20.244.56.144/numbers/primes", "http://20.244.56.144/numbers/fibo"]
  # This defines a list of URLs.
  numbers = get_numbers(urls)
  # This calls the `get_numbers()` function and stores the results in the `numbers` variable.
  print(json.dumps({"numbers": numbers}))
  # This prints the results to the terminal.

if _name_ == "_main_":
  main()
