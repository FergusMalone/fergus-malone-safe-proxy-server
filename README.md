# Fergus Malone Safe Proxy Server

A simple forward proxy server built in Python that allows you to safely access websites that may be blocked by your school or organization's network filters.

## How It Works

This proxy server acts as an intermediary between your device and the websites you want to visit. When you enter a URL into the proxy interface, the server fetches the website on your behalf and returns it to you. This can help bypass network restrictions because the traffic appears to come from the proxy server rather than your device.

## Features

- 🌐 **Web Interface**: Simple interface to enter URLs and browse through the proxy
- 🔒 **Safe Browsing**: Access blocked websites safely
- ⚙️ **Configurable**: Easy to customize port and settings
- 📝 **Lightweight**: Minimal dependencies, runs on most systems
- 🚀 **Easy to Deploy**: Works on local machines or cloud servers

## Requirements

- Python 3.7 or higher
- `pip` (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/FergusMalone/fergus-malone-safe-proxy-server.git
cd fergus-malone-safe-proxy-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the proxy server:
```bash
python app.py
```

2. By default, the server runs on `http://localhost:8080`

3. Open
# fergus-malone-safe-proxy-server
