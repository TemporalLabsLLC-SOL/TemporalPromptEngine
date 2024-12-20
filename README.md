Temporal Prompt Engine: Local, Open-Source, Intuitive, Cinematic Prompt Engine + Video and Audio Generation Suite for Nvidia GPUs

##NOW FEATURING custom 12b HunYuanVideo script with Incorporated MMAudio for 80gb cards.

<a href="https://ibb.co/PrRwywr"><img src="https://i.ibb.co/PrRwywr/Screenshot-1050.png" alt="Screenshot-1050" border="0"></a> <a href="https://ibb.co/xgsmcbh"><img src="https://i.ibb.co/xgsmcbh/Screenshot-1049.png" alt="Screenshot-1049" border="0"></a> <a href="https://ibb.co/xGxNTcV"><img src="https://i.ibb.co/xGxNTcV/Screenshot-1048.png" alt="Screenshot-1048" border="0"></a> <a href="https://ibb.co/k8Rx5wk"><img src="https://i.ibb.co/k8Rx5wk/Screenshot-1060.png" alt="Screenshot-1060" border="0"></a> <a href="https://ibb.co/ZGtzSL6"><img src="https://i.ibb.co/ZGtzSL6/Screenshot-1061.png" alt="Screenshot-1061" border="0"></a> <a href="https://ibb.co/ynzxCBj"><img src="https://i.ibb.co/ynzxCBj/Screenshot-1062.png" alt="Screenshot-1062" border="0"></a> <a href="https://ibb.co/1vg5Lqp"><img src="https://i.ibb.co/1vg5Lqp/Screenshot-1063.png" alt="Screenshot-1063" border="0"></a> <a href="https://ibb.co/MBDNgpH"><img src="https://i.ibb.co/MBDNgpH/Screenshot-1064.png" alt="Screenshot-1064" border="0"></a>

##MASSIVE UPDATE TO INSTRUCTIONS BELOW COMING VERY SOON (12/11/2024)

I am looking for a volunteer assistant if you're interested reach out at Sol@TemporalLab.com - This is going to a webapp version VERY soon.

## Table of Contents
1. [Introduction](#1-introduction)
2. [Features Overview](#2-features-overview)
3. [Installation](#3-installation)
   - [Prerequisites](#prerequisites)
4. [Quick Start Guide](#4-quick-start-guide)
5. [API Key Setup](#5-api-key-setup)
6. [Story Mode: Unleash Epic Narratives](#6-story-mode-unleash-epic-narratives)
7. [Inspirational Use Cases](#7-inspirational-use-cases)
8. [Harnessing the Power of ComfyUI](#8-harnessing-the-power-of-comfyui)
9. [Local Video Generation Using CogVideo](#9-local-video-generation-using-cogvideo)
10. [Join the Temporal Labs Journey](#10-join-the-temporal-labs-journey)
11. [Donations and Support](#11-donations-and-support)
12. [Additional Services Offered](#12-additional-services-offered)
13. [Attribution and Courtesy Request](#13-attribution-and-courtesy-request)
14. [Contact](#14-contact)
15. [Acknowledgments](#15-acknowledgments)

---

<a name="1-introduction"></a>
## Introduction

Welcome to the **Temporal Prompt Engine** a comprehensive framework for building out batch variations or story sequences for video prompt generators. This idea was original started as a comfyUI workflow for CogVideoX but has since evolved into a modular framework that has proven to scale with new foundational models and pipelines.

<a name="2-features-overview"></a>
## Features Overview

- **Cinematic Video Prompts**: Tailor every aspect of your scene—from camera type and lens to lighting and framing.
- **Temporal Awareness**: Pick a decade and the camera options will represent that time, adding depth and context to your scenes.
- **Dynamic Variables**: Adjust settings like lighting, camera movement, lighting, time of day and more through easy to use drop-down options.
- **Special Modes**:
  - **Story Mode**: Seamlessly blend prompts across frames to create cohesive narratives, enabling you to craft epic stories or intimate tales.
  - **Holiday Mode**: Generate seasonal content tailored to holidays, perfect for festive branding and marketing.
  - **Chaos Mode**: Add unpredictability with Chaos Mode.
- **Interconnected Settings**: Experience how choices like selecting an ancient art style influence other variables like color palette and texture, creating a cohesive and authentic output.
- **Cross-Platform Compatibility**: Available for **Windows** & **Linux**

---

<a name="3-installation"></a>
## Installation

Setting up the Temporal Prompt Engine is simple and hassle-free, allowing you to focus on creation rather than configuration. This section provides installation steps for **Windows** users.

<a name="System Preparation"></a>
### System Preparation

[YouTube Setup Guide Part 1](https://youtu.be/8GQr-lePOWw?si=GuEbjGhk-tbelpZ7):
- **Operating System**: Windows 10 or later
- **Python**: Version 3.10.9
    - **Download Python Installer**:
      - Visit the [Python Downloads](https://www.python.org/downloads/release/python-3109/) page.
      - Download the **Python 3.10.9** installer for Windows.
    - **Install Python**:
      - **Run the Installer**:
        - Double-click the downloaded EXE installer file.
        - **Important**:
          - **If you already have Python installed**:
            - Be cautious when adding Python to PATH, as it may overwrite your existing Python version in the system PATH.
            - To avoid conflicts, you can install Python 3.10.9 without adding it to the PATH. Instead, use the Python Launcher for Windows (`py`) to specify the version when running commands.
          - **If you don't have Python installed**:
            - Check the box **"Add Python to PATH"** at the bottom of the installer window.
        - Click **"Install Now"**.
    - **Verify Installation**:
      - Open a new Command Prompt.
      - Run:
        ```bash
        py -3.10 --version
        ```
      - You should see `Python 3.10.9`.
	 
##If you want the Video Generation capabilities to work you will also need a local Python 3.12.4 Installed as well. If this is in place the setup.py will handle everything.
##If you only want to use the prompt engine and sound effects generator then you are fine with only 3.10.9 even if the setup.py complains a little.

- **Operating System**: Windows 10 or later
- **Python**: Version 3.12.4
    - **Download Python Installer**:
      - Visit the [Python Downloads](https://www.python.org/downloads/release/python-3124/) page.
      - Download the **Python 3.12.4** installer for Windows.
    - **Install Python**:
      - **Run the Installer**:
        - Double-click the downloaded EXE installer file.
        - **Important**:
          - **If you already have Python installed**:
            - Be cautious when adding Python to PATH, as it may overwrite your existing Python version in the system PATH.
            - To avoid conflicts, you can install Python 3.10.9 without adding it to the PATH. Instead, use the Python Launcher for Windows (`py`) to specify the version when running commands.
          - **If you don't have Python installed**:
            - Check the box **"Add Python to PATH"** at the bottom of the installer window.
        - Click **"Install Now"**.
    - **Verify Installation**:
      - Open a new Command Prompt.
      - Run:
        ```bash
        py -3.12 --version
        ```
      - You should see `Python 3.12.4`.
	  - **Operating System**: Windows 10 or later
	  - Py -3.12 is used by important video generation environment back-end processes.
      
- **Git**: Installed and configured
    - **Install Git**:
      - Download Git from [Git for Windows](https://git-scm.com/download/win).
      - Run the installer with default settings.
    - **Verify Installation**:
      - Open a new Command Prompt.
      - Run:
        ```bash
        git --version
        ```
      - You should see the installed Git version.

- **NVIDIA GPU**: CUDA-enabled NVIDIA GPU for optimal performance
  - Ensure you have an NVIDIA GPU with the latest drivers.
  
- **CUDA Toolkit**: Version 11.8 compatible with your GPU and installed
  - **Install CUDA Toolkit**:
      - Download the CUDA Toolkit from [CUDA Toolkit Download](https://developer.nvidia.com/cuda-11-8-0-download-archive).
      - Run the installer and follow the on-screen instructions.
  - **Verify Installation**:
      - Open a new Command Prompt and run:
        ```bash
        nvcc --version
        ```
      - You should see the CUDA compilation tools version information.

- **FFmpeg**: Installed and added to system `PATH`
    - Step 1: Click [here](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z) to download the zip file of the latest version.
    - Step 2: Unzip this file by using any file archiver such as Winrar or 7z.
    - Step 3: Rename the extracted folder to ffmpeg and move it into the root of C: drive.
    - `setx /m PATH "C:\ffmpeg\bin;%PATH%"`
    - **Verify Installation**:
      - Open a new Command Prompt and run:
        ```bash
        ffmpeg -version
        ```
      - You should see FFmpeg version information.
      
- **Ollama**: Download from [Ollama Setup](https://ollama.com/download/OllamaSetup.exe) and follow the on-screen instructions to install.

##[Setup Video Guide Part 2)[https://youtu.be/_8TXLNwA9ak?si=EO73EDqXafBLqA_O]


## You are READY to begin the automated setup process:
**Clone the Repo**

`git clone https://github.com/TemporalLabsLLC-SOL/TemporalPromptEngine.git`

**Manually Download the Repository**:
   - Visit the [TemporalPromptGenerator GitHub Repository](https://github.com/TemporalLabsLLC-SOL/TemporalPromptGenerator).
   - Click on the **"Code"** button and select **"Download ZIP"**.
   - Extract the downloaded ZIP file to your desired location (e.g., `C:\TemporalPromptEngine`).


**EASY-ONE-CLICK-INSTALLER**

   Open the Extracted Archive (or cloned repo) and click
     ```
RUN-FIRST-PRE-FLIGHT-CHECK.bat
     ```
   - Follow the on-screen prompts. The script will automatically set up the python environment(s), install necessary packages, and configure settings.

   The application will launch, guiding you through the initial setup. DURING THIS SETUP, either after you close the app OR denying to open the open during setup, you will have the option to add a work-around shortcut to your desktop. It currently does not have an icon. That will load the env and scripts reliably going forward.

OR

**Manually Run the Setup Script**:

   - Open Command Prompt and navigate to the extracted `TemporalPromptEngine` directory:
     ```bash
     cd C:\TemporalPromptEngine-main
     ```
   - Navigate to the `WINDOWS` folder:
     ```bash
     cd WINDOWS
     ```
   - Run the setup script:
     ```bash
     py -3.10 SETUP.py
     ```
---

<a name="4-quick-start-guide"></a>
##Quick Start Guide

IF YOU ADDED THE SHORTCUT TO DESKTOP DURING SETUP
   ```bash
     Click the Temporal Prompt Engine Shortcut on your Windows Desktop
   ```

IF YOU DID NOT ADD SHORTCUT TO DESKTOP DURING SETUP

**Activate the Virtual Environment**:
   ```bash
   cd C:\TemporalPromptEngine-main
   TemporalPromptEngineEnv\Scripts\activate
   ```

**Launch the Application**:
   ```bash
   python TemporalPromptEngine.py
   ```


1. **Enter API Key in the Application**:
   - Paste your HuggingFace API key when prompted during the setup of the Temporal Prompt Engine. 
   - You only will need to enter this one time within a setup engine environment. You can simply close this popup in subsequent uses.


3. **Enter Your Scene Concept**:

   Input your creative idea or scene description (up to 400 characters).

   **Examples**:
   - **Ancient Perspectives**:

 "View the world through the eyes of an ancient astronomer, mapping the stars with rudimentary tools under a vast, unpolluted night sky."
   - **Crypto-Animal Footage**:
     > "Documentary-style footage capturing the elusive 'cryptolion,' a mythical creature that embodies digital patterns and luminescent fur."

4. **Configure Video and Audio Prompt Options**:
   Tailor your video and audio prompts using dropdowns and input fields.

5. **Generate Video and Audio Prompts**:
   - Click **Generate Video Prompts**.

6. **Save and Export**:
   All media and prompts are saved in your designated output directory.

---

<a name="6-story-mode-unleash-epic-narratives"></a>
## Story Mode: Unleash Epic Narratives

**Story Mode** cohesively crafts a story outline and then turns each beat within that sequence into  a full-fledged and optimized video prompts allowing for seamless batch processing of longer content pools. This isn't just throwing key-words into prompts. There are several layers of back-end logic focused on cinematic practice, theory and history.
---


<a name="10-join-the-temporal-labs-journey"></a>
## Join the Temporal Labs Journey

Support the mission of pushing the boundaries of AI and technology. Join as an investor, developer, or client.

---

<a name="12-additional-services-offered"></a>
##  Additional Services Offered

- **Tutoring**, **Development**, **Design**, **Consulting**, and **Workshops** are available to meet your AI and technology needs.

---

<a name="14-contact"></a>
##  Contact

For questions, support, collaboration opportunities, or to discuss how we can work together:

- **Email**: [Sol@TemporalLab.com](mailto:Sol@TemporalLab.com)
- **Phone**: +1-385-222-9920

---

<a name="15-acknowledgments"></a>
##  Acknowledgments

Thanks to the developers and communities behind **Git**, **Python**, **FFmpeg**,**HunYuanVideo**,**MMAudio**, **Ollama**, **AudioLDM2**, **CogVideo**, **ComfyUI**, and **HuggingFace** for making this project possible.
