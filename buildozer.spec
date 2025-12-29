[app]

# (str) Title of your application
title = Minhas Notas

# (str) Application version
version = 0.1

# (str) Package name
package.name = minhasnotas

# (str) Package domain (usually org.customer.name)
package.domain = org.flaboss

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,json,txt,spec,env

# (list) List of directory to exclude (let empty to include all the directories)
source.exclude_dirs = tests, bin, build, venv, .venv, .git, .pytest_cache, .ruff_cache

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,requests,python-dotenv,urllib3,chardet,idna,certifi,openssl,pyjnius

# (str) Custom source folders for requirements
# packagename = foldername
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/app/app_icon.png

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

# (str) author used in folder for user endpoint
#author = © BuzzLightYear

#
# Android specific
#

# (bool) indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (bool) Accept SDK license
android.accept_sdk_license = True

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 31

# (str) Android NDK version to use
#android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be downloaded)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be downloaded)
#android.sdk_path =

# (str) ANT directory (if empty, it will be downloaded)
#android.ant_path =

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) OUYA Console category. Should be one of GAME or APP
#android.ouya.category = APP

# (list) Android additionnal libraries to copy into libs/armeabi
#android.add_libs_armeabi = lib/armeabi/libtest.so

# (bool) skip byte compile for .py files
#android.skip_byte_compile = False

# (list) List of Java files to add to the android project
#android.add_src =

# (str) Logcat filter to use
#android.logcat_filter = *:S python:D

# (str) Android entry point, default is to use main.py
#android.entrypoint = main.py

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java classes to add to the manifest
#android.add_activites = com.google.android.gms.ads.AdActivity

# (list) Android architecture to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >= 23)
android.allow_backup = True

# (list) Android application meta-data to set (extensions)
#android.meta_data =

# (list) Android library project to add (requires android.library_references)
#android.library_references =

# (list) Android shared libraries which will be added to each activity of the manifest.
#android.add_libs_xml =

# (list) Android static libraries which will be added to each activity of the manifest.
#android.add_static_libs_xml =

# (str) Android log level (debug, info, warning, error, critical)
#android.log_level = debug

# (bool) Android warn on root (True or False)
#android.warn_on_root = True

# (str) Android manifest intent filters to add
#android.manifest.intent_filters =

# (str) Android launch mode
#android.manifest.launch_mode = standard

# (list) Android additional modules to include (comma separated)
#android.add_modules =

# (str) Android additional resources to include (comma separated)
#android.add_resources =

# (str) Android additional layout resources to include (comma separated)
#android.add_layout_resources =

# (str) Android additional manifest attributes to include (comma separated)
#android.manifest.attributes =

# (str) Android additional properties to include (comma separated)
#android.add_properties =

# (str) Android additional xml to include (comma separated)
#android.add_xml =

# (str) Android additional java classes to include (comma separated)
#android.add_java_classes =

# (str) Android additional native libraries to include (comma separated)
#android.add_native_libs =

# (str) Android additional native project references to include (comma separated)
#android.add_native_projects =

# (str) Android additional java dependencies to include (comma separated)
#android.add_java_deps =

# (str) Android additional gradle dependencies to include (comma separated)
#android.add_gradle_deps =

# (str) Android additional build repositories to include (comma separated)
#android.add_build_repositories =

# (str) Android additional packaging options to include (comma separated)
#android.add_packaging_options =

# (str) Android additional aapt options to include (comma separated)
#android.add_aapt_options =

# (str) Android additional manifest uses-features to include (comma separated)
#android.add_uses_features =

# (str) Android additional manifest uses-permission to include (comma separated)
#android.add_uses_permission =

# (str) Android additional manifest uses-library to include (comma separated)
#android.add_uses_library =

# (str) Android additional manifest queries to include (comma separated)
#android.add_queries =

# (str) Android additional manifest application attributes to include (comma separated)
#android.add_application_attributes =

# (str) Android additional manifest activity attributes to include (comma separated)
#android.add_activity_attributes =

# (str) Android additional manifest intent intent-filter attributes to include (comma separated)
#android.add_intent_filter_attributes =

# (str) Android additional manifest theme to include (comma separated)
#android.add_theme =

# (str) Android additional manifest meta-data to include (comma separated)
#android.add_meta_data =

# (str) Android additional manifest receiver attributes to include (comma separated)
#android.add_receiver_attributes =

# (str) Android additional manifest service attributes to include (comma separated)
#android.add_service_attributes =

# (str) Android additional manifest provider attributes to include (comma separated)
#android.add_provider_attributes =

# (str) Android additional manifest permission attributes to include (comma separated)
#android.add_permission_attributes =

# (str) Android additional manifest permission-group attributes to include (comma separated)
#android.add_permission_group_attributes =

# (str) Android additional manifest permission-tree attributes to include (comma separated)
#android.add_permission_tree_attributes =

# (str) Android additional manifest instrumentation attributes to include (comma separated)
#android.add_instrumentation_attributes =

# (str) Android additional manifest uses-configuration attributes to include (comma separated)
#android.add_uses_configuration_attributes =

# (str) Android additional manifest uses-feature attributes to include (comma separated)
#android.add_uses_feature_attributes =

# (str) Android additional manifest uses-sdk attributes to include (comma separated)
#android.add_uses_sdk_attributes =

# (str) Android additional manifest support-screens attributes to include (comma separated)
#android.add_support_screens_attributes =

# (str) Android additional manifest compatible-screens attributes to include (comma separated)
#android.add_compatible_screens_attributes =

# (str) Android additional manifest supports-gl-texture attributes to include (comma separated)
#android.add_supports_gl_texture_attributes =

# (str) Android additional manifest uses-permission-sdk-23 attributes to include (comma separated)
#android.add_uses_permission_sdk_23_attributes =

# (str) Android additional manifest uses-split attributes to include (comma separated)
#android.add_uses_split_attributes =

# (str) Android additional manifest meta-data for application to include (comma separated)
#android.add_application_meta_data =

# (str) Android additional manifest meta-data for activity to include (comma separated)
#android.add_activity_meta_data =

# (str) Android additional manifest meta-data for receiver to include (comma separated)
#android.add_receiver_meta_data =

# (str) Android additional manifest meta-data for service to include (comma separated)
#android.add_service_meta_data =

# (str) Android additional manifest meta-data for provider to include (comma separated)
#android.add_provider_meta_data =

# (str) Android additional manifest meta-data for permission to include (comma separated)
#android.add_permission_meta_data =

# (str) Android additional manifest meta-data for permission-group to include (comma separated)
#android.add_permission_group_meta_data =

# (str) Android additional manifest meta-data for permission-tree to include (comma separated)
#android.add_permission_tree_meta_data =

# (str) Android additional manifest meta-data for instrumentation to include (comma separated)
#android.add_instrumentation_meta_data =

# (str) Android additional manifest meta-data for uses-configuration to include (comma separated)
#android.add_uses_configuration_meta_data =

# (str) Android additional manifest meta-data for uses-feature to include (comma separated)
#android.add_uses_feature_meta_data =

# (str) Android additional manifest meta-data for uses-sdk to include (comma separated)
#android.add_uses_sdk_meta_data =

# (str) Android additional manifest meta-data for support-screens to include (comma separated)
#android.add_support_screens_meta_data =

# (str) Android additional manifest meta-data for compatible-screens to include (comma separated)
#android.add_compatible_screens_meta_data =

# (str) Android additional manifest meta-data for supports-gl-texture to include (comma separated)
#android.add_supports_gl_texture_meta_data =

# (str) Android additional manifest meta-data for uses-permission-sdk-23 to include (comma separated)
#android.add_uses_permission_sdk_23_meta_data =

# (str) Android additional manifest meta-data for uses-split to include (comma separated)
#android.add_uses_split_meta_data =

# (str) Android additional manifest meta-data for activity-alias to include (comma separated)
#android.add_activity_alias_meta_data =

# (str) Android additional manifest attribute for activity-alias to include (comma separated)
#android.add_activity_alias_attributes =

# (str) Android additional manifest intent intent-filter attribute for activity-alias to include (comma separated)
#android.add_activity_alias_intent_filter_attributes =


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1

# (str) Path to buildozer data directory
#buildozer_dir = .buildozer

# (str) Path to buildozer bin directory
#bin_dir = bin
