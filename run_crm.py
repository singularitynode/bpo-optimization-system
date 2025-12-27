#!/usr/bin/env python3
"""
🏭 BPO CRM DASHBOARD - NO WARNING VERSION
"""

import uvicorn
import webbrowser
import threading
import time

def open_browser():
    """Open browser after server starts"""
    time.sleep(2)  # Wait for server to start
    webbrowser.open("http://localhost:8080")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🏭 BPO CRM DASHBOARD - LIQUID ENGINEERING EDITION")
    print("="*60)
    print("💰 PHP 3.4M Monthly Savings | 3-Day ROI")
    print("🎨 Beautiful Glassmorphism UI")
    print("⚡ Real-time Updates & Charts")
    print("🎫 Ticket Management | 👥 Agent Monitoring")
    print("🌐 Opening: http://localhost:8080")
    print("="*60)
    
    # Open browser automatically
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Run server with NO WARNING
    uvicorn.run("crm_server:app", host="0.0.0.0", port=8080, reload=True)