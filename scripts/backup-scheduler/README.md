# 📁 Backup Scheduler

A Python script that automatically backs up your important documents on a daily schedule using a simple folder copying mechanism. 🔄

## ✨ Features

- **🕒 Automated Daily Backups**: Schedules backups to run at a specified time every day
- **📅 Date-Based Organization**: Creates backup folders named with the current date (YYYY-MM-DD format)
- **🚫 Duplicate Prevention**: Checks if a backup already exists for the current date to avoid overwriting
- **⚠️ Error Handling**: Includes basic error handling for file operations
- **🔄 Continuous Operation**: Runs continuously in the background

## 📋 Requirements

- 🐍 Python 3.x
- 📦 `schedule` library

## 🚀 Installation

1. 📥 Clone this repository:
   ```bash
   git clone https://github.com/qusai-Kagal/DevVault.git
   cd DevVault/scripts/backup-scheduler
   ```

2. 📦 Install required dependencies:
   ```bash
   pip install schedule
   ```

## ⚙️ Configuration

Before running the script, you need to modify the source and destination paths in `backup.py`: 📝

```python
# ⏰ Update these paths according to your system
source_dir = r"C:\Path\To\Your\Source\Folder"
destination_dir = r"C:\Path\To\Your\Backup\Location"
```

### 📅 Scheduling

By default, the script is set to run at 11:09 AM daily. To change the backup time, modify this line: ⏱️

```python
schedule.every().day.at("11:09").do(lambda: copy_folder_to_directory(source_dir, destination_dir))
```

Examples of different scheduling options: 🕐
- `"00:03"` - Run at 12:03 AM 🌙
- `"14:30"` - Run at 2:30 PM ☀️
- `"23:45"` - Run at 11:45 PM 🌙

## 🎯 Usage

1. **⚙️ Configure the paths** in the script as described above
2. **▶️ Run the script**:
   ```bash
   python backup.py
   ```
3. **🏃‍♂️ Keep the script running** - it will continue to monitor and execute backups according to the schedule

The script will: ✅
- 📁 Create a new backup folder each day with the current date
- 📋 Copy all contents from the source directory to the destination
- ⏭️ Skip backup if a folder for the current date already exists
- 🖨️ Print status messages to the console

## 📂 Backup Structure

Your backups will be organized as follows: 🗂️
```
Backup Directory/
├── 2025-01-15/
│   └── [copied files and folders]
├── 2025-01-16/
│   └── [copied files and folders]
└── 2025-01-17/
    └── [copied files and folders]
```

## 🔧 Running as a Service

For production use, consider running this script as a system service: 🏭

### 🪟 Windows (using Task Scheduler)
1. 📅 Open Task Scheduler
2. ➕ Create a new task that runs `python backup.py` at system startup
3. 🔒 Set it to run with highest privileges

### 🐧 Linux (using systemd)
Create a service file and enable it to run at startup. 🚀

## ⚠️ Important Notes

- **💾 Disk Space**: Monitor your backup destination for available disk space
- **📍 Path Format**: Use raw strings (r"path") for Windows paths to handle backslashes correctly
- **🔐 Permissions**: Ensure the script has read access to source and write access to destination
- **🧪 Testing**: Test the script with non-critical data first

## 🔧 Troubleshooting

**Common Issues:** 🚨

1. **🚫 Permission Denied**: Run the script with appropriate permissions or check folder access rights
2. **📂 Path Not Found**: Verify that both source and destination paths exist
3. **📦 Import Error**: Install the schedule library using `pip install schedule`

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements. 💡

## 📄 License

This project is open source and available under the [MIT License](LICENSE). 📜

---

**👨‍💻 Author**: Qusai Kagalwala  
**📁 Repository**: [DevVault](https://github.com/qusai-Kagal/DevVault)
