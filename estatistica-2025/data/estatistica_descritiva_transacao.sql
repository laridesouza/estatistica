WITH 
tb_usuario AS (
    SELECT idUsuario,
           SUM(qtdPontos) AS qtdPontos
    FROM points
    GROUP BY idUsuario
),

tb_subset_mediana AS (
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT COUNT(*) % 2 = 0 FROM tb_usuario)
    OFFSET (SELECT COUNT(*) / 2 FROM tb_usuario)
), 

tb_mediana AS ( 
    SELECT AVG(qtdPontos) AS Mediana
    FROM tb_subset_mediana
),

tb_subset_quartil_01 AS (
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT COUNT(*) % 2 = 0 FROM tb_usuario)
    OFFSET (SELECT 1 * COUNT(*) / 4 FROM tb_usuario)
),

tb_quartil_01 AS (
    SELECT AVG(qtdPontos) AS Quartil_01
    FROM tb_subset_quartil_01
),

tb_subset_quartil_03 AS (
    SELECT qtdPontos
    FROM tb_usuario
    ORDER BY qtdPontos
    LIMIT 1 + (SELECT COUNT(*) % 2 = 0 FROM tb_usuario)
    OFFSET (SELECT 3 * COUNT(*) / 4 FROM tb_usuario)
),

tb_quartil_03 AS (
    SELECT AVG(qtdPontos) AS Quartil_03
    FROM tb_subset_quartil_03
), 

tb_stats AS (
    SELECT MIN(qtdPontos) AS minimo,
           AVG(qtdPontos) AS media,
           MAX(qtdPontos) AS maximo
    FROM tb_usuario
)

SELECT * 
FROM tb_stats
CROSS JOIN tb_mediana
CROSS JOIN tb_quartil_01
CROSS JOIN tb_quartil_03;
