# Ariel

_Please note that this repo is no longer actively maintained, and it may not be compatible with recent changes to the Facebook Messenger API._

_Please note that this repo's code is very simple work and acts as a reminder to not over-engineer stuff and focus on the value to our players._

This repository contains the code for a simple Facebook chatbot developed for Dytomic's Facebook page, designed to engage with users and provide information about job opportunities at Dytomic and details about Pirate Raids Online.

The project is named "Ariel" in memory of our co-founder's beloved dog that passed away several years ago. A tribute to this furry companion and serves as a reminder of the co-founder's cherished memories with their canine friend.

<p align="center">
  <img src="./ariel.jpg" width=256 />
</p>

### Key Features

- **Welcome Message**: The chatbot welcomes users to the Dytomic Facebook page and provides an introduction to the company and its projects.

- **Job Opportunities**: Users can inquire about job opportunities in the video game industry and receive information about available positions.

- **Game Details**: The chatbot offers information about Pirate Raids Online, including its features, gameplay mechanics, and development progress.

- And more...
  
## Usage

To use the Dytomic Facebook Chatbot, follow these steps:

1. Clone this repository to your local machine.

2. Set up a Facebook App and Page for your organization if you haven't already.

3. Configure the necessary environment variables, including the Facebook Page access token and verification token.

4. Deploy the Flask app to a hosting platform or server.

5. Set up the webhook for your Facebook Page to point to the deployed Flask app's endpoint.

6. Interact with the chatbot through the Facebook Page's Messenger.

## Files

The repository contains the following files and folders:

**Core Files:**

- **ariel.py**: Python script for handling intents and responses.

- **facebook.py**: Python script for the Flask web application that integrates with the Facebook Messenger platform.

- **dytomic.json**: JSON file containing intents and responses for Dytomic-related interactions.

- **PRO.json**: JSON file containing intents and responses for Pirate Raids Online-related interactions.

**Heroku Configuration Files:**

- **runtime.txt**: Specifies the Python runtime version.

- **Procfile**: Configuration file for deploying the app to hosting platforms.

**Design Files:**

- **design**: Folder containing DrawIO designs for the conversation tree.

## License

This project is licensed under the MIT License.
