import requests


class OEISPlugin:
    def __init__(self):
        self.base_url = "https://oeis.org/search?fmt=json&q="

    def query_oeis(self, sequence):
        # Convert the sequence into a string format suitable for the query
        query_string = ",".join(str(num) for num in sequence)
        # Create the full URL for the query
        full_url = self.base_url + query_string
        # Send a GET request to the OEIS API
        response = requests.get(full_url)
        # If the request was successful, return the response
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def process(self, message):
        # Check if the message contains a sequence of integers
        sequence = [int(s) for s in message.split(',') if s.isdigit()]
        print(sequence)
        if sequence:
            # If it does, query the OEIS
            response = self.query_oeis(sequence)
            if response and response['results']:
                # If the query was successful, return the response
                result = response['results'][0]
                return {key: result[key] for key in ["name", "data"]}
            else:
                # If the query was not successful, return an error message
                return "I'm sorry, I couldn't find any sequences in the OEIS that match the sequence you provided."
