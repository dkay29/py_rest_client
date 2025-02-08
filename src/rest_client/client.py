import requests
import threading

class RestClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        self._handle_response(response)
        return response.json()

    def post(self, endpoint, data=None, json=None, headers=None):
        response = requests.post(f"{self.base_url}/{endpoint}", data=data, json=json, headers=headers)
        self._handle_response(response)
        return response.json()

    def put(self, endpoint, data=None, headers=None):
        response = requests.put(f"{self.base_url}/{endpoint}", data=data, headers=headers)
        self._handle_response(response)
        return response.json()

    def delete(self, endpoint):
        response = requests.delete(f"{self.base_url}/{endpoint}")
        self._handle_response(response)
        return response.json()

    def _handle_response(self, response):
        if not response.ok:
            raise Exception(f"Request failed: {response.status_code}, {response.text}")

# Example usage
if __name__ == "__main__":
    base_url = "http://localhost:9000/api"
    client = RestClient(base_url)
    resp=client.get("sleep",params={"secs":5})
    print(str(resp))
    print(resp.get("message"))

    def
    # Define the sleep parameters for each thread
    sleep_params = [2, 4, 6]

    # Create and start threads
    threads = []
    for secs in sleep_params:
        thread = threading.Thread(target=client.get, args=("sleep", secs))
        threads.append(thread)
        thread.start()

