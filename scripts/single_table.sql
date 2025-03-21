CREATE TABLE TOURNAMENT_DATA AS (
	SELECT
		SG_T2G.PLAYER AS PLAYER,
		SG_T2G.TOURNAMENT_DATE AS TOURNAMENT_DATE,
		SG_T2G.TOURNAMENT_NAME AS TOURNAMENT_NAME,
		SG_T2G.SG_OTT AS SG_OTT,
		SG_T2G.SG_APR AS SG_APR,
		SG_T2G.SG_ARG AS SG_ARG,
		SG_TOTAL.SG_TOTAL AS SG_TOTAL,
		SG_TOTAL.SG_T2G AS SG_T2G,
		SG_TOTAL.SG_P AS SG_P,
		DRIVING_DISTANCE.AVG_DISTANCE AS DISTANCE,
		DRIVING_ACCURACY.DRIVING_ACCURACY AS DRIVING_ACCURACY,
		BIRDIES.BIRDIES AS BIRDIES,
		BOGEYS.BOGEYS AS BOGEYS,
		BIRDIE_BOGEY_RATIO.BIRDIES_AND_BETTER AS BIRDIES_AND_BETTER,
		BIRDIE_BOGEY_RATIO.BOGEYS_AND_WORSE AS BOGEYS_AND_WORSE,
		BIRDIES_AND_BETTER - BIRDIES AS EAGLES,
		BOGEYS_AND_WORSE - BOGEYS AS DOUBLE_BOGEYS,
		18 * SG_T2G.ROUNDS - BIRDIES_AND_BETTER - BOGEYS_AND_WORSE AS PARS,
		TOURNAMENT_RESULTS.RANK AS FINISHING_POSITION,
		SG_T2G.ROUNDS AS ROUNDS
	FROM
		SG_T2G_CLEANED AS SG_T2G
		LEFT JOIN SG_TOTAL_CLEANED AS SG_TOTAL ON (
			SG_T2G.PLAYER = SG_TOTAL.PLAYER
			AND SG_T2G.TOURNAMENT_DATE = SG_TOTAL.TOURNAMENT_DATE
			AND SG_T2G.TOURNAMENT_NAME = SG_TOTAL.TOURNAMENT_NAME
		)
		LEFT JOIN DRIVING_DISTANCE_CLEANED AS DRIVING_DISTANCE ON (
			SG_T2G.PLAYER = DRIVING_DISTANCE.PLAYER
			AND SG_T2G.TOURNAMENT_DATE = DRIVING_DISTANCE.TOURNAMENT_DATE
			AND SG_T2G.TOURNAMENT_NAME = DRIVING_DISTANCE.TOURNAMENT_NAME
		)
		LEFT JOIN DRIVING_ACCURACY_CLEANED AS DRIVING_ACCURACY ON (
			SG_T2G.PLAYER = DRIVING_ACCURACY.PLAYER
			AND SG_T2G.TOURNAMENT_DATE = DRIVING_ACCURACY.TOURNAMENT_DATE
			AND SG_T2G.TOURNAMENT_NAME = DRIVING_ACCURACY.TOURNAMENT_NAME
		)
		LEFT JOIN BIRDIES_CLEANED AS BIRDIES ON (
			SG_T2G.PLAYER = BIRDIES.PLAYER
			AND SG_T2G.TOURNAMENT_DATE = BIRDIES.TOURNAMENT_DATE
			AND SG_T2G.TOURNAMENT_NAME = BIRDIES.TOURNAMENT_NAME
		)
		LEFT JOIN BOGEYS_CLEANED AS BOGEYS ON (
			SG_T2G.PLAYER = BOGEYS.PLAYER
			AND SG_T2G.TOURNAMENT_DATE = BOGEYS.TOURNAMENT_DATE
			AND SG_T2G.TOURNAMENT_NAME = BOGEYS.TOURNAMENT_NAME
		)
		LEFT JOIN BIRDIE_BOGEY_RATIO_CLEANED AS BIRDIE_BOGEY_RATIO ON (
			SG_T2G.PLAYER = BIRDIE_BOGEY_RATIO.PLAYER
			AND SG_T2G.TOURNAMENT_DATE = BIRDIE_BOGEY_RATIO.TOURNAMENT_DATE
			AND SG_T2G.TOURNAMENT_NAME = BIRDIE_BOGEY_RATIO.TOURNAMENT_NAME
		)
		LEFT JOIN TOURNAMENT_RESULTS ON (
			SG_T2G.PLAYER = TOURNAMENT_RESULTS.PLAYER
			AND SG_T2G.TOURNAMENT_DATE = TOURNAMENT_RESULTS.TOURNAMENT_DATE
			AND SG_T2G.TOURNAMENT_NAME = TOURNAMENT_RESULTS.TOURNAMENT_NAME
		)
)