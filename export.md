# Hosting Instructions & Folder Structure

## Part 1: Files to Upload (Folder Structure)

You need to upload the following files and folders to your GitHub repository.

**Tree Diagram of Files to Upload:**

```text
CV-Website/                  <-- ROOT FOLDER (Do not upload the root folder itself, just the contents below)
├── app/                     <-- UPLOAD THIS ENTIRE FOLDER
│   ├── data/                <-- Contains your JSON content (resume.json,etc.)
│   ├── static/              <-- Contains CSS, Images, and PDF
│   │   ├── css/
│   │   ├── img/
│   │   └── Shlok_Jain_AI_Devloper.pdf
│   ├── templates/           <-- Contains HTML files
│   └── main.py              <-- The main Python file for your app
├── Dockerfile               <-- UPLOAD THIS FILE
└── requirements.txt         <-- UPLOAD THIS FILE
```

**⚠️ DO NOT UPLOAD:**
*   `__pycache__`
*   `venv` or `env`
*   `.git`
*   `Shlok_Jain_AI_Devloper` (The folder with raw images)

---

## Part 2: Step-by-Step Hosting Guide

### Step 1: Upload Code to GitHub
1.  **Create a Repository**: Go to GitHub, create a new repository (e.g., `cv-website`).
2.  **Upload Files**:
    *   Click **Add file** > **Upload files**.
    *   Drag and drop the **`app`** folder, **`Dockerfile`**, and **`requirements.txt`**.
    *   Commit the changes.

### Step 2: Deploy on Render (Free Hosting)
1.  **Create Service**:
    *   Go to [dashboard.render.com](https://dashboard.render.com/).
    *   Click **New +** > **Web Service**.
    *   Select **Build and deploy from a Git repository**.
2.  **Connect GitHub**:
    *   Connect your GitHub account and select your `cv-website` repo.
3.  **Configure**:
    *   **Name**: `shlok-cv` (or similar).
    *   **Runtime**: **Docker**.
    *   **Instance Type**: **Free**.
    *   Click **Create Web Service**.
4.  **Wait**: It will take a few minutes to build. Once it says "Live", your site is up.

### Step 3: Connect GoDaddy Domain
1.  **Get Render IP**:
    *   In Render dashboard, go to **Settings** > **Custom Domains**.
    *   Add your domain (e.g., `www.yourdomain.com`).
    *   Copy the **A Record** (IP address) and **CNAME Record** (URL).
2.  **Update GoDaddy DNS**:
    *   Log in to GoDaddy > **DNS Management**.
    *   **Add A Record**:
        *   Type: `A`
        *   Name: `@`
        *   Value: `[Paste Render IP Address]`
    *   **Add CNAME Record**:
        *   Type: `CNAME`
        *   Name: `www`
        *   Value: `[Paste Render URL]` (e.g., `shlok-cv.onrender.com`)
3.  **Done**: Wait for changes to propagate (usually fast, but can take up to 24h).
