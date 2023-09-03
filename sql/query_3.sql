-- Создаем временную таблицу для хранения результатов
CREATE TEMPORARY TABLE IF NOT EXISTS balance_periods (
    acc INT,            -- Номер аккаунта
    dt_from DATE,       -- Начало периода
    dt_to DATE,         -- Конец периода
    balance INT         -- Остаток на счете
);

-- Выполняем основной запрос для заполнения таблицы balance_periods
INSERT INTO balance_periods (acc, dt_from, dt_to, balance)
SELECT 
    t.from AS acc,                                    -- Номер аккаунта, с которого сделан перевод
    t.tdate AS dt_from,                               -- Дата перевода как начало периода
    IFNULL(MIN(tnext.tdate), '3000-01-01') AS dt_to,  -- Если есть следующая дата, то это конец периода, иначе '3000-01-01'
    IFNULL(SUM(t.amount), 0) AS balance               -- Сумма переводов в данном периоде
FROM 
    transfers t
LEFT JOIN 
    transfers tnext ON t.from = tnext.from AND t.tdate < tnext.tdate  -- Присоединяем следующий перевод по дате и аккаунту
GROUP BY 
    t.from, t.tdate                                                   -- Группируем результаты по аккаунту и дате перевода
ORDER BY 
    t.from, t.tdate;                                                  -- Сортируем результаты по аккаунту и дате перевода

-- Выводим результаты из таблицы balance_periods
SELECT * FROM balance_periods;