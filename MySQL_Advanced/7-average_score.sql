-- script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (user_id int)
BEGIN 
  SET @avarege = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);
  UPDATE users SET average_score = @avarege WHERE id = user_id;
END $$
DELIMITER;
