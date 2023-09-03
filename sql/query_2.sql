-- Выбираем имя продавца, сумму и количество продаж,
-- а также ранжируем их по количеству и сумме продаж
SELECT
    e.id,                                                     -- id продавца
    e.name AS employee_name,                                  -- Имя продавца
    SUM(s.price) AS total_sales,                              -- Сумма продаж
    COUNT(s.id) AS total_sales_count,                         -- Количество продаж
    RANK() OVER (ORDER BY COUNT(s.id) DESC) AS sales_rank,    -- Ранг по количеству продаж
    RANK() OVER (ORDER BY SUM(s.price) DESC) AS revenue_rank  -- Ранг по сумме продаж
FROM
    employee e
LEFT JOIN
    sales s ON e.id = s.employee_id  -- Объединяем таблицы по идентификатору продавца
GROUP BY
    e.id, e.name                     -- Группируем результаты по идентификатору и имени продавца
ORDER BY
    sales_rank, revenue_rank;        -- Сортируем результаты по рангам
