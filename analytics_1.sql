/*
La siguiente (única) query genera una tabla con las cantidades ("amounts") de compras realizadas por cada usuario.
La primera columna indica el usuario, y la segunda la cantidad de compras. Está ordenada de manera decreciente.
Al final se selecciona el 5% de los usuarios con más compras, es decir, las 5% primeras filas de la tabla mencionada.

Es sobre estos usuarios que luego habría que calcular los tiempos promedios entre compras.

Nomenclatura:
amountswrn = amounts with row number
*/

SELECT amountswrn.device_id, amountswrn.amount
FROM (
  SELECT amounts.*, @counter:=@counter+1 AS rownumber 
  FROM (
    SELECT device_id, COUNT(device_id) AS amount
    FROM logs
    WHERE event_id='2'
    GROUP BY device_id
    ORDER BY amount DESC
    ) AS amounts, 
   (SELECT @counter:=0) AS initvar
  ) AS amountswrn
WHERE amountswrn.rownumber <= ceil(0.05*@counter);