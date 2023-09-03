-- Создаем временную таблицу для хранения дат
CREATE TEMPORARY TABLE IF NOT EXISTS random_dates (date_value DATE);

-- Устанавливаем начальную дату
SET @current_date = CURRENT_DATE();

-- Заполняем таблицу 100 случайными датами
INSERT INTO random_dates (date_value)
SELECT DATE_ADD(@current_date, INTERVAL FLOOR(RAND() * 6) + 2 DAY) AS random_date
FROM information_schema.tables LIMIT 100;

-- Выбираем 100 случайных дат из таблицы
SELECT date_value FROM random_dates;