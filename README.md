# PARAM Porul Supercomputer Mobile App (NIT Trichy)

This project contains everything needed to run and generate a standalone Android APK for the **PARAM Porul HPC Portal**.

---

### Method 1: Instant Cloud Build via GitHub Actions (No Android Studio required!)
1. Create a new GitHub repository (can be private or public).
2. Unzip this package and push all files to your GitHub repository.
3. Click on the **Actions** tab in your GitHub repository.
4. The **"Build Android APK"** action will run automatically.
5. In 2 minutes, open the completed run and download **ParamPorul-HPC-Debug-APK** directly to your phone!

---

### Method 2: Local Build using Android Studio / Capacitor
Requirements: Node.js (v18+) and Android Studio.

1. Open your terminal in this extracted folder.
2. Run:
   ```bash
   npm install
   npx cap add android
   npx cap sync android
   npx cap open android
   ```
3. In Android Studio: Click **Build** -> **Build Bundle(s) / APK(s)** -> **Build APK(s)**.
4. Your `.apk` will be in `android/app/build/outputs/apk/debug/app-debug.apk`.

---

### Method 3: Instant WebAPK / PWA (Zero compile)
1. Run `python3 -m http.server 8080` inside the `www` folder.
2. Open `http://<your-ip>:8080` on Chrome for Android.
3. Tap **Menu (⋮) -> Install App**. It installs as a real Android app with the PARAM Porul icon!
