# Jupyter Notebook Auto Launcher (With Chrome)

This project automatically launches Jupyter Notebook and opens the tokenized URL in **Google Chrome**. The terminal remains hidden using a `.vbs` script for a cleaner experience.

---

## Project Structure

```
jupyter_notebook_shortcut/
├── open_jupyter_browser.py   # Finds the tokenized URL and opens it in Chrome
├── start_notebook.bat        # Starts the Jupyter server and runs the Python script
├── start_hidden.vbs          # Runs the BAT file silently
├── icon.ico                  # (Optional) Custom icon for the VBS file
```

---

## How to Use

1. Extract the folder anywhere. For example:
   ```
   D:\Projects\jupyter_notebook_shortcut\
   ```

2. Double-click `start_hidden.vbs`

It will:
- Activate Anaconda environment
- Start the Jupyter server
- Wait for tokenized URL
- Open the URL in Google Chrome automatically

---

## Requirements

- Windows OS
- Anaconda installed (default path: `C:\Program Files\anaconda3`)
- Google Chrome installed
- Python (should match your Anaconda installation)

**Note:** You must edit file paths in `.bat`, `.py`, and `.vbs` to match your system.

---

## How to Stop

Since there is no terminal, to stop the server:

1. Press `CTRL + SHIFT + ESC` to open Task Manager
2. End the process for `python.exe` or `jupyter-notebook.exe`

You can also create a shutdown script:

```bat
@echo off
taskkill /F /IM python.exe >nul 2>&1
taskkill /F /IM jupyter-notebook.exe >nul 2>&1
exit
```

---

## Change the Icon

To change the VBS file icon:

1. Right-click on `start_hidden.vbs` → Create Shortcut
2. Right-click the shortcut → Properties → Change Icon
3. Choose the `icon.ico` file

---

## How It Works

- `.bat` file starts the Jupyter server
- `open_jupyter_browser.py` fetches the URL from Jupyter runtime
- Waits for server readiness
- Opens Chrome with the notebook
- `.vbs` keeps it silent

---

## License

MIT License – free to use, modify, or fork.

---

## Notice for Antivirus

Some antivirus tools may trigger a warning due to automation via `.bat` and `.vbs`. This is a false positive. You can inspect the code for transparency.

---

## Author

Created by [Arda Karakaş](https://github.com/ArdaKarakas)