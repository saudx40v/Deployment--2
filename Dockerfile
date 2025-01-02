# استخدم صورة Python الرسمية كقاعدة
FROM python:3.9-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ جميع ملفات التطبيق من المستودع إلى مجلد العمل في الحاوية
COPY . /app

# تثبيت الحزم من ملف requirements.txt (إذا كنت تستخدمه)
RUN pip install --no-cache-dir -r requirements.txt

# تحديد المنفذ الذي يستمع عليه التطبيق
EXPOSE 5000

# تشغيل التطبيق (يجب أن يكون لديك ملف بايثون مثل app.py)
CMD ["python", "easy.py"]
