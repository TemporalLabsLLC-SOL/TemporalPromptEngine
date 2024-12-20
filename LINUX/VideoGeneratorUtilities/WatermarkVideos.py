import os
import subprocess
import re
from tkinter import Tk, filedialog, messagebox
import requests
import shutil  # For copying files
import tempfile  # For creating temporary files

# Function to download "Poppins Bold" font if not present
def ensure_poppins_bold_font(font_dir):
    font_name = "Poppins-Bold.ttf"
    font_path = os.path.join(font_dir, font_name)
    if not os.path.exists(font_path):
        print(f"Downloading {font_name}...")
        # URL to the Poppins Bold font on Google Fonts
        url = "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Bold.ttf"
        response = requests.get(url)
        if response.status_code == 200:
            with open(font_path, 'wb') as f:
                f.write(response.content)
            print(f"{font_name} downloaded and saved to {font_path}")
        else:
            print(f"Failed to download {font_name}. Please check your internet connection.")
            return None
    else:
        print(f"{font_name} already exists at {font_path}")
    return font_path

# Define the directory to store fonts (e.g., a "fonts" directory next to your script)
script_dir = os.path.dirname(os.path.abspath(__file__))
font_dir = os.path.join(script_dir, "fonts")
if not os.path.exists(font_dir):
    os.makedirs(font_dir)

# Ensure "Poppins Bold" font is available
font_path = ensure_poppins_bold_font(font_dir)
if not font_path:
    print("Font could not be downloaded. Exiting.")
    exit(1)

# Step 1: Add settings text to video using FFmpeg with textfile
def add_text_overlay(video_path, output_path, settings_text):
    font_path_escaped = font_path.replace('\\', '/').replace(':', '\\:')

    # Create a temporary file for the settings text
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as settings_file:
        settings_file.write(settings_text)
        settings_file_path = settings_file.name.replace('\\', '/').replace(':', '\\:')

    # Include fontfile in the drawtext filter using textfile
    drawtext_settings = f"drawtext=textfile='{settings_file_path}':fontfile='{font_path_escaped}':fontcolor=white:fontsize=24:x=(w-tw)/2:y=h-th-10"

    # Build the ffmpeg command to add settings text overlay
    ffmpeg_command = [
        "ffmpeg", "-y", "-i", video_path, "-vf",
        f"{drawtext_settings}",
        "-codec:a", "copy", output_path
    ]

    # Print the FFmpeg command for debugging
    print(f"Running FFmpeg command for text overlay: {' '.join(ffmpeg_command)}")

    # Run the ffmpeg command and capture stdout and stderr
    process = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Clean up the temporary text file
    os.remove(settings_file.name)

    # Print FFmpeg output for debugging
    print("FFmpeg Output (Text Overlay):\n", process.stdout)
    print("FFmpeg Error Output (Text Overlay):\n", process.stderr)

    if process.returncode != 0:
        print(f"FFmpeg failed with return code {process.returncode} on text overlay.")
        return False
    return True

# Step 2: Add logo to video using FFmpeg (Unchanged)
def add_logo_overlay(video_path, output_path, logo_path):
    # Position the logo in the top-right corner and scale it down
    overlay_position = "W-w-10:10"
    scale_logo = "scale=iw*0.15:ih*0.15"  # Scale the logo down to 15% of its original size

    # Build the ffmpeg command to add logo overlay
    ffmpeg_command = [
        "ffmpeg", "-y", "-i", video_path, "-i", logo_path, "-filter_complex",
        f"[1:v] {scale_logo} [logo]; [0:v][logo] overlay={overlay_position}",
        "-codec:a", "copy", output_path
    ]

    # Print the FFmpeg command for debugging
    print(f"Running FFmpeg command for logo overlay: {' '.join(ffmpeg_command)}")

    # Run the ffmpeg command and capture stdout and stderr
    process = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print FFmpeg output for debugging
    print("FFmpeg Output (Logo Overlay):\n", process.stdout)
    print("FFmpeg Error Output (Logo Overlay):\n", process.stderr)

    if process.returncode != 0:
        print(f"FFmpeg failed with return code {process.returncode} on logo overlay.")
    else:
        print(f"Watermarked video saved to {output_path}")
        
# Function to extract settings from the filename
def extract_settings_from_filename(filename):
    # Regex pattern to extract 'cfg' and 'steps' (case-insensitive, and allows spaces and other words)
    pattern = r'video_\d+_(\d+[Bb])_(\d+\.\d+gs)_(\d+steps)_.*\.mp4'
    match = re.match(pattern, filename)
    
    if match:
        cfg = match.group(2)
        steps = match.group(3)
        settings_text = f"CFG {cfg} - Steps {steps}"
        return settings_text
    else:
        return "Settings not found"

# Function to watermark all videos in the selected directory
def watermark_videos_in_directory(base_dir, logo_path):
    # Create 'Watermarked' directory inside the base directory
    watermarked_dir = os.path.join(base_dir, "Watermarked")
    if not os.path.exists(watermarked_dir):
        os.makedirs(watermarked_dir)

    # Loop through all files in the base directory
    for filename in os.listdir(base_dir):
        if filename.endswith('.mp4'):  # Only process video files
            video_path = os.path.join(base_dir, filename)
            temp_output_path = os.path.join(base_dir, "temp_" + filename)
            final_output_path = os.path.join(watermarked_dir, filename)

            # Extract settings from the filename
            settings_text = extract_settings_from_filename(filename)

            # Step 1: Add settings text overlay
            if add_text_overlay(video_path, temp_output_path, settings_text):
                # Step 2: Add logo overlay to the video with text
                add_logo_overlay(temp_output_path, final_output_path, logo_path)

            # Cleanup temp file after processing
            if os.path.exists(temp_output_path):
                os.remove(temp_output_path)

            # Copy the .srt file to the Watermarked directory
            base_filename = os.path.splitext(filename)[0]
            srt_filename = base_filename + '.srt'
            srt_path = os.path.join(base_dir, srt_filename)
            if os.path.exists(srt_path):
                dest_srt_path = os.path.join(watermarked_dir, srt_filename)
                shutil.copyfile(srt_path, dest_srt_path)

    print(f"Watermarking complete. Watermarked videos saved to {watermarked_dir}")

# Function to open a folder selection dialog
def select_folder():
    root = Tk()
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()
    return folder_selected

# Function to open a file selection dialog
def select_logo_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_selected = filedialog.askopenfilename(
        title="Select Logo Image",
        filetypes=[("PNG Images", "*.png"), ("All Files", "*.*")]
    )
    return file_selected

# Function to download the Temporal Labs LLC logo
def download_logo(url, save_path):
    try:
        print(f"Downloading logo from {url}...")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                shutil.copyfileobj(response.raw, f)
            print(f"Logo downloaded and saved to {save_path}")
            return True
        else:
            print(f"Failed to download logo. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred while downloading the logo: {e}")
        return False

# Function to handle logo setup
def setup_logo():
    logo_name = "logo.png"
    logo_path = os.path.join(script_dir, logo_name)
    
    if not os.path.exists(logo_path):
        print(f"{logo_name} does not exist.")
        user_choice = messagebox.askyesno(
            "Logo Not Found",
            "logo.png was not found in the script directory.\nWould you like to select a PNG file for the logo?"
        )
        if user_choice:
            selected_file = select_logo_file()
            if selected_file:
                try:
                    shutil.copy(selected_file, logo_path)
                    print(f"Selected logo copied to {logo_path}")
                except Exception as e:
                    print(f"Failed to copy selected logo: {e}")
                    return None
            else:
                print("No file selected. Downloading default logo.")
                # URL to the Temporal Labs LLC logo
                logo_url = "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=450,fit=crop,q=95/A1aoblXx2KSKGq4r/tlclogorawnameonly-Awvk565gvMfLKVr4.png"
                if not download_logo(logo_url, logo_path):
                    print("Failed to download the default logo. Exiting.")
                    return None
        else:
            print("User chose not to select a logo. Downloading default logo.")
            # URL to the Temporal Labs LLC logo
            logo_url = "https://assets.zyrosite.com/cdn-cgi/image/format=auto,w=450,fit=crop,q=95/A1aoblXx2KSKGq4r/tlclogorawnameonly-Awvk565gvMfLKVr4.png"
            if not download_logo(logo_url, logo_path):
                print("Failed to download the default logo. Exiting.")
                return None
    else:
        print(f"{logo_name} already exists at {logo_path}")
    
    return logo_path

# Function to confirm usage of Temporal Prompt Engine Prompt Lists
def confirm_usage():
    while True:
        user_input = input("Are you using Temporal Prompt Engine Prompt Lists? (y/n): ").strip().lower()
        if user_input == 'y':
            print("Confirmation received. Proceeding with watermarking process.")
            return True
        elif user_input == 'n':
            print("You did not confirm the use of Temporal Prompt Engine Prompt Lists. Exiting.")
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# Main script
if __name__ == "__main__":
    # Confirm usage
    if not confirm_usage():
        exit(1)
    
    # Setup logo
    logo_path = setup_logo()
    
    if not logo_path:
        print("Logo setup failed. Exiting.")
        exit(1)
    
    # Prompt the user to select the folder containing the videos
    print("Please select the folder containing the videos to watermark.")
    base_dir = select_folder()

    if base_dir:
        # Call the function to watermark videos in the selected folder
        watermark_videos_in_directory(base_dir, logo_path)
    else:
        print("No folder selected. Exiting.")
