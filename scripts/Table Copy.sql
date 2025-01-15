--SG_Total
COPY sg_total(rank, player, avg, "TOTAL SG:T", "TOTAL SG:T2G", "TOTAL SG:P", "MEASURED ROUNDS", tournament_date, tournament_name)
FROM 'C:\Users\tungd\downloads\pga-tour-scraper\data\SG_Total\sg_total.csv'
ENCODING 'utf8'
DELIMITER ','
CSV HEADER;

--SG_T2G
COPY sg_t2g(rank, player, avg, "SG:OTT", "SG:APR", "SG:ARG", "MEASURED ROUNDS", tournament_date, tournament_name)
FROM 'C:\Users\tungd\downloads\pga-tour-scraper\data\SG_T2G\sg_t2g.csv'
ENCODING 'utf8'
DELIMITER ','
CSV HEADER;

--Birdie Bogey Ratio
COPY birdie_bogey_ratio(rank, player, "BIRDIE TO BOGEY RATIO", "TOTAL BIRDIES AND BETTER", "TOTAL BOGEYS AND WORSE", tournament_date, tournament_name)
FROM 'C:\Users\tungd\downloads\pga-tour-scraper\data\Birdie_Bogey_Ratio\birdie_bogey_ratio.csv'
ENCODING 'utf8'
DELIMITER ','
CSV HEADER;

--Birdies
COPY birdies(rank, player, total, tournament_date, tournament_name)
FROM 'C:\Users\tungd\downloads\pga-tour-scraper\data\Birdies\birdies.csv'
ENCODING 'utf8'
DELIMITER ','
CSV HEADER;

--Bogeys
COPY bogeys(rank, player, "AVERAGE BOGEYS PER ROUND", "TOTAL BOGEYS", "ROUNDS PLAYED", tournament_date, tournament_name)
FROM 'C:\Users\tungd\downloads\pga-tour-scraper\data\Bogeys\bogeys.csv'
ENCODING 'utf8'
DELIMITER ','
CSV HEADER;

--Tournament Results
COPY tournament_results(rank, player, money, tournament_date, tournament_name)
FROM 'C:\Users\tungd\downloads\pga-tour-scraper\data\Tournament_Results\tournament_results.csv'
ENCODING 'utf8'
DELIMITER ','
CSV HEADER;

--Driving Distance
COPY driving_distance(rank, player, avg, "TOTAL DISTANCE", "TOTAL DRIVES", tournament_date, tournament_name)
FROM 'C:\Users\tungd\downloads\pga-tour-scraper\data\Driving_Distance\driving_distance.csv'
ENCODING 'utf8'
DELIMITER ','
CSV HEADER;

--Driving Accuracy
COPY driving_accuracy(rank, player, "%", "FAIRWAYS HIT", "POSSIBLE FAIRWAYS", tournament_date, tournament_name)
FROM 'C:\Users\tungd\downloads\pga-tour-scraper\data\Driving_Accuracy\driving_accuracy.csv'
ENCODING 'utf8'
DELIMITER ','
CSV HEADER;