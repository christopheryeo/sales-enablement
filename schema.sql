DROP TABLE IF EXISTS viewed_sections;
DROP TABLE IF EXISTS correct_answers;

CREATE TABLE viewed_sections (
  user_id TEXT NOT NULL,      -- Using session-based UUID
  section_id TEXT NOT NULL,   -- The unique text identifier for the section
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, section_id)
);

CREATE TABLE correct_answers (
  user_id TEXT NOT NULL,
  question_id TEXT NOT NULL,  -- e.g., 'q1', 'q6'
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (user_id, question_id)
);
