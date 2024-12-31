COPY sg_total(player_id, player, "TOTAL SG:T", "TOTAL SG:T2G", "TOTAL SG:P", "MEASURED ROUNDS") 
FROM PROGRAM 'data/SG_T2G_*.csv | cat'
DELIMITER ','
CSV HEADER;