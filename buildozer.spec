[app]
title = Simple Pong Game
package.name = simplepong
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.0.0
orientation = landscape
fullscreen = 1

# Android specific settings
android.archs = arm64-v8a
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
