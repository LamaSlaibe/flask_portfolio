from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')
def home():
    projects= [ {
        'title': 'لعبة تخمين الأرقام',
        'description': 'لعبة سطر الأوامر :خمن رقما سريا بين 1و 100 مع ردود فعل عالية/منخفضة وعدادات ،وجولة اضافية اختيارية ',
        'tech_stack': ['بايثون'],
        'github_url': 'https://github.com/LamaSlaibe/Number-Guessing-Game',
        'image': 'images/number-guessing-game.jpg'},

         {
        'title':'مولد كلمات المرور',
        'description':'أداة بايثون تعمل عبر سطر الأوامر ، تقوم بإنشاء كلمات مرور عشوائية من الأحرف والأرقام والرموز بحد أدنى للطول يبلغ 4',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/Password-Generator-main',
        'image':'images/Password-Generator.jpg'},

        {
        'title':'تحميل فيديوهات يوتيوب',
        'description':'تطبيق سطح مكتب لتنزيل فيديوهات اليوتيوب والصوتيات بواجهة تفاعلية سهلة',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/ytdlp-gui-master',
        'image':'images/youtube.jpg'},
        {
        'title':'إعادة تسمية وتنظيم الملفات',
        'description':'تطبيق سطح مكتب لإعادة تسمية وتنظيم الملفات الضخمة بسرعة وسهولة بناء على قواعد مخصصة ',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/dirx-file-organizer',
        'image':'images/file.jpg'},
        {
        'title':'تحليل بيانات المبيعات',
        'description':'أداة لتحليل بيانات المبيعات الخام وتحويلها لرسومات بيانية ',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/sales-data-analysis-main',
        'image':'images/sale.jpg'},
         {
        'title':'الة حاسبة بواجهة رسومية',
        'description':'اّلة حاسبة ذكية بواجهة رسومية سهلة الاسنخدام لإجراء العمليات الحسابية بدقة وسرعة  ',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/TkinterCalculator-main',
        'image':'images/calculator.jpg'},
         {
        'title':'استخراج الصوت من الفيديو',
        'description':' أداة برمجية لفصل مسار الصوت عن ملف الفيديو وحفظه كملف صوتي مستقل',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/Audio-Extractor-master',
        'image':'images/voice.jpg'},
        {
        'title':'تصغير الصور وإضافة علامة مائية',
        'description':'أداة برمجية لتغيير أبعاد وحجم الصور رقمياّّ وإدمان علامة مائية عليها لحفظ حقوق الملكية',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/BulkImageEditor-main',
        'image':'images/images.jpg'},
        {
        'title':'اكتشاف الوجوه في الصور والفيديو',
        'description':'أداة تعتمد على الذكاء الاصطناعي لتحديد وتتبع الوجوه البشرية بدقة داخل الصور ومقاطع الفيديو في الوقت الفعلي',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/Face-Detection-using-OpenCV-in-Python-main',
        'image':'images/face.jpg'},
        {
        'title':'التحكم بحجم الصوت بإيماءات اليد',
        'description':'أداة تفاعلية للتحكم في مستوى صوت الجهاز بإيماءات اليد عبر الكاميرا دون الحاجة للمس لوحة المفاتيح',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/Gesture-Volume-Control-using-MediaPipe-and-OpenCV-master',
        'image':'images/volume.jpg'},
        {
        'title':'أداة التلخيص الذكي للمقالات',
        'description':'أداة ذكية لتحليل المقالات الطويلة وتلخيص أهم نقاطها وأفكارها الرئيسية في أسطر معدودة بدقة وسرعة',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/News-Article-Summarizer-main',
        'image':'images/articles.jpg'},
         {
        'title':'تتبع لون معين في الكاميرا',
        'description':'أداة تفاعلية لرصد وتتبع حركة أداة أو جسم بلون محدد عبر كاميرا الويب في الوقت الفعلي',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/Object-detection-based-on-colour-main',
        'image':'images/colour.jpg'},
         {
        'title':'مترجم نصوص فوري',
        'description':'أداة برمجية لترجمة النصوص بين اللغات المختلفة فورياّّ وبدقة عالية',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/-Professional-Language-Translator-Tkinter-GUI--main',
         'image':'images/translation.jpg'},   
        {
        'title':'تطبيق طقس تفاعلي',
        'description':'تطبيق ذكي لعرض حالة الطقس وتحديثات درجات الحرارة وتوقعاتها بشكل تفاعلي ولحظي ',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/Python-Weather-Info-App-main',
        'image':'images/weather.jpg'},
        {
        'title':'متتبع أسعار الأسهم لعالمية',
        'description':'أداة لمراقبة وتتبع حركة أسعار الأسهم والأسواق المالية العالمية بشكل تفاعلي لحظة بلحظة',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/Stock-Tracker-Using-Python-master',
        'image':'images/sales.jpg'},
        {
        'title':'محول النص الى كلام',
        'description':'أداة تفاعلية لتحويل النصوص المكتوبة الى نص مسموع بنطق طبيعي وواضح',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/texttospeech-master',
        'image':'images/texttospeech.jpg'},
        {
        'title':'تحليل بيانات التايتانيك',
        'description':'أداة تفاعلية لتحليل بيانات ركاب سفينة تايتنك واستكشاف العوامل المؤثرة في فرص نجاة المسافرين',
        'tech_stack':['Jupyter Notebook','بايثون'] ,
        'github_url':'https://github.com/LamaSlaibe/titanic-survival-analysis-main',
        'image':'images/titanic.jpg'},
               {
        'title':'استخراج البيانات من الويب',
        'description':'أداة برمجية لاستخراج وتجميع البيانات من مواقع الويب بشكل تلقائي وتحويلها الى معلومات منظمة وقابلة للتحليل',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/web-scraping-data-parsing-beautiful-soup-main-1-',
        'image':'images/webscraping.jpg'},
                       {
        'title':'عداد الكلمات الأكثر تكراراّّ',
        'description':'أداة برمجية لتحليل النصوص وحساب أكثر الكلمات تكراراّّ',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/word_frequency',
        'image':'images/wordfrequency.jpg'},
                               {
        'title':'أداة تحويل الصوت الى نص',
        'description':'أداة ذكية تقوم بتحويل التسجيلات الصوتية والمحادثات المباشرة الى نصوص مكتوبة بدقة وسرعة عالية',
        'tech_stack':['بايثون'],
        'github_url':'https://github.com/LamaSlaibe/Speech-Recognition-main',
        'image':'images/speechrecognition.jpg'},
    
    ]
    return render_template('index.html', projects= projects)
if __name__=='__main__':
    app.run(debug=True)