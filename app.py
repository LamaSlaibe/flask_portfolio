from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    projects= [ {
        'title': 'لعبة تخمين الأرقام',
        'description': 'لعبة سطر الأوامر :خمن رقما سريا بين 1و 100 مع ردود فعل عالية/منخفضة وعدادات ،وجولة اضافية اختيارية ',
        'tech_stack': 'بايثون',
        'github_url': 'https://github.com/LamaSlaibe/Number-Guessing-Game',
        'image': 'images/number-guessing-game.jpg'},

         {
        'title':'مولد كلمات المرور',
        'description':'أداة بايثون تعمل عبر سطر الأوامر ، تقوم بإنشاء كلمات مرور عشوائية من الأحرف والأرقام والرموز بحد أدنى للطول يبلغ 4',
        'tech_stack':'بايثون',
        'github_url':'https://github.com/LamaSlaibe/Password-Generator-main',
        'image':'images/Password-Generator.jpg'},

        {
        'title':'تحميل فيديوهات يوتيوب',
        'description':'تطبيق سطح مكتب لتنزيل فيديوهات اليوتيوب والصوتيات بواجهة تفاعلية سهلة',
        'tech_stack':'بايثون',
        'github_url':'https://github.com/LamaSlaibe/ytdlp-gui-master',
        'image':'images/youtube.jpg'},
        {
        'title':'إعادة تسمية وتنظيم الملفات',
        'description':'تطبيق سطح مكتب لإعادة تسمية وتنظيم الملفات الضخمة بسرعة وسهولة بناء على قواعد مخصصة ',
        'tech_stack':'بايثون',
        'github_url':'https://github.com/LamaSlaibe/dirx-file-organizer',
        'image':'images/file.jpg'},
        {
        'title':'متتبع أسعار الأسهم العالمية',
        'description':'أداة لتحليل بيانات المبيعات الخام وتحويلها لرسومات بيانية ',
        'tech_stack':'بايثون',
        'github_url':'https://github.com/LamaSlaibe/sales-data-analysis-main',
        'image':'images/sales.jpg'},
         {
        'title':'الة حاسبة بواجهة رسومية',
        'description':'اّلة حاسبة ذكية بواجهة رسومية سهلة الاسنخدام لإجراء العمليات الحسابية بدقة وسرعة  ',
        'tech_stack':'بايثون',
        'github_url':'https://github.com/LamaSlaibe/TkinterCalculator-main',
        'image':'images/calculator.jpg'}


    
    ]
    return render_template('index.html', projects= projects)
if __name__=='__main__':
    app.run(debug=True)