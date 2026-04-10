[app]

# (str) Title of your application
title = 工时计算器

# (str) Package name
package.name = workhourcalculator

# (str) Package domain (needed for android/ios packaging)
package.domain = org.workhour

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 30

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25c

# (bool) Accept SDK license
android.accept_sdk_license = True

# (str) Android Arch
android.archs = arm64-v8a, armeabi-v7a

# (bool) Android auto backup
android.allow_backup = True

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 0
