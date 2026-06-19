```markdown
# Social-Sentiment-Analysis Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the development patterns and conventions used in the Social-Sentiment-Analysis Python repository. You'll learn how to structure files, write imports and exports, and follow the project's unique coding and testing styles. This guide also outlines common workflows and provides example commands to streamline your development process.

## Coding Conventions

### File Naming
- Use **snake_case** for all file names.
  - Example: `data_loader.py`, `sentiment_analysis.py`

### Import Style
- Use **relative imports** within the package.
  - Example:
    ```python
    from .utils import preprocess_text
    from .models import SentimentModel
    ```

### Export Style
- Use **named exports** (explicitly define what is exported).
  - Example:
    ```python
    def analyze_sentiment(text):
        # implementation

    __all__ = ['analyze_sentiment']
    ```

### Commit Messages
- Freeform style, no strict prefixes.
- Average commit message length: ~32 characters.
  - Example: `add preprocessing for tweets`

## Workflows

### Running Sentiment Analysis
**Trigger:** When you want to analyze new social media data for sentiment.
**Command:** `/run-analysis`

1. Prepare your dataset (e.g., CSV of tweets).
2. Run the main analysis script:
    ```bash
    python sentiment_analysis.py --input data/tweets.csv --output results/sentiments.csv
    ```
3. Review the output in the specified results file.

### Adding a New Preprocessing Step
**Trigger:** When you need to add or modify text preprocessing logic.
**Command:** `/add-preprocessing`

1. Open or create a new function in `preprocessing.py`.
2. Use relative imports to access utility functions.
    ```python
    from .utils import clean_text
    ```
3. Add your new preprocessing logic.
4. Update the main pipeline to include your step.

### Writing and Running Tests
**Trigger:** When you add new features or fix bugs.
**Command:** `/run-tests`

1. Create a test file following the `*.test.*` pattern, e.g., `preprocessing.test.py`.
2. Write test functions for your code.
    ```python
    def test_clean_text():
        assert clean_text("Hello!!!") == "hello"
    ```
3. Run tests using your preferred method (framework not specified; could use `pytest` or direct execution).

## Testing Patterns

- Test files follow the `*.test.*` naming convention.
  - Example: `sentiment_analysis.test.py`
- Testing framework is not specified; tests may be run manually or with a tool like `pytest`.
- Test functions typically use assertions to validate behavior.

## Commands
| Command           | Purpose                                         |
|-------------------|-------------------------------------------------|
| /run-analysis     | Run sentiment analysis on a dataset             |
| /add-preprocessing| Add or modify a preprocessing step              |
| /run-tests        | Run the test suite for the codebase             |
```