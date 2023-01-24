import requests
import argparse
import os

# Set the organization as SFDC and input username from Jenkins
organization = 'prashantnewtestorg'
pat_token=os.environ.get('PAT_TOKEN')

parser = argparse.ArgumentParser(description="Check if the user is the member of GitHub organization if not add it ")
parser.add_argument('--username',help="GitHub user id of the user")
args=parser.parse_args()

# Set the API endpoint and personal access token
check_endpoint = f'https://api.github.com/orgs/{organization}/members/{args.username}'
add_endpoint = f'https://api.github.com/orgs/{organization}/memberships/{args.username}'
headers = {'Authorization': f'token {pat_token}'}

try:
    # Make the API request to check if the user is a member
    response = requests.get(check_endpoint, headers=headers)

    # If the user is not a member, add them
    if response.status_code != 204:
        # Set the API payload
        data = {'role': 'member'}

        # Make the API request to add the user
        response = requests.put(add_endpoint, headers=headers, json=data)

        # Check the response status code
        if response.status_code == 200:
            print(f'{args.username} was added to {organization} org')
        else:
            print(f'Error adding {args.username} to {organization} org')
    else:
        print(f'{args.username} is already a member of {organization} org')

# Catch any exceptions if it failed to add the user
except Exception as e:
    print(f'An error occurred: {e}')
