import numpy as np

def add_matrices(matrix1, matrix2):
    # Перевірка на валідність розмірів матриць
    if len(matrix1) != len(matrix2):
        return 'Розміри матриць нерівні'
    
    for i, _ in enumerate(matrix1):
        if len(matrix1[i]) != len(matrix2[i]):
            return 'Розміри матриць нерівні'

    # Створення нової матриці з нулями
    result = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]

    # Додавання елементів матриць
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result

def subtract_matrices(matrix1, matrix2):
    # Перевірка на валідність розмірів матриць
    if len(matrix1) != len(matrix2):
        return 'Розміри матриць нерівні'
    
    for i, _ in enumerate(matrix1):
        if len(matrix1[i]) != len(matrix2[i]):
            return 'Розміри матриць нерівні'


    # Створення нової матриці з нулями
    result = [[0] * len(matrix1[0]) for _ in range(len(matrix1))]

    # Віднімання елементів матриць
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]

    return result

def inverse_matrix(matrix):
    # Перевірка на валідність розміру матриці
    if type(matrix) != list:
        return 'Невірно введені дані'
    for i in matrix:
        if len(matrix) != len(i):
            return 'Це не є квадратна матриця, знайти обернену матрицю неможливо'
    # if len(matrix) != len(matrix[0]):
    #     return None

    n = len(matrix)
    
    # Створення розширеної матриці, яка містить початну матрицю та одиничну матрицю
    augmented_matrix = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]
    
    # Виконання елементарних операцій над рядками для отримання верхньої трикутної матриці
    for i in range(n):
        # Перевірка на ненульовий дільник
        if augmented_matrix[i][i] == 0:
            return 'Нульовий дільник, знайти обернену матрицю неможливо'
        
        # Нормалізація поточного рядка
        divisor = augmented_matrix[i][i]
        augmented_matrix[i] = [round(elem / divisor, 2) for elem in augmented_matrix[i]]
        # print(augmented_matrix)
        # Віднімання кратного поточного рядка від інших рядків
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = [elem - factor * augmented_matrix[i][index] for index, elem in enumerate(augmented_matrix[j])]
    
    # Витягнення оберненої матриці з розширеної матриці
    inverse = [row[n:] for row in augmented_matrix]
    # for i in range(len(inverse)):
    #     for j in range(len(inverse[i])):
    #         inverse[i][j] = round(inverse[i][j], 2)
    return inverse

def multiplication_scalar(object1, scalar):
    if type(object1) == list:
        # Створення нової матриці з нулями
        result = [[0] * len(object1[0]) for _ in range(len(object1))]

        # Множення елементів матриці на скаляр
        for i in range(len(object1)):
            for j in range(len(object1[0])):
                result[i][j] = object1[i][j] * scalar

        return result
    elif type(object1) == tuple:
        if len(object1) > 3:
            return 'Вектори можуть мати максимально 3 координати'
        result = [i*scalar for i in object1]
        return tuple(result)
    else:
        return 'Невірно введені дані'

def determinant(matrix):
    if type(matrix) != list:
        return 'Невірно введені дані'
    for i in matrix:
        if len(matrix) != len(i):
            return 'Це не є квадратна матриця, знайти обернену матрицю неможливо'
    matrix = np.array(matrix, dtype=float)  # Перетворюємо вхідну матрицю в NumPy-масив
    n = len(matrix)
    det = 1.0

    for i in range(n):
        if matrix[i][i] == 0:  # Якщо головний елемент дорівнює 0, проводимо перестановку рядків
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    det *= -1
                    break
            else:
                return 0.0  # Якщо всі елементи у стовпці рівні нулю, визначник рівний 0

        for j in range(i + 1, n):
            ratio = matrix[j][i] / matrix[i][i]
            matrix[j] -= ratio * matrix[i]

    for i in range(n):
        det *= matrix[i][i]  # Множимо головні діагональні елементи

    return det

def add_vectors(vector1, vector2):
    if len(vector1) > 3 or len(vector2) > 3:
        return 'Вектори можуть мати максимально 3 координати'
    
    if len(vector1) != len(vector2):
        return 'Кількість координат векторів нерівні'
    
    result = [vector1[i] + vector2[i] for i in range(len(vector1))]

    return tuple(result)

def subtract_vectors(vector1, vector2):
    if len(vector1) > 3 or len(vector2) > 3:
        return 'Вектори можуть мати максимально 3 координати'
    
    if len(vector1) != len(vector2):
        return 'Кількість координат векторів нерівні'
    
    result = [vector1[i] - vector2[i] for i in range(len(vector1))]

    return tuple(result)

def multiplication(object1, object2):
    if type(object1) == type(object2) and type(object1) == tuple:
        if len(object1) != len(object2):
            return 'Кількість координат векторів нерівні'
        
        result =  0

        for i in range(len(object1)):
            result += object1[i]*object2[i]

        return result
    
    elif type(object1) == type(object2) and type(object1) == list:

        matrix1 = np.array(object1)
        matrix2 = np.array(object2)
    
        if matrix1.shape[1] != matrix2.shape[0]:
            return "Кількість стовпців у першій матриці повинна дорівнювати кількості рядків у другій матриці."
        result = np.zeros((matrix1.shape[0], matrix2.shape[1]))

        for i in range(matrix1.shape[0]):
            for j in range(matrix2.shape[1]):
                for k in range(matrix1.shape[1]):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result.tolist()
    
    elif type(object1) != type(object2) and (type(object1) == list or type(object2) == list):
        result = []
        if type(object1) == list:
            if len(object2) > 3:
                return "Максимальна кількість координат у векторі 3"
            for i in object1:
                if len(object2) != len(i):
                    return "Довжина вектора повинна дорівнювати кількості стовпців у матриці."
            # if len(object2) != len(object1[0]):
            #     return "Довжина вектора повинна дорівнювати кількості стовпців у матриці."

            for row in object1:
                row_result = 0
                for i in range(len(object2)):
                    row_result += object2[i] * row[i]
                result.append([row_result])
            return result
        
        elif type(object2) == list:
            if len(object1) > 3:
                return "Максимальна кількість координат у векторі 3"
            
            for i in object2:
                if len(object1) != len(i):
                    return "Довжина вектора повинна дорівнювати кількості стовпців у матриці."
                
            # if len(object1) != len(object2[0]):
            #     return "Довжина вектора повинна дорівнювати кількості стовпців у матриці."
            
            for row in object2:
                row_result = 0
                for i in range(len(object1)):
                    row_result += object1[i] * row[i]
                result.append([row_result])
            return result
        
def vectors_multiplication(vector1, vector2):
    if len(vector1) == len(vector2) and len(vector1) == 3 and type(vector1) == type(vector2) and type(vector1) == tuple:
        x1, y1, z1 = vector1
        x2, y2, z2 = vector2

        result = [y1 * z2 - y2 * z1,
                z1 * x2 - z2 * x1,
                x1 * y2 - x2 * y1]
        return tuple(result)
    
    return 'Невірно введені дані'

def transpose_matrix(matrix):
    if type(matrix) != list:
        return 'Невірно введені дані'
    
    rows = len(matrix)
    columns = len(matrix[0])
    
    # Створюємо нову матрицю з розміняними рядками і стовпцями
    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(columns)]
    
    return transposed_matrix

def convertIn(*objects: str):
    if len(objects) == 1:
        if '(' in objects[0] and ')' in objects[0]:
            try:
                return tuple(map(float, objects[0].strip('() ').split()))
            except:
                return 'error'
        else:
            try:
                matrix = np.matrix(objects[0].replace('\n', ';')).tolist()
            except:
                return 'error'
            else:
                return matrix
    elif len(objects) == 2:
        result = []
        for i in objects:
            if '(' in i and ')' in i:
                try:
                    vector =  tuple(map(float, i.strip('() ').split()))
                except:
                    return 'error'
                else:
                    result.append(vector)
            else:
                try:
                    matrix = np.matrix(i.replace('\n', ';')).tolist()
                except:
                    return 'error'
                else:
                    result.append(matrix)
        return tuple(result)
    else:
        return 'Невірно введені дані'

def convertOut(res_in):
    if type(res_in) == tuple:
        res_out = [str(i) for i in res_in]
        for i, item in enumerate(res_out):
            if item[-2:] == '.0':
                res_out[i] = int(float(item))
            else:
                res_out[i] = float(item)
        return tuple(res_out)
    elif type(res_in) == list:
        for item in res_in:
            for i in range(len(item)):
                if str(item[i])[-2:] == '.0':
                    item[i] = int(float(item[i]))
        res_out = ''
        for i in res_in:
            res_out += ' '.join([str(number) for number in i]) + '\n'
        return res_out
    elif type(res_in) == str:
        return res_in
    else:
        n = str(res_in)
        return int(float(n)) if n[-2:] == '.0' else n
# print(transpose_matrix(array1))

# print(convertIn('1 2 3 4 5\n 1 2 3 4 5', '(1 2 3)'))