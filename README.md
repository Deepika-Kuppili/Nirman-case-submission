Overview

This project evaluates a student’s spoken self-introduction using their transcript.
The tool produces a detailed score based on the rubric provided in the case study.

The system analyzes:

Content & Structure

Speech Rate

Grammar & Vocabulary

Clarity

Engagement

The output includes:

Per-category scores

Intermediate metrics (WPM, filler rate, etc.)

Final score out of 100

Rubric Components Implemented
1. Content & Structure (40 points)

Salutation

Keyword Presence (required + optional keywords)

Flow & Organization
Scoring is based on presence, order, and completeness of introduction elements.

2. Speech Rate (10 points)

Words per minute (WPM) is calculated from:
WPM = total_words / (duration_in_seconds / 60)
Scored according to the ranges defined in the rubric.

3. Language & Grammar (20 points)

Grammar assessment based on rule checks.

Vocabulary richness measured using type-token ratio (TTR).

4. Clarity (15 points)

Filler words are detected and converted into filler rate (%)

Rate is mapped to clarity score.

5. Engagement (15 points)

Sentiment analysis determines level of positive tone.

Mapped to engagement score.

Files Included

scoring_result.json – Contains the evaluated scores for the sample transcript.

score.py – Prints the scoring result.

app.py – A placeholder Flask API structure (can be expanded into a full tool).

Sample transcript file (provided separately).

How to Use

Place transcript text into the scoring script or API.

Provide duration (in seconds) if available.

Run the scoring functions to generate JSON output.

Assumptions

Duration used for the sample transcript is based on provided information.

Grammar, vocabulary, and sentiment follow lightweight NLP methods suitable for a prototype.

Keywords are derived from typical self-introduction structure.

Possible Extensions

Integrate accurate grammar evaluation tools.

Add UI for transcript upload.

Replace vocabulary & sentiment heuristics with modern NLP models.

Add audio support to extract actual speech duration.
