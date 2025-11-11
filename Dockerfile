# ✅ Use a lightweight Python image
FROM python:3.10-slim

# ✅ Set working directory inside container
WORKDIR /app

# ✅ Copy only requirements first (for caching layers)
COPY requirements.txt .

# ✅ Install dependencies efficiently
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy rest of the project files
COPY . .

# ✅ Expose Flask’s default port
EXPOSE 5000

# ✅ Define environment variable to disable Flask buffering
ENV PYTHONUNBUFFERED=1

# ✅ Use Gunicorn for production server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
