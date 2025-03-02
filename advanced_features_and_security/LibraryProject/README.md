# LibraryProject
# LibraryProject/README.md

## Security Measures Implemented

### HTTPS Configuration
- `SECURE_SSL_REDIRECT` set to `True` to redirect all HTTP requests to HTTPS.
- HSTS settings: `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD` configured to enforce HTTPS.

### Secure Cookies
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` set to `True` to ensure cookies are only transmitted over HTTPS.

### Secure Headers
- `X_FRAME_OPTIONS` set to `DENY` to prevent clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF` set to `True` to prevent MIME-sniffing.
- `SECURE_BROWSER_XSS_FILTER` set to `True` to enable XSS filtering.

### Deployment Configuration
- SSL/TLS certificates setup and web server configuration to support HTTPS.
