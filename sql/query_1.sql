-- Создаем временную таблицу для хранения дат
CREATE TEMPORARY TABLE IF NOT EXISTS random_dates (date_value DATE);

-- Устанавливаем начальную дату
SET @current_date = CURRENT_DATE();

-- Заполняем таблицу 100 случайными датами
INSERT INTO random_dates (date_value)
SELECT DATE_ADD(@current_date, INTERVAL FLOOR(RAND() * 6) + 2 DAY) AS random_date
FROM (
    SELECT 1 AS n
    UNION ALL
    SELECT 2
    UNION ALL
    SELECT 3
    UNION ALL
    SELECT 4
    UNION ALL
    SELECT 5
    UNION ALL
    SELECT 6
    UNION ALL
    SELECT 7
    UNION ALL
    SELECT 8
    UNION ALL
    SELECT 9
    UNION ALL
    SELECT 10
) AS numbers
LIMIT 99;

-- Выбираем 100 случайных дат из таблицы
SELECT date_value FROM random_dates;