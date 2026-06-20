# Install Instructions

1. Create Virtual Environment
    ```bash
    python -m venv .venv
    ```

2. Activate Virtual Environment
    ```bash
    source .venv/Scripts/activate
    ```

3. Install requirements
    ```bash
    pip install -r requirements.txt
    ```

4. Build from setup.py
    ```bash
    python setup.py bdist_wheel sdist
    ```

5. Install Task_CLI package
    ```bash
    pip install -e .
    ```

## Usage

Run in bash terminal using:
```bash
YT_Clipper download --url <video-url>
```

```bash
YT_Clipper clip --url <video-url> --start <starting-timestamp> 
          --end <end-timestamp> --title <output-video-title> --output <output-path>
```

```bash
YT_Clipper delete_file --path <video-path>
```
