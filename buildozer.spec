[app]

# (str) Title of your application
title = SAM PREDICTION

# (str) Package name
package.name = sampridection

# (str) Package domain (needed for android/ios packaging)
package.domain = org.sam

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 16.2

# (list) Application requirements
requirements = python3,kivy==2.3.0,requests,certifi,urllib3,pyjnius==1.6.1

# (str) Application orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WAKE_LOCK

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (list) Android archs to build
android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable backup of the application
android.allow_backup = True

# (str) Android SDK License Acceptance
android.accept_sdk_license = True

# (str) Python-for-android branch
p4a.branch = master

# (str) Python-for-android bootstrap
p4a.bootstrap = sdl2

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
