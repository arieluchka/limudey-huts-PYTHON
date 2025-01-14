##### .lower()
יחליף את כל האותיות במחרוזת לאותיות קטנות
```python
var_1 = "Hello World! how Are yOu?"
print(var_1) #   "Hello World! how Are yOu?"

new_var = var_1.lower()
print(new_var) # "hello world! how are you?"
```
שמיש מאוד כשמקבלים קלט מהמשתמש ורוצים לוודא שהוא תקין (לדוגמה: כתובת מייל נעביר קודם לאותיות קטנות לפני שאנחנו בודקים אם היא תקינה וקיימת)
##### .upper()
```python
var_1 = "Hello World! how Are yOu?"
print(var_1) #   "Hello World! how Are yOu?"

new_var = var_1.upper()
print(new_var) # "HELLO WORLD! HOW ARE YOU?"
```

.startswith()
מאפשר לבדוק האם מחרוזת מתחילה עם תווים ספציפיים (מחזיר True/False)
```python
var_1 = "I love ice cream"

res = var_1.startswith("I") 
print(res) # True

res = var_1.startswith("I love ") 
print(res) # True

res = var_1.startswith("i") 
print(res) # False

res = var_1.startswith("love") 
print(res) # False
```

.endswith()
מאפשר לבדוק האם מחרוזת מסתיימת עם תווים ספציפיים (מחזיר True/False)
```python
var_1 = "I love ice cream"

res = var_1.endswith("I") 
print(res) # False

res = var_1.endswith("eam") 
print(res) # True

res = var_1.endswith("crea") 
print(res) # False
```

.join()
מחבר סדרה של ערכים (מחרוזת/רשימה/tuple וכו) למחרוזת חדשה, ומפריד בין ערכים עם מה שבמחרוזת.

```python
list1 = ["i", "love", "chocolate"]

connected1 = " ".join(list1)
print(connected1) # i love chocolate

connected2 = "+-".join(list1)
print(connected2) # i+-love+-chocolate
```

```python
list2 = ["192", "168", "1", "51"]

a_dot = "."

connected1 = a_dot.join(list2)
print(connected1) # 192.168.1.51

connected2 = "green".join(list2)
print(connected2) # 192green168green1green51

connected3 = list2[2].join(list2)
print(connected3) # 192116811151
```
