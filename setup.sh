#!/bin/bash

# setup.sh - إنشاء وتثبيت وتحميل package.json تلقائياً

echo "🚀 بدء الإنشاء التلقائي..."
echo ""

# 1. إنشاء package.json
echo "📄 جاري إنشاء package.json..."

cat > package.json << 'EOF'
{
  "name": "roum-token",
  "version": "1.0.0",
  "description": "ROUM Token - Cryptocurrency token built on Binance Smart Chain",
  "main": "index.js",
  "scripts": {
    "dev": "webpack --mode development --watch",
    "build": "webpack --mode production",
    "test": "jest",
    "lint": "eslint .",
    "format": "prettier --write ."
  },
  "dependencies": {
    "web3": "^1.10.0",
    "axios": "^1.6.0",
    "express": "^4.18.0",
    "cors": "^2.8.5"
  },
  "devDependencies": {
    "@babel/core": "^7.23.0",
    "@babel/preset-env": "^7.23.0",
    "webpack": "^5.89.0",
    "webpack-cli": "^5.1.0",
    "eslint": "^8.50.0",
    "prettier": "^3.0.0",
    "jest": "^29.7.0",
    "@testing-library/react": "^14.0.0",
    "nodemon": "^3.0.0"
  },
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  }
}
EOF

echo "✅ تم إنشاء package.json"
echo ""

# 2. تثبيت npm
echo "📦 جاري تثبيت الـ dependencies (قد يستغرق 2-3 دقائق)..."
npm install

if [ $? -eq 0 ]; then
  echo "✅ تم التثبيت بنجاح"
else
  echo "❌ خطأ في npm install"
  exit 1
fi

echo ""

# 3. رفع GitHub
echo "📤 جاري رفع الملفات إلى GitHub..."

git add package.json package-lock.json

if [ $? -eq 0 ]; then
  echo "✅ تم إضافة الملفات"
else
  echo "❌ خطأ في git add"
  exit 1
fi

git commit -m "chore: add project dependencies and auto setup"

if [ $? -eq 0 ]; then
  echo "✅ تم إنشاء commit"
else
  echo "❌ خطأ في git commit"
  exit 1
fi

git push origin main

if [ $? -eq 0 ]; then
  echo "✅ تم الرفع إلى GitHub"
else
  echo "❌ خطأ في git push - تأكد من الاتصال بالإنترنت والصلاحيات"
  exit 1
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo "🎉 تم كل شيء بنجاح!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "✅ تم إنشاء package.json"
echo "✅ تم تثبيت npm dependencies"
echo "✅ تم رفع الملفات إلى GitHub"
echo ""
echo "📊 الملفات المنشأة:"
echo "  • package.json"
echo "  • package-lock.json"
echo "  • node_modules/ (مجلد)"
echo ""
echo "════════════════════════════════════════════════════════════"
