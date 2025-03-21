CREATE TABLE DRIVING_ACCURACY_CLEANED AS (
	SELECT
		*,
		FAIRWAYS_HIT / POSSIBLE_FAIRWAYS AS DRIVING_ACCURACY
	FROM
		(
			SELECT
				PLAYER,
				TOURNAMENT_DATE,
				TOURNAMENT_NAME,
				CASE
					WHEN "POSSIBLE FAIRWAYS" < DIFF_POSSIBLE_FAIRWAYS THEN "FAIRWAYS HIT"
					ELSE "FAIRWAYS HIT" - COALESCE(DIFF_FAIRWAYS_HIT, 0)
				END AS FAIRWAYS_HIT,
				CASE
					WHEN "POSSIBLE FAIRWAYS" < DIFF_POSSIBLE_FAIRWAYS THEN "POSSIBLE FAIRWAYS"
					ELSE "POSSIBLE FAIRWAYS" - COALESCE(DIFF_POSSIBLE_FAIRWAYS, 0)
				END AS POSSIBLE_FAIRWAYS
			FROM
				(
					SELECT
						PLAYER,
						TOURNAMENT_DATE,
						TOURNAMENT_NAME,
						"FAIRWAYS HIT",
						LAG("FAIRWAYS HIT") OVER (
							PARTITION BY
								PLAYER
							ORDER BY
								TOURNAMENT_DATE ASC,
								"POSSIBLE FAIRWAYS" ASC
						) AS DIFF_FAIRWAYS_HIT,
						"POSSIBLE FAIRWAYS",
						LAG("POSSIBLE FAIRWAYS") OVER (
							PARTITION BY
								PLAYER
							ORDER BY
								TOURNAMENT_DATE ASC,
								"POSSIBLE FAIRWAYS" ASC
						) AS DIFF_POSSIBLE_FAIRWAYS
					FROM
						(
							SELECT
								PLAYER,
								TOURNAMENT_DATE,
								TOURNAMENT_NAME,
								CAST(CAST("FAIRWAYS HIT" AS MONEY) AS NUMERIC) AS "FAIRWAYS HIT",
								CAST(CAST("POSSIBLE FAIRWAYS" AS MONEY) AS NUMERIC) AS "POSSIBLE FAIRWAYS"
							FROM
								DRIVING_ACCURACY
						)
				)
		)
	WHERE
		POSSIBLE_FAIRWAYS > 0
)