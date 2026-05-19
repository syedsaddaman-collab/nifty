[app]
title = SAM PREDICTION
package.name = sampridection
package.domain = org.sam

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 16.2

requirements = python3,kivy==2.3.0,requests,certifi,urllib3,pyjnius==1.6.1

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE,WAKE_LOCK

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.allow_backup = True

p4a.branch = master
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1