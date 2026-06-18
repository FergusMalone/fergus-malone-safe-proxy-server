"""
Fergus Malone Safe Proxy Server
A simple forward proxy server to access blocked websites
"""

from flask import Flask, render_template, request, Response
import requests
from urllib.parse import urlparse, urljoin
from config import HOST, PORT, TIMEOUT, USER_AGENT, BLOCKED_DOMAINS, DEBUG, MAX_CONTENT_LENGTH
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Store for tracking visited URLs
visited_urls = []


def is_valid_url(url):
    """Validate if a URL is properly formatted"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False


def is_blocked_domain(url):
    """Check if a domain is in the blocked list"""
    try:
        domain = urlparse(url).netloc
        for blocked in BLOCKED_DOMAINS:
            if blocked.lower() in domain.lower():
                return True
    except:
        pass
    return False


def add_scheme_to_url(url):
    """Add http:// if no scheme is provided"""
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url


@app.route('/')
def index():
    """Home page with URL input form"""
    return render_template('index.html', visited_urls=visited_urls[-10:])  # Show last 10 URLs


@app.route('/proxy', methods=['POST'])
def proxy():
    """Proxy the requested URL"""
    try:
        # Get the URL from the form
        target_url = request.form.get('url', '').strip()
        
        if not target_url:
            return render_template('index.html', error='Please enter a URL', visited_urls=visited_urls[-10:])
        
        # Add scheme if missing
        target_url = add_scheme_to_url(target_url)
        
        # Validate URL
        if not is_valid_url(target_url):
            return render_template('index.html', error='Invalid URL format', visited_urls=visited_urls[-10:])
        
        # Check if domain is blocked
        if is_blocked_domain(target_url):
            return render_template('index.html', error='This domain is blocked', visited_urls=visited_urls[-10:])
        
        # Add to visited URLs
        if target_url not in visited_urls:
            visited_urls.append(target_url)
        
        logger.info(f"Proxying request to: {target_url}")

