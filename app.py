import os
from searx.webapp import app

# Set the custom settings file via environment variable
os.environ["SEARXNG_SETTINGS_PATH"] = "searx/settings.yml.custom"

if __name__ == "__main__":
    # Use Render's PORT env var, default to 10000
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
