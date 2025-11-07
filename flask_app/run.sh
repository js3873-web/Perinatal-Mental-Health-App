#!/bin/bash

# Quick start script for Flask Mental Health Screening App

echo "🏥 Perinatal Mental Health Screening - Flask App"
echo "================================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install/update requirements
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Starting Flask application..."
echo "📱 Open your browser to: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================================"
echo ""

# Run the Flask app
python app.py
