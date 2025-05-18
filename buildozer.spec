[app]

title = My Application
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# 최소 requirements로 먼저 성공한 뒤 필요한 패키지 추가 권장
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Android 최소 안정 구성 (AIDL 회피 목적)
android.api = 27
android.minapi = 21
android.sdk = 27
android.ndk = 19b
android.ndk_api = 21
android.private_storage = True
android.copy_libs = 1
android.archs = armeabi-v7a
android.allow_backup = True
android.logcat_filters = *:S python:D
android.permissions = android.permission.INTERNET

# Python-for-Android 설정 (안정 브랜치)
p4a.source = https://github.com/kivy/python-for-android.git@develop
