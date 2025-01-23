SELECT * from statcast_all;

DELETE FROM statcast_all
WHERE description IN ('pitchout', 'sac_fly', 'sac_bunt', 'missed_bunt');

UPDATE statcast_all
SET description = 'ball'
WHERE description = 'hit_by_pitch';