# Files Creator by Sabbah

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A simple command-line Python tool to create multiple files based on user input. You can specify file names, extensions, and target directory paths. This tool will also prompt you if a file with the same name already exists, giving you the option to overwrite it.

## Features

- **Multiple File Creation**: Easily create multiple files by entering their names separated by commas.
- **Custom File Extensions**: Choose the file extension (e.g., `.txt`, `.php`, `.js`) for your files.
- **File Existence Check**: Automatically checks if a file already exists and prompts for overwriting if needed.
- **Directory Targeting**: Specify the target directory where files will be created.
- **Colorized Output**: Uses ANSI escape codes to display beautiful colorized messages in the terminal.

## Preview

```
=================================
==== Files creator by Sabbah ====
=================================
Files names separated with comma: file1, file2, file3
Files extension (e.g., txt, php, js): txt
Paste the target path: /path/to/directory

Created file > /path/to/directory/file1.txt
Created file > /path/to/directory/file2.txt
There is a file with the name 'file3.txt'. Do you want to replace it? (yes/no): no
Skipped file: /path/to/directory/file3.txt

Task Completed!
```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/files-creator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd files-creator
   ```

3. Ensure you have Python 3.x installed. You can check your Python version with:

   ```bash
   python --version
   ```

## Usage

1. Run the script:

   ```bash
   python app.py
   ```

2. Follow the on-screen prompts:
   - Enter the file names separated by commas (e.g., `file1, file2, file3`).
   - Enter the file extension (e.g., `txt`, `php`, `js`).
   - Provide the target directory path (e.g., `/path/to/directory`).
   - If a file already exists, you'll be asked whether to overwrite it.

### Example:

```bash
Files extension (e.g., txt, php, js): txt
Paste the target path: /path/to/directory
```

You can now see the created files in the specified directory!

## Contributing

Contributions are always welcome! If you'd like to contribute to the project, feel free to open an issue or submit a pull request. You can also suggest new features, report bugs, or improve the documentation.

To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Feel free to reach out if you have any questions or feedback:
- **Author**: Sabbah Eltag 🇸🇩
