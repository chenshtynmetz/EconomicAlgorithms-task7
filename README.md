# EconomicAlgorithms-task7

שאלה 5: <br />
בשאלה זו התבקשנו למצוא עבור בעיית חלוקת החדרים ושכר הדירה חלוקת חדרים אגליטרית מתוך כל החלוקות ללא קנאה. <br />
בשיעור למדנו שיש שני שלבים לפתרון:<br /> 1. מציאת השמה x של דיירים לחדרים. <br />
2. חישוב תמחור p כך שהזוג (x,p) הוא חלוקה ללא קנאה. <br />
בשיעור הוכחנו את השקילות של התנאים הבאים:<br /> 1. ההשמה x ממקסמת סכום ערכים. <br /> 
2. קיים תמחור p כך שהחלוקה (x,p) הוא ללא קנאה. <br />
ולכן את שלב 1 עשינו על ידי מציאת השמה x הממקסמת את סכום הערכים. <br />
ביצענו זאת על ידי בניית גרף דו"צ כך שהקודקודים בצד אחד הם השחקנים ובצד השני הם החדרים והצלעות ביניהם זה הערך של כל שחקן עבור כל חדר. לאחר בניית הגרף מצאנו שידוך מקסימלי שזו ההשמה. <br />
את שלב 2 ביצענו על ידי linear programming כמו שהוסבר בשיעור:<br />
מקסמנו את התועלת המינמלית של שחקן והגדרנו את האילוצים שלכל שחקן התועלת שלו תהיה גדולה שווה למקרה שהוא היה מקבל השמה אחרת ובנוסף סכום מחירי החדרים יהיה שווה לסכום הכולל של שכר הדירה. <br />
וכך קיבלנו את מחירי החדרים. <br />
(את ה-linear programming ביצענו באמצעות הספרייה pulp).
