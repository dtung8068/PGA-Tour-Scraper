SELECT
	*
FROM
	(
		SELECT
			PLAYER,
			TOURNAMENT_DATE,
			TOURNAMENT_NAME,
			CASE
				WHEN "ROUNDS PLAYED" < DIFF_ROUNDS_PLAYED THEN "TOTAL BOGEYS"
				ELSE "TOTAL BOGEYS" - COALESCE(DIFF_BOGEYS, 0)
			END AS BOGEYS,
			CASE
				WHEN "ROUNDS PLAYED" < DIFF_ROUNDS_PLAYED THEN "ROUNDS PLAYED"
				ELSE "ROUNDS PLAYED" - COALESCE(DIFF_ROUNDS_PLAYED, 0)
			END AS ROUNDS_PLAYED
		FROM
			(
				SELECT
					PLAYER,
					TOURNAMENT_DATE,
					TOURNAMENT_NAME,
					"TOTAL BOGEYS",
					LAG("TOTAL BOGEYS") OVER (
						PARTITION BY
							PLAYER
						ORDER BY
							TOURNAMENT_DATE ASC,
							"ROUNDS PLAYED" ASC
					) AS DIFF_BOGEYS,
					"ROUNDS PLAYED",
					LAG("ROUNDS PLAYED") OVER (
						PARTITION BY
							PLAYER
						ORDER BY
							TOURNAMENT_DATE ASC,
							"ROUNDS PLAYED" ASC
					) AS DIFF_ROUNDS_PLAYED
				FROM
					BOGEYS
			)
	)
WHERE
	ROUNDS_PLAYED > 0