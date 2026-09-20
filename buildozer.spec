[app]
title = SMART CARAVAN
package.name = app
package.domain = Com.SmartCaravan
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,xml
version = 4.11
requirements = python3,kivy,pyjnius,plyer
orientation = portrait
fullscreen = 0
icon.filename = smart_caravan_icon.png
android.api = 35
android.minapi = 23
android.permissions = INTERNET,POST_NOTIFICATIONS
android.enable_androidx = True
android.add_src = android_src
android.gradle_dependencies = com.google.firebase:firebase-messaging:24.1.2, androidx.core:core:1.15.0
android.extra_manifest_xml = %(source.dir)s/fcm_manifest.xml

[buildozer]
log_level = 2
warn_on_root = 1
