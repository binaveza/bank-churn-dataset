import pandas as pd

def display_data(df, name):
    print(f"\n--- {name} ---")
    print(df.head())
    print("\nИнформация:\n")
    print(df.info())
    print("\nОписание:\n")
    print(df.describe())
    print("\n" + "#" * 30 + "\n")

submission = pd.read_csv('data/sample_submission.csv')
train = pd.read_csv('data/train.csv')  
test = pd.read_csv('data/test.csv')    

pd.set_option('display.max_columns', None)  
pd.set_option('display.width', 1000)  
pd.set_option('display.float_format', '{:.2f}'.format) 

# display_data(test, "Тестовые данные")
# display_data(train, "Обучающие данные")
# display_data(submission, "Данные для отправки")

# # Выявление пропусков (их в нашем датасэте нет)
# print(test.isna().sum())
# print(train.isna().sum())
# # print(submission.isna().sum())


# Получение размеров датафрейма
rows, columns = train.shape

# Вывод информации
print(f'{rows} rows × {columns} columns')
