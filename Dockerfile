FROM python:3.9-slim

# Set working directory
WORKDIR /docs

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose MkDocs port
EXPOSE 8000

# Default command
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
