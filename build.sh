#!/bin/bash
set -e
echo "==========================================="
echo " Building PARAM Porul Supercomputer APK "
echo "==========================================="

if ! command -v node &> /dev/null; then
    echo "Node.js is not installed. Please install Node.js (v18+)."
    exit 1
fi

echo "[1/4] Installing Capacitor dependencies..."
npm install

echo "[2/4] Setting up Android project..."
if [ ! -d "android" ]; then
    npx cap add android
fi

echo "[3/4] Syncing web app assets to Android..."
npx cap sync android

echo "[4/4] Opening Android Studio to compile APK..."
echo "In Android Studio: Click 'Build' -> 'Build Bundle(s) / APK(s)' -> 'Build APK(s)'"
npx cap open android

echo "Done! The APK will be compiled into android/app/build/outputs/apk/debug/app-debug.apk"
