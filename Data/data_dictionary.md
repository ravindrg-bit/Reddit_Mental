# Data Dictionary: reddit_mh_clean.parquet

Generated: 2026-03-27 18:55:21 UTC

## Dataset Overview
- File: Data/processed/reddit_mh_clean.parquet
- Rows: 1,107,302
- Columns: 357

## Feature Group Summary
| Group | Column Count |
|---|---:|
| labels | 2 |
| lexicon_totals | 6 |
| liwc | 62 |
| metadata | 5 |
| readability_length | 19 |
| sentiment | 4 |
| text | 3 |
| tfidf | 256 |

## Column Dictionary
List format understanding of each column:

1. subreddit
   - Group: metadata
   - Type: str
   - Understanding: Source subreddit name extracted from filename.
   - Profile: nulls=0 (0.0000%), unique=n/a, min=n/a, q1=n/a, median=n/a, q3=n/a, max=n/a, mean=n/a
   - Example: COVID19_support

2. author
   - Group: metadata
   - Type: str
   - Understanding: Reddit author username as provided in source data.
   - Profile: nulls=0 (0.0000%), unique=n/a, min=n/a, q1=n/a, median=n/a, q3=n/a, max=n/a, mean=n/a
   - Example: thatreddittherapist

3. date
   - Group: metadata
   - Type: str
   - Understanding: Post date string from source dataset.
   - Profile: nulls=0 (0.0000%), unique=n/a, min=n/a, q1=n/a, median=n/a, q3=n/a, max=n/a, mean=n/a
   - Example: 2020/02/15

4. post
   - Group: text
   - Type: str
   - Understanding: Original raw post text before cleaning.
   - Profile: nulls=0 (0.0000%), unique=n/a, min=n/a, q1=n/a, median=n/a, q3=n/a, max=n/a, mean=n/a
   - Example: Welcome to COVID19 Support! Hi everyone,  I'm a counselor (I mostly work in pers...

5. automated_readability_index
   - Group: readability_length
   - Type: float64
   - Understanding: Readability metric computed from the post text.
   - Profile: nulls=0 (0.0000%), unique=464792, min=-16.2200, q1=1.9480, median=3.6733, q3=5.5888, max=6315.8200, mean=4.0579

6. coleman_liau_index
   - Group: readability_length
   - Type: float64
   - Understanding: Readability metric computed from the post text.
   - Profile: nulls=0 (0.0000%), unique=468518, min=-63.2627, q1=3.7632, median=5.1498, q3=6.6324, max=7886.1668, mean=5.4558

7. flesch_kincaid_grade_level
   - Group: readability_length
   - Type: float64
   - Understanding: Readability metric computed from the post text.
   - Profile: nulls=0 (0.0000%), unique=311426, min=-3.6167, q1=3.3268, median=4.6411, q3=6.0916, max=3955.6214, mean=4.8510

8. flesch_reading_ease
   - Group: readability_length
   - Type: float64
   - Understanding: Readability metric computed from the post text.
   - Profile: nulls=0 (0.0000%), unique=307713, min=-28256.5383, q1=77.2662, median=84.1319, q3=90.1834, max=121.7839, mean=82.8814

9. gulpease_index
   - Group: readability_length
   - Type: float64
   - Understanding: Readability metric computed from the post text.
   - Profile: nulls=0 (0.0000%), unique=205415, min=-13295.7826, q1=68.1541, median=73.5455, q3=80.1811, max=731.5000, mean=75.1463

10. gunning_fog_index
   - Group: readability_length
   - Type: float64
   - Understanding: Readability metric computed from the post text.
   - Profile: nulls=0 (0.0000%), unique=199275, min=0.1778, q1=6.1478, median=7.6000, q3=9.1630, max=725.4959, mean=7.7630

11. lix
   - Group: readability_length
   - Type: float64
   - Understanding: Readability metric computed from the post text.
   - Profile: nulls=0 (0.0000%), unique=227605, min=0.4444, q1=22.6948, median=27.0291, q3=31.7414, max=1813.7676, mean=27.4868

12. smog_index
   - Group: readability_length
   - Type: float64
   - Understanding: Readability metric computed from the post text.
   - Profile: nulls=0 (0.0000%), unique=7225, min=3.1291, q1=7.1392, median=8.0765, q3=9.2231, max=87.9591, mean=8.0782

13. wiener_sachtextformel
   - Group: readability_length
   - Type: float64
   - Understanding: Readability metric computed from the post text.
   - Profile: nulls=0 (0.0000%), unique=820470, min=-4.0707, q1=0.7596, median=1.7692, q3=2.9014, max=304.2890, mean=1.9138

14. n_chars
   - Group: readability_length
   - Type: int64
   - Understanding: Text-length/readability count feature derived from source text.
   - Profile: nulls=0 (0.0000%), unique=7044, min=1.0000, q1=273.0000, median=532.0000, q3=961.0000, max=30935.0000, mean=748.5150

15. n_long_words
   - Group: readability_length
   - Type: int64
   - Understanding: Text-length/readability count feature derived from source text.
   - Profile: nulls=0 (0.0000%), unique=510, min=0.0000, q1=9.0000, median=19.0000, q3=35.0000, max=1282.0000, mean=27.0044

16. n_monosyllable_words
   - Group: readability_length
   - Type: int64
   - Understanding: Text-length/readability count feature derived from source text.
   - Profile: nulls=0 (0.0000%), unique=1870, min=0.0000, q1=52.0000, median=103.0000, q3=189.0000, max=12003.0000, mean=146.6265

17. n_polysyllable_words
   - Group: readability_length
   - Type: int64
   - Understanding: Text-length/readability count feature derived from source text.
   - Profile: nulls=0 (0.0000%), unique=295, min=0.0000, q1=4.0000, median=8.0000, q3=16.0000, max=769.0000, mean=12.3896

18. n_sents
   - Group: readability_length
   - Type: int64
   - Understanding: Text-length/readability count feature derived from source text.
   - Profile: nulls=0 (0.0000%), unique=320, min=1.0000, q1=6.0000, median=11.0000, q3=19.0000, max=4001.0000, mean=14.7695

19. n_syllables
   - Group: readability_length
   - Type: int64
   - Understanding: Text-length/readability count feature derived from source text.
   - Profile: nulls=0 (0.0000%), unique=2825, min=1.0000, q1=88.0000, median=173.0000, q3=313.0000, max=12003.0000, mean=243.3979

20. n_unique_words
   - Group: readability_length
   - Type: int64
   - Understanding: Text-length/readability count feature derived from source text.
   - Profile: nulls=0 (0.0000%), unique=797, min=1.0000, q1=49.0000, median=85.0000, q3=133.0000, max=1536.0000, mean=100.7474

21. n_words
   - Group: readability_length
   - Type: int64
   - Understanding: Text-length/readability count feature derived from source text.
   - Profile: nulls=0 (0.0000%), unique=2248, min=1.0000, q1=67.0000, median=133.0000, q3=240.0000, max=12003.0000, mean=186.7081

22. sent_neg
   - Group: sentiment
   - Type: float64
   - Understanding: VADER negative sentiment score.
   - Profile: nulls=0 (0.0000%), unique=806, min=0.0000, q1=0.0460, median=0.0940, q3=0.1520, max=1.0000, mean=0.1063

23. sent_neu
   - Group: sentiment
   - Type: float64
   - Understanding: VADER neutral sentiment score.
   - Profile: nulls=0 (0.0000%), unique=874, min=0.0000, q1=0.7230, median=0.7920, q3=0.8570, max=1.0000, mean=0.7870

24. sent_pos
   - Group: sentiment
   - Type: float64
   - Understanding: VADER positive sentiment score.
   - Profile: nulls=0 (0.0000%), unique=770, min=0.0000, q1=0.0580, median=0.0990, q3=0.1450, max=1.0000, mean=0.1066

25. sent_compound
   - Group: sentiment
   - Type: float64
   - Understanding: VADER compound sentiment score in [-1, 1].
   - Profile: nulls=0 (0.0000%), unique=19968, min=-1.0000, q1=-0.8138, median=0.0000, q3=0.8185, max=1.0000, mean=0.0117

26. economic_stress_total
   - Group: lexicon_totals
   - Type: int64
   - Understanding: Lexicon/category total count for 'economic_stress' terms in the post.
   - Profile: nulls=0 (0.0000%), unique=57, min=0.0000, q1=0.0000, median=0.0000, q3=2.0000, max=125.0000, mean=1.2277

27. isolation_total
   - Group: lexicon_totals
   - Type: int64
   - Understanding: Lexicon/category total count for 'isolation' terms in the post.
   - Profile: nulls=0 (0.0000%), unique=26, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=37.0000, mean=0.2144

28. substance_use_total
   - Group: lexicon_totals
   - Type: int64
   - Understanding: Lexicon/category total count for 'substance_use' terms in the post.
   - Profile: nulls=0 (0.0000%), unique=48, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=74.0000, mean=0.4161

29. guns_total
   - Group: lexicon_totals
   - Type: int64
   - Understanding: Lexicon/category total count for 'guns' terms in the post.
   - Profile: nulls=0 (0.0000%), unique=44, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=80.0000, mean=0.0740

30. domestic_stress_total
   - Group: lexicon_totals
   - Type: int64
   - Understanding: Lexicon/category total count for 'domestic_stress' terms in the post.
   - Profile: nulls=0 (0.0000%), unique=27, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=42.0000, mean=0.1408

31. suicidality_total
   - Group: lexicon_totals
   - Type: int64
   - Understanding: Lexicon/category total count for 'suicidality' terms in the post.
   - Profile: nulls=0 (0.0000%), unique=30, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1200.0000, mean=0.1434

32. punctuation
   - Group: readability_length
   - Type: float64
   - Understanding: Punctuation-related text feature from the original dataset.
   - Profile: nulls=0 (0.0000%), unique=667, min=0.0000, q1=7.0000, median=16.0000, q3=30.0000, max=4568.0000, mean=24.2144

33. liwc_1st_pers
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for '1st_pers'.
   - Profile: nulls=0 (0.0000%), unique=93, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=149.0000, mean=1.0831

34. liwc_2nd_pers
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for '2nd_pers'.
   - Profile: nulls=0 (0.0000%), unique=129, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=362.0000, mean=0.9491

35. liwc_3rd_pers
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for '3rd_pers'.
   - Profile: nulls=0 (0.0000%), unique=81, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=163.0000, mean=1.2187

36. liwc_achievement
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'achievement'.
   - Profile: nulls=0 (0.0000%), unique=74, min=0.0000, q1=0.0000, median=1.0000, q3=3.0000, max=132.0000, mean=2.1138

37. liwc_adverbs
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'adverbs'.
   - Profile: nulls=0 (0.0000%), unique=181, min=0.0000, q1=2.0000, median=5.0000, q3=11.0000, max=416.0000, mean=8.0801

38. liwc_affective_processes
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'affective_processes'.
   - Profile: nulls=0 (0.0000%), unique=199, min=0.0000, q1=2.0000, median=5.0000, q3=11.0000, max=1201.0000, mean=8.4495

39. liwc_anger
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'anger'.
   - Profile: nulls=0 (0.0000%), unique=76, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=1201.0000, mean=1.0713

40. liwc_anxiety
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'anxiety'.
   - Profile: nulls=0 (0.0000%), unique=39, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=97.0000, mean=0.6546

41. liwc_articles_article
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'articles_article'.
   - Profile: nulls=0 (0.0000%), unique=227, min=0.0000, q1=3.0000, median=6.0000, q3=12.0000, max=726.0000, mean=9.4571

42. liwc_assent
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'assent'.
   - Profile: nulls=0 (0.0000%), unique=28, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=53.0000, mean=0.1827

43. liwc_auxiliary_verbs
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'auxiliary_verbs'.
   - Profile: nulls=0 (0.0000%), unique=289, min=0.0000, q1=5.0000, median=11.0000, q3=20.0000, max=4001.0000, mean=15.1503

44. liwc_biological
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'biological'.
   - Profile: nulls=0 (0.0000%), unique=122, min=0.0000, q1=0.0000, median=1.0000, q3=4.0000, max=281.0000, mean=3.1320

45. liwc_body
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'body'.
   - Profile: nulls=0 (0.0000%), unique=67, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=281.0000, mean=0.9755

46. liwc_causation
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'causation'.
   - Profile: nulls=0 (0.0000%), unique=69, min=0.0000, q1=0.0000, median=1.0000, q3=3.0000, max=120.0000, mean=2.0141

47. liwc_certainty
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'certainty'.
   - Profile: nulls=0 (0.0000%), unique=61, min=0.0000, q1=0.0000, median=1.0000, q3=2.0000, max=114.0000, mean=1.6008

48. liwc_cognitive
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'cognitive'.
   - Profile: nulls=0 (0.0000%), unique=498, min=0.0000, q1=9.0000, median=19.0000, q3=36.0000, max=1357.0000, mean=28.0890

49. liwc_common_verbs
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'common_verbs'.
   - Profile: nulls=0 (0.0000%), unique=482, min=0.0000, q1=10.0000, median=20.0000, q3=37.0000, max=4001.0000, mean=28.2944

50. liwc_conjunctions
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'conjunctions'.
   - Profile: nulls=0 (0.0000%), unique=258, min=0.0000, q1=4.0000, median=9.0000, q3=16.0000, max=472.0000, mean=12.6210

51. liwc_death
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'death'.
   - Profile: nulls=0 (0.0000%), unique=43, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1200.0000, mean=0.3156

52. liwc_discrepancy
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'discrepancy'.
   - Profile: nulls=0 (0.0000%), unique=98, min=0.0000, q1=1.0000, median=2.0000, q3=5.0000, max=1200.0000, mean=3.6310

53. liwc_exclusive
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'exclusive'.
   - Profile: nulls=0 (0.0000%), unique=122, min=0.0000, q1=1.0000, median=4.0000, q3=7.0000, max=298.0000, mean=5.5389

54. liwc_family
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'family'.
   - Profile: nulls=0 (0.0000%), unique=75, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=156.0000, mean=0.8382

55. liwc_feel
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'feel'.
   - Profile: nulls=0 (0.0000%), unique=54, min=0.0000, q1=0.0000, median=0.0000, q3=2.0000, max=76.0000, mean=1.3687

56. liwc_fillers
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'fillers'.
   - Profile: nulls=0 (0.0000%), unique=49, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=67.0000, mean=0.9246

57. liwc_friends
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'friends'.
   - Profile: nulls=0 (0.0000%), unique=50, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=71.0000, mean=0.5842

58. liwc_future_tense
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'future_tense'.
   - Profile: nulls=0 (0.0000%), unique=60, min=0.0000, q1=0.0000, median=1.0000, q3=2.0000, max=86.0000, mean=1.6392

59. liwc_health
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'health'.
   - Profile: nulls=0 (0.0000%), unique=65, min=0.0000, q1=0.0000, median=0.0000, q3=2.0000, max=105.0000, mean=1.2274

60. liwc_hear
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'hear'.
   - Profile: nulls=0 (0.0000%), unique=51, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=152.0000, mean=0.9144

61. liwc_home
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'home'.
   - Profile: nulls=0 (0.0000%), unique=62, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=90.0000, mean=0.6221

62. liwc_humans
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'humans'.
   - Profile: nulls=0 (0.0000%), unique=58, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=138.0000, mean=0.9298

63. liwc_impersonal_pronouns
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'impersonal_pronouns'.
   - Profile: nulls=0 (0.0000%), unique=207, min=0.0000, q1=2.0000, median=6.0000, q3=11.0000, max=362.0000, mean=8.7309

64. liwc_inclusive
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'inclusive'.
   - Profile: nulls=0 (0.0000%), unique=216, min=0.0000, q1=2.0000, median=6.0000, q3=12.0000, max=353.0000, mean=9.2319

65. liwc_ingestion
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'ingestion'.
   - Profile: nulls=0 (0.0000%), unique=69, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=165.0000, mean=0.5504

66. liwc_inhibition
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'inhibition'.
   - Profile: nulls=0 (0.0000%), unique=41, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=61.0000, mean=0.8822

67. liwc_insight
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'insight'.
   - Profile: nulls=0 (0.0000%), unique=119, min=0.0000, q1=1.0000, median=3.0000, q3=6.0000, max=364.0000, mean=4.2261

68. liwc_leisure
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'leisure'.
   - Profile: nulls=0 (0.0000%), unique=59, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=362.0000, mean=0.9577

69. liwc_money
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'money'.
   - Profile: nulls=0 (0.0000%), unique=105, min=0.0000, q1=0.0000, median=0.0000, q3=2.0000, max=213.0000, mean=2.0046

70. liwc_motion
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'motion'.
   - Profile: nulls=0 (0.0000%), unique=88, min=0.0000, q1=0.0000, median=2.0000, q3=4.0000, max=154.0000, mean=3.0032

71. liwc_negations
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'negations'.
   - Profile: nulls=0 (0.0000%), unique=101, min=0.0000, q1=1.0000, median=2.0000, q3=5.0000, max=4001.0000, mean=3.9949

72. liwc_negative_emotion
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'negative_emotion'.
   - Profile: nulls=0 (0.0000%), unique=119, min=0.0000, q1=0.0000, median=2.0000, q3=5.0000, max=1201.0000, mean=3.5982

73. liwc_nonfluencies
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'nonfluencies'.
   - Profile: nulls=0 (0.0000%), unique=24, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=37.0000, mean=0.1759

74. liwc_numbers
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'numbers'.
   - Profile: nulls=0 (0.0000%), unique=45, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=73.0000, mean=1.0440

75. liwc_past_tense
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'past_tense'.
   - Profile: nulls=0 (0.0000%), unique=213, min=0.0000, q1=1.0000, median=3.0000, q3=7.0000, max=542.0000, mean=5.9015

76. liwc_perceptual_processes
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'perceptual_processes'.
   - Profile: nulls=0 (0.0000%), unique=98, min=0.0000, q1=0.0000, median=2.0000, q3=4.0000, max=216.0000, mean=3.2179

77. liwc_personal_pronouns
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'personal_pronouns'.
   - Profile: nulls=0 (0.0000%), unique=423, min=0.0000, q1=6.0000, median=13.0000, q3=26.0000, max=4001.0000, mean=20.1231

78. liwc_positive_emotion
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'positive_emotion'.
   - Profile: nulls=0 (0.0000%), unique=126, min=0.0000, q1=1.0000, median=3.0000, q3=6.0000, max=362.0000, mean=4.8700

79. liwc_prepositions
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'prepositions'.
   - Profile: nulls=0 (0.0000%), unique=410, min=0.0000, q1=7.0000, median=16.0000, q3=29.0000, max=1200.0000, mean=22.4660

80. liwc_present_tense
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'present_tense'.
   - Profile: nulls=0 (0.0000%), unique=314, min=0.0000, q1=7.0000, median=14.0000, q3=25.0000, max=4001.0000, mean=18.9126

81. liwc_quantifiers
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'quantifiers'.
   - Profile: nulls=0 (0.0000%), unique=108, min=0.0000, q1=1.0000, median=2.0000, q3=5.0000, max=362.0000, mean=3.8413

82. liwc_relativity
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'relativity'.
   - Profile: nulls=0 (0.0000%), unique=414, min=0.0000, q1=7.0000, median=15.0000, q3=30.0000, max=794.0000, mean=22.7037

83. liwc_religion
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'religion'.
   - Profile: nulls=0 (0.0000%), unique=46, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=89.0000, mean=0.1129

84. liwc_sadness
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'sadness'.
   - Profile: nulls=0 (0.0000%), unique=49, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=121.0000, mean=0.9259

85. liwc_see
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'see'.
   - Profile: nulls=0 (0.0000%), unique=45, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=65.0000, mean=0.7948

86. liwc_sexual
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'sexual'.
   - Profile: nulls=0 (0.0000%), unique=52, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=110.0000, mean=0.5068

87. liwc_social_processes
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'social_processes'.
   - Profile: nulls=0 (0.0000%), unique=399, min=0.0000, q1=3.0000, median=7.0000, q3=17.0000, max=728.0000, mean=14.6042

88. liwc_space
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'space'.
   - Profile: nulls=0 (0.0000%), unique=202, min=0.0000, q1=3.0000, median=6.0000, q3=12.0000, max=354.0000, mean=9.2755

89. liwc_swear_words
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'swear_words'.
   - Profile: nulls=0 (0.0000%), unique=58, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=281.0000, mean=0.3604

90. liwc_tentative
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'tentative'.
   - Profile: nulls=0 (0.0000%), unique=99, min=0.0000, q1=1.0000, median=2.0000, q3=5.0000, max=353.0000, mean=3.5296

91. liwc_time
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'time'.
   - Profile: nulls=0 (0.0000%), unique=222, min=0.0000, q1=3.0000, median=7.0000, q3=14.0000, max=724.0000, mean=10.5322

92. liwc_total_functional
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'total_functional'.
   - Profile: nulls=0 (0.0000%), unique=1382, min=0.0000, q1=33.0000, median=68.0000, q3=126.0000, max=8002.0000, mean=98.2925

93. liwc_total_pronouns
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'total_pronouns'.
   - Profile: nulls=0 (0.0000%), unique=548, min=0.0000, q1=9.0000, median=19.0000, q3=37.0000, max=4001.0000, mean=28.8540

94. liwc_work
   - Group: liwc
   - Type: int64
   - Understanding: LIWC-style linguistic category feature for 'work'.
   - Profile: nulls=0 (0.0000%), unique=114, min=0.0000, q1=0.0000, median=1.0000, q3=4.0000, max=707.0000, mean=3.0081

95. tfidf_abl
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'abl'.
   - Profile: nulls=0 (0.0000%), unique=93909, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0140

96. tfidf_abus
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'abus'.
   - Profile: nulls=0 (0.0000%), unique=32404, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0059

97. tfidf_actual
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'actual'.
   - Profile: nulls=0 (0.0000%), unique=92228, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0134

98. tfidf_addict
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'addict'.
   - Profile: nulls=0 (0.0000%), unique=15535, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0033

99. tfidf_adhd
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'adhd'.
   - Profile: nulls=0 (0.0000%), unique=26909, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0081

100. tfidf_advic
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'advic'.
   - Profile: nulls=0 (0.0000%), unique=121008, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0198

101. tfidf_ago
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'ago'.
   - Profile: nulls=0 (0.0000%), unique=126656, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0160

102. tfidf_alcohol
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'alcohol'.
   - Profile: nulls=0 (0.0000%), unique=17245, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0033

103. tfidf_almost
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'almost'.
   - Profile: nulls=0 (0.0000%), unique=75274, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0102

104. tfidf_alon
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'alon'.
   - Profile: nulls=0 (0.0000%), unique=66354, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0106

105. tfidf_alreadi
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'alreadi'.
   - Profile: nulls=0 (0.0000%), unique=72834, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0117

106. tfidf_also
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'also'.
   - Profile: nulls=0 (0.0000%), unique=193727, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0250

107. tfidf_alway
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'alway'.
   - Profile: nulls=0 (0.0000%), unique=136251, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0182

108. tfidf_amp
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'amp'.
   - Profile: nulls=0 (0.0000%), unique=74239, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0208

109. tfidf_amp x200b
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'amp x200b'.
   - Profile: nulls=0 (0.0000%), unique=48188, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=0.5981, mean=0.0142

110. tfidf_ani
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'ani'.
   - Profile: nulls=0 (0.0000%), unique=312491, min=0.0000, q1=0.0000, median=0.0000, q3=0.0677, max=1.0000, mean=0.0434

111. tfidf_anoth
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'anoth'.
   - Profile: nulls=0 (0.0000%), unique=94643, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0141

112. tfidf_anxieti
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'anxieti'.
   - Profile: nulls=0 (0.0000%), unique=103154, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0177

113. tfidf_anxious
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'anxious'.
   - Profile: nulls=0 (0.0000%), unique=32204, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0059

114. tfidf_anymor
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'anymor'.
   - Profile: nulls=0 (0.0000%), unique=81646, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0123

115. tfidf_anyon
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'anyon'.
   - Profile: nulls=0 (0.0000%), unique=175993, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0237

116. tfidf_anyon els
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'anyon els'.
   - Profile: nulls=0 (0.0000%), unique=42052, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=0.6851, mean=0.0076

117. tfidf_anyth
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'anyth'.
   - Profile: nulls=0 (0.0000%), unique=177029, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0235

118. tfidf_around
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'around'.
   - Profile: nulls=0 (0.0000%), unique=135387, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0190

119. tfidf_ask
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'ask'.
   - Profile: nulls=0 (0.0000%), unique=162467, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0281

120. tfidf_attack
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'attack'.
   - Profile: nulls=0 (0.0000%), unique=32717, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0065

121. tfidf_away
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'away'.
   - Profile: nulls=0 (0.0000%), unique=104358, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0142

122. tfidf_back
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'back'.
   - Profile: nulls=0 (0.0000%), unique=208080, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0293

123. tfidf_bad
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'bad'.
   - Profile: nulls=0 (0.0000%), unique=122370, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0159

124. tfidf_becaus
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'becaus'.
   - Profile: nulls=0 (0.0000%), unique=312369, min=0.0000, q1=0.0000, median=0.0000, q3=0.0644, max=1.0000, mean=0.0393

125. tfidf_becom
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'becom'.
   - Profile: nulls=0 (0.0000%), unique=52365, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0081

126. tfidf_befor
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'befor'.
   - Profile: nulls=0 (0.0000%), unique=158425, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0208

127. tfidf_believ
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'believ'.
   - Profile: nulls=0 (0.0000%), unique=57875, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0092

128. tfidf_best
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'best'.
   - Profile: nulls=0 (0.0000%), unique=94751, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0166

129. tfidf_better
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'better'.
   - Profile: nulls=0 (0.0000%), unique=117152, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0164

130. tfidf_bit
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'bit'.
   - Profile: nulls=0 (0.0000%), unique=69326, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0106

131. tfidf_bodi
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'bodi'.
   - Profile: nulls=0 (0.0000%), unique=41780, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0087

132. tfidf_bpd
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'bpd'.
   - Profile: nulls=0 (0.0000%), unique=11968, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0034

133. tfidf_brain
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'brain'.
   - Profile: nulls=0 (0.0000%), unique=28861, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0052

134. tfidf_call
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'call'.
   - Profile: nulls=0 (0.0000%), unique=116516, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0245

135. tfidf_came
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'came'.
   - Profile: nulls=0 (0.0000%), unique=58571, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0090

136. tfidf_care
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'care'.
   - Profile: nulls=0 (0.0000%), unique=90975, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0140

137. tfidf_caus
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'caus'.
   - Profile: nulls=0 (0.0000%), unique=61549, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0096

138. tfidf_chang
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'chang'.
   - Profile: nulls=0 (0.0000%), unique=83407, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0143

139. tfidf_come
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'come'.
   - Profile: nulls=0 (0.0000%), unique=150076, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0203

140. tfidf_complet
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'complet'.
   - Profile: nulls=0 (0.0000%), unique=70727, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0105

141. tfidf_constant
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'constant'.
   - Profile: nulls=0 (0.0000%), unique=51425, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0075

142. tfidf_control
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'control'.
   - Profile: nulls=0 (0.0000%), unique=38800, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0065

143. tfidf_could
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'could'.
   - Profile: nulls=0 (0.0000%), unique=185014, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0245

144. tfidf_coupl
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'coupl'.
   - Profile: nulls=0 (0.0000%), unique=62882, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0096

145. tfidf_cri
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'cri'.
   - Profile: nulls=0 (0.0000%), unique=51448, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0086

146. tfidf_day
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'day'.
   - Profile: nulls=0 (0.0000%), unique=251692, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0347

147. tfidf_deal
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'deal'.
   - Profile: nulls=0 (0.0000%), unique=68416, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0104

148. tfidf_depress
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'depress'.
   - Profile: nulls=0 (0.0000%), unique=115969, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0195

149. tfidf_diagnos
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'diagnos'.
   - Profile: nulls=0 (0.0000%), unique=37236, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0057

150. tfidf_die
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'die'.
   - Profile: nulls=0 (0.0000%), unique=61007, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0117

151. tfidf_differ
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'differ'.
   - Profile: nulls=0 (0.0000%), unique=83759, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0147

152. tfidf_disord
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'disord'.
   - Profile: nulls=0 (0.0000%), unique=22508, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0040

153. tfidf_doctor
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'doctor'.
   - Profile: nulls=0 (0.0000%), unique=42872, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0084

154. tfidf_doe
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'doe'.
   - Profile: nulls=0 (0.0000%), unique=133975, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0226

155. tfidf_done
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'done'.
   - Profile: nulls=0 (0.0000%), unique=83210, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0124

156. tfidf_dont
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'dont'.
   - Profile: nulls=0 (0.0000%), unique=43702, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0103

157. tfidf_drink
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'drink'.
   - Profile: nulls=0 (0.0000%), unique=32877, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0065

158. tfidf_drug
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'drug'.
   - Profile: nulls=0 (0.0000%), unique=24546, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0051

159. tfidf_eat
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'eat'.
   - Profile: nulls=0 (0.0000%), unique=52402, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0113

160. tfidf_els
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'els'.
   - Profile: nulls=0 (0.0000%), unique=115636, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0154

161. tfidf_emot
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'emot'.
   - Profile: nulls=0 (0.0000%), unique=47926, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0077

162. tfidf_end
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'end'.
   - Profile: nulls=0 (0.0000%), unique=140262, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0194

163. tfidf_enough
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'enough'.
   - Profile: nulls=0 (0.0000%), unique=82618, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0122

164. tfidf_etc
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'etc'.
   - Profile: nulls=0 (0.0000%), unique=70988, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0117

165. tfidf_even
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'even'.
   - Profile: nulls=0 (0.0000%), unique=256533, min=0.0000, q1=0.0000, median=0.0000, q3=0.0180, max=1.0000, mean=0.0298

166. tfidf_ever
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'ever'.
   - Profile: nulls=0 (0.0000%), unique=101276, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0135

167. tfidf_everi
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'everi'.
   - Profile: nulls=0 (0.0000%), unique=131775, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0172

168. tfidf_everyon
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'everyon'.
   - Profile: nulls=0 (0.0000%), unique=91722, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0138

169. tfidf_everyth
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'everyth'.
   - Profile: nulls=0 (0.0000%), unique=121103, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0161

170. tfidf_experi
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'experi'.
   - Profile: nulls=0 (0.0000%), unique=62887, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0105

171. tfidf_famili
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'famili'.
   - Profile: nulls=0 (0.0000%), unique=107864, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0166

172. tfidf_fear
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'fear'.
   - Profile: nulls=0 (0.0000%), unique=33086, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0056

173. tfidf_feel
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'feel'.
   - Profile: nulls=0 (0.0000%), unique=352848, min=0.0000, q1=0.0000, median=0.0000, q3=0.0765, max=1.0000, mean=0.0497

174. tfidf_feel like
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'feel like'.
   - Profile: nulls=0 (0.0000%), unique=173678, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=0.7127, mean=0.0219

175. tfidf_felt
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'felt'.
   - Profile: nulls=0 (0.0000%), unique=75344, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0102

176. tfidf_final
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'final'.
   - Profile: nulls=0 (0.0000%), unique=61734, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0098

177. tfidf_find
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'find'.
   - Profile: nulls=0 (0.0000%), unique=129521, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0202

178. tfidf_first
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'first'.
   - Profile: nulls=0 (0.0000%), unique=159121, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0225

179. tfidf_food
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'food'.
   - Profile: nulls=0 (0.0000%), unique=33185, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0070

180. tfidf_found
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'found'.
   - Profile: nulls=0 (0.0000%), unique=76404, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0130

181. tfidf_friend
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'friend'.
   - Profile: nulls=0 (0.0000%), unique=191271, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0343

182. tfidf_fuck
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'fuck'.
   - Profile: nulls=0 (0.0000%), unique=76687, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0152

183. tfidf_get
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'get'.
   - Profile: nulls=0 (0.0000%), unique=448715, min=0.0000, q1=0.0000, median=0.0000, q3=0.0990, max=1.0000, mean=0.0589

184. tfidf_give
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'give'.
   - Profile: nulls=0 (0.0000%), unique=120978, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0181

185. tfidf_go
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'go'.
   - Profile: nulls=0 (0.0000%), unique=372204, min=0.0000, q1=0.0000, median=0.0000, q3=0.0793, max=1.0000, mean=0.0467

186. tfidf_good
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'good'.
   - Profile: nulls=0 (0.0000%), unique=163248, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0238

187. tfidf_got
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'got'.
   - Profile: nulls=0 (0.0000%), unique=184930, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0270

188. tfidf_great
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'great'.
   - Profile: nulls=0 (0.0000%), unique=74933, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0120

189. tfidf_guess
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'guess'.
   - Profile: nulls=0 (0.0000%), unique=52673, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0079

190. tfidf_guy
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'guy'.
   - Profile: nulls=0 (0.0000%), unique=100704, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0194

191. tfidf_happen
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'happen'.
   - Profile: nulls=0 (0.0000%), unique=122969, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0175

192. tfidf_happi
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'happi'.
   - Profile: nulls=0 (0.0000%), unique=74241, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0120

193. tfidf_hard
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'hard'.
   - Profile: nulls=0 (0.0000%), unique=97601, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0128

194. tfidf_hate
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'hate'.
   - Profile: nulls=0 (0.0000%), unique=69288, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0118

195. tfidf_head
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'head'.
   - Profile: nulls=0 (0.0000%), unique=58920, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0090

196. tfidf_health
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'health'.
   - Profile: nulls=0 (0.0000%), unique=51354, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0091

197. tfidf_hear
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'hear'.
   - Profile: nulls=0 (0.0000%), unique=46042, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0090

198. tfidf_heart
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'heart'.
   - Profile: nulls=0 (0.0000%), unique=31370, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0056

199. tfidf_help
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'help'.
   - Profile: nulls=0 (0.0000%), unique=250472, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0344

200. tfidf_high
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'high'.
   - Profile: nulls=0 (0.0000%), unique=68655, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0114

201. tfidf_home
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'home'.
   - Profile: nulls=0 (0.0000%), unique=116351, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0205

202. tfidf_hope
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'hope'.
   - Profile: nulls=0 (0.0000%), unique=81828, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0121

203. tfidf_hour
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'hour'.
   - Profile: nulls=0 (0.0000%), unique=91771, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0154

204. tfidf_hous
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'hous'.
   - Profile: nulls=0 (0.0000%), unique=86060, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0195

205. tfidf_hurt
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'hurt'.
   - Profile: nulls=0 (0.0000%), unique=62680, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0100

206. tfidf_idea
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'idea'.
   - Profile: nulls=0 (0.0000%), unique=69871, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0124

207. tfidf_im
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'im'.
   - Profile: nulls=0 (0.0000%), unique=54306, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0144

208. tfidf_issu
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'issu'.
   - Profile: nulls=0 (0.0000%), unique=91332, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0148

209. tfidf_job
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'job'.
   - Profile: nulls=0 (0.0000%), unique=118396, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0239

210. tfidf_keep
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'keep'.
   - Profile: nulls=0 (0.0000%), unique=130003, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0187

211. tfidf_kill
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'kill'.
   - Profile: nulls=0 (0.0000%), unique=53714, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0104

212. tfidf_kind
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'kind'.
   - Profile: nulls=0 (0.0000%), unique=72743, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0108

213. tfidf_know
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'know'.
   - Profile: nulls=0 (0.0000%), unique=382559, min=0.0000, q1=0.0000, median=0.0000, q3=0.0807, max=1.0000, mean=0.0470

214. tfidf_last
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'last'.
   - Profile: nulls=0 (0.0000%), unique=157936, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0205

215. tfidf_late
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'late'.
   - Profile: nulls=0 (0.0000%), unique=54455, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0090

216. tfidf_leav
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'leav'.
   - Profile: nulls=0 (0.0000%), unique=88650, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0142

217. tfidf_left
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'left'.
   - Profile: nulls=0 (0.0000%), unique=80510, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0131

218. tfidf_let
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'let'.
   - Profile: nulls=0 (0.0000%), unique=101607, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0154

219. tfidf_life
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'life'.
   - Profile: nulls=0 (0.0000%), unique=194125, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0263

220. tfidf_like
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'like'.
   - Profile: nulls=0 (0.0000%), unique=440592, min=0.0000, q1=0.0000, median=0.0000, q3=0.0936, max=1.0000, mean=0.0550

221. tfidf_littl
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'littl'.
   - Profile: nulls=0 (0.0000%), unique=95533, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0143

222. tfidf_live
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'live'.
   - Profile: nulls=0 (0.0000%), unique=173749, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0275

223. tfidf_long
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'long'.
   - Profile: nulls=0 (0.0000%), unique=130974, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0173

224. tfidf_look
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'look'.
   - Profile: nulls=0 (0.0000%), unique=177507, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0292

225. tfidf_lose
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'lose'.
   - Profile: nulls=0 (0.0000%), unique=52496, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0090

226. tfidf_lost
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'lost'.
   - Profile: nulls=0 (0.0000%), unique=59896, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0097

227. tfidf_lot
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'lot'.
   - Profile: nulls=0 (0.0000%), unique=135677, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0178

228. tfidf_love
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'love'.
   - Profile: nulls=0 (0.0000%), unique=121696, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0199

229. tfidf_made
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'made'.
   - Profile: nulls=0 (0.0000%), unique=114309, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0162

230. tfidf_make
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'make'.
   - Profile: nulls=0 (0.0000%), unique=281498, min=0.0000, q1=0.0000, median=0.0000, q3=0.0505, max=1.0000, mean=0.0362

231. tfidf_mani
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'mani'.
   - Profile: nulls=0 (0.0000%), unique=80033, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0123

232. tfidf_mayb
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'mayb'.
   - Profile: nulls=0 (0.0000%), unique=77728, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0112

233. tfidf_mean
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'mean'.
   - Profile: nulls=0 (0.0000%), unique=70623, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0112

234. tfidf_med
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'med'.
   - Profile: nulls=0 (0.0000%), unique=26176, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0054

235. tfidf_medic
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'medic'.
   - Profile: nulls=0 (0.0000%), unique=54276, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0102

236. tfidf_mental
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'mental'.
   - Profile: nulls=0 (0.0000%), unique=63042, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0099

237. tfidf_might
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'might'.
   - Profile: nulls=0 (0.0000%), unique=66050, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0102

238. tfidf_mind
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'mind'.
   - Profile: nulls=0 (0.0000%), unique=69863, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0105

239. tfidf_mom
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'mom'.
   - Profile: nulls=0 (0.0000%), unique=53996, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0124

240. tfidf_month
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'month'.
   - Profile: nulls=0 (0.0000%), unique=216989, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0350

241. tfidf_move
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'move'.
   - Profile: nulls=0 (0.0000%), unique=111413, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0209

242. tfidf_much
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'much'.
   - Profile: nulls=0 (0.0000%), unique=210113, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0259

243. tfidf_need
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'need'.
   - Profile: nulls=0 (0.0000%), unique=228559, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0321

244. tfidf_never
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'never'.
   - Profile: nulls=0 (0.0000%), unique=190322, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0250

245. tfidf_new
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'new'.
   - Profile: nulls=0 (0.0000%), unique=130928, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0243

246. tfidf_next
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'next'.
   - Profile: nulls=0 (0.0000%), unique=87618, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0138

247. tfidf_night
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'night'.
   - Profile: nulls=0 (0.0000%), unique=78717, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0120

248. tfidf_normal
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'normal'.
   - Profile: nulls=0 (0.0000%), unique=64484, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0096

249. tfidf_noth
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'noth'.
   - Profile: nulls=0 (0.0000%), unique=103396, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0147

250. tfidf_notic
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'notic'.
   - Profile: nulls=0 (0.0000%), unique=56480, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0107

251. tfidf_old
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'old'.
   - Profile: nulls=0 (0.0000%), unique=102634, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0187

252. tfidf_onc
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'onc'.
   - Profile: nulls=0 (0.0000%), unique=70484, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0101

253. tfidf_one
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'one'.
   - Profile: nulls=0 (0.0000%), unique=280839, min=0.0000, q1=0.0000, median=0.0000, q3=0.0517, max=1.0000, mean=0.0380

254. tfidf_onli
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'onli'.
   - Profile: nulls=0 (0.0000%), unique=213170, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0274

255. tfidf_pain
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'pain'.
   - Profile: nulls=0 (0.0000%), unique=45028, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0085

256. tfidf_panic
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'panic'.
   - Profile: nulls=0 (0.0000%), unique=26527, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0051

257. tfidf_parent
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'parent'.
   - Profile: nulls=0 (0.0000%), unique=82533, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0171

258. tfidf_part
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'part'.
   - Profile: nulls=0 (0.0000%), unique=74202, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0117

259. tfidf_past
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'past'.
   - Profile: nulls=0 (0.0000%), unique=90288, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0121

260. tfidf_peopl
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'peopl'.
   - Profile: nulls=0 (0.0000%), unique=207148, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0307

261. tfidf_person
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'person'.
   - Profile: nulls=0 (0.0000%), unique=145556, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0215

262. tfidf_place
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'place'.
   - Profile: nulls=0 (0.0000%), unique=88091, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0137

263. tfidf_pleas
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'pleas'.
   - Profile: nulls=0 (0.0000%), unique=67476, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0126

264. tfidf_point
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'point'.
   - Profile: nulls=0 (0.0000%), unique=109869, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0151

265. tfidf_possibl
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'possibl'.
   - Profile: nulls=0 (0.0000%), unique=65928, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0112

266. tfidf_post
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'post'.
   - Profile: nulls=0 (0.0000%), unique=95595, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0158

267. tfidf_pretti
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'pretti'.
   - Profile: nulls=0 (0.0000%), unique=85403, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0127

268. tfidf_probabl
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'probabl'.
   - Profile: nulls=0 (0.0000%), unique=61955, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0090

269. tfidf_problem
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'problem'.
   - Profile: nulls=0 (0.0000%), unique=91268, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0131

270. tfidf_ptsd
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'ptsd'.
   - Profile: nulls=0 (0.0000%), unique=10521, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=0.9753, mean=0.0022

271. tfidf_put
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'put'.
   - Profile: nulls=0 (0.0000%), unique=112823, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0187

272. tfidf_question
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'question'.
   - Profile: nulls=0 (0.0000%), unique=104506, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0213

273. tfidf_quit
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'quit'.
   - Profile: nulls=0 (0.0000%), unique=54786, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0084

274. tfidf_read
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'read'.
   - Profile: nulls=0 (0.0000%), unique=77798, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0123

275. tfidf_real
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'real'.
   - Profile: nulls=0 (0.0000%), unique=48542, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0083

276. tfidf_realli
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'realli'.
   - Profile: nulls=0 (0.0000%), unique=260728, min=0.0000, q1=0.0000, median=0.0000, q3=0.0337, max=1.0000, mean=0.0329

277. tfidf_reason
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'reason'.
   - Profile: nulls=0 (0.0000%), unique=90379, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0132

278. tfidf_recent
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'recent'.
   - Profile: nulls=0 (0.0000%), unique=102403, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0157

279. tfidf_relationship
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'relationship'.
   - Profile: nulls=0 (0.0000%), unique=84657, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0153

280. tfidf_rememb
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'rememb'.
   - Profile: nulls=0 (0.0000%), unique=39284, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0067

281. tfidf_right
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'right'.
   - Profile: nulls=0 (0.0000%), unique=154375, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0218

282. tfidf_said
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'said'.
   - Profile: nulls=0 (0.0000%), unique=142797, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0247

283. tfidf_say
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'say'.
   - Profile: nulls=0 (0.0000%), unique=214429, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0338

284. tfidf_scare
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'scare'.
   - Profile: nulls=0 (0.0000%), unique=53237, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0083

285. tfidf_school
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'school'.
   - Profile: nulls=0 (0.0000%), unique=106233, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0217

286. tfidf_see
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'see'.
   - Profile: nulls=0 (0.0000%), unique=178549, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0240

287. tfidf_seem
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'seem'.
   - Profile: nulls=0 (0.0000%), unique=128154, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0186

288. tfidf_self
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'self'.
   - Profile: nulls=0 (0.0000%), unique=55612, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0090

289. tfidf_sever
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'sever'.
   - Profile: nulls=0 (0.0000%), unique=50753, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0079

290. tfidf_shit
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'shit'.
   - Profile: nulls=0 (0.0000%), unique=59257, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0098

291. tfidf_sinc
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'sinc'.
   - Profile: nulls=0 (0.0000%), unique=169755, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0220

292. tfidf_situat
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'situat'.
   - Profile: nulls=0 (0.0000%), unique=79483, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0124

293. tfidf_sleep
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'sleep'.
   - Profile: nulls=0 (0.0000%), unique=60537, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0110

294. tfidf_social
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'social'.
   - Profile: nulls=0 (0.0000%), unique=58509, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0106

295. tfidf_someon
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'someon'.
   - Profile: nulls=0 (0.0000%), unique=144767, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0219

296. tfidf_someth
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'someth'.
   - Profile: nulls=0 (0.0000%), unique=179707, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0231

297. tfidf_sometim
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'sometim'.
   - Profile: nulls=0 (0.0000%), unique=67760, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0097

298. tfidf_sorri
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'sorri'.
   - Profile: nulls=0 (0.0000%), unique=54708, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0082

299. tfidf_start
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'start'.
   - Profile: nulls=0 (0.0000%), unique=222911, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0296

300. tfidf_stay
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'stay'.
   - Profile: nulls=0 (0.0000%), unique=73933, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0111

301. tfidf_still
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'still'.
   - Profile: nulls=0 (0.0000%), unique=177464, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0230

302. tfidf_stop
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'stop'.
   - Profile: nulls=0 (0.0000%), unique=109651, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0152

303. tfidf_stress
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'stress'.
   - Profile: nulls=0 (0.0000%), unique=41033, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0067

304. tfidf_struggl
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'struggl'.
   - Profile: nulls=0 (0.0000%), unique=52580, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0080

305. tfidf_stuff
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'stuff'.
   - Profile: nulls=0 (0.0000%), unique=56012, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0091

306. tfidf_suicid
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'suicid'.
   - Profile: nulls=0 (0.0000%), unique=53273, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0103

307. tfidf_support
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'support'.
   - Profile: nulls=0 (0.0000%), unique=46785, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0083

308. tfidf_sure
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'sure'.
   - Profile: nulls=0 (0.0000%), unique=127755, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0188

309. tfidf_symptom
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'symptom'.
   - Profile: nulls=0 (0.0000%), unique=23837, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0043

310. tfidf_take
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'take'.
   - Profile: nulls=0 (0.0000%), unique=207237, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0292

311. tfidf_talk
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'talk'.
   - Profile: nulls=0 (0.0000%), unique=166188, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0248

312. tfidf_tell
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'tell'.
   - Profile: nulls=0 (0.0000%), unique=138835, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0199

313. tfidf_thank
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'thank'.
   - Profile: nulls=0 (0.0000%), unique=148612, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0229

314. tfidf_therapi
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'therapi'.
   - Profile: nulls=0 (0.0000%), unique=31980, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0054

315. tfidf_therapist
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'therapist'.
   - Profile: nulls=0 (0.0000%), unique=30246, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0053

316. tfidf_thing
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'thing'.
   - Profile: nulls=0 (0.0000%), unique=252609, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0308

317. tfidf_think
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'think'.
   - Profile: nulls=0 (0.0000%), unique=262359, min=0.0000, q1=0.0000, median=0.0000, q3=0.0350, max=1.0000, mean=0.0325

318. tfidf_though
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'though'.
   - Profile: nulls=0 (0.0000%), unique=88665, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0115

319. tfidf_thought
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'thought'.
   - Profile: nulls=0 (0.0000%), unique=152729, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0206

320. tfidf_time
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'time'.
   - Profile: nulls=0 (0.0000%), unique=356105, min=0.0000, q1=0.0000, median=0.0000, q3=0.0757, max=1.0000, mean=0.0437

321. tfidf_tire
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'tire'.
   - Profile: nulls=0 (0.0000%), unique=43105, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0083

322. tfidf_today
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'today'.
   - Profile: nulls=0 (0.0000%), unique=89683, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0151

323. tfidf_told
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'told'.
   - Profile: nulls=0 (0.0000%), unique=138431, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0224

324. tfidf_took
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'took'.
   - Profile: nulls=0 (0.0000%), unique=61423, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0096

325. tfidf_tri
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'tri'.
   - Profile: nulls=0 (0.0000%), unique=257015, min=0.0000, q1=0.0000, median=0.0000, q3=0.0271, max=1.0000, mean=0.0328

326. tfidf_turn
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'turn'.
   - Profile: nulls=0 (0.0000%), unique=69132, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0112

327. tfidf_two
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'two'.
   - Profile: nulls=0 (0.0000%), unique=111637, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0177

328. tfidf_understand
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'understand'.
   - Profile: nulls=0 (0.0000%), unique=78395, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0118

329. tfidf_us
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'us'.
   - Profile: nulls=0 (0.0000%), unique=95680, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0215

330. tfidf_use
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'use'.
   - Profile: nulls=0 (0.0000%), unique=165345, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0289

331. tfidf_usual
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'usual'.
   - Profile: nulls=0 (0.0000%), unique=50013, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0077

332. tfidf_veri
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'veri'.
   - Profile: nulls=0 (0.0000%), unique=162160, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0221

333. tfidf_want
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'want'.
   - Profile: nulls=0 (0.0000%), unique=375749, min=0.0000, q1=0.0000, median=0.0000, q3=0.0882, max=1.0000, mean=0.0530

334. tfidf_way
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'way'.
   - Profile: nulls=0 (0.0000%), unique=187258, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0245

335. tfidf_week
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'week'.
   - Profile: nulls=0 (0.0000%), unique=166140, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0241

336. tfidf_weight
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'weight'.
   - Profile: nulls=0 (0.0000%), unique=34781, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0103

337. tfidf_well
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'well'.
   - Profile: nulls=0 (0.0000%), unique=132718, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0179

338. tfidf_went
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'went'.
   - Profile: nulls=0 (0.0000%), unique=103741, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0144

339. tfidf_whi
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'whi'.
   - Profile: nulls=0 (0.0000%), unique=126350, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0238

340. tfidf_whole
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'whole'.
   - Profile: nulls=0 (0.0000%), unique=56116, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0081

341. tfidf_wish
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'wish'.
   - Profile: nulls=0 (0.0000%), unique=44843, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0081

342. tfidf_without
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'without'.
   - Profile: nulls=0 (0.0000%), unique=101786, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0149

343. tfidf_wonder
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'wonder'.
   - Profile: nulls=0 (0.0000%), unique=70736, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0134

344. tfidf_work
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'work'.
   - Profile: nulls=0 (0.0000%), unique=259196, min=0.0000, q1=0.0000, median=0.0000, q3=0.0341, max=1.0000, mean=0.0427

345. tfidf_worri
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'worri'.
   - Profile: nulls=0 (0.0000%), unique=65920, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0105

346. tfidf_wors
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'wors'.
   - Profile: nulls=0 (0.0000%), unique=55413, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0078

347. tfidf_would
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'would'.
   - Profile: nulls=0 (0.0000%), unique=314069, min=0.0000, q1=0.0000, median=0.0000, q3=0.0749, max=1.0000, mean=0.0489

348. tfidf_wrong
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'wrong'.
   - Profile: nulls=0 (0.0000%), unique=70461, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=1.0000, mean=0.0111

349. tfidf_x200b
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'x200b'.
   - Profile: nulls=0 (0.0000%), unique=48188, min=0.0000, q1=0.0000, median=0.0000, q3=0.0000, max=0.5981, mean=0.0142

350. tfidf_year
   - Group: tfidf
   - Type: float64
   - Understanding: TF-IDF feature weight for token/ngram 'year'.
   - Profile: nulls=0 (0.0000%), unique=330321, min=0.0000, q1=0.0000, median=0.0000, q3=0.0760, max=1.0000, mean=0.0480

351. timeframe
   - Group: metadata
   - Type: str
   - Understanding: Temporal split extracted from filename (2018, 2019, pre, post).
   - Profile: nulls=0 (0.0000%), unique=n/a, min=n/a, q1=n/a, median=n/a, q3=n/a, max=n/a, mean=n/a
   - Example: post

352. is_mental_health
   - Group: labels
   - Type: int64
   - Understanding: Binary label: 1 if subreddit belongs to curated mental-health set, else 0.
   - Profile: nulls=0 (0.0000%), unique=2, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=1.0000, mean=0.4261

353. covid_period
   - Group: labels
   - Type: int64
   - Understanding: Binary indicator: 1 for post period, 0 otherwise.
   - Profile: nulls=0 (0.0000%), unique=2, min=0.0000, q1=0.0000, median=0.0000, q3=1.0000, max=1.0000, mean=0.2893

354. clean_text
   - Group: text
   - Type: str
   - Understanding: Normalized and lemmatized text generated in preprocessing.
   - Profile: nulls=0 (0.0000%), unique=n/a, min=n/a, q1=n/a, median=n/a, q3=n/a, max=n/a, mean=n/a
   - Example: welcome covid support hi everyone counselor mostly work person sometimes online ...

355. tokens
   - Group: text
   - Type: object
   - Understanding: Token list produced from normalized text.
   - Profile: nulls=0 (0.0000%), unique=n/a, min=n/a, q1=n/a, median=n/a, q3=n/a, max=n/a, mean=n/a
   - Example: ['welcome' 'covid' 'support' 'hi' 'everyone' 'counselor' 'mostly' 'work'  'perso...

356. clean_word_count
   - Group: readability_length
   - Type: int64
   - Understanding: Number of tokens in clean_text.
   - Profile: nulls=0 (0.0000%), unique=1182, min=0.0000, q1=31.0000, median=61.0000, q3=109.0000, max=4001.0000, mean=84.8709

357. source_text_col
   - Group: metadata
   - Type: str
   - Understanding: Original text column used as source during preprocessing.
   - Profile: nulls=0 (0.0000%), unique=n/a, min=n/a, q1=n/a, median=n/a, q3=n/a, max=n/a, mean=n/a
   - Example: post


* Unique counts are reported for numeric columns; for large text/list columns they are intentionally omitted for profiling performance.