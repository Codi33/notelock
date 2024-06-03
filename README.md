# Notelock
NoteLock is a lightweight, secure FastAPI service designed for creating and reading notes safely and anonymously. 📝🔒

## Features
- Encryption
- Automatically deleted after being read

## Getting started
- Create config file
```bash
cp .env.example .env
```

## Running Locally
- Clone the repository
```bash
git clone https://github.com/Codi33/notelock
```
- Navigate to the project directory
```bash
cd notelock
```
- Install dependencies
```bash
pip install -r requirements.txt
```
- Start FastAPI Server
```bash
fastapi run app/main.py --port 8000
```

## Running with Docker
- Clone the repository
```bash
git clone https://github.com/Codi33/notelock
```
- Navigate to the project directory
```bash
cd notelock
```
- Build docker image
```bash
docker build -t notelock .
```
- Run docker container
```bash
docker run -p 8000:8000 -d notelock
```

## Contributing

Contributions to NoteLock are welcome! If you encounter any issues or have suggestions for improvements,
please feel free to open an issue or submit a pull request.