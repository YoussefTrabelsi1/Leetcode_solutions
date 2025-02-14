WITH user_by_tweet AS (
  SELECT
    user_id,
    COUNT(msg) AS nb_tweets
  FROM tweets
  WHERE EXTRACT(YEAR FROM tweet_date)='2022'
  GROUP BY user_id)

SELECT 
  nb_tweets AS tweet_bucket,
  COUNT(user_id) AS users_num
FROM user_by_tweet
GROUP BY tweet_bucket