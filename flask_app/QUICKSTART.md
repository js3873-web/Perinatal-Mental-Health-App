# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Open Terminal
Navigate to this directory:
```bash
cd /Users/josesalinas/Desktop/Foundations_Project/flask_app
```

### Step 2: Run the Start Script
```bash
./run.sh
```

This will automatically:
- Create a virtual environment
- Install all dependencies
- Start the Flask server

### Step 3: Open Your Browser
Navigate to:
```
http://localhost:5000
```

That's it! 🎉

---

## 📖 Manual Setup (Alternative)

If the script doesn't work, follow these steps:

1. **Create virtual environment**:
   ```bash
   python3 -m venv venv
   ```

2. **Activate virtual environment**:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```

5. **Open browser**:
   ```
   http://localhost:5000
   ```

---

## 🛑 Stop the Server

Press `Ctrl + C` in the terminal

---

## 📁 Project Structure

```
flask_app/
├── app.py              # Main Flask application
├── templates/          # HTML pages
├── static/            # CSS, JavaScript, images
├── requirements.txt   # Python dependencies
├── run.sh            # Quick start script
└── README.md         # Full documentation
```

---

## 🎨 Features

- ✅ Interactive 10-question screening
- ✅ Real-time progress tracking
- ✅ Beautiful, responsive design
- ✅ Risk classification algorithm
- ✅ Personalized results
- ✅ Analytics dashboard
- ✅ Crisis resources

---

## 🆘 Troubleshooting

### Port Already in Use
If you see "Address already in use", kill the existing process:
```bash
lsof -ti:5000 | xargs kill -9
```

### Python Not Found
Make sure Python 3.8+ is installed:
```bash
python3 --version
```

### Permission Denied
Make the script executable:
```bash
chmod +x run.sh
```

---

## 📚 Need More Help?

See the full [README.md](README.md) for detailed documentation.

---

**Enjoy using the Mental Health Screening App! 💙**
