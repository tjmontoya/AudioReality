# AudioReality Overview

Enabling blind people to enjoy 'sightseeing' in their unique way by providing them with literary-pleasing descriptions of their surroundings. AudioReality is a mobile app that uses user location data to output descriptions of user's surroundings. Currently, backend logic exists, but front end features like text-to-speech are not yet implemented. We will discuss next steps at the bottom of this README.

## Overview of fils:

1. `flutter_files` contain our frontend files.
2. `python_files` contain our backend files.
3/ Audioreality_slides is our pitch deck.


## Getting started

The following are steps to run AudioReality locally, through an android simulator. 

1. Download [flutter](https://docs.flutter.dev/get-started/install).
2. Download [android studio](https://developer.android.com/studio) for android emulator.
3. Clone repository.
4. Open terminal, and navigate to flutter root directory: `../AudioReality/flutter_files/geolocation_test/`, then execute `flutter run`. On android emulator, flutter app should automatically be built. There will an app in the homepage called 'geolocation_test'.
5. Open new terminal navigate to python root directory: `../AudioReality/python_files/`, and run `export REPLICATE_API_TOKEN="ac37eca7ce769850a8c17bbbc9ab8e8e8658c9ba"`. This is the necessary API key. Once done, run 'python3 app.py'.
7. On emulator, press button "Get Location Data". After loading, app will output surrounding location description.

## Tech Stack

### Frontend
1. Flutter.
2. Flutter's geolocation identifier library.

### Backend
1. Python.
2. Google's Streetview API.
3. Clip-interrogator API.
4. Open AI's GPT API, Davinci.
