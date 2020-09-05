# Classic Cryptographic Encryption Backend
This repository will serve as backend service. Here, the service will be implementing various classic cruptographic encryption.

# TL;DR;
```
make
```

# Prerequisite
Make sure these modules is installed in your system:
* python 3

## Virtual Environment 
This is an optional, but recommended step.
Before you start this project, we recommend you create your virtual environment first.
There are several ways to create virtual environment, you can follow these steps or create your own virtual environment.
```bash
# Create virtual environment (once in installation)
python3 -m venv virtualenv

# Activate it (do this every time you start this project)
source virtualenv/bin/activate
```

## Install Dependency
```
pip3 install -r requirements.txt
```

# Start Server
```
python3 app.py
```
## Access
Development server will listen in http://localhost:5000

# Sample Request

## Text

### Playfair

```bash
curl --location --request POST 'localhost:5000/text' \
--form 'key=JALANGANESHASEPULUH' \
--form 'text=halowakgeng' \
--form 'algorithm=playfair' \
--form 'mode=encrypt'
```

### Affine
```bash
curl --location --request POST 'localhost:5000/text' \
--form 'text=paymoremoney' \
--form 'key={
        "m": 7,
        "b": 10
    }' \
--form 'algorithm=affine' \
--form 'mode=encrypt'
```

### Hill
```bash
curl --location --request POST 'localhost:5000/text' \
--form 'text=paymoremoney' \
--form 'key={
    "key": [
        17,
        17,
        5,
        21,
        18,
        21,
        2,
        2,
        19
    ]
}' \
--form 'algorithm=hill' \
--form 'mode=encrypt'
```
### Vigenere

```bash
curl --location --request POST 'localhost:5000/text' \
--form 'key=sony' \
--form 'text=thisplaintext' \
--form 'algorithm=vigenere' \
```

### Full Vigenere

```bash
curl --location --request POST 'localhost:5000/text' \
--form 'key=sony' \
--form 'text=thisplaintext' \
--form 'algorithm=vigenere_full' \
--form 'mode=encrypt'
```

## File Text
```bash
curl --location --request POST 'localhost:5000/file_text' \
--form 'text=@/home/rika/Downloads/coba.txt' \
--form 'key=JALANGANESHASEPULUH' \
--form 'algorithm=playfair' \
--form 'mode=encrypt'
```

## File binary
```bash
curl --location --request POST 'localhost:5000/file_binary' \
--form 'text=@/home/rika/Downloads/test.png' \
--form 'key=JALANGANESHASEPULUH' \
--form 'algorithm=playfair' \
--form 'mode=encrypt'
```

## Output to file
Add url parameter `output` with value `file`
```bash
curl --location --request POST 'localhost:5000/text?output=file' \
--form 'key=JALANGANESHASEPULUH' \
--form 'text=halo' \
--form 'algorithm=playfair' \
--form 'mode=encrypt'
```