from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Define the target Ansible API URL
ansible_api_url = "http://192.168.1.19/api/v2/job_templates/41/launch/"
# Define your fixed bearer token
bearer_token = "zzghA1107f5SbKovtqj5Gbrgtqm9dy"

@app.route('/launch_job', methods=['GET','POST'])
def launch_job():
    try:
        # Define the headers with the fixed bearer token
        headers = {
            "Authorization": "Bearer " + bearer_token,
            "Content-Type": "application/json",
        }

        # Forward a GET request to the Ansible API with the fixed token
        response = requests.request("POST", ansible_api_url, headers=headers)

        # Check if the request to the Ansible API was successful
        if response.status_code in (200,201):
            print(response.json())
            return jsonify({"message": "Job launched successfully"}), 200
        else:
            return jsonify({"message": "Failed to launch job", "status_code": response.status_code}), response.status_code

    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

