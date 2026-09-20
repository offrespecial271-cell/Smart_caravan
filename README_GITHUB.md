# SMART CARAVAN 4.11 — GitHub APK + FCM

This project is based on the working 4.11 CLEAN app and adds an Android FCM service.

## Build the APK with GitHub Actions

1. Create a GitHub repository, for example `smart-caravan`.
2. Upload all files/folders from this project to the repository root.
3. Commit to the `main` branch.
4. Open **Actions** in GitHub.
5. Select **Build SMART CARAVAN APK**.
6. Click **Run workflow** if it is not triggered automatically.
7. Wait for the workflow to finish.
8. Open the completed workflow run and download the artifact **smart-caravan-apk**.

The APK is a debug build intended for testing on the team's Android phones.

## FCM

The Android app initializes Firebase from the supplied project configuration and subscribes to:
`smart_caravan_team`

Your server must use a Firebase Admin service-account credential to send to that topic. Never put the service-account JSON in the APK or GitHub repository.

## Important

The package ID used for this build is `Com.SmartCaravan.app`. If the Firebase Android app is registered under a different package ID, register `Com.SmartCaravan.app` as an additional Android app in the same Firebase project before testing FCM.
