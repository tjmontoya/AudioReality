# AudioReality Overview

Enabling blind people to enjoy 'sightseeing' in their unique way by providing them with literary-pleasing descriptions of their surroundings. AudioReality is a mobile app that uses user location data to output descriptions of user's surroundings. Currently, backend logic exists, but front end features like text-to-speech are not yet implemented. We will discuss next steps at the bottom of this README.

## Overview of fils:

1. `flutter_files` contain our frontend files.
2. `python_files` contain our backend files.
3. Audioreality_slides is our pitch deck.


## Getting started

The following are steps to run AudioReality locally, through an android/ios simulator. 

1. Download [flutter](https://docs.flutter.dev/get-started/install).
2. Download [android studio](https://developer.android.com/studio) for android emulator. For macbook users who would prefer ios emulator,download xcode by opening terminal and running `xcode-select —install`.
3. Clone repository.
4. Open terminal, and navigate to flutter root directory: `../AudioReality/flutter_files/geolocation_test/`, then execute `flutter run`. On emulator, flutter app should subsequently be built. There will an app in the homepage called 'geolocation_test'.
5. Open new terminal navigate to python root directory: `../AudioReality/python_files/`, and run `export REPLICATE_API_TOKEN="ac37eca7ce769850a8c17bbbc9ab8e8e8658c9ba"`. This is the necessary API key. Once done, run 'python3 app.py'.
6. On emulator, press button "Get Location Data". After loading, app will output surrounding location description.
7. (Optional) xcode contains a change laptop location feature, which can be user to manually test for desriptions for different locations. Open macbook settings & select "set location". From there, type in the lattitud and longitude of desired location, then on AudioReality flutter app, click on "Get Location Data" button to output description of new location.

## Tech Stack

### Frontend
1. Flutter.
2. Flutter's geolocation identifier library.

### Backend
1. Python.
2. Google's Streetview API.
3. Clip-interrogator API.
4. Open AI's GPT API, Davinci.

## What's next for AudioReality?

1. Conduct optimization on GPT's queries, so erroneous descriptions of locations will be reduced. Also conduct optimization to reduce loading time.
2. Create an app that is fully text-to-speech, so blind users can use the app without needing the help of caretakers to navigate its functions.
3. Enable profile creation, so users can tailor the output of descriptions to their profile settings. For instance, ask for age, so we can query GPT to give descriptions that consist of less complicated words to children. Alternatively, create options for styles descriptions. For instance, "Victorian era poems" style, etc.
4. Create a database of poems. We hope to collaborate with poets in Singapore and ask for copyright access, so we can integrate poems from poems.com.sg into our app. From there, we can programme our app to read poems about specific locations in Singapore if user happens to be close by.
5. Automate. Currently, user needs to click "get location" for the app to output a description of the location. We hope to automate this process, so users can simply wear their earphones, walk around Singapore, and have poems / beautiful descriptions played to them as and when something relevant comes into their vicinity.
6. Enable photo-taking. Currently, we provide location descriptions with google streetview. This works, but we'd like to improve upon it since google streeview may not necessarily reflect what the location currently looks like. We hope to enable photo-taking, or even video, so users can get the most current description of their surroudings.
