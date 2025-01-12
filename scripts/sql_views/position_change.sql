SELECT * FROM fangraphs_fielding_2024;

ALTER TABLE fangraphs_batting_stats_2024 ADD COLUMN Pos text;

UPDATE fangraphs_batting_stats_2024 fb
SET Pos = ff."Pos"
FROM fangraphs_fielding_2024 ff
WHERE fb."IDfg" = ff."IDfg";

SELECT * FROM fangraphs_batting_stats_2024;

SELECT * FROM fangraphs_batting_stats_2024
WHERE "pos" = 'DH';

UPDATE fangraphs_batting_stats_2024
SET "pos" = 'DH'
WHERE "pos" IS NULL;