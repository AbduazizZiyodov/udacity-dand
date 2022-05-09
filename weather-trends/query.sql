SELECT
SELECT
    c.year AS c_year,
    c.city,
    c.country,
    c.avg_temp AS c_temp,
    g.year AS g_year,
    g.avg_temp AS g_temp
FROM city_data AS c
    JOIN global_data g ON c.year = g.year
WHERE c.city LIKE 'Tashkent'