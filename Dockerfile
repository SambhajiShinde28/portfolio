# ---------- builder stage ----------
FROM python:3.11-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install build deps required for many Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /build

# Copy requirements and build wheels (speeds up final install)
COPY requirements.txt .

# Build wheels into /wheels so final stage can install without build tools
RUN pip install --upgrade pip wheel setuptools && \
    pip wheel --wheel-dir /wheels -r requirements.txt

# Copy application code
COPY . /build/app

# ---------- final stage ----------
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_HOME=/home/app/.streamlit

# Create non-root user
RUN groupadd -r app && useradd --no-log-init -r -g app app

# Install only runtime packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy wheels from builder and install (no build tools needed)
COPY --from=builder /wheels /wheels
COPY --from=builder /build/app /app

RUN pip install --upgrade pip && \
    pip install --no-index --find-links=/wheels -r requirements.txt && \
    rm -rf /wheels

# make Streamlit not try to open browser, run as non-root
ENV PATH="/home/app/.local/bin:${PATH}"

# Ensure .streamlit directory exists and is owned by app user (optional)
RUN mkdir -p /home/app/.streamlit && chown -R app:app /home/app

# Expose Streamlit default port
EXPOSE 8501

# Use non-root user
USER app

# Recommended streamlit flags for containerized deployment
ENTRYPOINT ["streamlit", "run", "portfolio.py", "--server.port=8501", "--server.headless=true", "--server.enableCORS=false"]
