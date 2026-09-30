[app]

title = SMART CARAVAN
package.name = smartcaravan
package.domain = com.smartcaravan

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

version = 4.11

requirements = python3==3.11.9,kivy==2.3.1,pyjnius,plyer

orientation = portrait
fullscreen = 0

icon.filename = smart_caravan_icon-2.png

android.api = 35
android.minapi = 23
android.ndk = 28c

android.permissions = INTERNET,POST_NOTIFICATIONS

android.enable_androidx = True

[buildozer]

log_level = 2
warn_on_root = 1
