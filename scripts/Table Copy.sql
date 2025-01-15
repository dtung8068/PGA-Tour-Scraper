

COPY sg_total(rank, player, avg, "TOTAL SG:T", "TOTAL SG:T2G", "TOTAL SG:P", "MEASURED ROUNDS", tournament_date, tournament_name)
FROM 'C:\Users\tungd\downloads\pga-tour-scraper\data\SG_Total\sg_total.csv'
ENCODING 'utf8'
DELIMITER ','
CSV HEADER;